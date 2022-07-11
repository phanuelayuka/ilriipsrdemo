from django.db import models
from django.utils import timezone

from core import innovation_fields_choices as innovation_choices


class CoreAbstractModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=timezone.now)
    deleted = models.BooleanField(default=False)
    deleted_on = models.DateTimeField(null=True)

    class Meta:
        abstract = True


class InnovationProfile(CoreAbstractModel):
    title = models.CharField(max_length=500)
    description = models.TextField(null=False)
    in_cgiar_innovation_dashboard = \
        models.CharField(max_length=50, choices=innovation_choices.IN_INNOVATION_DASH_CHOICES)
    innovation_dashboard_id_or_title = models.CharField(max_length=300, null=True, blank=True)
    characterization = models.CharField(max_length=100, choices=innovation_choices.CHARACTERIZATION_CHOICES)
    topology = models.CharField(max_length=100, choices=innovation_choices.TOPOLOGY_CHOICES)
    new_improved_variety_breed = models.CharField(max_length=10, choices=innovation_choices.YES_NO_CHOICES,
                                                  null=True, blank=True)
    improved_varieties_number = models.IntegerField(null=True, blank=True)


class InnovationImage(CoreAbstractModel):
    innovation = models.ForeignKey(InnovationProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='innovationprofiles')


class InnovationReferenceMaterialUrl(CoreAbstractModel):
    innovation = models.ForeignKey(InnovationProfile, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return self.url


class InnovationContactPerson(CoreAbstractModel):
    innovation = models.ForeignKey(InnovationProfile, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def initials(self):
        return f'{self.first_name[0].upper()} {self.last_name[0].upper()}'


class InnovationContributor(CoreAbstractModel):
    innovation = models.ForeignKey(InnovationProfile, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contributor_order = models.IntegerField(default=0)

    class Meta:
        ordering = ['contributor_order']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def initials(self):
        return f'{self.first_name[0].upper()} {self.last_name[0].upper()}'

    def save(self, *args, **kwargs):
        if not self.id:
            last_contributor = self.__class__.objects.filter(innovation_id=self.innovation_id, deleted=False).last()
            if last_contributor:
                self.contributor_order = last_contributor.contributor_order + 1
        super(InnovationContributor, self).save(*args, **kwargs)



