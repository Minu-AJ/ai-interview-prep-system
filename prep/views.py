from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Topic, Question, UserAnswer


# Select Topic View
class SelectTopicView(View):

    def get(self, request):
        topics = Topic.objects.all()
        return render(request, 'select_topic.html', {'topics': topics})


# Question View
class QuestionView(View):

    def get(self, request, topic_id, question_id):
        topic = get_object_or_404(Topic, id=topic_id)
        question = get_object_or_404(Question, id=question_id, topic_id=topic_id)

        return render(request, 'question.html', {
            'topic': topic,
            'question': question
        })


    def post(self, request, *args, **kwargs):
        question_id = self.kwargs.get('question_id')
        topic_id = self.kwargs.get('topic_id')
        
        # topic = get_object_or_404(Topic, id=topic_id)
        question = get_object_or_404(Question, id=question_id)

        user_answer = request.POST.get('answer')
        correct_answer = question.correct_answer

        # Score logic
        if user_answer.strip().lower() == correct_answer.strip().lower():
            score = 1
            request.session['score'] = request.session.get('score', 0) + 1
        else:
            score = 0
        
        UserAnswer.objects.create(
            question = question,
            answer_text = user_answer,
            score = score
        )   
            

        # Get next question (same topic only)
        next_question = Question.objects.filter(
            topic_id=topic_id,
            id__gt=question_id
        ).order_by('id').first()

        if next_question:
            return redirect('question', topic_id=topic_id, question_id=next_question.id)
        else:
            total_score = request.session.get('score', 0)
            
            return render(request, 'result.html', {
                              'message': 'Interview Completed',
                              'total_score': total_score
                              })
        

def start_question(request, topic_id):
    
    # initialize interview session
    request.session['score'] = 0
    first_question = Question.objects.filter(
        topic_id=topic_id
        ).order_by('id').first()
    
    return redirect(
        'question',
        topic_id=topic_id, 
        question_id=first_question.id
        )