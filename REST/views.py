from .models import Post, Album, File
from .serializer import PostSerializer, AlbumSerializer, FileSerializer

from rest_framework import viewsets
from rest_framework.filters import SearchFilter

# @action 관련
from rest_framework import renderers
from rest_framework.decorators import action
from django.http import HttpResponse

# File parser 관련
from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework.response import Response
from rest_framework import status



class PostViewSet(viewsets.ModelViewSet):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    filter_backends = [SearchFilter]    # 검색 필터 추가
    search_fields = ('title', 'body')

    # @action(method=['post])
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])

    # Custom API (http://localhost:8000/post/:id/hello_world)
    def hello_world(self, request, *args, **kwargs):
        return HttpResponse('Hello World!')

    def perform_create(self, serializer):           
        serializer.save(author=self.request.user)   # 글 작성했을 때 유저 정보(author field)를 자동 저장 
    
    def get_queryset(self):     # 본인이 작성한 글들만 볼 수 있도록 (다른 유저가 작성한 글들은 못보게)
        query_set =  super().get_queryset()

        if self.request.user.is_authenticated:
            query_set = query_set.filter(author = self.request.user) 
        else:
            query_set = query_set.none()
        
        return query_set
    
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    # 다양한 미디어 파일들로 request를 수락하는 방법. (파일은 형식이 다양함)

    # parser_class 지정
    parser_classes = (MultiPartParser, FormParser)  

    # create overriding
    def post(self, request, *args, **kwargs):

        serializer = FileSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        
        else:
            return Response(serializer.error, status=HTTP_400_BAD_REQUEST)

