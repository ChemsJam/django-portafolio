# Generated by Django 5.0.2 on 2024-10-24 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Certificate',
        ),
        migrations.DeleteModel(
            name='Technology',
        ),
    ]
