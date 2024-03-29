from rest_framework.response import Response
from main.models import Post, PostImages
from .serializers import PostSerializer

from django.shortcuts import get_object_or_404
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
      posts = Post.objects.filter(contacts=False).order_by("-published")[:20]
      serializer = PostSerializer(posts, many=True)
      return Response(serializer.data)





   def post(self,request):
      contactHtml = request.data['contact']
      images = request.data['images']
      postId = request.data['postId']
      offerId = request.data['offerId']

      return Response(contactHtml)





class PostContactDetailApiView(GenericAPIView):
   serializer_class = PostSerializer
   queryset = Post.objects.all()


   def get(self,request,pk):
      post = get_object_or_404(self.queryset, pk=pk)
      serializer = PostSerializer(post)
      return Response(serializer.data)






   def post(self,request,pk):
      print("=== IN POST ===")
      print("PK = ", pk)


      post = Post.objects.get(id=pk)
      post_images = post.images.all()

      # Previous Images Deletion
      for i in post_images:
         i.delete()

      for i in request.data['images']:
         print('NEW Image: ',i)
         post_image = post.images.create(post=post, url=i).save()
         print(post_image)
      
      
      bodyHtml = post.body + request.data['contact']
      post.body = bodyHtml



      post.contacts = True
      post.save()

      return Response(request.data)