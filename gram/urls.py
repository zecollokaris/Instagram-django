from django.urls import path
''' 
This is to allow us to connect the PROJECT's  url with this APP's url 
it will then allow us to define paths here as we had included (grams urls)
in the PROJECT.
'''

from . import views
'''
Here we are importing the views as we shall connect templates from there 
'''

from django.conf import settings
'''
This is importing the settings configurations to (gramapp)
'''

from django.conf.urls.static import static
'''
This is to import static-files in urls
'''


'''End Of Import'''
#---------------------------------------------------------------------#

urlpatterns=[



#################################################################################################################################################################################
#URL FOR  HOME PAGE
#################################################################################################################################################################################

    #HOME Page url!
    #This is the home page url pattern 
    path('',views.index, name='index'),

#################################################################################################################################################################################
#URL FOR EXPLORE-PAGE
#################################################################################################################################################################################

    #EXPLORE-Page url!
    
    #This is the Explore page url 
    path('explore',views.explore,name ='explore'),
]