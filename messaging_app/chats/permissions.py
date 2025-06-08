""" this is the permissions module """
from rest_framework import permissions
from .models import Conversation  # Import your Conversation model

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission to only allow participants of a conversation to interact with its messages.
    """

    def has_permission(self, request, view):
        # Only allow access to authenticated users
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # obj is expected to be a Message instance that has a 'conversation' ForeignKey
        return request.user in obj.conversation.participants.all()

