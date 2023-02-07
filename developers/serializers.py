from rest_framework import serializers
from .models import Profile

class DeveloperSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Profile
        fields = ['id', 'user_id', 'location', 'short_intro', 'bio', 'profile_image',
                  'social_github', 'social_twitter', 'social_linkedin', 'social_youtube', 
                  'social_website']
    
    def create(self, validated_data):
        user_id = self.context['request'].user.id
        return Profile.objects.create(user_id=user_id, **validated_data)