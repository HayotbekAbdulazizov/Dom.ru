from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.



class Post(models.Model):
	title = models.CharField("Title", max_length=300, blank=True)
	slug = models.SlugField("*", max_length=300, unique=True, blank=True)
	rich_body = RichTextField()
	published = models.DateTimeField(auto_now_add=True)
	source = models.URLField(max_length=200, blank=True)
	
	def __str__(self):
		return f"{self.title}"

	class Meta:
		ordering = ["-published",]
		verbose_name_plural = 'Posts'
