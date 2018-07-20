from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf.urls.static import static
from django.contrib.auth.models import User
from . import models



#The @login_required declarator limits access of view function to only 
#authenticated users

'''End Of Import'''
#---------------------------------------------------------------------#

# VIEW FUNCTIONS HERE!




#################################################################################################################################################################################
#HOME PAGE VIEW FUNCTION
#################################################################################################################################################################################

#Home page view function
def index(request):
    return render(request, 'display/home.html',)
