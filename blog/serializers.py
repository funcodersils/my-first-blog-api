#-*- coding: utf-8 -*-
from rest_framework import serializers
from models import Post, Kullanicilar

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        field = ('id', 'baslik', 'yazi', 'avatar',)

class KullanicilarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kullanicilar
        field = ('id', 'kullanici', 'parola', 'adi', 'soyadi', 'email')
