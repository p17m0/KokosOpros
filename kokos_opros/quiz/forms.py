from django import forms


class QuestionForm(forms.Form):
    num_of_answer = forms.IntegerField()
