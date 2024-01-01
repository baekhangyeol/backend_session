from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from myapp.serializers import *

@swagger_auto_schema(method='post', request_body=PostCreateSerializer)
@api_view(['POST'])
def create_post(request):
    """
    게시물을 생성합니다.
    """
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message': '게시물이 성공적으로 생성되었습니다.',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response({
        'message': '유효하지 않은 입력입니다.',
        'data': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='get', responses={200: PostSerializer(many=True)})
@api_view(['GET'])
def get_posts(request):
    """
    모든 게시물을 조회합니다.
    """
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response({
        'message': '게시물 목록을 성공적으로 조회했습니다.',
        'data': serializer.data
    }, status=status.HTTP_200_OK)