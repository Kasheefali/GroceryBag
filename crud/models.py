from django.db import models

# Create your models here.

class Product(models.Model):
	CATEGORY = (
		('PENDING', 'PENDING'),
		('BOUGHT', 'BOUGHT'),
		('NOT AVAILABLE', 'NOT AVAILABLE'),
		)

	item_name = models.CharField(max_length=200, null=True)
	item_quantity = models.CharField(max_length=200)
	item_status = models.CharField(max_length=200, null=True, choices=CATEGORY)
	date_created = models.DateField(auto_now_add=False, null=True)

	def __str__(self):
		return self.item_name