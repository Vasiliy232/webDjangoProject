import time
from django.core.mail import send_mail


def send_email_job(subject, message, from_email, to_email):
    time.sleep(5)
    send_mail(subject, message, from_email, [to_email])
