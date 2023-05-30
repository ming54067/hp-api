from django.shortcuts import render
from django.http import JsonResponse
from .models import Property
from .models import Customer
from .models import Owner
from .models import Reservation
from .serializers import PropertySerializer
from .serializers import CustomerSerializer
from .serializers import OwnerSerializer
from .serializers import ReservationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status




# Create your views here.
@api_view(['GET', 'POST'])
def Property_list(request, format=None):

    if request.method == 'GET':
        property = Property.objects.all()
        serializer = PropertySerializer(property, many=True)
        return JsonResponse({'properties': serializer.data}, safe=False)
    
    elif request.method == 'POST':
        serializer = PropertySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def Property_detail(request, id, format=None):

    try:
        property = Property.objects.get(pk=id)
    except Property.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PropertySerializer(property)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PropertySerializer(property, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        property.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def Owner_list(request, format=None):

    if request.method == 'GET':
        owner = Owner.objects.all()
        serializer = OwnerSerializer(owner, many=True)
        return JsonResponse({'Owners': serializer.data}, safe=False)
    
    if request.method == 'POST':
        serializer = OwnerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def Owner_detail(request, id, format=None):

    try:
        owner = Owner.objects.get(pk=id)
    except Owner.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OwnerSerializer(owner)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = OwnerSerializer(owner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        owner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def Customer_list(request, format=None):

    if request.method == 'GET':
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return JsonResponse({'customers': serializer.data}, safe=False)
    
    if request.method == 'POST':
        serializer = CustomerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def Customer_detail(request, id, format=None):

    try:
        customer = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def Reservation_list(request, format=None):

    if request.method == 'GET':
        reservation = Reservation.objects.all()
        serializer = ReservationSerializer(reservation, many=True)
        return JsonResponse({'reservations': serializer.data}, safe=False)
    
    if request.method == 'POST':
        serializer = ReservationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def Reservation_detail(request, id, format=None):

    try:
        reservation = Reservation.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ReservationSerializer(reservation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)