from django.shortcuts import render, get_object_or_404, redirect
from .models import Topic, Card
from .forms import CardForm, QuizForm, QuizStartForm, TopicForm
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

def add_topic(request):
    if request.method == "POST":
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("topics")
    else:
        form = TopicForm()

    return render(request, "add_topic.html", {"form": form})

def add_card(request):
    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CardForm()

    return render(request, "add_card.html", {"form": form})

def quiz_start(request):
    if request.method == "POST":
        form = QuizStartForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data["topic"]

            if topic:
                cards = list(Card.objects.filter(topic=topic))
            else:
                cards = list(Card.objects.all())

            random.shuffle(cards)

            request.session["quiz_cards"] = [card.id for card in cards[:10]]
            request.session["quiz_score"] = 0
            request.session["quiz_index"] = 0

            return redirect("quiz")
    else:
        form = QuizStartForm()

    return render(request, "quiz_start.html", {"form": form})

def quiz(request):
    if "quiz_cards" not in request.session:
        return redirect("quiz_start")

    quiz_cards = request.session["quiz_cards"]
    index = request.session["quiz_index"]

    if index >= len(quiz_cards):
        score = request.session["quiz_score"]

        # очистка
        del request.session["quiz_cards"]
        del request.session["quiz_score"]
        del request.session["quiz_index"]

        return render(request, "quiz_result.html", {
            "score": score,
            "total": len(quiz_cards)
        })

    card = Card.objects.get(id=quiz_cards[index])

    if request.method == "POST":
        form = QuizForm(request.POST)
        if form.is_valid():
            answer = form.cleaned_data["answer"]

            if answer.lower() == card.translation.lower():
                request.session["quiz_score"] += 1

            request.session["quiz_index"] += 1
            return redirect("quiz")

    else:
        form = QuizForm()

    return render(request, "quiz.html", {
        "card": card,
        "form": form,
        "number": index + 1,
        "total": len(quiz_cards)
    })