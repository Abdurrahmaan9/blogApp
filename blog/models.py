from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
            .filter(status='PUBLISHED')
class Post(models.Model):
    
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PS', 'Published'
        
    title = models.CharField(max_length = 250)
    slug = models.SlugField(max_length = 250)
    author = models.ForeignKey(User,
                               on_delete = models.CASCADE,
                               related_name = 'blog_post' )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length = 2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    
    objects = models.Manager()
    Published = models.Manager()
    

class Meta:
    ordering = ['-publish']
    indexes = [
        models.Index(fields=['-publish'])
    ]
    # verbose_name = _("Post")
    # verbose_name_plural = _("Posts")

def __str__(self):
    return self.name

# def get_absolute_url(self):
#     return reverse("Post_detail", kwargs={"pk": self.pk})