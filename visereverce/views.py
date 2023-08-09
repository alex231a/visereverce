from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    origin_text = request.GET['usertext']
    reversed_text = origin_text[::-1]
    return render(request, 'reverse.html', {'origin_test': origin_text, 'reversed_text': reversed_text})
