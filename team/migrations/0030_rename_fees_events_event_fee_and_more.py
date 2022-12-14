# Generated by Django 4.1.1 on 2022-09-29 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0029_events_event_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='fees',
            new_name='event_fee',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='host_user_email',
            new_name='host_email',
        ),
        migrations.AddField(
            model_name='events',
            name='host_phone',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
