from .models import Post, Album, File
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Post
        fields = ('pk', 'author_name', 'title', 'body')
        # fields = '__all__'
        # fields = ('title', 'body')  # or '__all__' 
        # read_only_fields = ('id',)  # 콤마(,) 안쓰면 튜플 아닌 문자열로 인식함. id는 default로 readonly

class AlbumSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    image = serializers.ImageField(use_url=True)    # 업로드 확인을 url 로 하겠다는것을 명시

    class Meta:
        model = Album 
        fields = ('pk', 'author_name', 'image', 'description')

class FileSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    file = serializers.FileField(use_url=True)    # 업로드 확인을 url 로 하겠다는것을 명시

    class Meta:
        model = File
        fields = ('pk', 'author_name', 'file', 'description')

