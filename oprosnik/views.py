from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .models import Survey, Question
from .serializers import SurveySerializer, QuestionSerializer
from rest_framework.views import APIView

class Survey(generics.ListAPIView):

  serializer_class = SurveySerializer
  queryset = Survey.objects.all()

class SurveyQuestion(APIView):

  def get(self, request, format=None, **kwargs):
    survey = Question.objects.filter(survey__title=kwargs['surveyTitle'])
    serializer = QuestionSerializer(survey, many=True)
    return Response(serializer.data)