""" serializers module """
from rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    """ user serializer class """
    class Meta:

        model = User
        fields = '__all__'


class ConversationSerializer(serializers.ModelSerializer):

    id_1 = serializers.SerializerMethodField()

    class Meta:

        model = Conversation
        fields = ['id_1']

    def get_id_1(self, obj):
        """ get the id of the conversation """
        if obj.conversation_id:
            return obj.conversation_id
        else:
            raise serializers.ValidationError("conversation don't have id")

class MessageSerializer(serializers.ModelSerializer):
    """ Message serializer class """
    message_body = serializers.CharField(max_length=500)
    conversation = ConversationSerializer()

    class Meta:
        model = Message
        fields = ['message_id', 'message_body', 'sent_at', 'created_at', 'conversation']
