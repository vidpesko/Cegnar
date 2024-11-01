from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField


class HomePage(Page):
    # Hero section
    heading = models.CharField(max_length=50, blank=True, verbose_name="Naslov")
    hero_small_text = models.CharField(
        max_length=50, blank=True, verbose_name="Podnaslov"
    )

    # CTA section
    cta_title = models.CharField(max_length=50, blank=True, verbose_name="CTA - naslov")
    cta_small_text = RichTextField(blank=True, verbose_name="CTA - opis")
    cta_btn_text = models.CharField(max_length=20, blank=True, verbose_name="CTA - gumb")
    cta_btn_destination = models.CharField(max_length=20, blank=True, verbose_name="CTA - gumb destinacija")

    # Gallery section
    gallery_title = models.CharField(max_length=50, blank=True, verbose_name="Galerija - naslov")
    gallery_description = RichTextField(blank=True, verbose_name="Galerija - opis")
    gallery_btn_label = models.CharField(max_length=10, blank=True, verbose_name="Galerija - napis v gumbu")

    # About me section
    about_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Slike mene",
    )
    about_title = models.CharField(max_length=50, blank=True, verbose_name="O meni - naslov")
    about_description = RichTextField(blank=True, verbose_name="O meni - kratek opis")
    about_btn_label = models.CharField(max_length=50, blank=True, verbose_name="O meni - napis v gumbu")

    content_panels = Page.content_panels + [
        # Hero section
        MultiFieldPanel(
            [
                FieldPanel("heading"),
                FieldPanel("hero_small_text"),
                InlinePanel("hero_sidebar_links", label="Povezava - stranska vrstica"),
            ],
            "Nastavitev hero sekcije",
        ),
        # CTA section
        MultiFieldPanel(
            [
                FieldPanel("cta_title"),
                FieldPanel("cta_small_text"),
                FieldPanel("cta_btn_text"),
                FieldPanel("cta_btn_destination"),
            ],
            "Nastavitev kratkega uvoda",
        ),
        # Features
        MultiFieldPanel(
            [
                InlinePanel("home_page_feature_card", label="Znacilnost"),
            ],
            "Nastavitev znacilnosti",
        ),
        # Gallery
        MultiFieldPanel(
            [
                FieldPanel("gallery_title"),
                FieldPanel("gallery_description"),
                FieldPanel("gallery_btn_label"),
            ],
            "Nastavitev galerije",
        ),
        # About me
        MultiFieldPanel(
            [
                FieldPanel("about_image"),
                FieldPanel("about_title"),
                FieldPanel("about_description"),
                FieldPanel("about_btn_label"),
            ],
            "Nastavitev o meni sekcije"
        ),
    ]

    api_fields = [
        # Hero
        APIField("heading"),
        APIField("hero_small_text"),
        APIField("hero_sidebar_links"),
        # CTA
        APIField("cta_title"),
        APIField("cta_small_text"),
        APIField("cta_btn_text"),
        APIField("cta_btn_destination"),
        # Features
        APIField("home_page_feature_card"),
        # Gallery showcase
        APIField("gallery_title"),
        APIField("gallery_description"),
        APIField("gallery_btn_label"),
        # About me
        APIField("about_image", serializer=ImageRenditionField('fill-300x400')),
        APIField("about_title"),
        APIField("about_description"),
        APIField("about_btn_label"),
    ]


class HeroLink(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name="hero_sidebar_links")
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="+"
    )
    destination = models.CharField(max_length=20)
    label = models.CharField(max_length=20)

    panels = [
        FieldPanel("image"),
        FieldPanel("destination"),
        FieldPanel("label"),
    ]

    api_fields = [
        APIField("image", serializer=ImageRenditionField('fill-600x400')),
        APIField("destination"),
        APIField("label"),
    ]


class FeatureCard(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name="home_page_feature_card")
    knife_image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="+"
    )
    heading = models.CharField(max_length=20)
    description = RichTextField()
    btn_label = models.CharField(max_length=20)
    btn_destination = models.CharField(max_length=20)

    panels = [
        FieldPanel("knife_image"),
        FieldPanel("heading"),
        FieldPanel("description"),
        FieldPanel("btn_label"),
        FieldPanel("btn_destination"),
    ]

    api_fields = [
        APIField("knife_image", serializer=ImageRenditionField("width-800")),
        APIField("heading"),
        APIField("description"),
        APIField("btn_label"),
        APIField("btn_destination"),
    ]
