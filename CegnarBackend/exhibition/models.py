from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField
from modelcluster.models import ClusterableModel

from base.models import BasePage
from .fields import ProductCategoryField, RawImageField


class GalleryPage(BasePage):
    small_text = RichTextField(verbose_name="Opis strani")

    content_panels = BasePage.content_panels + [
        FieldPanel("small_text"),
    ]

    api_fields = BasePage.api_fields + [
        APIField("small_text"),
    ]
    api_fields[1] = APIField("hero_image", serializer=ImageRenditionField("fill-1800x400"))


class GalleryImage(ClusterableModel, models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ustvarjeno")
    category = models.ForeignKey("ProductCategory", on_delete=models.SET_NULL, null=True, blank=True, related_name="+", verbose_name="Kategorija")
    name = models.CharField(max_length=100, verbose_name="Ime noza", help_text="To ni isto kot kategorija (pravilno: Lovski noz iz kaljenega jekla)")
    image_description = RichTextField(blank=True, verbose_name="Kratek opis")

    panels = [
        InlinePanel("image", label="Slike"),
        FieldPanel("category"),
        FieldPanel("name"),
        FieldPanel("image_description"),
    ]

    def __str__(self):
        return self.name


# Seperate image model to allow multiple images
class GalleryActualImage(models.Model):
    snippet = ParentalKey(GalleryImage, related_name="image", on_delete=models.CASCADE)
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, null=True, related_name="+"
    )

    panels = [
        FieldPanel("image"),
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
