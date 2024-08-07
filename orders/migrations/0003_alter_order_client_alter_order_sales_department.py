# Generated by Django 5.0.6 on 2024-07-02 16:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_initial'),
        ('users', '0002_alter_manager_sales_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='users.client'),
        ),
        migrations.AlterField(
            model_name='order',
            name='sales_department',
            field=models.ManyToManyField(blank=True, related_name='orders', to='users.salesdepartment'),
        ),
    ]
