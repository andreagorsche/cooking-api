from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
from django.utils import timezone
from allauth.account.models import EmailConfirmation
from allauth.account.models import EmailAddress


class DefaultAccountAdapterCustom(DefaultAccountAdapter):
    def send_mail(self, template_prefix, email, context):
        # Generate a key or retrieve the key from the context
        key = context.get('key', None)
        if not key:
            raise ValueError("Key not found in context")

        # Include the activation URL in the context
        context['activate_url'] = f"{settings.URL_FRONT}/verify-email/{key}"
      
        # Pass the key to create_email_confirmation
        confirmation = create_email_confirmation(email, key)

        # Render the email message
        msg = self.render_mail(template_prefix, email, context)
        # Send the email
        msg.send()


def create_email_confirmation(email, key):
    try:
        # Retrieve the EmailAddress instance associated with the email
        email_address_instance = EmailAddress.objects.get(email=email)
    except EmailAddress.DoesNotExist:
        # Handle the case where the EmailAddress instance does not exist
        # (This depends on your application logic)
        raise ValueError(f"No EmailAddress found for email: {email}")

    # Get the current timestamp for creation and sent time
    now = timezone.now()

    # Create the EmailConfirmation instance
    confirmation = EmailConfirmation.objects.create(
        email_address=email_address_instance,
        created=now,
        sent=now,
        key=key,
    )
    return confirmation
