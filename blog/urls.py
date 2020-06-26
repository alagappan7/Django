from django.urls import path
from . import views

urlpatterns = [
    
    
    
    path('scores/', views.scores, name='scores'),
    path('exam/', views.exam, name='exam'),
    path('register/register1', views.register, name='register1'),
    path('register/', views.register, name='register'),
    #path('sign/postsign',views.postsign,name='postsign'),
    path('signup/',views.signup,name= 'signup'),
    path('test/',views.test),
    #path('print/',views.test),
    path('sign/', views.signIn,name='signIn'),
    #path('login', views.login, name='login'),
    path('', views.post_list, name='post_list'),
    #path('click/',views.click,name='click'),
    path('profile_url/',views.profile_url, name='profile_url'),
    path('persprof', views.persprof,name='persprof'),
    
    
]  

