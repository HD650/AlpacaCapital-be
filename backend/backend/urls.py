"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import company_show.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', company_show.views.index_page, name='index'),
    path('get_company_list/', company_show.views.get_company_list),
    path('', company_show.views.index_page, name='home'),
    path('user_test/', company_show.views.user_test),
    path('log_in/', company_show.views.log_in),
    path('new_user/', company_show.views.new_user),
    path("log_out/", company_show.views.log_out),
]


# code only run once to setup the user group, permission data
#from django.contrib.auth.models import User, Group, Permission, ContentType
#groups = ["test1", "test2"]
#permission = [["play", "save"], ["load"]]
#for i, name in enumerate(groups):
#    group_temp, test = Group.objects.get_or_create(name=name)
#    for permission_name in permission[i]:
#        ct, test = ContentType.objects.get_or_create(app_label="company_show", model="whatever")
#        if not Permission.objects.filter(codename=permission_name).exists():
#            permission_temp = Permission.objects.create(codename=permission_name,
#                                                        name=permission_name+" permission", content_type=ct)
#            group_temp.permissions.add(permission_temp)

# user = User.objects.get(username="axios@test.com")
# group_temp = Group.objects.get(name='test1')
# group_temp.user_set.add(user)
#
# user = User.objects.get(username="test.ncsu.edu")
# group_temp = Group.objects.get(name='test2')
# group_temp.user_set.add(user)
#
# temp = User.objects.get(username="axios@test.com")
#
# if temp.has_perm('company_show.play'):
#     print("pass")








