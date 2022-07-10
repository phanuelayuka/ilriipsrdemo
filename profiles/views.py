from django.shortcuts import render


def index(request):
    return render(request, 'profiles/index.html')


def forms(request):
    return render(request, 'profiles/forms.html')