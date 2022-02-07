from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
STATUS = (
    (0,'Draft'),
    (1,'Publish')
)

class Post(models.Model):

    title = models.CharField(max_length=50)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    status = models.IntegerField(choices=STATUS,default=0)


    class Meta:
        verbose_name = ("post")
        verbose_name_plural = ("posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

class Comment(models.Model):
    """Model definition for Comment."""
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        """Meta definition for Comment."""
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-created_on']

    def __str__(self):
        """Unicode representation of Comment."""
        return f"Comment {self.body} by {self.name}"


