# Generated by Django 4.1.1 on 2022-10-06 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0047_remove_events_total_number_of_members_allowed'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='rank',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
