from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField

from base.models import BasePage


class ContactPage(BasePage):
    content_panels = BasePage.content_panels + []
    api_fields = BasePage.api_fields + []


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Prejeto")
    name = models.CharField(max_length=100, verbose_name="Ime")
    email = models.EmailField(verbose_name="Email naslov")
    contact_reason = models.CharField(max_length=50, verbose_name="Razlog", blank=True)
    product_model = models.CharField(max_length=100, verbose_name="Izdelek", blank=True)
    message = RichTextField(verbose_name="Sporočilo", blank=True)

    panels = [
        FieldPanel("name"),
        FieldPanel("email"),
        FieldPanel("contact_reason"),
        FieldPanel("product_model"),
        FieldPanel("message"),
    ]

    def __str__(self):
        return f"Sporočilo od: {self.name}"
