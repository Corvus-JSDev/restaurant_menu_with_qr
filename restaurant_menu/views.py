from django.shortcuts import render
from django.views import generic
from restaurant_menu.models import Item

# Create your views here.

class MenuList(generic.ListView):
	queryset = Item.objects.order_by("creation_date")
	template_name = "index.html"


class MenuItemDetail(generic.DetailView):
	model = Item
	template_name = "menu_item_detail.html"

