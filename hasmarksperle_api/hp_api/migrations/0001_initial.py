# Generated by Django 4.2.1 on 2023-05-27 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('CustomerId', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('phoneNumber', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('countryOfOrigin', models.CharField(max_length=25)),
                ('dateAdded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('ownerId', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('phoneNumber', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('dateAdded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('propertyId', models.BigAutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=25)),
                ('sqMeters', models.FloatField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.FloatField()),
                ('guests', models.IntegerField()),
                ('price', models.FloatField()),
                ('dateAdded', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hp_api.owner')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservationId', models.BigAutoField(primary_key=True, serialize=False)),
                ('checkInDate', models.DateField()),
                ('checkOutDate', models.DateField()),
                ('dateAdded', models.DateTimeField(auto_now_add=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hp_api.property')),
            ],
        ),
    ]
