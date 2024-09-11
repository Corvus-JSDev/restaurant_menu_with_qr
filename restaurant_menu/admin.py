from django.contrib import admin
from restaurant_menu.models import Item

# Register your models here.

class MenuItemAdmin(admin.ModelAdmin):
	list_display = ("meal", "is_available")
	list_filter = ("is_available", )
	search_fields = ("meal", "desc")


admin.site.register(Item, MenuItemAdmin)