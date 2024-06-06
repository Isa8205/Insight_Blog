from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100 , null=False)
    username = models.CharField(max_length=100 , null=False, unique=True)
    email = models.EmailField(max_length=100 , null=False, unique=True)
    password = models.CharField(max_length=100 , null=False)
    profile_name = models.TextField(null=False, default="avatar6.png")

    def __str__(self):
        return self.username
    
class Articles(models.Model):
    title = models.CharField(max_length=100 , null=False)
    content = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    likes = models.TextField
    dislikes = models.TextField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.title
    
class comments(models.Model):
    content = models.TextField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
    
class reviews(models.Model):
    content = models.TextField(null=False)
    author = models.CharField(max_length=100 , null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content