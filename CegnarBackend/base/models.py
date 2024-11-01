from django.db import models
from wagtail.models import (
    DraftStateMixin,
    PreviewableMixin,
    RevisionMixin,
    TranslatableMixin,
)
from wagtail.fields import RichTextField
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, PublishingPanel
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting


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
