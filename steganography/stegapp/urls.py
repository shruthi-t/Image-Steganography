from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('encrypt/', views.encrypt_text, name='encrypt_text'),  
    path('decrypt/', views.decrypt_text, name='decrypt_text'),
]
