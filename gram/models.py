from django.db import models

#Import User method for django
from django.contrib.auth.models import User

#Importing date method
import datetime

#import Image resizers, (Can translate large image to a small one when 
# called in another location where it is needed in a smaller version.)  



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
    profile_avatar = models.ImageField(upload_to='AvatorPicture/')
    date = models.DateTimeField(auto_now_add=True, null= True)  


    '''Method to filter database results'''
    def __str__(self):
        return self.profile.user



#################################################################################################################################################################################################################################

#...Class IMAGE added here...


class Image(models.Model):
#Attribute Variables for Image class to represent different columns in database 
    '''
    -image_uploader-: (this is the profile of person, uploading the image which is ,-linked to profile using 
    foreign key,-which is then linked to imported user at the top (for ease in querying the database the image creator
    is used which is linked directly to user)

    -image_likes-: This is attribute created with a (ManyToManyField)-to allow many users to like one picture

    -image_comments-: This is attribute created with a (ManyToManyField)-to allow many users to comment on one picture and still get their profiles

    -date-: imported as a django relative import ('from django.contrib.auth.models import User'))
        set to auto using python model, this allows for date to be added automaticaly

    -imageuploader_profile-: this is the person who posted the picture (User)
        '''
    image = models.ImageField(upload_to ='pictsagram/')
    image_caption = models.CharField(max_length=700)
    tag_someone = models.CharField(max_length=50,blank=True)
    imageuploader_profile = models.ForeignKey(User, on_delete=models.CASCADE,null='True', blank=True)
    image_likes = models.ManyToManyField('Profile', default=False, blank=True, related_name='likes')
    date = models.DateTimeField(auto_now_add=True, null= True)

    '''Method to filter database results'''
    def __str__(self):
        return self.image_caption


#################################################################################################################################################################################################################################



#...Class Comments added here...


class Comments (models.Model):
#Attribute Variables for COMMENTS class to represent different columns in database
    '''
    -comment-: this is the commentstext which will be uploaded
    -author-: this is the writer of the comment
    -commented_image-: this is the image that has been commented on
    date-: this is the date the comment was posted
    '''
    comment_post = models.CharField(max_length=150)
    author = models.ForeignKey('Profile',related_name='commenter' , on_delete=models.CASCADE)
    commented_image = models.ForeignKey('Image', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    '''Method to filter database results'''
    def __str__(self):
        return self.author
    



#################################################################################################################################################################################################################################

