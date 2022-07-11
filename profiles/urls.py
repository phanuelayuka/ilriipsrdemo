from django.urls import path

from profiles import views
from profiles import innovation_submission as inno_create

app_name = 'profiles'

urlpatterns = [
    path('', views.index, name='index'),
    path('forms/', views.forms, name='form'),
    path('innovations/create/basic/', inno_create.basic_information, name='inno-create-basic'),
    path('innovations/create/<int:innovation_id>/documentation/', inno_create.images_and_ref, name='inno-create-doc'),
    path('innovations/create/<int:innovation_id>/detailed/', inno_create.detailed_information,
         name='inno-create-detailed'),
    path('innovations/create/<int:innovation_id>/persons/', inno_create.persons_info, name='inno-create-persons'),

    path('innovations/<int:innovation_id>/save-contact-person/', inno_create.save_contact_person,
         name='inno-save-contact-person'),
    path('innovations/<int:innovation_id>/save-contributor/', inno_create.save_contributor,
         name='inno-save-contributor'),
]
