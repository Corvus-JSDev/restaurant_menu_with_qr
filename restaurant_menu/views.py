from django.shortcuts import render
from django.views import generic
from restaurant_menu.models import Item, CATEGORY, AVAILABILITY

# Create your views here.

class MenuList(generic.ListView):
	queryset = Item.objects.order_by("creation_date")
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["meals"] = CATEGORY
		context["available"] = AVAILABILITY

		return context


class MenuItemDetail(generic.DetailView):
	model = Item
	template_name = "menu_item_detail.html"

