import json

from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from django.views import View

from interface_app import common


class UserViews(View):

    def get(self, request, *args, **kwargs):
        token = request.META.get("HTTP_TOKEN", None)
        if token is None:
            return common.respone_failed("用户未登录")
        else:
            try:
                session = Session.objects.get(pk=token)
            except Session.DoesNotExist:
                return common.respone_failed("用户session失效")
            except Exception as e:
                print(e)
                return common.respone_failed("未知错误")
            else:
                # django的session固定获取用户的id
                user_id = session.get_decoded().get('_auth_user_id', None)
                if user_id is None:
                    return common.respone_failed("用户id已失效")
                try:
                    user = User.objects.get(pk=user_id)
                except User.DoesNotExist:
                    return common.respone_failed("用户不存在")
                else:
                    return common.respone_success({"username": user.username, "user_id": user.id})

    def post(self, request, *args, **kwargs):
        body = request.body
        params = json.loads(body)
        if "name" in params and "" != str(params['name']) and "pwd" in params and "" != str(params['pwd']):
            user = User.objects.create_user(username=str(params["name"]), password=str(params["pwd"]))
            if user:
                login(request, user)
                session = request.session.session_key
                return common.respone_success({"session": session})
            else:
                return common.respone_failed("注册失败")
        else:
            return common.respone_failed("参数不正确")

    def put(self, request, *args, **kwargs):
        body = request.body
        params = json.loads(body)
        if "name" in params and "" != str(params['name']) and "pwd" in params and "" != str(params['pwd']):
            user = authenticate(username=params["name"], password=str(params["pwd"]))
            if user:
                login(request, user)
                session = request.session.session_key
                return common.respone_success({"session": session})
            else:
                return common.respone_failed("登录失败")
        else:
            return common.respone_failed("参数不正确")

    def patch(self, *args, **kwargs):
        return common.respone_success({"method": "patch"})

    def delete(self, *args, **kwargs):
        return common.respone_success({"method": "delete"})
