from http import HTTPStatus

import simplejson as simplejson
from django.http import Http404, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
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
        'images_form_action': reverse('profiles:inno-save-image', kwargs={'innovation_id': innovation.id}),
        'ref_form_action': reverse('profiles:inno-save-ref', kwargs={'innovation_id': innovation.id}),
        'next_form': reverse('profiles:inno-create-detailed', kwargs={'innovation_id': innovation.id}),
    }
    return render(request, 'profiles/innovation_form_snippets/images_and_links.html', context=context)


def save_innovation_url(request, innovation_id):
    if request.method != 'POST':
        return JsonResponse({'message': 'Method not allowed.'}, status=HTTPStatus.BAD_REQUEST)

    form = InnovationReferenceMaterialUrlForm(request.POST)
    if form.is_valid():
        innovation_ref = form.save(commit=False)
        innovation_ref.innovation_id = innovation_id
        innovation_ref.save()

        entry_html = render_to_string('profiles/innovation_data_snippets/ref_item_url_tr.html',
                                      request=request, context={'reference_url': innovation_ref})
        return HttpResponse(simplejson.dumps({'entry_html': entry_html}), 'application/json')
    else:
        return JsonResponse({'message': 'Reference Material URL not saved.'}, status=HTTPStatus.BAD_REQUEST)


def save_innovation_image(request, innovation_id):
    if request.method != 'POST':
        return JsonResponse({'message': 'Method not allowed.'}, status=HTTPStatus.BAD_REQUEST)

    form = InnovationImageForm(request.POST, request.FILES)
    if form.is_valid():
        innovation_image = form.save(commit=False)
        innovation_image.innovation_id = innovation_id
        innovation_image.save()

        entry_html = render_to_string('profiles/innovation_data_snippets/images_tr.html',
                                      request=request, context={'innovation_image': innovation_image})
        return HttpResponse(simplejson.dumps({'entry_html': entry_html}), 'application/json')
    else:
        return JsonResponse({'message': 'Image not saved.'}, status=HTTPStatus.BAD_REQUEST)


def detailed_information(request, innovation_id):
    try:
        innovation = InnovationProfile.objects.get(id=innovation_id, deleted=False)
    except InnovationProfile.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        detail_form = DetailedInformationForm(data=request.POST, instance=innovation)
        if detail_form.is_valid():
            detail_form.save()
            return redirect('profiles:inno-create-persons', innovation_id=innovation.id)
    else:
        detail_form = DetailedInformationForm(instance=innovation)

    context = {
        'form_step': 2,
        'detail_form': detail_form,
        'form_action': reverse('profiles:inno-create-detailed', kwargs={'innovation_id': innovation.id}),
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
        'contributor_form_action': reverse('profiles:inno-save-contributor', kwargs={'innovation_id': innovation.id}),
        'contact_person_form_action': reverse('profiles:inno-save-contact-person',
                                              kwargs={'innovation_id': innovation.id}),
        'previous_form': reverse('profiles:inno-create-detailed', kwargs={'innovation_id': innovation.id})
    }
    return render(request, 'profiles/innovation_form_snippets/contact_persons_and_contributors.html',
                  context=context)


def save_contact_person(request, innovation_id):
    if request.method != 'POST':
        return JsonResponse({'message': 'Method not allowed.'}, status=HTTPStatus.BAD_REQUEST)

    form = InnovationContactPersonForm(request.POST)
    if form.is_valid():
        contact_person = form.save(commit=False)
        contact_person.innovation_id = innovation_id
        contact_person.save()

        entry_html = render_to_string('profiles/innovation_data_snippets/contact_person_tr.html',
                                      request=request, context={'contact_person': contact_person})
        return HttpResponse(simplejson.dumps({'entry_html': entry_html}), 'application/json')
    else:
        return JsonResponse({'message': 'Contact person not saved.'}, status=HTTPStatus.BAD_REQUEST)


def save_contributor(request, innovation_id):
    if request.method != 'POST':
        return JsonResponse({'message': 'Method not allowed.'}, status=HTTPStatus.BAD_REQUEST)

    form = InnovationContributorForm(request.POST)
    if form.is_valid():
        contributor = form.save(commit=False)
        contributor.innovation_id = innovation_id
        contributor.save()

        entry_html = render_to_string('profiles/innovation_data_snippets/contributors_tr.html',
                                      request=request, context={'contributor': contributor})
        return HttpResponse(simplejson.dumps({'entry_html': entry_html}), 'application/json')
    else:
        return JsonResponse({'message': 'Contributor not saved.'}, status=HTTPStatus.BAD_REQUEST)
