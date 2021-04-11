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
  path('add_image/<int:speech_item_id>', views.add_image),
  path('edit', views.edit),
  path('<url>', views.catch_all),
]