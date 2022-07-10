from django import forms


class BasicInformationForm(forms.ModelForm):
    class Meta:
        fields = ('title', 'description', 'in_cgiar_innovation_dashboard', 'innovation_dashboard_id_or_title')


class InnovationImageForm(forms.ModelForm):
    class Meta:
        fields = ('image',)


class InnovationReferenceMaterialUrlForm(forms.ModelForm):
    class Meta:
        fields = ('url', )


class InnovationContactPersonForm(forms.ModelForm):
    class Meta:
        fields = ('first_name', 'last_name', 'email_address',)


class InnovationContributorForm(forms.ModelForm):
    class Meta:
        fields = ('first_name', 'last_name',)