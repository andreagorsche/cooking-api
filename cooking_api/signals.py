from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Define the signal handler
@receiver(post_save, sender=User)
def send_registration_email(sender, instance, created, **kwargs):
    if created:
        print("Sending registration email...")
        subject = "Welcome to Cook-Around-The-Clock"
        message = "Congrats. Your registration to Cook-Around-The-Clock was successful. Jump right in and keep on cookin'."
        from_email = "andrea.gorsche@gmail.com"  
        recipient_list = [instance.email]  # Use instance.email to get the email of the newly created user

        send_mail(subject, message, from_email, recipient_list)
        
# Connect the signal
post_save.connect(send_registration_email, sender=User)
