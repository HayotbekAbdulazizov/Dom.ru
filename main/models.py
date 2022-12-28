from tinymce.models import HTMLField
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.



class Post(models.Model):
	title = models.CharField("Title", max_length=300, blank=True)
	slug = models.SlugField("*", unique=True, blank=True)
	category = models.CharField("Category", max_length=200 ,blank=True)
	price = models.PositiveIntegerField("Price", default=0, blank=True)
	priceCurrency = models.CharField("Currency", max_length=20, blank=True)
	pricePerMeter = models.CharField("Price Per Meter", max_length=100, blank=True)
	city = models.CharField("City", max_length=200, blank=True)
	address = models.CharField("Address", max_length=200, blank=True)
	description = models.TextField("Description", blank=True)
	offerId = models.IntegerField("Offer Id", unique=True, blank=True)

	body = RichTextField("Body" , blank=True)
	content = HTMLField()
	published = models.DateTimeField(auto_now_add=True)
	source = models.URLField(max_length=200, blank=True)


	def __str__(self):
		return f"{self.title}"
 
	class Meta:
		ordering = ["-published",]
		verbose_name_plural = 'Posts'











class Contact(models.Model):
	post_id = models.ForeignKey(Post, max_length=20, on_delete=models.CASCADE,blank=True)
	done = models.BooleanField("Status", default=False, blank=True)
	date = models.DateTimeField("date ", auto_now_add=True, blank=True)

	def __str__(self):
		return self.post_id.title




# https://www.youtube.com/watch?v=l9VZlqCbiLk









links = {
	"Купить квартиру на Сахалине":{
		"all":"https://domik65.ru/flat/sell",
		"daily":"https://domik65.ru/list?object=flat&deal=sell&page=1&search_query=ee1b36e93e7cd7befcc1e1c318f533ac"
	},

	"Снять квартиру посуточно на Сахалине":{
		"all":"https://domik65.ru/list?object=flat&deal=lease&s%5Bperiod%5D=%D0%BF%D0%BE%D1%81%D1%83%D1%82%D0%BE%D1%87%D0%BD%D0%BE&page=1&search_query=1d05f563764961fc61f95a0390b3f6c3",
		"daily":"https://domik65.ru/list?object=flat&deal=lease&s%5Bperiod%5D=%D0%BF%D0%BE%D1%81%D1%83%D1%82%D0%BE%D1%87%D0%BD%D0%BE&page=1&search_query=528984f74264b1bb7c144b98c1a1671d"
	},

}