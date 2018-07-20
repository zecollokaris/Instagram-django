from django.db import models

#Import User method for django
from django.contrib.auth.models import User

#Importing date method
import datetime

#import Image resizers, (Can translate large image to a small one when 
# called in another location where it is needed in a smaller version.)  
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from django.db.models.signals import post_save
from django.dispatch import receiver
'''End Of Import'''
#---------------------------------------------------------------------#


###### Created models here! ######

#...Class PROFILE added here...
class Profile(models.Model):
#Attribute Variables for Profile class to represent different columns in database
    '''
    -profile avator-: (used to resize profile picture which could be 
    used espesially in comment section to display profile photo)
    -bio-: used to describe user using text
    posted by
    -profile pic-: saved to profile picture folder created using django model
    '''

    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=350) 
    profile_pic = models.ImageField(upload_to='ProfilePicture/')
    profile_avatar = ImageSpecField(source='profile_pic',
                                         processors=[ResizeToFill(100, 50)],
                                         format='JPEG''PNG''GIF''JPG',
                                         options={'quality':60})
    date = models.DateTimeField(auto_now_add=True, null= True)  


    '''Method to filter database results'''
    def __str__(self):
        return self.user.user


