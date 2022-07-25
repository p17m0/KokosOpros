from attr import field
from django import forms
from .models import Question


class CheckAnswer(forms.Form):
    your_answer = forms.CharField(label='Answer')
    your_question = Question

    def clean(self):
        cleaned_data=super(CheckAnswer,self).clean()
        response=cleaned_data.get("your_answer")
        try:
            p = Question.objects.get(answer__iexact=response)
            if(self.your_answer == p.answer and self.your_question == p.question):
                response.user.golden_coins += 1
            else:
                raise forms.ValidationError("Wrong Answer.")
        except Question.DoesNotExist:
            raise forms.ValidationError("Wrong Answer.")