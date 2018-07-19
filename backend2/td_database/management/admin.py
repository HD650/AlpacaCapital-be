from django.contrib import admin
from management.models import CompanyDetail, Founder, Investor, Category, ChineseCollaborator

# Register your models here.

class CompanyDetailAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    

admin.site.register(CompanyDetail, CompanyDetailAdmin)
admin.site.register(Founder)
admin.site.register(Investor)
admin.site.register(Category)
admin.site.register(ChineseCollaborator)
