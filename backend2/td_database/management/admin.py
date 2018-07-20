from django.contrib import admin
from management.models import CompanyDetail, Founder, Investor, Category, ChineseCollaborator


# Register your models here.
class CompanyDetailAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    search_fields = ('company_name', 'description', 'hq_location', 'founder')
    list_display = ('company_name', 'description', 'hq_location', 'found_time')


admin.site.register(CompanyDetail, CompanyDetailAdmin)
admin.site.register(Founder)
admin.site.register(Investor)
admin.site.register(Category)
admin.site.register(ChineseCollaborator)
