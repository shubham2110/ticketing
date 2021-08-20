from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def Authenticate(request):
    username, password =(request.POST)['username'] , (request.POST)['password']
    if username == password:
        return HttpResponse("true", status=201)
    else:
        return HttpResponse("false", status=201)