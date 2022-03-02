from django.shortcuts import render
import json
# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Content,Comment,Rate
from .serializers import ContentSerializer

@api_view(['GET'])
def list_content(request):
    content_type = request.GET.get('type')
    if content_type:
        query = Content.objects.all().filter(type=int(content_type)).values()
        return Response({'content':query})
    else:
        query = Content.objects.all().values()
    
    return Response({'content':query})

@api_view(['GET'])
def get_content(request,id_):
    try:
        content = Content.objects.get(id=int(id_))
        serialized_content = ContentSerializer(content)
        return Response({"content":serialized_content.data})
    except Exception as e:
        return Response({"error":e.args})

@api_view(['POST'])
def create_content(request):
    data = json.loads(request.body.decode('utf-8'))
    print(data)
    try:
        new_content = Content.objects.create(**data)
        print(new_content)
        return Response({'success':True})
    except Exception as e:
        return Response({'succes':e.args})
