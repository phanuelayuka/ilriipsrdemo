from django.urls import path

from profiles import views
from profiles import innovation_submission as inno_create

app_name = 'profiles'

urlpatterns = [
    path('', views.index, name='index'),
    path('forms/', views.forms, name='form'),
    path('innovations/create/basic/', inno_create.basic_information, name='inno-create-basic'),
    path('innovations/create/documentation/', inno_create.images_and_ref, name='inno-create-doc'),
    path('innovations/create/detailed/', inno_create.detailed_information, name='inno-create-detailed'),
]
