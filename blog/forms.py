from django import forms
from models import Article, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    writer = forms.BooleanField(required=False)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'writer', 'password1', 'password2')
        
    def save(self, commit = True):
        user = super(MyRegistrationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.writer = self.cleaned_data['writer']
        
        if commit:
            user.save()
            
        return user

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ('title', 'body', 'thumbnail')
        #fields = '__all__'
        
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('comments',)
        
        