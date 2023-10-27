from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.core.mail import send_mail

@receiver(user_signed_up)
def send_registration_email(sender, request, user, **kwargs):
    subject = "Welcome to Cook-Around-The-Clock"
    message = "Congrats. Your registration to Cook-Around-The-Clock was successful. Jump right in and keep on cookin'."
    from_email = "DEFAULT_FROM_EMAIL"  
    recipient_list = [user.email]

    send_mail(subject, message, from_email, recipient_list)