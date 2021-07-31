# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models
#
#
# class Agreementtypes(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=200)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'AgreementTypes'
#
#
# class Agreements(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=200)
#     start_date = models.DateField()
#     end_date = models.DateField(blank=True, null=True)
#     news_url = models.TextField(blank=True, null=True)  # This field type is a guess.
#     comments = models.TextField(blank=True, null=True)  # This field type is a guess.
#     id_agrtype = models.ForeignKey(Agreementtypes, models.DO_NOTHING,
#                                    db_column='id_agrType')  # Field name made lowercase.
#     id_researchdomain = models.ForeignKey('Researchdomains', models.DO_NOTHING,
#                                           db_column='id_researchDomain')  # Field name made lowercase.
#     id_representative = models.ForeignKey('Representatives', models.DO_NOTHING, db_column='id_representative')
#     id_partner = models.ForeignKey('Partners', models.DO_NOTHING, db_column='id_partner')
#     id_status = models.ForeignKey('Status', models.DO_NOTHING, db_column='id_status')
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'Agreements'
#
#
#
# class Engineeringschools(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=200)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'EngineeringSchools'
#
#
# class Partners(models.Model):
#     id = models.IntegerField(primary_key=True)
#     first_name = models.CharField(max_length=100)
#     second_name = models.CharField(max_length=100)
#     third_name = models.CharField(max_length=100, blank=True, null=True)
#     email = models.CharField(max_length=100, blank=True, null=True)
#     phone = models.CharField(max_length=50, blank=True, null=True)
#     id_company = models.ForeignKey(Companies, models.DO_NOTHING, db_column='id_company')
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'Partners'
#
#
# class Representatives(models.Model):
#     id = models.IntegerField(primary_key=True)
#     first_name = models.CharField(max_length=100)
#     second_name = models.CharField(max_length=100)
#     third_name = models.CharField(max_length=100, blank=True, null=True)
#     email = models.CharField(max_length=100, blank=True, null=True)
#     phone = models.CharField(max_length=50, blank=True, null=True)
#     id_school = models.ForeignKey(Engineeringschools, models.DO_NOTHING, db_column='id_school')
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'Representatives'
#
#
# class Researchdomains(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=200)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'ResearchDomains'
#
#
# class Status(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=300)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'Status'
#
#
# class Usertypes(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=200)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'UserTypes'
#
#
# class Users(models.Model):
#     id = models.IntegerField(primary_key=True)
#     login = models.CharField(unique=True, max_length=100)
#     password = models.CharField(max_length=300)
#     salt = models.CharField(max_length=30)
#     restore_email = models.CharField(max_length=100)
#     id_usertype = models.ForeignKey(Usertypes, models.DO_NOTHING, db_column='id_userType')  # Field name made lowercase.
#     id_representative = models.ForeignKey(Representatives, models.DO_NOTHING, db_column='id_representative')
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'Users'
#         unique_together = (('id', 'id_representative'),)
#
#
# class AlembicVersion(models.Model):
#     version_num = models.CharField(primary_key=True, max_length=32)
#
#     class Meta:
#         managed = False
#         db_table = 'alembic_version'
