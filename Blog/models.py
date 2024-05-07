from django.db import models

class ArticleCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name="category title")
    url_title = models.CharField(max_length=200, unique=True, verbose_name="category url title")
    is_active = models.BooleanField(default=True, verbose_name="is active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at", blank=True, null=True)
    short_description = models.TextField(verbose_name="category description", blank=True, null=True)
    description = models.TextField(verbose_name="category description", blank=True, null=True)
    image = models.ImageField(upload_to='images/category', verbose_name="category image", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "article category"
        verbose_name_plural = "article categories"


class Article(models.Model):
    title = models.CharField(max_length=350 ,verbose_name="article title")
    url_title = models.CharField(max_length=350 ,verbose_name="article url title", db_index=True)
    meta_title = models.CharField(max_length=80 ,verbose_name="meta title", blank=True, null=True)
    image = models.ImageField(upload_to='images/article', verbose_name="article image", blank=True)
    short_description = models.TextField(verbose_name="short description", blank=True)
    text = models.TextField(verbose_name="article text", blank=True)
    text_with_code = models.TextField(verbose_name="article text with code", blank=True)
    is_active = models.BooleanField(default=True, verbose_name="is active")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at", blank=True, null=True)
    priority = models.IntegerField(verbose_name="priority", blank=True, null=True)
    author = models.CharField(max_length=200, verbose_name="author name", blank=True, null=True)
    selected_categories = models.ManyToManyField(ArticleCategory, verbose_name="article's categories", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "article"
        verbose_name_plural = "articles"



class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', default=None)
    name = models.CharField(max_length=100)
    text = models.TextField()
    admin_answer = models.TextField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.text[:50]
