import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from interface_app import common


def register_user(request):
    if "POST" == request.method:
        body = request.body
        params = json.loads(body)
        print(body)
        if "name" in params and "" != str(params['name']) and "pwd" in params and "" != str(params['pwd']):
            user = User.objects.create_user(username=str(params["name"]), password=str(params["pwd"]))
            if user:
                login(request, user)
                return common.respone_success("注册成功")
            else:
                return common.respone_failed("注册失败")
        else:
            return common.respone_failed("参数不正确")
    else:
        return HttpResponse(status=404)


def login_user(request):
    if "POST" == request.method:
        body = request.body
        params = json.loads(body)
        print(body)
        if "name" in params and "" != str(params['name']) and "pwd" in params and "" != str(params['pwd']):
            user = authenticate(username=params["name"], password=str(params["pwd"]))
            if user:
                login(request, user)
                return common.respone_success("登录成功")
            else:
                return common.respone_failed("登录失败")
        else:
            return common.respone_failed("参数不正确")
    else:
        return HttpResponse(status=404)
