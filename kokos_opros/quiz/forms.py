from django import forms


class QuestionForm(forms.Form):
    num_of_answer = forms.IntegerField()
    
    def clean(self):
        cleaned_data = super().clean()
        num = int(cleaned_data['num_of_answer'])

        if num <= 0 and num > 4:
            raise forms.ValidationError('Не может быть меньше или равен нулю')
