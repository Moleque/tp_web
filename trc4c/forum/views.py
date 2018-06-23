from django.shortcuts import render, render_to_response, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Question, Answer, Tag

from django.http import HttpResponse
from django.template import RequestContext, loader

from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
from django.views.decorators import csrf
#from django.core.context_processors import csrf

def index(request):
    questions_list = Question.objects.all()
    #answers = Answer.objects.all()
    #tags = Tag.objects.all()
    questions, page = paginating(questions_list, request)
    return render(request, 'forum/index.html', {"questions": questions, "page": page, "sort": "new"})#, "answers": answers, "tags": tags})

def hot(request):
    questions_list = Question.objects.all()
    #answers = Answer.objects.all()
    #tags = Tag.objects.all()
    questions, page = paginating(questions_list, request)
    return render(request, 'forum/index.html', {"questions": questions, "page": page, "sort": "hot"})#, "answers": answers, "tags": tags})

def question(request, question_id):
	answers_list = Answer.objects.filter(question = question_id)
	answers, page = paginating(answers_list, request)
	context = {'question': Question.objects.get(id = question_id), 'questions': answers, "page": page, 'tags': Tag.objects.filter(question = question_id)}
	return render(request, 'forum/question.html', context)

def ask(request):
	return render(request, 'forum/ask.html')

def tag(request, tag_id):
	tag = Tag.objects.get(id = tag_id)
	context = {"tag": tag, "questions": tag.question.all()}
	return render(request, 'forum/tag.html', context)

def settings(request):
	return render(request, 'forum/settings.html')

@csrf_protect
def login(request):
	args = {}
	if request.POST:
		username = request.POST.get('inputLogin', '')
		password = request.POST.get('inputPassword', '')
		user = auth.authenticate(username = username, password = password)
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			args['login_error'] = "Sorry, you have some error!"
			return render(request, 'forum/login.html', args);
	else:
		return render(request, 'forum/login.html', args);

def logout(request):
	auth.logout(request)
	return redirect("/")

@csrf_protect
def signup(request):
	args = {}
	if request.POST:
		username = request.POST.get('inputLogin', '')
		email = request.POST.get('inputEmail', '')
		nick = request.POST.get('inputNick', '')
		password1 = request.POST.get('inputPassword1', '')
		password2 = request.POST.get('inputPassword2', '')
		avatar = request.POST.get('inputAvatar', '')

		user = auth.authenticate(username = username, password = password)
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			args['login_error'] = "Sorry, you have some error!"
			return render(request, 'forum/login.html', args);
	else:
		return render(request, 'forum/login.html', args);

def paginating(object_list, request):
    paginator = Paginator(object_list, 2)
    page = request.GET.get('page')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)
    return objects, page;