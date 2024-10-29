from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField


class AboutPage(Page):
    small_text = RichTextField(verbose_name="Opis strani")

    content_panels = Page.content_panels + [
        FieldPanel("small_text"),
    ]

    api_fields = [
        APIField("small_text"),
    ]

