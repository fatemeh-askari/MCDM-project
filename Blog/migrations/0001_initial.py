# Generated by Django 5.0.4 on 2024-05-05 06:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='category title')),
                ('url_title', models.CharField(max_length=200, unique=True, verbose_name='category url title')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created at')),
                ('short_description', models.TextField(blank=True, null=True, verbose_name='category description')),
                ('description', models.TextField(blank=True, null=True, verbose_name='category description')),
                ('image', models.ImageField(blank=True, upload_to='images/category', verbose_name='category image')),
            ],
            options={
                'verbose_name': 'article category',
                'verbose_name_plural': 'article categories',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=350, verbose_name='article title')),
                ('url_title', models.CharField(db_index=True, max_length=350, verbose_name='article url title')),
                ('meta_title', models.CharField(blank=True, max_length=80, null=True, verbose_name='meta title')),
                ('image', models.ImageField(blank=True, upload_to='images/article', verbose_name='article image')),
                ('short_description', models.TextField(blank=True, verbose_name='short description')),
                ('text', models.TextField(blank=True, verbose_name='article text')),
                ('text_with_code', models.TextField(blank=True, verbose_name='article text with code')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created at')),
                ('priority', models.IntegerField(blank=True, null=True, verbose_name='priority')),
                ('author', models.CharField(blank=True, max_length=200, null=True, verbose_name='author name')),
                ('selected_categories', models.ManyToManyField(blank=True, to='Blog.articlecategory', verbose_name="article's categories")),
            ],
            options={
                'verbose_name': 'article',
                'verbose_name_plural': 'articles',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('admin_answer', models.TextField(blank=True, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Blog.article')),
            ],
        ),
    ]
