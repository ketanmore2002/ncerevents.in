# Generated by Django 4.1.1 on 2022-09-27 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0025_alter_player_fees_alter_teams_fees'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='payment_status',
            field=models.CharField(blank=True, default='upaid', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='teams',
            name='payment_status',
            field=models.CharField(blank=True, default='upaid', max_length=30, null=True),
        ),
    ]
