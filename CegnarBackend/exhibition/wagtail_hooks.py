from wagtail import hooks
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from .models import ProductCategory, GalleryImage


# Icons
@hooks.register("register_icons")
def register_icons(icons):
    return icons + ["exhibition/category.svg"]


class ProductCategoryViewSet(SnippetViewSet):
    model = ProductCategory
    icon = "category"
    menu_label = "Kategorije izdelkov"
    add_to_admin_menu = True

# register_snippet(ProductCategory)  # register call below seems to register both
register_snippet(ProductCategoryViewSet)


class ImageViewSet(SnippetViewSet):
    model = GalleryImage
    icon = "image"
    list_display = ["__str__", "category__name", "category__super_category", "created_at"]
    list_filter = ["category__name", "category__super_category"]
    menu_label = "Izdelki"
    add_to_admin_menu = True

register_snippet(ImageViewSet)
