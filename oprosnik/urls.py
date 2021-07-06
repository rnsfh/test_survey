from django.urls import path
from .views import Survey, SurveyQuestion

app_name='oprosnik'

urlpatterns = [
    path('', Survey.as_view(), name='survey'),
    path('<str:surveyTitle>/', SurveyQuestion.as_view(), name='questions')
]