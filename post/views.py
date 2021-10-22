# from rest_framework import serializers
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import Post
# from .serializers import PostSerializer

# @api_view(['GET'])
# def helloAPI(request):
#     return Response("hello world!!")

# @api_view(['GET'])
# def postList(request):
#     totalPost = Post.objects.all()
#     serializers = PostSerializer(totalPost, many=True)
#     return Response(serializers.data)

from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer
from .pagination import CustomPagination


class ListCreatePostAPIView(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RetrieveUpdateDestroyPostAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
