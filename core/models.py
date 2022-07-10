from django.db import models
from django.utils import timezone


class CoreAbstractModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=timezone.now)
    deleted = models.BooleanField(default=False)
    deleted_on = models.DateTimeField(null=True)

    class Meta:
        abstract = True


class InnovationProfile(models.Model):
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

    title = models.CharField(max_length=500)
    description = models.TextField(null=False)
    in_cgiar_innovation_dashboard = models.CharField(max_length=50, choices=IN_INNOVATION_DASH_CHOICES)
    innovation_dashboard_id_or_title = models.CharField(max_length=300, null=True, blank=True)


class InnovationImage(CoreAbstractModel):
    innovation = models.ForeignKey(InnovationProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='innovationprofiles')


class InnovationReferenceMaterialUrl(CoreAbstractModel):
    innovation = models.ForeignKey(InnovationProfile, on_delete=models.CASCADE)
    url = models.URLField()
