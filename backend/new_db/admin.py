from django.contrib import admin
from new_db.models import IndustrialSector, Person, IpProtection, FDAApprovalStatus, CoreTechnology, Product, Market, FundingStage, OpenFunding, Company, TeamMember, TargetMarket


class TargetMarketInline(admin.StackedInline):
    model = TargetMarket
    extra = 1


class TeamMemberInline(admin.StackedInline):
    model = TeamMember
    extra = 1


class CompanyAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    filter_horizontal = ('core_technology', 'product', 'financial')
    inlines = (TargetMarketInline, TeamMemberInline)


admin.site.register(Company, CompanyAdmin)


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
