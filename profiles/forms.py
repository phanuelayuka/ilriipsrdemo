from django import forms

from core.models import InnovationProfile, InnovationImage, InnovationReferenceMaterialUrl, InnovationContactPerson, \
    InnovationContributor


class BasicInformationForm(forms.ModelForm):
    class Meta:
        model = InnovationProfile
        fields = ('title', 'description', 'in_cgiar_innovation_dashboard', 'innovation_dashboard_id_or_title')


class DetailedInformationForm(forms.ModelForm):
    class Meta:
        model = InnovationProfile
        fields = ('characterization', 'topology', 'new_improved_variety_breed', 'improved_varieties_number')


class InnovationImageForm(forms.ModelForm):
    class Meta:
        model = InnovationImage
        fields = ('image',)


class InnovationReferenceMaterialUrlForm(forms.ModelForm):
    class Meta:
        model = InnovationReferenceMaterialUrl
        fields = ('url', )


class InnovationContactPersonForm(forms.ModelForm):
    class Meta:
        model = InnovationContactPerson
        fields = ('first_name', 'last_name', 'email_address',)


class InnovationContributorForm(forms.ModelForm):
    class Meta:
        model = InnovationContributor
        fields = ('first_name', 'last_name',)