from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.core.serializers import serialize
import json
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home(request):
  pass


def users_index(request):
  if request.user.is_authenticated:
    print(request.headers['cookie'])
    users = list(User.objects.values())
    # print(users)
    return JsonResponse({'data': users}, status=200)
  else:
    return JsonResponse({'status': 401, 'message': 'Not authorized'}, status=401)



def users_show(request, pk):
  if request.user.is_authenticated:
    user = User.objects.get(id=pk)
    user = model_to_dict(user)
    # print(users)
    return JsonResponse({'data': user}, status=200)
  else:
    return JsonResponse({'status': 401, 'message': 'Not authorized'}, status=401)
