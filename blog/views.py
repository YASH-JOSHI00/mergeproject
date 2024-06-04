from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post,User, Comment
from django.contrib.auth import authenticate, login, logout
from .forms import PostForm,  UserForm, SignupForm,ProfilePhotoForm,CommentForm , ReplyForm
from django.shortcuts import redirect
from django.contrib import messages




def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "blog/post_list.html", {"posts": posts})

def category(request,slug):
    
    categories = Post.objects.filter(category__slug=slug)
    return render(request, "blog/category.html", {"categories": categories})


# def tag(request, slug):
#     print(slug)
#     if slug:
#         tags = Post.objects.filter(tag__slug=slug).order_by("published_date")
#     else:
#         tags = Post.objects.all().order_by("published_date")
#     return render(request, "blog/tag.html", {"tags": tags})

def comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            post = get_object_or_404(Post, id=request.POST.get('post_id'))
            comment.post = post
            comment.user = request.user
            parent_id = request.POST.get('parent_id')
            if parent_id:
                comment.parent = get_object_or_404(Comment, id=parent_id)
            comment.save()
            return redirect('post_detail', slug=post.slug)
    return redirect('post_list' )


def reply(request):
    comment_id = request.POST.get('comment_id')
    parent_comment = get_object_or_404(Comment, id=comment_id)
    post = parent_comment.post
    if request.method == 'POST':
        print(request.POST)
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.post = post
            reply.comment = parent_comment
            reply.user = request.user  
            reply.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = ReplyForm()
    return render(request, 'blog/post_detail.html', {'form': form, 'post': post,'parent_comment': parent_comment,})





def post_detail(request, slug):
    post = get_object_or_404(Post,slug=slug)
    comments = Comment.objects.filter(post=post).select_related('user','parent')
    form = CommentForm()
    context= {
        'post':post,
        'form':form,
        'comments':comments,
        'user':request.user,

    }
    return render(request, 'blog/post_detail.html', context)

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
        
            post.published_date = timezone.now()

            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
 
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post,)
        if form.is_valid():
            post = form.save(commit=False)
            
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def user_login(request):
    form=UserForm()
    
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        
        print(username,password)
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            print('good job')
            login(request, user)
            return redirect('/',"Welcomemessage= {}!".format(request.user.username))
            
    return render(request,"blog/userlogin.html", {"form":form})

def signup(request):
    if request.method=="POST":
        username=request.POST["username"]
        fname=request.POST["firstname"]
        lname=request.POST["lastname"]
        email=request.POST["email"]
        password=request.POST["password"]
        myuser = User.objects.create_user(username=username, email=email, password=password,firstname=fname,lastname=lname)
        myuser.save()
        messages.success(request,"successful!")

        return redirect('/login/')
    else:
        form=SignupForm()
    return render(request,"blog/userlogin.html",{"form":form})

def signout(request):
    print(1)
    logout(request)
    return redirect('/login')



def userdetail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    
    return render(request, 'blog/userdetail.html', {'user': user})

def upload_profile_photo(request):
    if request.method == 'POST':
        form = ProfilePhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('post_list') 
    else:
        form = ProfilePhotoForm(instance=request.user)
    
    return render(request, 'blog/upload_profile_photo.html',{'form':form})  



