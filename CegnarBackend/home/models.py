from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField


class HomePage(Page):
    # Hero section
    heading = models.CharField(max_length=50, verbose_name="Naslov")
    hero_small_text = models.CharField(
        max_length=50, blank=True, verbose_name="Podnaslov"
    )

    # CTA section
    cta_title = models.CharField(max_length=50, blank=True, verbose_name="CTA naslov")
    cta_small_text = RichTextField(blank=True, verbose_name="CTA opis")
    cta_btn_text = models.CharField(max_length=20, blank=True, verbose_name="CTA gumb")
    cta_btn_destination = models.CharField(max_length=20, blank=True, verbose_name="CTA gumb destinacija")

    content_panels = Page.content_panels + [
        # Hero section
        FieldPanel("heading"),
        FieldPanel("hero_small_text"),
        InlinePanel("hero_images", label="Slike - stranska vrstica"),
        # CTA section
        FieldPanel("cta_title"),
        FieldPanel("cta_small_text"),
        FieldPanel("cta_btn_text"),
        
    ]

    api_fields = [
        APIField("heading"),
        APIField("cta_title"),
        APIField("cta_small_text"),
        APIField("cta_btn_text"),
    ]


class HeroLink(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name="hero_images")
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="+"
    )
    destination = models.CharField(max_length=20)
    title = models.CharField(max_length=20)

    panels = [
        FieldPanel("image"),
        FieldPanel("destination"),
    ]
