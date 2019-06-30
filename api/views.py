from rest_framework import generics

from journal.models import Post
from journal.serializers import PostSerializer


# Create your views here.
class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer