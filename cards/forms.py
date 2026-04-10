from django import forms
from .models import Card
from .models import Topic


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['topic', 'spanish_word', 'translation', 'image']

class QuizStartForm(forms.Form):
    topic = forms.ModelChoiceField(
        queryset=Topic.objects.all(),
        required=False,
        empty_label="Все темы",
        label="Выберите тему"
    )

class QuizForm(forms.Form):
    answer = forms.CharField(
        label="Ваш перевод",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )