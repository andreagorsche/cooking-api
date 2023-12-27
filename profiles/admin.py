from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_active')
    actions = ['delete_selected_users_and_profiles']

    def delete_selected_users_and_profiles(self, request, queryset):
        """
        Custom action to delete selected users and their profiles.
        """
        for user in queryset:
            profile = Profile.objects.get(owner=user)

            # Check if a token exists before attempting to delete it
            #try:
            #    token = TokenModel.objects.get(user=user)
            #    token.delete()
            #except TokenModel.DoesNotExist:
            #    pass

            profile.delete()
            user.delete()

        self.message_user(request, f'Selected users and their profiles have been deleted.')

    delete_selected_users_and_profiles.short_description = 'Delete selected users and profiles'

# Register the User and Profile models with the customized admin class
admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)
admin.site.register(Profile)
