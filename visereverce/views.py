from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    origin_text = request.GET['usertext']
    list_text_origin = origin_text.split(' ')
    len_list = len(list_text_origin)
    reversed_text = origin_text[::-1]
    return render(request, 'reverse.html', {'origin_test': origin_text, 'reversed_text': reversed_text, 'len_list': len_list})


def calc(request):
    return render(request, 'calc.html')


def result(request):
    val1 = request.GET['val1']
    val2 = request.GET['val2']
    val1 = int(val1)
    val2 = int(val2)
    action = request.GET['action']
    if action == '+':
        res = val1+val2
    elif action == '-':
        res = val1 - val2
    elif action == '*':
        res = val1 * val2
    elif action == '/' and val2 != 0:
        res = val1/val2
    else:
        res = 'Wrong value'
    return render(request, 'result.html',
                  {'val1': val1, 'val2': val2, 'action': action, 'res': res})


