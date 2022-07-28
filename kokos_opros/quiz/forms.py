from django import forms


class QuestionForm(forms.Form):
    num_of_answer = forms.IntegerField(label='Номер ответа:',
                                       min_value=1,
                                       max_value=4)
