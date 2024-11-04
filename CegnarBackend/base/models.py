from django.db import models
from wagtail.models import (
    DraftStateMixin,
    PreviewableMixin,
    RevisionMixin,
    TranslatableMixin,
    Page,
    Orderable,
)
from wagtail.fields import RichTextField
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, PublishingPanel
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField


@register_setting
class PersonalSettings(BaseGenericSetting):
    instagram_url = models.URLField(verbose_name="Instagram URL", blank=True)
    facebook_url = models.URLField(verbose_name="Facebook URL", blank=True)

    email = models.EmailField(verbose_name="Email", blank=True)
    phone_number = models.CharField(max_length=20, verbose_name="Telefon", blank=True)
    workshop_address = RichTextField(verbose_name="Naslov delavnice", blank=True)
    workshop_address_raw = models.CharField(max_length=100, verbose_name="Naslov delavnice brez novih vrstic", blank=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("instagram_url"),
                FieldPanel("facebook_url"),
            ],
            "Nastavitve socialnih omrezij",
        ),
        MultiFieldPanel(
            [
                FieldPanel("email"),
                FieldPanel("phone_number"),
                FieldPanel("workshop_address"),
                FieldPanel("workshop_address_raw"),
            ],
            "Nastavitve osebnih podatkov",
        )
        
    ]

    class Meta:
        verbose_name = "Nastavitve osebnih podatkov"


# @register_snippet
class FooterText(
    DraftStateMixin,
    RevisionMixin,
    PreviewableMixin,
    TranslatableMixin,
    models.Model,
):

    body = RichTextField()

    panels = [
        FieldPanel("body"),
        PublishingPanel(),
    ]

    def __str__(self):
        return "Footer text"

    def get_preview_template(self, request, mode_name):
        return "base.html"

    def get_preview_context(self, request, mode_name):
        return {"footer_text": self.body}

    class Meta(TranslatableMixin.Meta):
        verbose_name_plural = "Footer Text"


# Base template for child pages
class BasePage(Page):
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


    class Meta:
        abstract = True
