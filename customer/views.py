from django.shortcuts import render
from .serializers import CustomerSerializer
from .models import Customer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

class CustomerViewset(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

@api_view(['POST'])
def create_customer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        print("Request data:", request.data)
        print("Serializer errors:", serializer.errors)
    return Response(serializer.errors, status=400)
