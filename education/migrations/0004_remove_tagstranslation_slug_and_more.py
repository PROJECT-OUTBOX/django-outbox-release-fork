# Generated by Django 4.1.2 on 2022-11-04 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_remove_popuptranslation_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tagstranslation',
            name='slug',
        ),
        migrations.AlterField(
            model_name='tagstranslation',
            name='name',
            field=models.CharField(max_length=50, verbose_name='tags name (id)'),
        ),
    ]
