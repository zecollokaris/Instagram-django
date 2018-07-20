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


