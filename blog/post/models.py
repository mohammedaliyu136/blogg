from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    post = models.CharField(max_length=500)
    date = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    picture = models.CharField(max_length=500)


    def __str__(self):
        return self.title + "-  By  -" + self.post
