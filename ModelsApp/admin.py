from django.contrib import admin
from .models import Article, Category

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
   list_display = ("id", "title", "author", "category", "created_at")
   search_fields = ("title", "author")
   list_filter = ("category", "created_at")
 
admin.site.register(Category)