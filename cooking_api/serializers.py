from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from profiles.models import Profile as ProfileModel


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class CurrentUserSerializer(UserDetailsSerializer):
    profile = ProfileSerializer(many=True)

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('profile',)
        read_only_fields = ('',)

# from .models import userProfileModel

# class Profile(serializers.ModelSerializer):
#    user = UserDetailsSerializer()
 #   class Meta:
  #      model = ProfileModel
   #     fields = ('chef',)


#class CurrentUserSerializer(UserDetailsSerializer):
 #   profile = Profile(many=True)

  #  class Meta(UserDetailsSerializer.Meta):
   #     fields = UserDetailsSerializer.Meta.fields + ('profile',)
    #    read_only_fields = ('',)


# class CurrentUserSerializer(UserDetailsSerializer):
#     # profile = Profile(source='userprofile')
#     # profile = Profile(many=True)
#     # profile = serializers.ReadOnlyField(source='userprofile')
#     # profile_id = serializers.ReadOnlyField(source='profile')
#     # profile_image = serializers.ReadOnlyField(source='profile.image.url')
#     # profile_image = serializers.ImageField(
#     #     max_length=None, use_url=True,source='profile.image.url'
#     # )

#     # class Meta(UserDetailsSerializer.Meta):
#     #     fields = UserDetailsSerializer.Meta.fields + (
#     #         # 'profile_id', 'profile_image'
#     #         'profile',
#     #     )
"""