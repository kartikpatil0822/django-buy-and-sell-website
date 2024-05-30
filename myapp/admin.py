from django.contrib import admin
from .models import Product

# Register your models here.

# Change the header text
admin.site.site_header = 'Buy & Sell Website'

# Changing title
admin.site.site_title = 'ABC Website'

# Changing index title
admin.site.index_title = 'Manage ABC buying website'

# overriding the existing implementation of displaying model in django admin panel
class ProductAdmin(admin.ModelAdmin):
    # implementing the search field using name
    search_fields = ('name',)
    # listing the fields that will be displayed the existing model
    list_display = ('name', 'price', 'desc')
    
    # adding custom action items in models. Default is delete
    def set_price_to_zero(self, request, queryset):
        queryset.update(price=0)
    
    actions = ('set_price_to_zero',)

    # making fields editable
    list_editable = ('price', 'desc')


admin.site.register(Product, ProductAdmin)