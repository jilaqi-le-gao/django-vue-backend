from django.urls import path

from . import views

urlpatterns = [
    path('setsession/', views.TestSession, name='setSession'),
    path('showsession/', views.ShowSession, name='ShowSession'),
    path('delsession/', views.DelSession, name='DelSession'),
]