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


class ProductCategory(models.Model):
    name = models.CharField(max_length=20, blank=True, verbose_name="Ime kategorije", help_text="Primer: kuhinjski noz, lovski noz,...")

    panels = [
        FieldPanel("name"),
    ]

    def __str__(self):
        return self.name


class GalleryImages(Orderable):
    page = ParentalKey(
        GalleryPage, on_delete=models.CASCADE, related_name="gallery_images"
    )
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="+"
    )
    category = models.ForeignKey("ProductCategory", on_delete=models.SET_NULL, null=True, blank=True, related_name="+", verbose_name="Kategorija")
    image_description = RichTextField(blank=True)

    panels = [
        FieldPanel("image"),
        FieldPanel("category"),
        FieldPanel("image_description"),
    ]

    api_fields = [
        APIField("image", serializer=ImageRenditionField("fill-300x400")),
        APIField("category"),
        APIField("image_description"),
    ]
