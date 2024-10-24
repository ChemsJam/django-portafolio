# Generated by Django 5.0.2 on 2024-10-24 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0006_certificate_url'),
        ('portfolio', '0002_alter_projects_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='technologies',
            field=models.ManyToManyField(related_name='all_technologies_projects', to='certificates.technology'),
        ),
    ]