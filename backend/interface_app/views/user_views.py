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
from interface_app.form.user import UserForm
from interface_app.my_exception import MyException


class UserViews(View):

    def get(self, request, *args, **kwargs):
        # raise MyException("test啊")
        token = request.META.get("HTTP_TOKEN", None)
        print(token)
        if token is None:
            raise MyException("用户未登录")
        else:
            try:
                session = Session.objects.get(pk=token)
            except Session.DoesNotExist:
                raise MyException("用户session失效")
            else:
                # django的session固定获取用户的id
                user_id = session.get_decoded().get('_auth_user_id', None)
                if user_id is None:
                    raise MyException("用户id已失效")
                try:
                    user = User.objects.get(pk=user_id)
                except User.DoesNotExist:
                    raise MyException("用户不存在")
                else:
                    return common.respone_success({"username": user.username,
                                                   "user_id": user.id})

    def post(self, request, *args, **kwargs):
        body = request.body
        params = json.loads(body)
        form = UserForm(params)
        result = form.is_valid()
        if result:
            user = User.objects.create_user(username=form.cleaned_data["username"],
                                            password=form.cleaned_data["password"])
            if user:
                login(request, user)
                session = request.session.session_key
                return common.respone_success({"session": session})
            else:
                raise MyException("注册失败")
        else:
            print(form.errors.as_json())
            raise MyException(form.errors.as_json())

    def put(self, request, *args, **kwargs):
        body = request.body
        params = json.loads(body)
        form = UserForm(params)
        result = form.is_valid()
        if result:
            user = authenticate(username=params["username"],
                                password=str(params["password"]))
            if user:
                login(request, user)
                session = request.session.session_key
                return common.respone_success({"msg": "登录成功",
                                               "session": session})
            else:
                raise MyException("登录失败")
        else:
            print(form.errors.as_json())
            raise MyException(form.errors.as_json())
