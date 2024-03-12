from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [

    path('home/',views.index, name="home"),
    path('guideline/', views.guideline, name='guideline'),  # Guideline page
    path('about/', views.about, name='about'),  # About project page
    path('maps/', views.maps, name='maps'),  # Maps page
    path('classify/', views.classify, name='classify'),  # Maps page
    path('process-elements-form/', views.process_elements_form, name='process_elements_form'),
    path('test-ajax/', views.test_ajax, name='test_ajax'),

]
