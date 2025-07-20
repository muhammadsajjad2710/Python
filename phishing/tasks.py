from celery import shared_task
from django.core.mail import send_mail
from django.utils.html import strip_tags

from apps.phishing.utils import replace_variables


@shared_task
def send_phishing_mail(user, template, password=None):
    subject = replace_variables(template.sending_subject, user)
    content = replace_variables(template.content, user)
    name = replace_variables(template.sending_name, user)
    sender = template.sending_email

    send_mail(
        subject=subject,
        from_email=f'{name} <{sender}>',
        recipient_list=[user.email],
        message=strip_tags(content),
        html_message=content,
        auth_user=sender,
        auth_password=password
    )
