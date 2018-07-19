# -*- coding: utf-8 -*-


from django.db import models



class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=512)
    
    def __str__(self):
        return self.category

    class Meta:
        managed = True
        db_table = 'category'


class ChineseCollaborator(models.Model):
    id = models.AutoField(primary_key=True)
    collaborator_name = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return self.collaborator_name

    class Meta:
        managed = True
        db_table = 'chinese_collaborator'


class Investor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'investor'


class Founder(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'founder'

class CompanyDetail(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=512)
    description = models.TextField(blank=True, null=True)
    hq_location = models.CharField(max_length=512, blank=True, null=True)
    logo = models.CharField(max_length=1024, blank=True, null=True)
    found_time = models.DateField(blank=True, null=True)
    founder = models.ManyToManyField(Founder, through='Foundation')
    financing_stage = models.CharField(max_length=128, blank=True, null=True)
    investor = models.ManyToManyField(Investor)
    employee_count = models.IntegerField(blank=True, null=True)
    site_url = models.CharField(max_length=512, blank=True, null=True)
    linkedin_url = models.CharField(max_length=512, blank=True, null=True)
    facebook_url = models.CharField(max_length=512, blank=True, null=True)
    company_contact = models.CharField(max_length=2048, blank=True, null=True)
    category = models.ManyToManyField(Category)
    business_description = models.TextField(blank=True, null=True)
    main_products = models.TextField(blank=True, null=True)
    
    capability_maturity = models.IntegerField(blank=True, null=True)
    capability_maturity_des = models.TextField(blank=True, null=True)
    technology_leadership = models.IntegerField(blank=True, null=True)
    technology_leadership_des = models.TextField(blank=True, null=True)
    key_capability_assessment_ai = models.IntegerField(blank=True, null=True)
    key_capability_assessment_ai_des = models.TextField(blank=True, null=True)
    key_capability_assessment_flexibility_and_openness = models.IntegerField(blank=True, null=True)
    key_capability_assessment_flexibility_and_openness_des = models.TextField(blank=True, null=True)
    key_capability_assessment_performance_and_scalability = models.IntegerField(blank=True, null=True)
    key_capability_assessment_performance_and_scalability_des = models.TextField(blank=True, null=True)
    comprehensive_assessment = models.TextField(blank=True, null=True)

    collaborate_with_chinese_company = models.BooleanField()
    chinese_collaborator = models.ManyToManyField(ChineseCollaborator)
    
    td_cooperation_status = models.TextField(blank=True, null=True)
    matching_direction_with_td = models.TextField(blank=True, null=True)
    key_person_interview = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.company_name

    class Meta:
        managed = True
        db_table = 'company_detail'

class Foundation(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(CompanyDetail, on_delete=models.CASCADE)
    founder = models.ForeignKey(Founder, on_delete=models.CASCADE)
    role = models.CharField(max_length=512)

    class Meta:
        managed = True
        db_table = 'foundation'
