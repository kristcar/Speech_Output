from django.urls import path  
from . import views  

urlpatterns = [
  path('', views.loginRegister),
  path('register', views.register),
  path('login', views.login),
  path('logout', views.logout),
  path('home', views.home),
  path('typeToSpeak', views.typeToSpeak),
  path('<url>', views.catch_all),
]