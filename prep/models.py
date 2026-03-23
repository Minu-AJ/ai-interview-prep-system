from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    question_text = models.TextField()
    correct_answer = models.TextField(default="")
    
    def __str__(self):
        return self.question_text

class UserAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()
    score = models.FloatField(default=0)
    
    def __str__(self):
        return f"Answer for {self.question.id}"
    