# Generated by Django 4.1.1 on 2022-09-26 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_events_names_of_team_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='team_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
