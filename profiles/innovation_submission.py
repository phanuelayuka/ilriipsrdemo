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
        'form_step': 1,
        'images_form': InnovationImageForm(),
        'references_form': InnovationReferenceMaterialUrlForm(),
        'next_form': reverse('profiles:inno-create-detailed'),
        'previous_form': reverse('profiles:inno-create-basic')
    }
    return render(request, 'profiles/innovation_form_snippets/images_and_links.html', context=context)


def detailed_information(request):
    context = {
        'form_step': 2,
        'detail_form': DetailedInformationForm(),
        'next_form': reverse('profiles:inno-create-persons'),
        'previous_form': reverse('profiles:inno-create-doc')
    }
    return render(request, 'profiles/innovation_form_snippets/detailed_information.html', context=context)


def persons_info(request):
    context = {
        'form_step': 3,
        'contact_person_form': InnovationContactPersonForm(),
        'contributor_form': InnovationContributorForm(),
        'previous_form': reverse('profiles:inno-create-detailed')
    }
    return render(request, 'profiles/innovation_form_snippets/contact_persons_and_contributors.html',
                  context=context)

