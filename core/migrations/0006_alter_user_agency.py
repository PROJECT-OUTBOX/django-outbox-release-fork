# Generated by Django 4.1.2 on 2022-12-28 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_userlog_active_domain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='agency',
            field=models.ManyToManyField(to='core.agency'),
        ),
    ]