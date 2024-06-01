from django import forms


from .models import Post, User, Comment, Reply
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title', 'text','thumbnail','feature','category', 'tag')




class UserForm(forms.ModelForm):
    email = forms.EmailField(
        label='Email',
    widget=forms.EmailInput(attrs={'class': 'col-10', 'id': 'email', 'name': 'email'}))
    
    password=forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'col-10', 'id': 'password', 'name': 'password'}))
    
    class Meta:
        model = User                
        fields = ("email","password",)

class ProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['image']

    

class SignupForm(forms.ModelForm):
    username=forms.CharField(
        label='User Name',
        widget=forms.TextInput(attrs={'class': 'col-10', 'id': 'username', 'name': 'username'})
    )

    firstname=forms.CharField(
        label='First name',
        widget=forms.TextInput(attrs={'class': 'col-10', 'id': 'firstname', 'name': 'firstname'}),
    )
    lastname=forms.CharField(
        label='last name',
        widget=forms.TextInput(attrs={'class': 'col-10', 'id': 'lastname', 'name': 'lastname'}),
    )
    
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'col-10', 'id': 'email', 'name': 'email'})
    )
    

    password=forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'col-10', 'id': 'password', 'name': 'password'})
    )
    class Meta:
        model = User
        fields = ("username","firstname","lastname","email","password","password")
    





class CommentForm(forms.ModelForm):
    body=forms.CharField(
        label='Comment',
        widget=forms.TextInput(attrs={'class': 'col-10', 'id': 'body', 'name': 'body'})
    )
    class Meta:
        model = Comment
        fields = ['body']
    

class ReplyForm(forms.ModelForm):
    body=forms.CharField(
        widget=forms.TextInput(attrs={'class': 'col-10', 'id': 'body', 'name': 'body'})

    )
    class Meta:
        model = Reply
        fields = ['body']