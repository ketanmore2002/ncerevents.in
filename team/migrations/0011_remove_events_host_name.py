# Generated by Django 4.1.1 on 2022-09-26 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0010_events_names_of_team_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='host_name',
        ),
    ]
