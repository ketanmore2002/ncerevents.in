# Generated by Django 4.1.1 on 2022-09-27 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0022_rename_event_date_events_closing_event_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='host_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='host',
            name='user_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='event_participated',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='razorpay_credentials',
            name='host_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='event_participated',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
