from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
import uuid


from django.urls import reverse



# Create 

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    username = models.CharField(max_length = 200)
    profession = models.CharField(max_length = 200)
    picture = models.ImageField(upload_to =  'assets/imgs', blank = True, null = True)
    about = models.TextField()
    profile_id = models.UUIDField(default = uuid.uuid4, editable=False, unique=True, primary_key=True)


     
    # def get_absolute_url(self):
    #         return reverse('detail', kwargs={'slug':self.slug})
    
    
    # def get_absolute_url(self):
    #     return reverse('delete', kwargs={'slug':self.slug})








    def __str__(self):
        return self.username
        

