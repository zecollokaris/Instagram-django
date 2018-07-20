"""insta URL Configuration"""

from django.contrib import admin

from django.urls import path, include
'''Here we have imported (include)-: this allows us to add the gram url pattern
as done below this is to avoid filling up all our urls in this page'''

''' End Of Import'''
#-------------------------------#


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('gram.urls')),

]
