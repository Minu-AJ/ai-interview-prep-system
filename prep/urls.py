from django.urls import path
from .views import SelectTopicView, QuestionView

urlpatterns = [
    path('', SelectTopicView.as_view(), name='select_topic'),
    path('question/<int:topic_id>/', QuestionView.as_view(), name='question'),
]
