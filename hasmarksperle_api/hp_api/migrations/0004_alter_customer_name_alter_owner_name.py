# Generated by Django 4.2.1 on 2023-05-27 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hp_api', '0003_rename_customer_reservation_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(help_text='full name', max_length=25),
        ),
        migrations.AlterField(
            model_name='owner',
            name='name',
            field=models.CharField(help_text='full name', max_length=25),
        ),
    ]
