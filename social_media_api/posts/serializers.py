from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  # shows author's __str__ (e.g., username/email)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  # shows author's __str__
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Comment content cannot be empty.")
        return value
