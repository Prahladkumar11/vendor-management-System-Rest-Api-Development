# Generated by Django 4.2.6 on 2023-11-25 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_app', '0005_alter_historialperformance_averageresponsetime_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='historialPerformance',
            new_name='Performance',
        ),
    ]