from django import forms
from django.forms import Textarea
from django.contrib.auth.forms import UserCreationForm
#from tinymce.widgets import TinyMCE
from models import Article, Comment, User

class MyRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'name')
        
    def save(self, commit = True):
        user = super(MyRegistrationForm, self).save(commit = False)
    
        if commit:
            user.save()
    
        return user    

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article

        fields = ('title', 'body', 'thumbnail')
        widgets = {'body': Textarea}
        
        
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('comments',)
        
        