from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name = "home"),
        path('about/', views.about, name = "about"),
        path('meet_the_team/', views.members, name = "members"),
        path('contact/', views.contact, name = "contact"),
]
