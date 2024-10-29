from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField


class GalleryPage(Page):
    small_text = RichTextField(verbose_name="Opis strani")

    content_panels = Page.content_panels + [
        FieldPanel("small_text"),
        InlinePanel("gallery_images", label="Slike"),
    ]

    api_fields = [
        APIField("small_text"),
        APIField("gallery_images"),
    ]


class GalleryImages(Orderable):
    page = ParentalKey(
        GalleryPage, on_delete=models.CASCADE, related_name="gallery_images"
    )
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="+"
    )
    knife_model = models.CharField(max_length=20)
    image_description = RichTextField(blank=True)

    panels = [
        FieldPanel("image"),
        FieldPanel("knife_model"),
        FieldPanel("image_description"),
    ]

    api_fields = [
        APIField("image", serializer=ImageRenditionField("fill-300x400")),
        APIField("knife_model"),
        APIField("image_description"),
    ]
