from django.contrib import admin
from .models import Topic, Question, UserAnswer

admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(UserAnswer)
