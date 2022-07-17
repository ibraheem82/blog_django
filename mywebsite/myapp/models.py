# from distutils.command.upload import upload
# from email.quoprimime import unquote
from django.db import models
import uuid
# from ckeditor.fields import RichTextField

from django.urls import reverse

from profiles.models import UserProfile
# Create your models here.

class Post(models.Model):
    
    # A user can have many post
    # anytime a profile is deleted the post that the user has created should also be deleted
    writer = models.ForeignKey(UserProfile, on_delete = models.SET_NULL, null=True, blank = True)
    
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to = 'assets/imgs')
    body = models.TextField()
    # body = RichTextField()
    post_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now = True)
    slug = models.SlugField()
    category = models.ForeignKey('Category', on_delete = models.SET_NULL, blank=True, null=True)
    
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug':self.slug})
    
    
    def get_absolute_url(self):
        return reverse('delete', kwargs={'slug':self.slug})
    
    
    
    
    
    
    def __str__(self):
        return self.title
    
    # A particular category can have= several post
class Category(models.Model):
    title = models.CharField(max_length=100)
    category_id = models.UUIDField(default = uuid.uuid4, primary_key = True, unique = True, editable = False)
    slug = models.SlugField()


    def __str__(self):
        return self.title