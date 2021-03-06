from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
import bcrypt

#************************LOGIN AND REGISTRATION********************

def loginRegister(request):
  return render(request, 'loginReg.html')


def register(request):
  if request.method == "POST":
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0: 
      for key, value in errors.items():
        messages.error(request, value)
      return redirect("/login_register")
    else: 
      hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
      print(hashed_pw)
      user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password=hashed_pw)
      request.session['user_id'] = user.id
      return redirect('/home')
  else:
    return redirect('/login_register')
    

def login(request):
  if request.method == 'POST':
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0: 
      for key, value in errors.items():
        messages.error(request, value)
      return redirect("/login_register")
    user = User.objects.filter(email=request.POST['email']) 
    if len(user) > 0:
      user = user[0]
      if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        request.session['user_id'] = user.id
        return redirect('/home')
  messages.error(request, "Email or password is incorrect")
  return redirect('/login_register')


def logout(request):
  request.session.clear()
  return redirect('/')

#********************END LOGIN AND REGISTRATION*********************

def catch_all(request, url):
  return redirect('/')

def welcome(request):
  return render(request, "welcome.html")

def type_to_speak(request):
  if "user_id" not in request.session: 
    messages.error(request, "Please log in or register")
    return redirect('/login_register')
  context = {
    "current_user": User.objects.get(id = request.session['user_id']),
  }
  return render(request,"typeToSpeak.html", context)

def picture_speak(request):
  if "user_id" not in request.session: 
    messages.error(request, "Please log in or register")
    return redirect('/login_register')
  context = {
    "current_user": User.objects.get(id = request.session['user_id']),
    "all_speech_items": Speech_Item.objects.all(),
  }
  return render(request, 'picToSpeak.html', context)

def speak_to_text(request):
  if "user_id" not in request.session: 
    messages.error(request, "Please log in or register")
    return redirect('/login_register')  
  context = {
    "current_user": User.objects.get(id = request.session['user_id']),
  }
  return render(request, "speakToText.html", context)

def home(request):
  if "user_id" not in request.session: 
    messages.error(request, "Please log in or register")
    return redirect('/login_register')
  context = {
    "current_user": User.objects.get(id = request.session['user_id']),
  }
  return render(request, 'home.html', context)

def add(request):
  if "user_id" not in request.session: 
    messages.error(request, "Please log in or register")
    return redirect('/login_register')
  context = {
    "current_user": User.objects.get(id = request.session['user_id']),
  }
  return render(request, "add.html", context)

def edit(request):
  if "user_id" not in request.session: 
    messages.error(request, "Please log in or register")
    return redirect('/login_register')
  context = {
    "all_speech_items": Speech_Item.objects.all(),
    "current_user": User.objects.get(id = request.session['user_id']),
  }
  return render(request, "edit.html", context)

def create(request):
  if "user_id" not in request.session: 
    messages.error(request, "Please log in or register")
    return redirect('/login_register')
  if request.method == "POST":
    errors = Speech_Item.objects.speech_validator(request.POST)
    if len(errors) > 0: 
      for key, value in errors.items():
        messages.error(request, value)
      return redirect("/add")
    else: 
      speech_item = Speech_Item.objects.create(
        saying = request.POST['saying'], 
        url = request.POST['url'],
        creator = User.objects.get(id = request.session['user_id']),
        )
      return redirect("/pictureToSpeak")

def delete(request, speech_id):

  if "user_id" not in request.session: 
    messages.error(request, "Please log in or register")
    return redirect('/login_register')

  #verify speech_id passed is valid
  speech_items_with_id = Speech_Item.objects.filter(id = speech_id)
  if len(speech_items_with_id) == 0: #not in database
    return redirect('/edit')

  if request.method == "POST":
    speech_item_to_delete=Speech_Item.objects.filter(id = speech_id)
    speech_item_to_delete.delete()

  return redirect("/edit")  

