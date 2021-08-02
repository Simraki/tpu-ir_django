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
