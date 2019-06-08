from django.shortcuts import render
# IMPORT DJANGO AUTH
from django.contrib import auth
# IMPORT DJANGO USER MODEL
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

@csrf_exempt
def register(request):
  if request.method == 'POST':
    data = json.loads(request.body)
    # print('Request = ', data['name'])
    # Get values
    first_name = data['first_name']
    last_name = data['last_name']
    username = data['username']
    email = data['email']
    password = data['password']
    password2 = data['password2']
     # Check if passwords match
    if password == password2:
      # Check if username exists
      if User.objects.filter(email=email).exists():
          return JsonResponse({'status': 400, 'message': 'That username has already been registered. Please try a different username'})
      else:
        # Register User
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        user.save()
        return JsonResponse({'status': 200, 'message': 'Registration success'}, status=200)
    else:
      return JsonResponse({'status': 400, 'message': 'Passwords do not match'}, status=400)
  else:
    return JsonResponse({'status': 400, 'message': 'Bad Request. Please try again'}, status=400)


@csrf_exempt
def login(request):
  if request.method == 'POST':
    data = json.loads(request.body)
    username = data['username']
    password = data['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      return JsonResponse({'status': 200, 'message': 'Login success', 'user': model_to_dict(user)['id']}, status=200)
    else:
      return JsonResponse({'status': 400, 'message': 'Invalid credentials'}, status=400)

  else:
    return JsonResponse({'status': 400, 'message': 'Bad Request. Please try again'}, status=400)


@csrf_exempt
def logout(request):
  auth.logout(request)
  return JsonResponse({'status': 200, 'message': 'Logout successful'}, status=200)
