from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse

from core.models import InnovationImage, InnovationReferenceMaterialUrl, InnovationProfile, InnovationContactPerson, \
    InnovationContributor
from profiles.forms import BasicInformationForm, InnovationImageForm, InnovationReferenceMaterialUrlForm, \
    DetailedInformationForm, InnovationContactPersonForm, InnovationContributorForm


def basic_information(request):
    if request.method == 'POST':
        basic_form = BasicInformationForm(data=request.POST)
        if basic_form.is_valid():
            innovation = basic_form.save(commit=True)
            return redirect('profiles:inno-create-doc', innovation_id=innovation.id)
    else:
        basic_form = BasicInformationForm()

    context = {
        'form_step': 0,
        'basic_form': basic_form,
        'form_action': reverse('profiles:inno-create-basic'),
    }
    return render(request, 'profiles/innovation_form_snippets/basic_information.html', context=context)


def images_and_ref(request, innovation_id):
    try:
        innovation = InnovationProfile.objects.get(id=innovation_id, deleted=False)
    except InnovationProfile.DoesNotExist:
        raise Http404

    innovation_images = InnovationImage.objects.filter(innovation_id=innovation_id, deleted=False)
    innovation_refs = InnovationReferenceMaterialUrl.objects.filter(innovation_id=innovation_id, deleted=False)

    context = {
        'form_step': 1,
        'innovation_images': innovation_images,
        'innovation_refs': innovation_refs,
        'images_form': InnovationImageForm(),
        'references_form': InnovationReferenceMaterialUrlForm(),
        'next_form': reverse('profiles:inno-create-detailed', kwargs={'innovation_id': innovation.id}),
    }
    return render(request, 'profiles/innovation_form_snippets/images_and_links.html', context=context)


def detailed_information(request, innovation_id):
    try:
        innovation = InnovationProfile.objects.get(id=innovation_id, deleted=False)
    except InnovationProfile.DoesNotExist:
        raise Http404

    context = {
        'form_step': 2,
        'detail_form': DetailedInformationForm(instance=innovation),
        'next_form': reverse('profiles:inno-create-persons', kwargs={'innovation_id': innovation.id}),
        'previous_form': reverse('profiles:inno-create-doc', kwargs={'innovation_id': innovation.id})
    }
    return render(request, 'profiles/innovation_form_snippets/detailed_information.html', context=context)


def persons_info(request, innovation_id):
    try:
        innovation = InnovationProfile.objects.get(id=innovation_id, deleted=False)
    except InnovationProfile.DoesNotExist:
        raise Http404

    contact_persons = InnovationContactPerson.objects.filter(innovation_id=innovation_id, deleted=False)
    contributors = InnovationContributor.objects.filter(innovation_id=innovation_id, deleted=False)

    context = {
        'form_step': 3,
        'contact_persons': contact_persons,
        'contributors': contributors,
        'contact_person_form': InnovationContactPersonForm(),
        'contributor_form': InnovationContributorForm(),
        'previous_form': reverse('profiles:inno-create-detailed', kwargs={'innovation_id': innovation.id})
    }
    return render(request, 'profiles/innovation_form_snippets/contact_persons_and_contributors.html',
                  context=context)

