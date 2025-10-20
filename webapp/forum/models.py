from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_theme = models.CharField(max_length=200)
    publish_date = models.DateTimeField("publish_date", auto_now_add=True)
    author = models.CharField(max_length=20, default="Ашот")


class Message(models.Model):
    message_text = models.CharField(max_length=800)
    publish_date = models.DateTimeField("publish_date", auto_now_add=True)
    author = models.CharField(max_length=20, default="Ашот")
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)