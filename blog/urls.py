from django.urls import path
from . import views



urlpatterns = [
    path('post/<str:slug>/edit/', views.post_edit, name='post_edit'),
    path('category/<str:slug>/', views.category, name='category'),
    path('post/new/', views.post_new, name='postnew'),
    path('post/<str:slug>/', views.post_detail, name='post_detail'),
    path('login/', views.user_login, name='user-login'),
    path('signup/', views.signup, name='sign-up'),
    path('cust-logout/', views.signout, name='log-out'),
    path('user/<int:user_id>/', views.userdetail, name='userdetail'),
    path('upload-profile-photo/', views.upload_profile_photo, name='uploadprofilephoto'),
    path('comment/', views.comment, name='comment'),
    path('reply/', views.reply, name='reply'),
    path('', views.post_list, name='post_list'),
    
]