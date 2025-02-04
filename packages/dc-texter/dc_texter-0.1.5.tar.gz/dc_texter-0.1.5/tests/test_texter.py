"""
tests/test_texter.py
Tests sending an SMS text with Python and Gmail.
"""

import os
import pytest
from unittest.mock import patch, MagicMock
from dc_texter.texter import send_text
from dc_texter.config import load_config

# Sample TOML config as a string
SAMPLE_TOML_CONFIG = """
outgoing_email_host = "smtp.example.com"
outgoing_email_port = "587"
outgoing_email_address = "user@example.com"
outgoing_email_password = "securepassword"
sms_address_for_texts = "1234567890@example.com"
"""


@pytest.fixture
def temp_config_file(tmp_path):
    """Creates a temporary .env.toml file for testing."""
    config_file = tmp_path / ".env.toml"
    config_file.write_text(SAMPLE_TOML_CONFIG)
    return config_file


def test_no_env_no_file(monkeypatch):
    """Test when neither environment variables nor a file exist."""
    for key in os.environ.keys():
        if key.startswith("OUTGOING_") or key == "SMS_ADDRESS_FOR_TEXTS":
            monkeypatch.delenv(key, raising=False)

    with pytest.raises(
        RuntimeError, match="Please provide required configuration variables."
    ):
        load_config()


def test_env_vars_only(monkeypatch):
    """Test when only environment variables exist, no config file."""
    monkeypatch.setenv("OUTGOING_EMAIL_HOST", "smtp.env.com")
    monkeypatch.setenv("OUTGOING_EMAIL_PORT", "465")
    monkeypatch.setenv("OUTGOING_EMAIL_ADDRESS", "env_user@example.com")
    monkeypatch.setenv("OUTGOING_EMAIL_PASSWORD", "envpassword")
    monkeypatch.setenv("SMS_ADDRESS_FOR_TEXTS", "envsms@example.com")

    config = load_config()
    assert config["outgoing_email_host"] == "smtp.env.com"
    assert config["outgoing_email_port"] == "465"
    assert config["outgoing_email_address"] == "env_user@example.com"
    assert config["outgoing_email_password"] == "envpassword"
    assert config["sms_address_for_texts"] == "envsms@example.com"


def test_file_only(temp_config_file, monkeypatch):
    """Test when only a config file exists, no environment variables."""
    for key in os.environ.keys():
        if key.startswith("OUTGOING_") or key == "SMS_ADDRESS_FOR_TEXTS":
            monkeypatch.delenv(key, raising=False)

    config = load_config(config_file=str(temp_config_file))
    assert config["outgoing_email_host"] == "smtp.example.com"
    assert config["outgoing_email_port"] == "587"
    assert config["outgoing_email_address"] == "user@example.com"
    assert config["outgoing_email_password"] == "securepassword"
    assert config["sms_address_for_texts"] == "1234567890@example.com"


def test_both_env_and_file(temp_config_file, monkeypatch):
    """Test when both environment variables and a file exist, env vars take priority."""
    # Set environment variables that should override file values
    monkeypatch.setenv("OUTGOING_EMAIL_HOST", "smtp.override.com")
    monkeypatch.setenv("OUTGOING_EMAIL_PORT", "2525")
    monkeypatch.setenv("OUTGOING_EMAIL_ADDRESS", "override_user@example.com")
    monkeypatch.setenv("OUTGOING_EMAIL_PASSWORD", "overridepassword")
    monkeypatch.setenv("SMS_ADDRESS_FOR_TEXTS", "overridesms@example.com")

    config = load_config(config_file=str(temp_config_file))

    # ENV VARS should take priority over file config
    assert config["outgoing_email_host"] == "smtp.override.com"
    assert config["outgoing_email_port"] == "2525"
    assert config["outgoing_email_address"] == "override_user@example.com"
    assert config["outgoing_email_password"] == "overridepassword"
    assert config["sms_address_for_texts"] == "overridesms@example.com"


@pytest.mark.parametrize(
    "message, recipient, port",
    [
        ("Test message 1", "1234567890@example.com", 465),  # SMTP_SSL expected
        (
            "Hello, this is a test!",
            "9876543210@example.com",
            587,
        ),  # SMTP with TLS expected
        (
            "Text alert from your Python program",
            "testing@example.com",
            2525,
        ),  # Uncommon port
    ],
)
def test_send_text_mocked(message, recipient, port, monkeypatch):
    """Test send_text() with mocked SMTP client."""

    monkeypatch.setenv("OUTGOING_EMAIL_HOST", "smtp.example.com")
    monkeypatch.setenv("OUTGOING_EMAIL_PORT", str(port))  # Ensure correct port
    monkeypatch.setenv("OUTGOING_EMAIL_ADDRESS", "user@example.com")
    monkeypatch.setenv("OUTGOING_EMAIL_PASSWORD", "securepassword")
    monkeypatch.setenv("SMS_ADDRESS_FOR_TEXTS", recipient)

    with (
        patch("dc_texter.texter.smtplib.SMTP") as mock_smtp,
        patch("dc_texter.texter.smtplib.SMTP_SSL") as mock_smtp_ssl,
    ):

        # Mock correct SMTP class based on port
        mock_server = MagicMock()
        if port == 465:
            mock_smtp_ssl.return_value.__enter__.return_value = mock_server
        else:
            mock_smtp.return_value.__enter__.return_value = mock_server

        # Simulate successful SMTP interactions
        mock_server.login.return_value = True
        mock_server.send_message.return_value = None

        try:
            send_text(body=message, recipient=recipient)

            # Ensure correct SMTP class is used
            if port == 465:
                mock_smtp_ssl.assert_called_once()
            else:
                mock_smtp.assert_called_once()

            mock_server.login.assert_called_once()
            mock_server.send_message.assert_called_once()

        except Exception as e:
            pytest.fail(f"send_text() raised an exception: {e}")
