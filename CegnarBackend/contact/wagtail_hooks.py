from wagtail import hooks
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from .models import Order


class OrderViewSet(SnippetViewSet):
    model = Order
    icon = "mail"
    list_display = ["__str__", "created_at"]
    menu_label = "Sporočila/naročila"
    add_to_admin_menu = True

# register_snippet(ProductCategory)  # register call below seems to register both
register_snippet(OrderViewSet)
