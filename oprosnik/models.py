from django.db import models

# Create your models here.

class Survey(models.Model):
  title = models.CharField(max_length=30)
  start_date = models.DateTimeField(auto_now_add=True)
  end_date = models.DateTimeField()
  description = models.CharField(max_length=255)

  def __str__(self):
    return self.title

class Question(models.Model):
  TYPE = (
    (0, 'Single choice'),
    (1, 'Multiple choice'),
    (2, 'Text'),
  )

  survey = models.ForeignKey(Survey, related_name='question', on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=255)
  question_type = models.IntegerField(choices=TYPE, default=0)

  def __str__(self):
    return self.title

class Answer(models.Model):
  question = models.ForeignKey(Question, related_name='answer', on_delete=models.DO_NOTHING)
  answer_text = models.CharField(max_length=255)
  correct = models.BooleanField(default=False)

  def __str__(self):
    return self.answer_text

