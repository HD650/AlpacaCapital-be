from django.contrib import admin
from new_db.models import *


class TargetMarketInline(admin.StackedInline):
    model = TargetMarket
    extra = 1


class TeamMemberInline(admin.StackedInline):
    model = TeamMember
    extra = 1


class CompanyAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    filter_horizontal = ('core_technology', 'product', 'financial', 'offtake_agreements')
    inlines = (TargetMarketInline, TeamMemberInline)
    fieldsets = (
        ('Basic information', {
            'classes': ('collapse',),
            'fields': ('company_name', 'company_logo', 'company_website', 'industrial_sector', 'two_lines_company_summary'),
        }),
        ('Contact information', {
            'classes': ('collapse',),
            'fields': ('contact_information',),
        }),
        ('TPM', {
            'classes': ('collapse',),
            'fields': ('core_technology', 'product'),
        }),
        ('Strategy', {
            'classes': ('collapse',),
            'fields': ('value_proposition', 'business_model_description', 'entry_expansion_strategy', 'strategy_for_setting_barriers'),
        }),
        ('Financial', {
            'classes': ('collapse',),
            'fields': ('financial', 'current_round'),
        }),
        ('Related files', {
            'classes': ('collapse',),
            'fields': ('executive_summary', 'pitch_deck', 'financial_projections', 'business_plan', 'other'),
        }),
        ('Misc', {
            'fields': ('offtake_agreements',),
        }),
    )


admin.site.register(Company, CompanyAdmin)


class OfftakeAgreementsAdmin(admin.ModelAdmin):
    pass

admin.site.register(OfftakeAgreements, OfftakeAgreementsAdmin)


class IndustrialSectorAdmin(admin.ModelAdmin):
    pass


admin.site.register(IndustrialSector, IndustrialSectorAdmin)


class PersonAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)


class IpProtectionAdmin(admin.ModelAdmin):
    pass


admin.site.register(IpProtection, IpProtectionAdmin)


class FDAApprovalStatusAdmin(admin.ModelAdmin):
    pass


admin.site.register(FDAApprovalStatus, FDAApprovalStatusAdmin)


class CoreTechnologyAdmin(admin.ModelAdmin):
    pass


admin.site.register(CoreTechnology, CoreTechnologyAdmin)


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)


class MarketAdmin(admin.ModelAdmin):
    pass


admin.site.register(Market, MarketAdmin)


class FundingStageAdmin(admin.ModelAdmin):
    pass


admin.site.register(FundingStage, FundingStageAdmin)


class OpenFundingAdmin(admin.ModelAdmin):
    pass


admin.site.register(OpenFunding, OpenFundingAdmin)


class TeamMemberAdmin(admin.ModelAdmin):
    pass


admin.site.register(TeamMember, TeamMemberAdmin)


class TargetMarketAdmin(admin.ModelAdmin):
    pass


admin.site.register(TargetMarket, TargetMarketAdmin)
