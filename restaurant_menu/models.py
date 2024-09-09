from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY = (
	("starters", 'Starters'),
	("salades", "Salades"),
	("mean_dishes", "Mean Dishes"),
	("desserts", "Desserts")
)

AVAILABILITY = (
	(0, "no"),
	(1, "yes")
)


class Item(models.Model):
	meal = models.CharField(max_length=200, unique=True)
	desc = models.CharField(max_length=2000)
	price = models.DecimalField(decimal_places=2, max_digits=2)
	category = models.CharField(max_length=500, choices=CATEGORY)
	# author = models.ForeignKey(User, on_delete=models.CASCADE)  # If the user is deleted from the tabel, all the items that user created would also be deleted
	author = models.ForeignKey(User, on_delete=models.PROTECT)  # If the user is deleted from the tabel, none of its creations will be deleted
	available = models.IntegerField(choices=AVAILABILITY, default=0)
	creation_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.meal
