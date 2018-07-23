from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf.urls.static import static
from django.contrib.auth.models import User
from . import models

from django.core.mail import send_mail
'''
send mail enables sends confirmation mail using @gmail
'''


#The @login_required declarator limits access of view function to only 
#authenticated users

'''End Of Import'''
#---------------------------------------------------------------------#

# VIEW FUNCTIONS HERE!



#################################################################################################################################################################################
#LOGIN PAGE VIEW FUNCTION
#################################################################################################################################################################################

#Login page view function
def login(request):
    return render(request, 'registration/login.html')
    
#################################################################################################################################################################################
#HOME PAGE VIEW FUNCTION
#################################################################################################################################################################################

#Home page view function
def index(request):
    return render(request, 'display/home.html',)

#################################################################################################################################################################################
#EXPLORE PAGE VIEW FUNCTION
#################################################################################################################################################################################

#Explore page view function
def explore(request):
    return render(request, 'display/explore.html')

#################################################################################################################################################################################
#NOTIFICATION PAGE VIEW FUNCTION
#################################################################################################################################################################################

#Notification page view function
def notification(request):
    return render(request, 'display/notification.html')

#################################################################################################################################################################################
#PROFILE PAGE VIEW FUNCTION
#################################################################################################################################################################################

#Profile page view function
def profile(request):
    return render(request, 'display/userprofile.html')
