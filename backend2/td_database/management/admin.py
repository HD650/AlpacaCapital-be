from django.contrib import admin
from management.models import *


# Register your models here.
class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1


class RankInline(admin.StackedInline):
    model = Rank
    extra = 1


class TeamMemberInline(admin.StackedInline):
    model = TeamMember
    extra = 1


class CompanyAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    search_fields = ('company_name', 'hq_location', 'tag__name', 'investor__name', 'team__name', 'category__category')
    list_display = ('company_name', 'description', 'hq_location', 'found_time')
    filter_horizontal = ('category', 'chinese_collaborator', 'competitor', 'tag', 'investor')
    inlines = (CommentInline, RankInline, TeamMemberInline)


class TopBoardAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'


class PersonAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'


class InvestorAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'


class InvestmentAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'


admin.site.register(Company, CompanyAdmin)
admin.site.register(TopBoard, TopBoardAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Investor, InvestorAdmin)
#admin.site.register(Investment, InvestorAdmin)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(ChineseCollaborator)
