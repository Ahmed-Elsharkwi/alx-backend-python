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
    message_body = serializer.CharField(max_length=500)

    class Meta:
        model = Message
        field = '__all__'

class ConversationSerializer(serializer.ModelSerializer):
    """ conversation serializer class """
    message = MessageSerializer()
    id_1 = serializers.SerializerMethodField()

    class Meta:

        model = Conversation
        field = ['id_1', 'messages']

    def get_id_1(self, obj):
        """ get the id of the conversation """
        if obj.conversation_id:
            return obj.conversation_id
        else:
            raise serializers.ValidationError("conversation don't have id")
