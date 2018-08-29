from django.db import connection
from django.shortcuts import HttpResponse
import json
import pymysql
from django.shortcuts import redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout

one_page = 50


def index_page(request):
    return redirect('/AlpacaCapital-fe/index.html')


def log_in(request):
    if request.method == "POST":
        email = request.POST.get("email", "")
        passwd = request.POST.get("password", "")
        # no data in the form, try body
        if email == "" or passwd == "":
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            email = body['email']
            passwd = body['password']
        if email == "" or passwd == "":
            return HttpResponse("FAIL")
        login_user = authenticate(username=email, password=passwd)
        if login_user is not None:
            if login_user.is_active:
                request.session.set_expiry(86400)
                login(request, login_user)
                return HttpResponse("OK")
    return HttpResponse("FAIL")


def log_out(request):
    try:
        logout(request)
        return HttpResponse("OK")
    except Exception:
        return HttpResponse("FAIL")


def new_user(request):
    if request.method == "POST":
        email = request.POST.get("email", "")
        passwd = request.POST.get("password", "")
        # no data in the form, try body
        if email == "" or passwd == "":
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            email = body['email']
            passwd = body['password']
        if email == "" or passwd == "":
            return HttpResponse("FAIL")
        if User.objects.filter(username=email).exists():
            return HttpResponse("ALREADY EXISTS")
        new_created_user = User.objects.create_user(username=email, password=passwd)

        if new_created_user is not None:
            return HttpResponse("OK")
        else:
            return HttpResponse("FAIL")


def user_group(request):
    if request.method == "POST":
        user = request.user
        my_group = Group.objects.get(name='my_group_name')
        my_group.user_set.add(user)
        return HttpResponse("OK")
    else:
        return HttpResponse("FAIL")


def user_test(request):
    if request.user.is_authenticated:
        return HttpResponse("OK")
    else:
        return HttpResponse("FAIL")


def get_company_list(request):
    page_num = request.GET.get('page', 1)
    page_num = int(page_num)
    try:
    
        json_raw["amount"] = company_num[0][0]

        json_res = json.dumps(company_raw)
    except Exception as e:
        return HttpResponse("INNER ERROR"+str(e))
    return HttpResponse(json_res)


def get_company_detail(request):
    if request.user.is_authenticated:
        pass
    else:
        return HttpResponse("USER NOT LOGIN")
