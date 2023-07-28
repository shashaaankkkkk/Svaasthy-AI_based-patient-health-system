from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PatientSerializer
from django.views.decorators.csrf import csrf_exempt

@api_view(['POST'])
@csrf_exempt
def create_patient(request):
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
