from django.db import models
from django.utils import timezone


class CoreAbstractModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=timezone.now)
    deleted = models.BooleanField(default=False)
    deleted_on = models.DateTimeField(null=True)

    class Meta:
        abstract = True


class InnovationProfile(CoreAbstractModel):
    IN_INNOVATION_DASH_YES = 'yes'
    IN_INNOVATION_DASH_YES_NO_ID = 'yes_no_id'
    IN_INNOVATION_DASH_DONT_KNOW = 'i_dnt_know'
    IN_INNOVATION_DASH_NO = 'no'

    IN_INNOVATION_DASH_CHOICES = (
        (IN_INNOVATION_DASH_YES, "Yes, provide the CGIAR Innovation Dashboard ID or Title of Innovation as answer"
                                 " to the next question"),
        (IN_INNOVATION_DASH_YES_NO_ID, "Yes, but I cannot find the Innovation ID or Title of Innovation in the CGIAR"
                                       " Innovation Dashboard"),
        (IN_INNOVATION_DASH_DONT_KNOW, "I do not know"),
        (IN_INNOVATION_DASH_NO, "No, this innovation is not documented in the existing CGIAR Innovation Dashboard"),
    )
    
    CHARACTERIZATION_INCREMENTAL = 'incremental'
    CHARACTERIZATION_RADICAL = 'radical'
    CHARACTERIZATION_DISRUPTIVE = 'disruptive'
    CHARACTERIZATION_OTHER = 'other'

    CHARACTERIZATION_CHOICES = (
        (CHARACTERIZATION_INCREMENTAL, "Incremental innovation (constant, steady progress or improvement to existing "
                                       "innovations; aims at improving existing products, systems, processes, "
                                       "policies, etc.)"),
        (CHARACTERIZATION_RADICAL, "Radical innovation (new innovations that replace existing products, systems, "
                                   "processes and policies)"),
        (CHARACTERIZATION_DISRUPTIVE, "Disruptive innovation (new innovations that cause/ require broader "
                                      "reconfiguration of the farming, market or policy systems and business models "
                                      "in which they are embedded)"),
        (CHARACTERIZATION_OTHER, "Other/ I’m not sure/ This characterization does not work for my innovation"),
    )

    TOPOLOGY_TECHNOLOGICAL = 'technological'
    TOPOLOGY_CAPACITY_DVT = 'capacity_dvt'
    TOPOLOGY_POLICY_MODEL = 'policy_or_model'
    TOPOLOGY_OTHER = 'other'

    TOPOLOGY_CHOICES = (
        (TOPOLOGY_TECHNOLOGICAL, "Technological innovation (e.g. varieties/ breeds; crop and livestock management "
                                 "practices; machines; processing technologies; big data and information systems; etc.)"),
        (TOPOLOGY_CAPACITY_DVT, "Capacity development innovation (e.g. farmer, extension or investor decision-support "
                                "tools; farmer service provision model; training programs and curricula; online "
                                "courses; etc.)"),
        (TOPOLOGY_POLICY_MODEL, "Policy, organizational or institutional innovation (e.g. policy engagement strategies;"
                                " business models; policy arrangements; finance and regulatory mechanisms; partnership"
                                " models or mechanisms; public or private delivery strategies; etc.)"),
        (TOPOLOGY_OTHER, "Other/ I’m not sure/ This typology does not work for my innovation"),
    )

    YES_CHOICE_VALUE = 'yes'
    NO_CHOICE_VALUE = 'no'

    YES_NO_CHOICES = (
        (YES_CHOICE_VALUE, 'Yes'),
        (NO_CHOICE_VALUE, 'No'),
    )

    title = models.CharField(max_length=500)
    description = models.TextField(null=False)
    in_cgiar_innovation_dashboard = models.CharField(max_length=50, choices=IN_INNOVATION_DASH_CHOICES)
    innovation_dashboard_id_or_title = models.CharField(max_length=300, null=True, blank=True)
    characterization = models.CharField(max_length=100, choices=CHARACTERIZATION_CHOICES)
    topology = models.CharField(max_length=100, choices=TOPOLOGY_CHOICES)
    new_improved_variety_breed = models.CharField(max_length=10, choices=YES_NO_CHOICES, null=True, blank=True)
    improved_varieties_number = models.IntegerField(null=True, blank=True)


class InnovationImage(CoreAbstractModel):
    innovation = models.ForeignKey(InnovationProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='innovationprofiles')


class InnovationReferenceMaterialUrl(CoreAbstractModel):
    innovation = models.ForeignKey(InnovationProfile, on_delete=models.CASCADE)
    url = models.URLField()


class InnovationContactPerson(CoreAbstractModel):
    innovation = models.ForeignKey(InnovationProfile, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class InnovationContributor(CoreAbstractModel):
    innovation = models.ForeignKey(InnovationProfile, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contributor_order = models.IntegerField(default=0)

    class Meta:
        ordering = ['contributor_order']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        if not self.id:
            last_contributor = self.objects.filter(innovation_id=self.innovation_id, deleted=False).last()
            if last_contributor:
                self.contributor_order = last_contributor + 1
        super(InnovationContributor, self).save(*args, **kwargs)



