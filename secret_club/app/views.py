from django.shortcuts import render
import json
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def authenticate(request):
    data = json.loads(request.body.decode('utf-8'))
    if data['pass'] == 'teste':
        return Response({'authorized':True})
    else:
        return Response({'authorized':False})