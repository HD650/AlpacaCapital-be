# -*- coding: utf-8 -*-


from django.db import models
from django.contrib.auth.models import User, Group


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


# class Investment(models.Model):
#     id = models.AutoField(primary_key=True)
#     invest_date = models.DateField(blank=True, null=True)
#     invested_company = models.ManyToManyField('Company')
#     financing_stage = models.CharField(max_length=128, blank=True, null=True)
#     financing_amount = models.IntegerField(blank=True, null=True)

#     def __str__(self):
#         return str(self.financing_stage) + str(self.financing_amount)

#     class Meta:
#         managed = True
#         db_table = 'investment'


# class BaseInvestor(models.Model):
#     id = models.AutoField(primary_key=True)
#     quit_count = models.IntegerField(blank=True, null=True)
#     quit_company = models.CharField(max_length=512, blank=True, null=True)
#     investor_category = models.CharField(max_length=512, blank=True, null=True)
#     investment = models.ManyToManyField('Investment')

#     def __str__(self):
#         return self.quit_company

#     class Meta:
#         managed = True
#         db_table = 'base_investor'


# class Person(BaseInvestor):
#     name = models.CharField(max_length=128, blank=True, null=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         managed = True
#         db_table = 'person'


class TeamMember(models.Model):
    id = models.AutoField(primary_key=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    title = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return '%s %s' % (str(self.person.name), str(self.title))

    class Meta:
        managed = True
        db_table = 'team_member'


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    url = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'person'


# class Investor(BaseInvestor):
#     name = models.CharField(max_length=128, blank=True, null=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         managed = True
#         db_table = 'investor'

class Investor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    url = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'investor'


class TopBoard(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'top_board'


class Rank(models.Model):
    id = models.AutoField(primary_key=True)
    top_board = models.ForeignKey('TopBoard', on_delete=models.CASCADE)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    rank = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.top_board.name) + str(self.rank)

    class Meta:
        managed = True
        db_table = 'rank'


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.TextField(blank=True, null=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.company.name) + str(self.user.name)

    class Meta:
        managed = True
        db_table = 'comment'


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'tag'


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=512)
    description = models.TextField(blank=True, null=True)
    hq_location = models.CharField(max_length=512, blank=True, null=True)
    logo = models.CharField(max_length=1024, blank=True, null=True)
    found_time = models.IntegerField(blank=True, null=True)

    team = models.ManyToManyField(Person, through='TeamMember', blank=True, null=True)
    investor = models.ManyToManyField(Investor, blank=True, null=True)

    financing_stage = models.CharField(max_length=128, blank=True, null=True)

    employee_count = models.IntegerField(blank=True, null=True)
    site_url = models.CharField(max_length=512, blank=True, null=True)
    linkedin_url = models.CharField(max_length=512, blank=True, null=True)
    facebook_url = models.CharField(max_length=512, blank=True, null=True)
    company_contact = models.CharField(max_length=2048, blank=True, null=True)

    category = models.ManyToManyField(Category, blank=True, null=True)
    tag = models.ManyToManyField(Tag, blank=True, null=True)

    business_description = models.TextField(blank=True, null=True)
    main_products = models.TextField(blank=True, null=True)

    ranking = models.ManyToManyField('TopBoard', through='Rank', blank=True, null=True)

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

    chinese_collaborator = models.ManyToManyField(ChineseCollaborator, blank=True, null=True)

    td_cooperation_status = models.TextField(blank=True, null=True)
    matching_direction_with_td = models.TextField(blank=True, null=True)

    td_comment = models.ManyToManyField(User, through=Comment, blank=True, null=True)

    business_mode = models.TextField(blank=True, null=True)
    main_market = models.TextField(blank=True, null=True)
    key_customer = models.TextField(blank=True, null=True)

    #activity = models.ManyToManyField(Activity)

    competitor = models.ManyToManyField('self')
    
    def __str__(self):
        return self.company_name

    class Meta:
        managed = True
        db_table = 'company'


