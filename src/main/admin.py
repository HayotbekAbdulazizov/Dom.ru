from tinymce.widgets import TinyMCE
from django.contrib import admin
from .models import Post



#  Registering main Post model
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'id']
	list_display_links = ['title', 'id' ]
	prepopulated_fields = {'slug':('title',)}
   

	