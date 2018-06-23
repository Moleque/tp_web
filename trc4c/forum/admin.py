from __future__ import unicode_literals

from django.contrib import admin
from models import Profile, Question, Answer, Tag, Like


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	pass;

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	pass;

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
	pass;

@admin.register(Tag)
class AnswerAdmin(admin.ModelAdmin):
	pass;

@admin.register(Like)
class AnswerAdmin(admin.ModelAdmin):
	pass;
# Register your models here.
