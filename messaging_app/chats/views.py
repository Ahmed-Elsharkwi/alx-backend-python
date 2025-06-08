from django.shortcuts import render
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework import viewsets
from chats.models import Conversation, Message
from chats.serializers import ConversationSerializer, MessageSerializer
from rest_framework.decorators import api_view


class ConversationViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving conversations.
    """
    def list(self, request):
        queryset = Conversation.objects.all()
        serializer = ConversationSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """ create new conversation """
        conversation_data = JSONParser().parse(request)
        conversation_serializer = ConversationSerializer(data=conversation_data)
        print(conversation_serializer)
        
        if conversation_serializer.is_valid():
            conversation_serializer.save()

            return JsonResponse({"message": "new message was created"}, status=status.HTTP_201_CREATED)
        return JsonResponse(conversation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MessageViewSet(viewsets.ViewSet):
    """ viewset for messages """
    def list(self, request):
        queryset = Message.objects.all()
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """ create new message """
        message_data = JSONParser().parse(request)
        message_serializer = MessageSerializer(data=message_data)
        print(message_serializer)
        if message_serializer.is_valid():
            message_serializer.save()
            return JsonResponse({"response": "message was created"}, status=status.HTTP_201_CREATED)
        return JsonResponse(message_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
