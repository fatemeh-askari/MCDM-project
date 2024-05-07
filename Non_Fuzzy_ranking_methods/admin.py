from django.contrib import admin
from .models import Method, Indicator, Choice, Request, MatrixData

@admin.register(Method)
class MethodAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description')
    search_fields = ('name', 'short_description')

@admin.register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'weight', 'method')
    search_fields = ('name', 'type', 'method__name')

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'method')
    search_fields = ('name', 'method__name')

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('method', 'get_indicators', 'get_choices')
    search_fields = ('method__name',)
    filter_horizontal = ('indicators', 'choices')

    def get_indicators(self, obj):
        return ', '.join([indicator.name for indicator in obj.indicators.all()])

    def get_choices(self, obj):
        return ', '.join([choice.name for choice in obj.choices.all()])

