from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(default='')
    pub_date = models.DateField('date published')
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Choice(models.Model):
    select = models.ForeignKey(Post, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)