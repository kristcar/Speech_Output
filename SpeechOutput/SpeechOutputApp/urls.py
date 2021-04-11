from django.urls import path  
from . import views  

urlpatterns = [
  path('', views.loginRegister),
  path('register', views.register),
  path('login', views.login),
  path('logout', views.logout),
  path('home', views.pictureSpeak),
  path('typeToSpeak', views.typeToSpeak),
  path('add', views.add),
  path('create', views.create),
  path('edit', views.edit),
  path('delete/<int:speech_id>', views.delete)
  path('<url>', views.catch_all),
]