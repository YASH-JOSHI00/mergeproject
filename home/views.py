from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from blog.models import User,Category,Post, Comment, Reply  # Replace 'blog' with your app name where User model is defined
from .Serializers import UserSerializer, CategorySerializer, PostSerializer, CommentSerializer, ReplySerializer # Adjust the import path as per your project structur
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


#  Create views 


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def userdata(request, id=None):
    if request.method == 'GET':
        if id:
            user = get_object_or_404(User, id=id)
            serializer = UserSerializer(user)
            return Response({'status': 200, 'payload': serializer.data})
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response({'status': 200, 'payload': serializer.data})
    
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'status': 200, 'payload': serializer.data, 'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method in ['PUT', 'PATCH']:
        user = get_object_or_404(User, id=id)
        serializer = UserSerializer(user, data=request.data, partial=request.method == 'PATCH')
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user = get_object_or_404(User, id=id)
        user.delete()
        return Response({'status': 204, 'message': 'User deleted'}, status=status.HTTP_204_NO_CONTENT)




@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def categorydata(request, slug=None):
    if request.method == 'GET':
        if slug:
            catg = get_object_or_404(Category, slug=slug)
            serializer = CategorySerializer(catg)
            return Response({'status': 200, 'payload': serializer.data})
        else:
            catg = Category.objects.all()
            serializer = CategorySerializer(catg, many=True)
            return Response({'status': 200, 'payload': serializer.data})

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 201, 'payload': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        catg = get_object_or_404(Category, slug=slug)
        serializer = CategorySerializer(catg, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        catg = get_object_or_404(Category, slug=slug)
        serializer = CategorySerializer(catg, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        catg = get_object_or_404(Category, slug=slug)
        catg.delete()
        return Response({'status': 204, 'message': 'Category deleted'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def postdata(request, slug=None):
    print("fdfsadf")
    if request.method == 'GET':
        if slug:
            post = get_object_or_404(Post, slug=slug)
            serializer = PostSerializer(post)
            return Response({'status': 200, 'payload': serializer.data})
        else:
            post = Post.objects.all()
            serializer = PostSerializer(post, many=True)
            return Response({'status': 200, 'payload': serializer.data})
    
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 201, 'payload': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        post = get_object_or_404(Post, slug=slug)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        post = get_object_or_404(Post, slug=slug)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post = get_object_or_404(Post, slug=slug)
        post.delete()
        return Response({'status': 204, 'message': 'Post deleted'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def commentdata(request, id=None):
    if request.method == 'GET':
        if id:
            comm = get_object_or_404(Comment, id="parent_id")
            serializer = CommentSerializer(comm)
            return Response({'status': 200, 'payload': serializer.data})
        else:
            comm = Comment.objects.all()
            serializer = CommentSerializer(comm, many=True)
            return Response({'status': 200, 'payload': serializer.data})
    
         
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 201, 'payload': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

         
    if request.method == 'PUT':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 201, 'payload': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 201, 'payload': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        comm = get_object_or_404(Comment, id="parent_id")
        comm.delete()
        return Response({'status': 204, 'message': 'Comment deleted'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def replydata(request,  id=None):
    if request.method == 'GET':
        if id:
            reply = get_object_or_404(Reply, id="comment_id")
            serializer = ReplySerializer(reply)
            return Response({'status': 200, 'payload': serializer.data})
        else:
            reply = Reply.objects.all()
            serializer = ReplySerializer(reply, many=True)
            return Response({'status': 200, 'payload': serializer.data})
        
    if request.method == 'POST':
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 201, 'payload': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        reply = get_object_or_404(Reply, id="comment_id")
        serializer = ReplySerializer(reply, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        reply = get_object_or_404(Reply, id="comment_id")
        serializer = ReplySerializer(reply, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        reply = get_object_or_404(Reply,id="comment_id")
        reply.delete()
        return Response({'status': 204, 'message': 'Reply deleted'}, status=status.HTTP_204_NO_CONTENT)