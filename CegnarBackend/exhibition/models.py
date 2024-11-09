from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField

from .serializers import ProductCategoryField


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
    category = models.ForeignKey("ProductCategory", on_delete=models.SET_NULL, null=True, blank=True, related_name="+", verbose_name="Kategorija")
    image_description = RichTextField(blank=True)

    panels = [
        FieldPanel("image"),
        FieldPanel("category"),
        FieldPanel("image_description"),
    ]

    api_fields = [
        APIField("image", serializer=ImageRenditionField("fill-300x400")),
        APIField("category", serializer=ProductCategoryField()),
        APIField("image_description"),
    ]


# Product category model
class ProductCategory(models.Model):
    name = models.CharField(max_length=20, verbose_name="Ime kategorije", help_text="Primer: kuhinjski noz, lovski noz,...")
    super_category = models.CharField(max_length=20, blank=True, verbose_name="Ime nadkategorije", help_text="Primer: nož, obesek,...")

    panels = [
        FieldPanel("name"),
        FieldPanel("super_category"),
    ]

    def __str__(self):
        return self.name
