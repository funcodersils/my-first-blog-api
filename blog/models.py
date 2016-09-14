from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    yazar = models.ForeignKey('auth.User')
    baslik = models.CharField(max_length=200)
    yazi = models.TextField()
    avatar = models.ImageField(max_length=255, upload_to='images/')

    def yayinla(self):
        self.yazar = auth.User
        self.save()

    def __str(self):
        return self.baslik

    def __unicode__(self):
        return self.baslik

    def Avatar(self):
        return '<img src="%s" height="150"/>' % (self.avatar)
    Avatar.allow_tags = True

class Kullanicilar(models.Model):
    kullanici = models.CharField(max_length=150)
    parola = models.CharField(max_length=8)
    adi = models.CharField(max_length=130)
    soyadi = models.CharField(max_length=130)
    email = models.CharField(max_length=100)

    def __unicode__(self):
        return self.kullanici
