from django.urls import path  
from . import views  

urlpatterns = [
  path('', views.welcome),
  path('login_register', views.loginRegister),
  path('register', views.register),
  path('login', views.login),
  path('logout', views.logout),
  path('home', views.home),
  path('pictureToSpeak', views.picture_speak),
  path('typeToSpeak', views.type_to_speak),
  path('speakToText', views.speak_to_text),
  path('add', views.add),
  path('create', views.create),
  path('edit', views.edit),
  path('delete/<int:speech_id>', views.delete),

  path('<url>', views.catch_all),
]