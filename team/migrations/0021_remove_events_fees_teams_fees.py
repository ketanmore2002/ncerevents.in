# Generated by Django 4.1.1 on 2022-09-27 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0020_remove_events_names_of_team_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='fees',
        ),
        migrations.AddField(
            model_name='teams',
            name='fees',
            field=models.CharField(blank=True, default='upaid', max_length=30, null=True),
        ),
    ]
