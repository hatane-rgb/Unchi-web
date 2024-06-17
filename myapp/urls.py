from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index_template, name='index_template'),
    path('timeline/', views.timeline_view, name='timeline_view'),
    path('logout/', views.custom_logout, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
]