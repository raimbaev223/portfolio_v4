from django.shortcuts import render, redirect
import telebot

from .models import Project
from .forms import ContactForm


def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)


def contact_page(request):
    return render(request, 'contact.html', {})


def contact(request):
    bot = telebot.TeleBot('1566152078:AAFn5Gy6C4tDvQwp-vHrQmHAdsC73PuNgVg')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            mail = form.cleaned_data['mail']
            message = form.cleaned_data['message']
            msg = f'Имя: {name} \nПочта: {mail} \nСообщение: {message}'
            bot.send_message(959339948, msg)
    return redirect('project_index')

def test_html(request):
    return render(request, 'abc.html', {})