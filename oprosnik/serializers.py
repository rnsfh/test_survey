
from rest_framework import serializers
from .models import Survey, Question, Answer


class SurveySerializer(serializers.ModelSerializer):

  class Meta:
    model = Survey
    fields = [
      'title',
      'start_date',
      'end_date',
      'description'
    ]

class AnswerSerializer(serializers.ModelSerializer):

  class Meta:
    model = Answer
    fields = [
      'id',
      'answer_text',
      'correct'
    ]


class QuestionSerializer(serializers.ModelSerializer):

  answer = AnswerSerializer(many=True, read_only=True)
  survey = SurveySerializer(read_only=True)

  class Meta:

    model = Question
    fields = [
      'survey','title','answer'
    ]