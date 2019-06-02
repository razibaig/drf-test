from rest_framework import generics

from .models import Post
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions


class PostsView(generics.ListCreateAPIView, generics.RetrieveUpdateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    lookup_field = 'pk'

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        if self.request.method == "PATCH":
            queryset = Post.objects.filter(owner=self.request.user)
        else:
            queryset = Post.objects.all()
        return queryset
