# Generated by Django 4.1.1 on 2022-09-29 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0031_remove_teams_payment_status_teams_payment_statu_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teams',
            old_name='payment_statu',
            new_name='payment_status',
        ),
    ]
