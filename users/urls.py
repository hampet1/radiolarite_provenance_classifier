from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [

    path('',views.index, name="home"),
    path('guideline/', views.guideline, name='guideline'),  # Guideline page
    path('about/', views.about, name='about'),  # About project page
    path('maps/', views.maps, name='maps'),  # Maps page
    path('classify/', views.classify, name='classify'),  # Maps page
]
