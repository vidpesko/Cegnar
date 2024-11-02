from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField


class ContactPage(Page):
    # Image and title
    heading = models.CharField(max_length=50, blank=True, verbose_name="Naslov")
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Slika ozadja, za naslovom",
        verbose_name="Glavna slika",
    )

    content_panels = Page.content_panels + [
        # Hero section
        MultiFieldPanel(
            [
                FieldPanel("heading"),
                FieldPanel("hero_image"),
            ],
            "Nastavitev hero sekcije",
        ),
    ]

    api_fields = [
        # Hero
        APIField("heading"),
        APIField("hero_image", serializer=ImageRenditionField("fill-300x400")),
    ]


# class HeroLink(Orderable):
#     page = ParentalKey(
#         HomePage, on_delete=models.CASCADE, related_name="hero_sidebar_links"
#     )
#     image = models.ForeignKey(
#         "wagtailimages.Image", on_delete=models.CASCADE, related_name="+"
#     )
#     destination = models.CharField(max_length=20)
#     label = models.CharField(max_length=20)

#     panels = [
#         FieldPanel("image"),
#         FieldPanel("destination"),
#         FieldPanel("label"),
#     ]

#     api_fields = [
#         APIField("image", serializer=ImageRenditionField("fill-600x400")),
#         APIField("destination"),
#         APIField("label"),
#     ]
