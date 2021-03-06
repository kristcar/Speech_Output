from django.db import models
import re
from datetime import datetime
from django.core.exceptions import ValidationError


#*********************LOGIN AND REGISTRATION***********************
class UserManager(models.Manager):
  def register_validator(self, postData):
    errors = {}
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

    if not EMAIL_REGEX.match(postData['email']) and len(postData['email']) != 0:
      errors['email'] = "Invalid email address format"

    if len(postData['first_name']) < 2 and len(postData['first_name']) != 0:
      errors['first_name_short'] = "First name must be at least 2 characters"

    if len(postData['last_name']) < 2 and len(postData['last_name']) != 0:
      errors['last_name_short'] = "Last name must be at least 2 characters"
      
    if len(postData['password']) < 8 and len(postData['password']) != 0:
      errors['password_short'] = "Password must be at least 8 characters"

    if postData['password'] != postData['conf_password']:
      errors['match'] = "Passwords do not match"

    for user in User.objects.all():
      if user.email == postData['email']:
        errors['email_exists'] = "An account with this email address exists already."

    if len(postData['first_name']) ==0 or len(postData['last_name']) ==0 or len(postData['email']) ==0 or len(postData['password']) == 0 or len(postData['conf_password']) == 0:
      errors['empty_fields'] = "Please fill out all Registration fields."

    return errors

  def login_validator(self, postData):
    errors = {}
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

    if not EMAIL_REGEX.match(postData['email']) and len(postData['email']) != 0:
      errors['login_email'] = "Invalid email address format"

    if len(postData['email']) == 0 or len(postData['password']) == 0 :
      errors['login_email_password_empty'] = "Please enter both an email and a password."

    return errors
#************************END LOGIN AND REGISTRATION*******************

class User(models.Model):
  first_name = models.CharField(max_length = 200)
  last_name = models.CharField(max_length = 200)
  email = models.TextField()
  password = models.CharField(max_length = 200)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now = True)
  objects = UserManager()


class SpeechManager(models.Manager):
  def speech_validator(self, postData):
    errors = {}
    if len(postData['saying']) > 300:
      errors['saying_long'] = "Name is too long"
    if len(postData['saying']) == 0 or len(postData['url']) == 0:
      errors['saying_url_empty'] = "Please enter both a saying and an image URL."
    return errors

class Speech_Item(models.Model):
  saying = models.CharField(max_length = 300, default = "");
  url = models.CharField(max_length = 300, default = "");
  creator = models.ForeignKey(User, related_name = "user_speech_item", on_delete = models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now = True)
  objects = SpeechManager()

