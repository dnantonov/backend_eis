# Generated by Django 3.2.7 on 2021-09-06 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_auto_20210906_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accrual',
            name='payment',
        ),
    ]
