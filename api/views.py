from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home(request):
  pass

def users_index(request):
  users = [
    { 'id': 1, 'name': 'John Doe', 'email': 'jdoe@gmail.com' },
    { 'id': 2, 'name': 'Jane Doe', 'email': 'jane@gmail.com' },
    { 'id': 3, 'name': 'Steve Smith', 'email': 'ssmith@gmail.com' },
  ]

  return JsonResponse(users, safe=False)
