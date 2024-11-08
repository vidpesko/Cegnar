from wagtail import hooks
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from .models import ProductCategory


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