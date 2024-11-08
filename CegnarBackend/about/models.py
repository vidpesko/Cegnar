from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField

from base.models import BasePage
from .serializers import RichTextWithImagesField


class AboutPage(BasePage):
    # Content
    story = RichTextField(verbose_name="Zgodba", blank=True)

    content_panels = BasePage.content_panels + [
        # Content
        MultiFieldPanel(
            [
                InlinePanel("about_me_fact", label="Dejstva o meni"),
                FieldPanel("story"),
            ],
            "Nastavitev vsebine",
        ),
    ]

    api_fields = BasePage.api_fields + [
        # Content
        APIField("about_me_fact"),
        APIField("story", serializer=RichTextWithImagesField()),
    ]


class FactCard(Orderable):
    page = ParentalKey(
        AboutPage, on_delete=models.CASCADE, related_name="about_me_fact"
    )
    title = models.CharField(max_length=20, verbose_name="Naslov")
    description = models.CharField(max_length=40, verbose_name="Opis")

    panels = [
        FieldPanel("title"),
        FieldPanel("description"),
    ]

    api_fields = [
        APIField("title"),
        APIField("description"),
    ]
