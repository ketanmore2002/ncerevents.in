# Generated by Django 4.1.1 on 2022-09-27 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0016_events_payment_id_events_payment_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='fees',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
