# Generated by Django 4.0.4 on 2022-05-04 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate_info',
            old_name='last_company',
            new_name='pcompany',
        ),
        migrations.AlterField(
            model_name='candidate_info',
            name='status',
            field=models.CharField(default='Applied', max_length=25),
        ),
    ]