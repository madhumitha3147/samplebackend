from rest_framework import serializers
from .models import Note, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class NoteSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=Tag.objects.all(),
        source='tags'
    )

    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'tags', 'tag_ids']

