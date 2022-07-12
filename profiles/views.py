from django.shortcuts import render

from core.models import InnovationProfile


def index(request):
    innovations = InnovationProfile.objects.filter(deleted=False)
    return render(request, 'profiles/index.html', context={'innovations': innovations})


def forms(request):
    return render(request, 'profiles/innovation_submission_form_base.html')