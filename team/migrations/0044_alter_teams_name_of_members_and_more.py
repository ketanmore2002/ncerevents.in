# Generated by Django 4.1.1 on 2022-10-05 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0043_rename_enrty_events_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='name_of_members',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='number_of_members',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
