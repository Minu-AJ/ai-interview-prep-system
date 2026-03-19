from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Topic, Question
from .forms import AnswerForm

# Select Topic View
class SelectTopicView(View):
    
    def get(self, request):
        topics = Topic.objects.all()
        return render(request, 'select_topic.html', {'topics':topics})
    
# Question + Answer View
class QuestionView(View):
    
    def get(self, request, topic_id):
        topic = get_object_or_404(Topic, id=topic_id)
        question=Question.objects.filter(topic=topic).first()
        form = AnswerForm()
        
        return render(request, 'question.html', {
            'topic': topic,
            'question': question,
            'form': form
        })
        
    def post(self, request, topic_id):
        topic = get_object_or_404(Topic, id=topic_id)
        question = Question.objects.filter(topic=topic).first()
        
        form = AnswerForm(request.POST)
        
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            
            # Scoring Logic
            if len(answer.answer_text) > 50:
                answer.score = 80
            else:
                answer.score = 40
                
            answer.save()
            
            return render(request, 'result.html', {
                'question': question,
                'answer': answer
            })
        return render(request, 'question.html', {
            'topic': topic,
            'question': question,
            'form': form
        })
        