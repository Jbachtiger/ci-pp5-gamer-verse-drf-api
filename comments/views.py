from rest_framework import generics, permissions
from pp5_gamer_verse_drf_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer

# DRF-API walkthrough used to get guidance on creating comment model


class CommentList(generics.ListCreateAPIView):
    '''
    List comments and create a comment if logged in 
    '''
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


