from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .models import Survey, Question, AnonUser, Answer
from .models import Survey as s
from .serializers import SurveySerializer, QuestionSerializer, AnonUserSerializer
from rest_framework.views import APIView
import json

class Survey(generics.ListAPIView):

  serializer_class = SurveySerializer
  queryset = Survey.objects.all()

class SurveyQuestion(APIView):

  def get(self, request, format=None, **kwargs):
    survey = Question.objects.filter(survey__title=kwargs['surveyTitle'])
    serializer = QuestionSerializer(survey, many=True)
    return Response(serializer.data)

  def post(self, request, format=None, **kwargs):
    request.data['session_id'] = request.session._get_or_create_session_key()
    serializer = AnonUserSerializer(data = request.data)
    if serializer.is_valid():
      survey = s.objects.get(id = request.data['survey'])
      question = Question.objects.get(id = request.data['question'])
      answer = Answer.objects.get(id = request.data['answer'])
      serializer.save(survey=survey, question=question, answer=answer,session_id=request.data['session_id'])
      return Response(status = 200)
    else:
      return Response(status = 500)

class AnonSummary(generics.ListAPIView):

  def get(self, request, format=None, **kwargs):
    #session = request.session._get_or_create_session_key()
    anon_user = AnonUser.objects.filter(session_id=request.session._get_or_create_session_key())
    serializer = AnonUserSerializer(anon_user, many=True)
    return Response(serializer.data)