from django.contrib import admin
from django.urls import path, include
from home import views
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns  = [

 path('users/', views.userdata, name='userdata1'),
 path('users/<int:id>', views.userdata, name='userdata2'),
 path('categories/', views.categorydata, name='categorydata1'),
 path('categories/<str:slug>', views.categorydata, name='categorydata2'),
 path('posts/', views.postdata, name='postdata1'),
 path('posts/<str:slug>', views.postdata, name='postdata2'),
 path('comments/', views.commentdata, name='commentdata1'),
 path('comments/<int:id>', views.commentdata, name='commentsdata2'),
 path('reply/', views.replydata, name='replydata1'),
 path('reply/<int:id>', views.replydata, name='replydata2'),
 path('api-token-auth/', obtain_auth_token, name='api_token_auth'),







]
