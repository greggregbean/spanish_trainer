from django.shortcuts import render, get_object_or_404, redirect
from .models import Topic, Card
from .forms import CardForm, QuizForm
import random


def home(request):
    return render(request, "home.html")


def topic_list(request):
    topics = Topic.objects.all()
    return render(request, "topics.html", {"topics": topics})


def cards_by_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    cards = Card.objects.filter(topic=topic)
    return render(request, "cards.html", {
        "topic": topic,
        "cards": cards
    })


def add_card(request):
    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CardForm()

    return render(request, "add_card.html", {"form": form})


def quiz(request):
    cards = Card.objects.all()
    if not cards:
        return render(request, "quiz.html", {"error": "Нет карточек"})

    card = random.choice(cards)

    if request.method == "POST":
        form = QuizForm(request.POST)
        if form.is_valid():
            answer = form.cleaned_data["answer"]
            correct = answer.lower() == card.translation.lower()

            return render(request, "quiz_result.html", {
                "correct": correct,
                "card": card
            })
    else:
        form = QuizForm()

    return render(request, "quiz.html", {
        "card": card,
        "form": form
    })