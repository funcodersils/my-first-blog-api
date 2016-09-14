#-*- coding: utf-8 -*-
from django.shortcuts import render
from rest_framework import generics
from serializers import PostSerializer, KullanicilarSerializer
from models import Post, Kullanicilar

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class KullaniciList(generics.ListCreateAPIView):
    queryset = Kullanicilar.objects.all()
    serializer_class = KullanicilarSerializer

class KullaniciDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kullanicilar.objects.all()
    serializer_class = KullanicilarSerializer

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
