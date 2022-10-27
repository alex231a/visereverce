from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['user_text']
    print(user_text)
    new_list = user_text.split()
    print(new_list)
    len_list = len(new_list)
    print(len_list)
    reverse_text = user_text[::-1]
    print(reverse_text)
    return render(request, 'reverse.html', {'user_text': user_text, 'reverse_text': reverse_text, 'len_list': len_list})


