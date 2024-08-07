# Generated by Django 5.0.6 on 2024-07-03 13:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_alter_order_options_order_vin_code'),
        ('users', '0012_rename_client_car_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='client',
        ),
        migrations.RemoveField(
            model_name='order',
            name='vin_code',
        ),
        migrations.AddField(
            model_name='order',
            name='car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='users.car'),
        ),
    ]
