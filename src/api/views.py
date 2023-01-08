from rest_framework.response import Response
from main.models import Post, PostImages
from .serializers import PostSerializer

# generic view
from rest_framework.generics import CreateAPIView, GenericAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin


import json










class PostApiView(GenericAPIView, CreateModelMixin):
   serializer_class = PostSerializer
   queryset = Post.objects.all()



   def get(self, request):
      posts = Post.objects.all().order_by("-published")
      serializer = PostSerializer(posts, many=True)
      return Response(serializer.data)
      # return 200





   def post(self,request):
      title = request.data['title']
      slug = request.data['slug']
      category = request.data['category']
      price = request.data['price']
      priceCurrency = request.data['priceCurrency']
      pricePerMeter = request.data['pricePerMeter']
      city = request.data['city']   
      аddress = request.data['address']   
      description = request.data['description']   
      offerId = request.data['offerId']   
      contacts = request.data['contacts']   
      body = request.data['body']   
      source = request.data['source']   
      images_list = json.loads(request.data['images'])



      post = Post.objects.update_or_create(offerId=offerId, defaults={
         "title":title,
         "slug":slug,
         "category" :category,
         "price":price,
         "priceCurrency":priceCurrency,
         "pricePerMeter":pricePerMeter,
         "city":city,
         "address":аddress,
         "description":description,
         "offerId":offerId,
         "contacts":contacts,
         "body":body,
         "source":source
      })

      print(post[1])

      if post[1] == True and request.data['images']:
         for image in images_list: 
            PostImages.objects.create(post=post[0], url=image)



      return Response(200)



















class PostContactApiView(GenericAPIView):
   serializer_class = PostSerializer
   queryset = Post.objects.all()

   def get(self,request):
      posts = Post.objects.filter(contacts=False).order_by("-published")
      serializer = PostSerializer(posts, many=True)
      return Response(serializer.data) 





   def post(self,request):
      contactHtml = request.data['contact']
      images = request.data['images']
      postId = request.data['postId']
      offerId = request.data['offerId']

      return Response(contactHtml)