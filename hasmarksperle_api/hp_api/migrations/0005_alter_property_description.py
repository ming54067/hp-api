# Generated by Django 4.2.1 on 2023-05-28 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hp_api', '0004_alter_customer_name_alter_owner_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]
