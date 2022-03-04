from django.contrib.auth.models import User
import json
# Create your views here.

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Content,Comment,Rate
from .serializers import ContentSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_content(request):
    content_type = request.GET.get('type')
    if content_type:
        query = Content.objects.all().filter(type=int(content_type)).values()
        return Response({'content':query})
    else:
        query = Content.objects.all().values()
    
    return Response({'content':query})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_content(request,id_):
    try:
        content = Content.objects.get(id=int(id_))
        serialized_content = ContentSerializer(content)
        return Response({"content":serialized_content.data})
    except Exception as e:
        return Response({"error":e.args})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_content(request):
    data = json.loads(request.body.decode('utf-8'))
    try:
        new_content = Content.objects.create(**data)
        return Response({'success':True})
    except Exception as e:
        return Response({'succes':e.args})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_comments(request,content_id):
    comments = Comment.objects.filter(content__pk=int(content_id)).values()
    return Response({'content':comments})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request,content_id):
    text = data = json.loads(request.body.decode('utf-8')).get('text')
    try:
        content = Content.objects.get(id=int(content_id))
        current_user = request.user
        new_comment = Comment.objects.create(content=content,user=current_user,text=text)
        print(new_comment)
        return Response({'success':True})
    except Exception as e:
        return Response({'succes':e.args})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_ratings(request,content_id):
    rates = Rate.objects.filter(content__pk=int(content_id)).values()
    return Response({'content':rates})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_rating(request,content_id):
    rating = json.loads(request.body.decode('utf-8')).get('rate')
    try:
        content = Content.objects.get(id=int(content_id))
        current_user = request.user
        try:
            already_rate = Rate.objects.get(content=content)
            already_rate.rating = int(rating)
            already_rate.save()
            return Response({'success':True})
        except Rate.DoesNotExist:
            new_rate = Rate.objects.create(content=content,user=current_user,rating=int(rating))
            return Response({'success':True})
    except Exception as e:
        return Response({'succes':e.args})
