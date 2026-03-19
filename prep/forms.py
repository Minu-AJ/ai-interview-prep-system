from django import forms
from .models import UserAnswer

class AnswerForm(forms.ModelForm):
    
    class Meta:
        model = UserAnswer
        fields = ['answer_text']
        widgets = {
            'answer_text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Type your answer here...',
                'rows': 5
            })
        }