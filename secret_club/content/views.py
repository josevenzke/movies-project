from django.shortcuts import render
import json
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Content,Comment,Rate

@api_view(['GET'])
def list_content(request):
    content_type = request.GET.get('type')
    if content_type:
        query = Content.objects.all().filter(type=int(content_type)).values()
        return Response({'teste':query})
    else:
        query = Content.objects.all().values()
    
    return Response({'teste':query})


@api_view(['POST'])
def create_content(request):
    content_type = request.GET.get('type')
    if content_type:
        query = Content.objects.all().filter(type=int(content_type)).values()
        return Response({'teste':query})
    else:
        query = Content.objects.all().values()
    
    return Response({'teste':query})
