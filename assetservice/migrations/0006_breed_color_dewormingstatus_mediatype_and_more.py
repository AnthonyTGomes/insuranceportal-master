# Generated by Django 5.1.7 on 2025-05-08 03:57

import django.db.models.deletion
from django.db import migrations, models

import assetservice.models


class Migration(migrations.Migration):

    dependencies = [
        ('assetservice', '0005_rename_asset_id_from_asset_asset_id_from_ai_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DewormingStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MediaType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='VaccinationStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='asset',
            name='asset_id_from_ai_service',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='chairman_certificate',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='challan_paper',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='left_side_image',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='muzzle_video',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='right_side_image',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='vet_certificate',
        ),
        migrations.AlterField(
            model_name='asset',
            name='breed',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assets', to='assetservice.breed'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assets', to='assetservice.color'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='deworming_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assets', to='assetservice.dewormingstatus'),
        ),
        migrations.AlterField(
            model_name='assethistory',
            name='deworming_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='history_dewormings', to='assetservice.dewormingstatus'),
        ),
        migrations.CreateModel(
            name='AssetMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=assetservice.models.asset_upload_path)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media_files', to='assetservice.asset')),
                ('media_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='assetservice.mediatype')),
            ],
            options={
                'ordering': ['-uploaded_at'],
            },
        ),
        migrations.AlterField(
            model_name='asset',
            name='vaccination_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assets', to='assetservice.vaccinationstatus'),
        ),
        migrations.AlterField(
            model_name='assethistory',
            name='vaccination_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='history_vaccinations', to='assetservice.vaccinationstatus'),
        ),
    ]
