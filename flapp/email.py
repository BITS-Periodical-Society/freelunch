import os

from django.conf import settings

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from .models import Subscriber


def email_for_subscribers(self):
	subscribers = [s.email for s in Subscriber.objects.all()]
	from_email = settings.EMAIL_HOST_USER
	to_email = subscribers
	msg = f"{self.title}\nNew Post is uploaded."
	sub = "New Article"
	print("added")
	message = Mail(
		from_email=from_email,
		to_emails=to_email,
		subject=sub,
		html_content=msg)
	try:
		sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
		response = sg.send(message)
		print(response.status_code)
		print(response.body)
		print(response.headers)
	except Exception as e:
		print(e)