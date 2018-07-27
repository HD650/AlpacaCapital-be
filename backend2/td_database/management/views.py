from django.http import HttpResponse
from management.models import CompanyDetail, Investor, Founder, ChineseCollaborator, Category
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
import json
import codecs
import csv

english_keys = ['company_name',
                'description',
                'hq_location',
                'logo',
                'found_time',
                'financing_stage',
                'employee_count',
                'site_url',
                'linkedin_url',
                'facebook_url',
                'company_contact',
                'business_description',
                'main_products',
                'capability_maturity',
                'capability_maturity_des',
                'technology_leadership',
                'technology_leadership_des',
                'key_capability_assessment_ai',
                'key_capability_assessment_ai_des',
                'key_capability_assessment_flexibility_and_openness',
                'key_capability_assessment_flexibility_and_openness_des',
                'key_capability_assessment_performance_and_scalability',
                'key_capability_assessment_performance_and_scalability_des',
                'comprehensive_assessment',
                'collaborate_with_chinese_company',
                'td_cooperation_status',
                'matching_direction_with_td',
                'key_person_interview']


# Create your views here.
def import_data(request):
    count = 0
    with codecs.open('./data.csv', 'r', 'utf-8') as data_file:
        reader = csv.reader(data_file)
        for i, row in enumerate(reader):
            if i == 0:
                raw_keys = row
            else:
                data_row = dict(zip(raw_keys, row))
                # check founder
                founders = data_row["创始人"].split("\n")
                if founders[0] == '':
                    founders = []
                founders_models = []
                for founder in founders:
                    if Founder.objects.filter(name=founder).exists():
                        pass
                    else:
                        # new founder
                        Founder.objects.create(name=founder)
                    founders_models.append(Founder.objects.get(name=founder))

                # check investor
                investors = data_row["投资者"].split("\n")
                if investors[0] == '':
                    investors = []
                investors_models = []
                for investor in investors:
                    if Investor.objects.filter(name=investor).exists():
                        pass
                    else:
                        # new investor
                        Investor.objects.create(name=investor)
                    investors_models.append(Investor.objects.get(name=investor))

                # check category
                categories = data_row["公司品类"].split("\n")
                if categories[0] == '':
                    categories = []
                categories_models = []
                for category in categories:
                    if Category.objects.filter(category=category).exists():
                        pass
                    else:
                        # new category
                        Category.objects.create(category=category)
                    categories_models.append(Category.objects.get(category=category))

                # check collaborator
                collaborators = data_row["与哪些中国企业合作"].split("\n")
                if collaborators[0] == '':
                    collaborators = []
                collaborators_models = []
                for collaborator in collaborators:
                    if ChineseCollaborator.objects.filter(collaborator_name=collaborator).exists():
                        pass
                    else:
                        # new collaborator
                        ChineseCollaborator.objects.create(collaborator_name=collaborator)
                        collaborators_models.append(ChineseCollaborator.objects.get(collaborator_name=collaborator))

                # add a company detail
                del data_row['创始人']
                del data_row['投资者']
                del data_row['公司品类']
                del data_row['与哪些中国企业合作']
                row = data_row.values()
                data_row = dict(zip(english_keys, row))

                if data_row['collaborate_with_chinese_company'] == '是':
                    data_row['collaborate_with_chinese_company'] = True
                else:
                    data_row['collaborate_with_chinese_company'] = False

                for key in data_row:
                    if data_row[key] == '':
                        data_row[key] = None

                if not CompanyDetail.objects.filter(company_name=data_row['company_name']).exists():
                    temp = CompanyDetail.objects.create(**data_row)
                    count += 1
                    for f in founders_models:
                        temp.founder.add(f)
                    for i in investors_models:
                        temp.investor.add(i)
                    for c in categories_models:
                        temp.category.add(c)
                    for cc in collaborators:
                        temp.chinese_collaborator.add(cc)
                    temp.save()

    return HttpResponse("import %d companies" % count)


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


