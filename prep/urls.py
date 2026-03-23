from django.urls import path
from .views import SelectTopicView, QuestionView, start_question

urlpatterns = [
    path('', SelectTopicView.as_view(), name='select_topic'),
    path('question/<int:topic_id>/<int:question_id>/', QuestionView.as_view(), name='question'),
    path('start/<int:topic_id>/', start_question, name='start_question')
]
