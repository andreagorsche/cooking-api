from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User
from allauth.account.models import EmailConfirmation

# Define the signal handler
@receiver(post_save, sender=User)
def send_registration_email(sender, instance, created, **kwargs):
    if created:
        print("Sending registration email...")
        subject = "Welcome to Cook-Around-The-Clock"
        message = "Congrats. Your registration to Cook-Around-The-Clock was successful. Jump right in and keep on cookin'."
        from_email = "andrea.gorsche@gmail.com"  
        recipient_list = [instance.email]

        # Create EmailConfirmation instance
        email_confirmation = EmailConfirmation.create(instance.email)
        
        # Customize the email confirmation
        email_confirmation.sent = True
        email_confirmation.save()

        # Send the confirmation email
        email_confirmation.send()

        # access confirmation key in email:
        confirmation_key = email_confirmation.key
       

        # Send the registration email
        send_mail(subject, message, from_email, recipient_list)
        
# Connect the signal
post_save.connect(send_registration_email, sender=User)
