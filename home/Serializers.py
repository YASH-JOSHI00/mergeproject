from rest_framework import serializers
from blog.models import User  # Replace 'blog' with your app name where User model is defined
from blog.models import User, Post, Comment, Category, Reply, Tags

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'        

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ReplySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reply
        fields = '__all__'      

