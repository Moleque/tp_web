from django.shortcuts import render

def index(request):
	return render(request, 'forum/index.html')

def question(request):
	return render(request, 'forum/question.html')