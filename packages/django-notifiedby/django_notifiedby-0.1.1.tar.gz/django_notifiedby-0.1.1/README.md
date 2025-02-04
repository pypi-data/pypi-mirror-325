# django-notifiedby

Integrate `django-notifiedby` as an email backend for Django.

## Installation

Using [pip](https://pip.pypa.io/en/stable/):

```bash
pip install django-notifiedby
```

## Configuration

Add the `django-notifiedby` email backend.

```python
# my_project/settings.py

EMAIL_BACKEND = "django-notifiedby.NotifiedByEmailBackend"
NOTIFIEDBY_API_KEY = "YOUR_API_KEY"
```

API Keys can be purchased from [NotifiedBy.com site](https://notifiedby.com/)

## Usage

Now the built-in django emails will send through NotifiedBy

```python

from django.core.mail import EmailMessage

email = EmailMessage(
    subject='Subject Here',
    body='Body of the email here',
    from_email='your_email@example.com',
    to=['recipient@example.com'],  # List of recipients
    cc=['cc_recipient@example.com'],  # CC
    bcc=['bcc_recipient@example.com'],  # BCC
)

# Attach a file?
email.attach('example.pdf', b'Some binary data', 'application/pdf')
email.send()
```
