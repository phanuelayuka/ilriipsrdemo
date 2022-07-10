from django.shortcuts import render
from django.urls import reverse

from profiles.forms import BasicInformationForm, InnovationImageForm, InnovationReferenceMaterialUrlForm, \
    DetailedInformationForm, InnovationContactPersonForm, InnovationContributorForm


def basic_information(request):
    context = {
        'basic_form': BasicInformationForm(),
        'form_step': 0,
        'next_form': reverse('profiles:inno-create-doc')
    }
    return render(request, 'profiles/innovation_form_snippets/basic_information.html', context=context)


def images_and_ref(request):
    context = {
        'images_form': InnovationImageForm(),
        'references_form': InnovationReferenceMaterialUrlForm(),
        'form_step': 1,
        'next_form': reverse('profiles:inno-create-detailed')
    }
    return render(request, 'profiles/innovation_form_snippets/images_and_links.html', context=context)


def detailed_information(request):
    context = {
        'detail_form': DetailedInformationForm(),
        'contact_persons_form': InnovationContactPersonForm(),
        'contributors_form': InnovationContributorForm(),
        'form_step': 2
    }
    return render(request, 'profiles/innovation_form_snippets/detailed_information.html', context=context)




