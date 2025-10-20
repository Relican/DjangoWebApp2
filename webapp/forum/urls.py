from django.contrib import admin
from django.urls import path

from .views import index, details, create_topic, create, add, register, register_user, login, login_page, logout_view

urlpatterns = [
    path('', index, name = "index"),
    path('<int:topic_id>/', details, name = "details"),
    path('create_topic.html', create_topic , name = "create_topic"),
    path('create/', create, name="create"),
    path('<int:topic_id>/add/', add, name = "add"),
    path('register.html', register, name = "register"),
    path('register/', register_user, name="register_user"),
    path('login.html', login_page, name="login_page"),
    path('login/', login, name="login"),
    path('logout/', logout_view, name="logout")
]