from django.db import models

# Create your models here.
from django.db import models
from account.models import User


class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=250)
    image = models.ImageField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title

class Like(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='likes')
    post =  models.ForeignKey(Post,
                              on_delete=models.CASCADE,
                              related_name='post_like',
                              related_query_name='Post_like')

class Comment(models.Model):
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='comments')
    post =  models.ForeignKey(Post,
                              on_delete=models.CASCADE,
                              related_name='post_comment',
                              related_query_name='Post_comment')

    def __str__(self):
        return f'commented by {self.post.user.username}'