# Generated by Django 5.2.1 on 2025-05-11 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authservice', '0007_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='access_token',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='token',
            name='refresh_token',
            field=models.TextField(blank=True, null=True),
        ),
    ]
