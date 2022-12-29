from rest_framework.response import Response
from main.models import Post
from .serializers import PostSerializer

# generic view
from rest_framework.generics import CreateAPIView, GenericAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin


class PostApiView(GenericAPIView, CreateModelMixin):
   serializer_class = PostSerializer
   queryset = Post.objects.all()

   def get(self, request):
      posts = Post.objects.all().order_by("-id")[:3]
      print("--- Posts ---")
      print(posts)
      serializer = PostSerializer(posts, many=True)
      return Response(serializer.data)


   def post(self,request):
      print(request)
      return self.create(request)


