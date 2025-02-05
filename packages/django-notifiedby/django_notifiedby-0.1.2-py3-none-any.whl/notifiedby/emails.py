import requests
from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend
from django.utils import timezone


API_VERSION = 1
BASE_URL = "https://api.notifiedby.com"


class NotifiedByEmailBackend(BaseEmailBackend):
    # This is the function to handle standard Django emails like password reset.
    def send_messages(self, email_messages):
        num_sent = 0
        if not email_messages:
            return num_sent

        for message in email_messages:
            try:
                sent = self._send(message)
            except Exception as e:
                raise
            if sent:
                num_sent += 1

        return num_sent

    def _send(self, message):
        return send_email_via_api(message)


def send_email_via_api(message):
    """Sends the EmailMessage message, and returns the Gemini Message ID if the message was sent.

    This is called by the base send_messages loop and can also be called directly

    Implementations must raise exceptions derived from AnymailError for
    anticipated failures that should be suppressed in fail_silently mode.
    """

    url = f"{BASE_URL}/v{API_VERSION}/email/send/"
    api_key = getattr(settings, 'NOTIFIEDBY_API_KEY', None)
    if not api_key:
        raise Exception("NOTIFIEDBY_API_KEY is not set in settings.py")
    
    headers = {"Authorization": f"Api-Key {api_key}"}

    encryption_key = getattr(settings, 'NOTIFIEDBY_ENCRYPTION_KEY', None)
    if encryption_key:
        headers["Encryption-Key"] = encryption_key

    if type(message.to) is list:
        recipient = message.to[0]
    else:
        recipient = message.to

    payload = {
        "recipient": recipient,
        "subject": f"{settings.EMAIL_SUBJECT_PREFIX}{message.subject}",
        "body": message.body,
    }

    # Handle attachments
    files = []
    for attachment in message.attachments:
        filename, file_content, mime_type = attachment
        if isinstance(file_content, str):
            file_content = file_content.encode()
        files.append(('attachment', (filename, file_content, mime_type)))

    if files:
        response = requests.post(url, headers=headers, data=payload, files=files)
    else:
        response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        # Pull the message ID out of the response and return it to the caller
        try:
            return response.json()["id"]
        except Exception as e:
            return None

    return None
