from django.contrib import admin
from .models import Category, Recipe


'''
    To register class in admin, u can use the followint choices:
        class CategoryAdmin(admin.ModelAdmin):
            ...

        admin.site.register(Category, CategoryAdmin)
    
    or:
        @admin.register(Category)
        class CategoryAdmin(admin.ModelAdmin):
            ...
'''


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...