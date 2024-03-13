from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.models import EmailConfirmation

class DefaultAccountAdapterCustom(DefaultAccountAdapter):
    def send_mail(self, template_prefix, email, context):
        # Generate an activation key
        confirmation = EmailConfirmation.create(email)
        confirmation.send()

        # Include the activation URL in the context
        context['activate_url'] = f"{settings.URL_FRONT}/verify-email/{confirmation.key}"
        
        # Render the email message
        msg = self.render_mail(template_prefix, email, context)
        
        # Send the email
        msg.send()
