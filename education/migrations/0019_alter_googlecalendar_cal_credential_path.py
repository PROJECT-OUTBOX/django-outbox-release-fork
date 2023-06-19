# Generated by Django 4.1.2 on 2023-06-17 06:35

from django.db import migrations, models
import education.models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0018_googlecalendar_googlecalendardetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='googlecalendar',
            name='cal_credential_path',
            field=models.FileField(blank=True, null=True, upload_to=education.models.get_upload_path, verbose_name='google calendar credentials path'),
        ),
    ]