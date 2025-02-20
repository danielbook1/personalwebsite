from rest_framework import serializers

from portfolio.models import Project
from contact.models import Message


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("title", "subtitle", "description")

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("name", "email", "subject", "message")