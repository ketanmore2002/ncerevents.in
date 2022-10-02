# Generated by Django 4.1.1 on 2022-09-26 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0012_events_host_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='razorpay_credentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RAZOR_KEY_ID', models.CharField(blank=True, max_length=300, null=True)),
                ('RAZOR_KEY_SECRET', models.CharField(blank=True, max_length=300, null=True)),
                ('host_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='team.host')),
            ],
        ),
    ]
