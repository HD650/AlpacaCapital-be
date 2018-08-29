from django.db import models


class IndustrialSector(models.Model):
    id = models.AutoField(primary_key=True)
    sector_name = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return self.sector_name

    class Meta:
        managed = True
        db_table = 'industrial_sector'


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=512, blank=True, null=True)
    title = models.CharField(max_length=512, blank=True, null=True)
    email = models.CharField(max_length=512, blank=True, null=True)
    phone_number = models.CharField(max_length=512, blank=True, null=True)
    company_mailing_address = models.CharField(max_length=512, blank=True, null=True)
    linkedin = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'person'


class IpProtection(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'ip_protection'


class FDAApprovalStatus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'fda_approval_status'


class CoreTechnology(models.Model):
    id = models.AutoField(primary_key=True)
    technology_name = models.CharField(max_length=512, blank=True, null=True)
    technology_description = models.TextField(blank=True, null=True)
    problems_the_technology_solves = models.TextField(blank=True, null=True)
    ip_protection = models.OneToOneField(IpProtection, on_delete=models.CASCADE)
    fda_approval_status = models.OneToOneField(FDAApprovalStatus, on_delete=models.CASCADE)

    def __str__(self):
        return self.technology_name

    class Meta:
        managed = True
        db_table = 'core_technology'


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=512, blank=True, null=True)
    product_description = models.TextField(blank=True, null=True)
    major_competitive_advantage = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.product_name

    class Meta:
        managed = True
        db_table = 'product'


class Market(models.Model):
    id = models.AutoField(primary_key=True)
    market_name = models.CharField(max_length=512, blank=True, null=True)
    market_description = models.TextField(blank=True, null=True)
    unsolved_problem = models.TextField(blank=True, null=True)
    size_of_market = models.CharField(max_length=512, blank=True, null=True)
    targeting_customers = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.market_name

    class Meta:
        managed = True
        db_table = 'market'


class FundingStage(models.Model):
    id = models.AutoField(primary_key=True)
    round_name = models.CharField(max_length=512, blank=True, null=True)
    date_closed = models.DateField(blank=True, null=True)
    amount_raised = models.IntegerField(blank=True, null=True)
    number_of_investors = models.IntegerField(blank=True, null=True)
    lead_investor = models.CharField(max_length=512, blank=True, null=True)
    attorney = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return '%s %s' % (str(self.round_name), str(self.date_closed))

    class Meta:
        managed = True
        db_table = 'founding_stage'


class OpenFunding(models.Model):
    id = models.AutoField(primary_key=True)
    round_name = models.CharField(max_length=512, blank=True, null=True)
    estimated_pre_money_valuation = models.IntegerField(blank=True, null=True)
    amount_of_capital_seeking = models.IntegerField(blank=True, null=True)
    amount_of_equity_selling = models.FloatField(blank=True, null=True)
    projected_monthly_burn_rate = models.IntegerField(blank=True, null=True)
    current_year_revenue = models.IntegerField(blank=True, null=True)
    exit_strategy = models.TextField(blank=True, null=True)

    def __str__(self):
        return '%s %s' % (str(self.round_name), str(self.estimated_pre_money_valuation))

    class Meta:
        managed = True
        db_table = 'open_funding'


class OfftakeAgreements(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.IntegerField(blank=True, null=True)
    buyer = models.OneToOneField('Company', on_delete=models.CASCADE, blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return "%s %s %s " % (str(self.buyer.company_name), str(self.amount), str(self.delivery_date))

    class Meta:
        managed = True
        db_table = 'offtake_agreements'


# Create your models here.
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    # Basic information
    company_name = models.CharField(max_length=512)
    company_logo = models.CharField(max_length=1024, blank=True, null=True)
    company_website = models.CharField(max_length=512, blank=True, null=True)
    industrial_sector = models.OneToOneField(IndustrialSector, on_delete=models.CASCADE, blank=True, null=True)
    two_lines_company_summary = models.TextField(blank=True, null=True)
    # founding_stage (calculate in the runtime)
    year_founded = models.IntegerField(blank=True, null=True)
    number_of_employees = models.IntegerField(blank=True, null=True)
    product_or_service_development_status = models.CharField(max_length=128, blank=True, null=True)
    product_TRI = models.IntegerField(blank=True, null=True)

    # Contact information
    contact_information = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='contact_person', blank=True, null=True)

    # Team
    team = models.ManyToManyField(Person, through='TeamMember', blank=True, null=True)

    # TPM
    core_technology = models.ManyToManyField(CoreTechnology, blank=True, null=True)
    product = models.ManyToManyField(Product, blank=True, null=True)
    market = models.ManyToManyField(Market, through='TargetMarket', blank=True, null=True)

    # Strategy
    value_proposition = models.TextField(blank=True, null=True)
    business_model_description = models.TextField(blank=True, null=True)
    entry_expansion_strategy = models.TextField(blank=True, null=True)
    strategy_for_setting_barriers = models.TextField(blank=True, null=True)

    # Financial
    financial = models.ManyToManyField(FundingStage, blank=True, null=True)
    current_round = models.OneToOneField(OpenFunding, on_delete=models.CASCADE, blank=True, null=True)
    # total_amount_raised (calculate in the runtime)

    offtake_agreements = models.ManyToManyField(OfftakeAgreements, blank=True, null=True)

    # Related files
    executive_summary = models.CharField(max_length=1024, blank=True, null=True)
    pitch_deck = models.CharField(max_length=1024, blank=True, null=True)
    financial_projections = models.CharField(max_length=1024, blank=True, null=True)
    business_plan = models.CharField(max_length=1024, blank=True, null=True)
    other = models.CharField(max_length=1024, blank=True, null=True)

    def __str__(self):
        return self.company_name

    class Meta:
        managed = True
        db_table = 'company'
        permissions = (('visitor', 'see basic info'),
                       ('membership', 'see most info'),
                       ('admin', 'see all info'))


class TeamMember(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    share = models.IntegerField()
    title = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return '%s %s %s\%' % (str(self.person.name), str(self.title), str(self.share))

    class Meta:
        managed = True
        db_table = 'team_member'


class TargetMarket(models.Model):
    id = models.AutoField(primary_key=True)
    market_name = models.ForeignKey(Market, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    advantage = models.CharField(max_length=512, blank=True, null=True)
    disadvantage = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return self.market_name.market_name

    class Meta:
        managed = True
        db_table = 'target_market'
