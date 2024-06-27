from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.utils.timezone import now





class User(AbstractUser):
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to="my_images", blank=True,null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state= models.CharField(max_length=255, blank=True, null=True)
    firstname= models.CharField(max_length=255, blank=True, null=True)
    lastname= models.CharField(max_length=255, blank=True, null=True)
    SearchableFields = ['title','author']
 
    REQUIRED_FIELDS =[]
    USERNAME_FIELD = 'email'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    
    


class Tags(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    slug = AutoSlugField( max_length=300, unique=True,populate_from='name')
    SearchableFields = ['name']
    FilterFields = ['name']
    def __str__(self): 
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    slug = AutoSlugField( max_length=300, unique=True,populate_from='name')
    SearchableFields = ['name']
    FilterFields = ['name']
    def __str__(self): 
        return self.name

    
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to="my-thumbnail", blank=True, null=True)
    feature = models.ImageField(upload_to="my-feature", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    tag = models.ManyToManyField(Tags, blank=True)
    slug = AutoSlugField( max_length=300, unique=True,populate_from='title')
    SearchableFields = ['title']
    FilterFields = ['title']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)   
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    body = models.TextField(max_length=500)
    published_date = models.DateTimeField( default=now )
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null = True, blank = True)
    SearchableFields = ['User','post']
    FilterFields = ['post']

    def __str__(self):
        return f'Comment by {self.user} on {self.post}'
        
class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True ,blank= True)
    body = models.TextField(max_length=500)
    time =models.DateTimeField(default=now)
    SearchableFields = ['User','post','body']
    FilterFields = ['post']

def __str__(self):
    return f'comment by {self.user} on {self.post} in {self.body}'
