from django.urls import path

from api import views

urlpatterns = [
    path('', views.PostView.as_view(), name='home')
]
