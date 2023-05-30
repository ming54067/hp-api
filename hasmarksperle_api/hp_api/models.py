from django.db import models



# Create your models here.
class Owner(models.Model):
    ownerId         = models.BigAutoField(primary_key=True)
    name            = models.CharField(max_length=25, help_text="full name")
    phoneNumber     = models.IntegerField()
    email           = models.EmailField(max_length=50)
    dateAdded       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Customer(models.Model):
    CustomerId      = models.BigAutoField(primary_key=True)
    name            = models.CharField(max_length=25, help_text="full name")
    phoneNumber     = models.IntegerField()
    email           = models.EmailField(max_length=50)
    countryOfOrigin = models.CharField(max_length=25)
    dateAdded       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, {self.phoneNumber}, {self.email}"


class Property(models.Model):
    propertyId      = models.BigAutoField(primary_key=True)
    address         = models.CharField(max_length=50)
    description     = models.TextField(max_length=200)
    country         = models.CharField(max_length=25)
    sqMeters        = models.FloatField()
    bedrooms        = models.IntegerField()
    bathrooms       = models.FloatField()
    guests          = models.IntegerField()
    price           = models.FloatField()
    dateAdded       = models.DateTimeField(auto_now_add=True)
    owner           = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.address}, {self.country}"
    

class Reservation(models.Model):
    reservationId   = models.BigAutoField(primary_key=True)
    checkInDate     = models.DateField()
    checkOutDate    = models.DateField()
    dateAdded       = models.DateTimeField(auto_now_add=True)
    property        = models.ForeignKey(Property, on_delete=models.CASCADE)
    customer        = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer} | {self.property} | {self.checkInDate}, {self.checkOutDate}"