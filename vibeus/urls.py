from django.urls import path , re_path
from. import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('dashboard/<str:username>/', views.dashboard, name='dashboard'),
    path('chat/', views.chat_view, name='chat'),
    path('chat/<int:user_id>/', views.private_chat_view, name='private_chat'),
    path('map/', views.map, name='map'),


]
