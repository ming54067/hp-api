from rest_framework import serializers
from .models import Property
from .models import Owner
from .models import Customer
from .models import Reservation




class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = [
            'propertyId',
            'address',
            'description',
            'country',
            'sqMeters',
            'bedrooms',
            'bathrooms',
            'guests',
            'price',
            'dateAdded',
            'owner'
        ]


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = [
            'ownerId',
            'name',
            'phoneNumber',
            'email',
            'dateAdded'
        ]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'customerId',
            'name',
            'phoneNumber',
            'email',
            'countryOfOrigin',
            'dateAdded'
        ]


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = [
            'reservationId',
            'checkInDate',
            'checkOutDate',
            'dateAdded',
            'property',
            'customer'
        ]