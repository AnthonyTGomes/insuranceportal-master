# Generated by Django 5.2.1 on 2025-05-11 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insuranceservice', '0003_remove_insuranceperiod_category_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='InsuranceProduct',
        ),
    ]
