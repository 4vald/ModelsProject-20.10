from django.contrib import admin
from .models import Article, Category, Author

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
   list_display = ("id", "title", "author", "category", "created_at")
   search_fields = ("title", "author")
   list_filter = ("category", "created_at")
 
admin.site.register(Category)


class ArticleInline(admin.TabularInline): 
    model = Article
    extra = 0

class UserAdmin(admin.ModelAdmin):
    inlines = [ArticleInline]
    list_display = ('full_name', 'email')

admin.site.register(Author, UserAdmin)
