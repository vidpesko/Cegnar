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
