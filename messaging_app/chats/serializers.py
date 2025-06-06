""" serializers module """
from rest_framework import serializers
from .models import User, Conversation, message


class UserSerializer(serializer.ModelSerializer):
    """ user serializer class """
    class Meta:

        model = User
        fields = '__all__'

class MessageSerializer(serializer.ModelSerializer):
    """ Message serializer class """
    class Meta:
        model = Message
        field = '__all__'

class ConversationSerializer(serializer.ModelSerializer):
    """ conversation serializer class """
    message = MessageSerializer()

    class Meta:

        model = Conversation
        field = '__all__'
