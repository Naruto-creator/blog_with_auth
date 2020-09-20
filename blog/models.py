from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


