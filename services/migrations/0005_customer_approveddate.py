# Generated by Django 5.0.1 on 2024-03-19 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_alter_customer_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='approvedDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]