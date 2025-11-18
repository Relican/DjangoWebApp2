from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as dj_login, authenticate, logout

from .models import Topic, Message
from .forms import TopicForm, MessageForm


# Create your views here.

def index(request):
    ordered_topics = Topic.objects.order_by("-publish_date")
    context = {"topics": ordered_topics}
    template = loader.get_template("forum.html")
    return HttpResponse(template.render(context, request))

def details(request, topic_id):
    ordered_messages = Message.objects.filter(topic=topic_id).order_by("-publish_date")
    template = loader.get_template("topic.html")
    message_form = MessageForm()
    context = {"topic": get_object_or_404(Topic, pk=topic_id), "messages": ordered_messages, "message_form": message_form}
    return HttpResponse(template.render(context, request))

def create_topic(request):
    topic_form = TopicForm()
    message_form = MessageForm()
    return render(request, "create_topic.html", {'form': topic_form, 'message_form': message_form})

def create(request):
    # получаем из данных запроса POST отправленные через форму данные
    topic_form = TopicForm(request.POST)
    message_form = MessageForm(request.POST)
    if topic_form.is_valid() and message_form.is_valid():
        topic = topic_form.save(commit=False)
        topic.author = request.user
        topic.save()
        message = message_form.save(commit=False)
        message.topic = topic
        message.author = request.user
        message.save()
        return redirect('index')
    else:
        return HttpResponse("Что-то пошло не так!")

def add(request, topic_id):
    # получаем из данных запроса POST отправленные через форму данные
    message_form = MessageForm(request.POST)
    if message_form.is_valid():
        message = message_form.save(commit=False)
        message.topic = get_object_or_404(Topic, pk=topic_id)
        message.author = request.user
        message.save()
    return redirect('details', topic_id)

def register(request):
    form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            dj_login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_page(request):
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def login(request):
    form = AuthenticationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                dj_login(request, user)
                return redirect('index')
            else:
                return HttpResponse("Неверное имя пользователя или пароль.")

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect("index")
