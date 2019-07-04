from django.db import models

class Post(models.Model):
    post = models.TextField()

    def __str__(self):
        return self.post[:50]

class Samochod(models.Model):
    samochod = models.CharField(max_length=50)

    def __str__(self):
        return self.post[:50]


