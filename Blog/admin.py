from django.contrib import admin
from . import models

class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'is_active']
    list_filter = ['url_title', 'is_active']

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'display_selected_categories', 'created_at', 'is_active']

    def display_selected_categories(self, obj):
        return ', '.join(category.title for category in obj.selected_categories.all())

    display_selected_categories.short_description = 'Selected Categories'
    list_filter = ['author', 'selected_categories', 'is_active']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'is_approved', 'article',]
    list_filter = ['is_approved']

admin.site.register(models.ArticleCategory, ArticleCategoryAdmin)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Comment, CommentAdmin)
