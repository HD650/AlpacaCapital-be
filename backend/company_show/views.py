from django.db import connection
from django.shortcuts import HttpResponse
import json
import pymysql
from django.shortcuts import redirect
from django.contrib.auth.models import User
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


def user_test(request):
    if request.user.is_authenticated:
        return HttpResponse("OK")
    else:
        return HttpResponse("FAIL")


def get_company_list(request):
    page_num = request.GET.get('page', 1)
    page_num = int(page_num)

    cur = connection.cursor()
    try:
        query = '''SELECT * FROM ncbi.company ORDER BY id limit {0},{1};'''.format(page_num * one_page, one_page)

        result = cur.execute(query)
        rows = cur.fetchall()
        company_raw = []
        for row in rows:
            temp_dict = dict()
            temp_dict['company_name'] = row[1]
            temp_dict['company_description'] = row[2]
            temp_dict['company_location'] = row[3]
            temp_dict['phone'] = row[4]
            temp_dict['fax'] = row[5]
            temp_dict['county'] = row[6]
            temp_dict['region'] = row[7]
            temp_dict['company_type'] = row[8]
            temp_dict['year_founded'] = row[9]
            temp_dict['employment_in_nc'] = row[10]
            temp_dict['us_headquarters'] = row[11]
            temp_dict['global_headquarters'] = row[12]
            company_raw.append(temp_dict)
        json_raw = dict()
        json_raw["data"] = company_raw

        query = '''SELECT count(*) FROM ncbi.company;'''
        cur.execute(query)
        company_num = cur.fetchall()
        json_raw["amount"] = company_num[0][0]

        json_res = json.dumps(company_raw)
    except Exception as e:
        return HttpResponse("INNER ERROR"+str(e))
    finally:
        cur.close()
    return HttpResponse(json_res)
