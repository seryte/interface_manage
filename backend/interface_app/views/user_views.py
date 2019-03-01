import json
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def login(request):
    return HttpResponse("来了老弟！")