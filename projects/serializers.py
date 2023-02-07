from rest_framework import serializers
from projects.models import Project, Tag, Review

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class ProjectSerializer(serializers.ModelSerializer):
    vote_total = serializers.IntegerField()
    vote_ratio = serializers.IntegerField()
    tags = TagSerializer(many=True, read_only=True)
    owner = serializers.UUIDField(read_only=True)
    
    class Meta:
        model = Project
        fields = ['id', 'owner', 'title', 'description', 'featured_image', 'demo_link', 'source_link',
                  'tags', 'vote_total', 'vote_ratio']
        
    def create(self, validated_data):
        owner_id = self.context['request'].user.profile.id
        return Project.objects.create(owner_id=owner_id, **validated_data)
    
class DeleteProjectSerializer(serializers.ModelSerializer):
    model = Project
    fields = ['title', 'description', 'featured_image', 'demo_link', 'source_link',
                  'tags', 'vote_total', 'vote_ratio']
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'owner', 'body', 'value', 'created']
    
    def create(self, validated_data):
        project_id = self.context['project_id']
        return Review.objects.create(project_id=project_id, **validated_data)