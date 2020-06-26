"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import url 
from django.urls import path, include
from blog import views


urlpatterns = [
    path('admin/',admin.site.urls),
    path('blog/',include('blog.urls')),
    url('newuser',views.newuser),
    #url('postsignup',views.postsignup,name='postsignup'),
    url('storepara',views.storepara),
    url('test',views.test),
    #url('print',views.print),
    url('register', views.register, name='register'),
    #url('postsign',views.postsign),
    #url('profile_url',views.profile_url, name='profile_url'),
    #url('persprof', views.persprof,name='persprof'),
    url('section_url',views.section_url, name='section_url'),
    url('loadque',views.loadque,name='loadque')

]
