from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.



class Post(models.Model):
	title = models.CharField("Title", max_length=300, blank=True)

	price = models.PositiveIntegerField("Price", default=0, blank=True)
	priceCurrency = models.CharField("Currency", max_length=20, blank=True)
	pricePerMeter = models.CharField("Price Per Meter", max_length=100, blank=True)
	city = models.CharField("City", max_length=200, blank=True)
	address = models.CharField("Address", max_length=200, blank=True)
	description = models.TextField("Description", blank=True)
	offerId = models.IntegerField("Offer Id", unique=True, blank=True)

	body = RichTextField("Body" , blank=True)
	published = models.DateTimeField(auto_now_add=True)
	source = models.URLField(max_length=200, blank=True)
	
	def __str__(self):
		return f"{self.title}"
 
	class Meta:
		ordering = ["-published",]
		verbose_name_plural = 'Posts'
