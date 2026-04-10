from django import forms
from .models import Card


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['topic', 'spanish_word', 'translation', 'image']


class QuizForm(forms.Form):
    answer = forms.CharField(
        label="Ваш перевод",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )