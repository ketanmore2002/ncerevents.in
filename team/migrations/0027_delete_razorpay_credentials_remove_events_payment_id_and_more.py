# Generated by Django 4.1.1 on 2022-09-28 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0026_player_payment_status_teams_payment_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='razorpay_credentials',
        ),
        migrations.RemoveField(
            model_name='events',
            name='payment_id',
        ),
        migrations.RemoveField(
            model_name='events',
            name='payment_key',
        ),
        migrations.AddField(
            model_name='host',
            name='status',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
