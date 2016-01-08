from django.shortcuts import render, render_to_response
from .models import Article
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from forms import ArticleForm, CommentForm, MyRegistrationForm
from django.template.context_processors import csrf

# Create your views here.


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('blog/login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/blog/logged_in/')
    else:
        return HttpResponseRedirect('/blog/invalid/')

def loggedin(request):
    return render_to_response('blog/logged_in.html',
                              {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('blog/invalid.html')

def logout(request):
    auth.logout(request)
    return render_to_response('blog/logout.html')

def articles(request):
    language = 'en-gb'
    session_language = 'en-gb'
    
    try:
        language = request.COOKIES['lang']
    except:
        pass
    try:
        session_language = request.session['lang']
    except:
        pass
    
    return render_to_response('blog/articles.html', 
                              {'articles': Article.objects.order_by('published').reverse()[:5],
                               'language': language,
                               'session_language': session_language})

def article(request, article_id = 1):
    return render_to_response('blog/article.html', 
                              {'article': Article.objects.get(id = article_id) })

def language(request, language='en-gb'):
    response = HttpResponse('setting language to %s' % language)
    
    response.set_cookie('lang', language)
    
    request.session['lang'] = language
    
    return response

def create(request):
    if request.POST:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/blog/index')
    else:
        form = ArticleForm()
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render_to_response('blog/create_article.html', args)
        
def like(request, article_id):
    if article_id:
        a = Article.objects.get(id = article_id)
        a.likes += 1
        a.save()
    
    return HttpResponseRedirect('/blog/get/%s' % article_id)

def register(request):
    if request.method == "POST":
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blog/register_success')
        else:
            return HttpResponseRedirect('/blog/invalid')
    
    args = {}
    args.update(csrf(request))
    
    args['form'] = MyRegistrationForm()
    
    return render_to_response('blog/register.html', args)

def register_success(request):
    return render_to_response('blog/register_success.html')