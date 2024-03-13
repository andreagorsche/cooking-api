from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings

class DefaultAccountAdapterCustom(DefaultAccountAdapter):
    def send_mail(self, template_prefix, email, context):
        # Include the activation URL in the context
        context['activate_url'] = f"{settings.URL_FRONT}/verify-email/{context['key']}"
        # Render the email message
        msg = self.render_mail(template_prefix, email, context)
        # Send the email
        msg.send()
