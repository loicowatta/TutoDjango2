# Generated by Django 2.0.2 on 2018-02-27 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TutoDjango', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='cellphone_number',
            new_name='cellphone',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='home_phone_number',
            new_name='home_phone',
        ),
    ]