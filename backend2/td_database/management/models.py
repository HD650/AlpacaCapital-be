from django.db import models


# Create your models here.
class Collaboration(models.Model):
    id = models.IntegerField(primary_key=True)
    company_a = models.ForeignKey('CompanyDetail', models.DO_NOTHING, db_column='company_a', blank=True, null=True)
    company_b = models.ForeignKey('Collaborator', models.DO_NOTHING, db_column='company_b', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collaboration'


class Collaborator(models.Model):
    id = models.IntegerField(primary_key=True)
    collaborator_name = models.CharField(max_length=512, blank=True, null=True)
    contact = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collaborator'


class Investment(models.Model):
    id = models.IntegerField(primary_key=True)
    company = models.ForeignKey(CompanyDetail, models.DO_NOTHING, blank=True, null=True)
    investor = models.ForeignKey('Investor', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'investment'


class Investor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    contact = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'investor'


class CompanyDetail(models.Model):
    id = models.AutoField(primary_key=True)
    main_products = models.TextField(blank=True, null=True)
    company_name = models.CharField(max_length=512)
    description = models.TextField(blank=True, null=True)
    hq_location = models.CharField(max_length=512, blank=True, null=True)
    logo = models.TextField(blank=True, null=True)
    found_time = models.DateField(blank=True, null=True)
    founder = models.CharField(max_length=256, blank=True, null=True)
    financing_stage = models.CharField(max_length=45, blank=True, null=True)
    employee_count = models.IntegerField(blank=True, null=True)
    site_url = models.CharField(max_length=512, blank=True, null=True)
    linkedin_url = models.CharField(max_length=512, blank=True, null=True)
    facebook_url = models.CharField(max_length=512, blank=True, null=True)
    contact = models.CharField(max_length=512, blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)
    business_description = models.TextField(blank=True, null=True)
    capability_maturity = models.IntegerField(blank=True, null=True)
    technology_leadership = models.IntegerField(blank=True, null=True)
    key_capability_assessment_ai = models.IntegerField(db_column='key_capability_assessment_AI', blank=True, null=True)  # Field name made lowercase.
    key_capability_assessment_flexibility_and_openness = models.IntegerField(blank=True, null=True)
    key_capability_assessment_performance_and_scalability = models.IntegerField(blank=True, null=True)
    comprehensive_assessment = models.CharField(max_length=4096, blank=True, null=True)
    collaborate_with_chinese_company = models.BooleanField(blank=True)
    td_cooperation_status = models.TextField(blank=True, null=True)
    matching_direction_with_td = models.TextField(blank=True, null=True)
    key_person_interview = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_detail'