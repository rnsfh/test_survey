from django.contrib import admin
from . import models

@admin.register(models.Survey)
class SurveyAdmin(admin.ModelAdmin):
	list_display = [
    'id',
    'title',
    'start_date',
    'end_date',
    'description'
  ]

class AnswerInlineModel(admin.TabularInline):
  model = models.Answer
  fields = [
    'answer_text',
    'correct'
  ]

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
  list_display = [
    'title',
    'survey',
    'question_type'
  ]
  inlines = [
    AnswerInlineModel
  ]

@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
  list_display = [
    'answer_text',
    'correct',
    'question'
  ]
