from django.urls import path
from .views import Survey, SurveyQuestion, AnonSummary

app_name='oprosnik'

urlpatterns = [
    path('', Survey.as_view(), name='survey'),
    path('summary/', AnonSummary.as_view()),
    path('<str:surveyTitle>/', SurveyQuestion.as_view(), name='questions'),

]