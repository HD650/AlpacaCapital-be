"""td_database URL Configuration

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
from management.views import user_group, user_test, new_user, log_in, log_out

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('import_data', import_data),
    path('user_test/', user_test),
    path('log_in/', log_in),
    path('new_user/', new_user),
    path("log_out/", log_out),
]
