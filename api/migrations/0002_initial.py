# Generated by Django 3.2 on 2021-08-22 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='representative',
            name='id_user',
            field=models.ForeignKey(db_column='id_user', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='partner',
            name='id_company',
            field=models.ForeignKey(db_column='id_company', on_delete=django.db.models.deletion.DO_NOTHING, to='api.company'),
        ),
        migrations.AddField(
            model_name='company',
            name='id_country',
            field=models.ForeignKey(db_column='id_country', on_delete=django.db.models.deletion.DO_NOTHING, to='api.country'),
        ),
        migrations.AddField(
            model_name='agreement',
            name='id_agr_type',
            field=models.ForeignKey(db_column='id_agr_type', on_delete=django.db.models.deletion.DO_NOTHING, to='api.agreementtype'),
        ),
        migrations.AddField(
            model_name='agreement',
            name='id_partner',
            field=models.ForeignKey(db_column='id_partner', on_delete=django.db.models.deletion.DO_NOTHING, to='api.partner'),
        ),
        migrations.AddField(
            model_name='agreement',
            name='id_representative',
            field=models.ForeignKey(db_column='id_representative', on_delete=django.db.models.deletion.DO_NOTHING, to='api.representative'),
        ),
        migrations.AddField(
            model_name='agreement',
            name='id_research_domain',
            field=models.ForeignKey(db_column='id_research_domain', on_delete=django.db.models.deletion.DO_NOTHING, to='api.researchdomain'),
        ),
        migrations.AddField(
            model_name='agreement',
            name='id_status',
            field=models.ForeignKey(db_column='id_status', on_delete=django.db.models.deletion.DO_NOTHING, to='api.status'),
        ),
    ]
