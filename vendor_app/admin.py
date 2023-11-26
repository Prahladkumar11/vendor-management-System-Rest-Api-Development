# Import necessary modules from Django
from django.contrib import admin
from .models import *

# Define the administration settings for the 'vendor' model
class CompanyAdmin(admin.ModelAdmin):
    """
    Customizes the appearance of the 'vendor' model in the Django admin interface.
    """
    list_display = ['name', 'address', 'vendor_code']
    # Specifies the fields to be displayed in the change list view

# Define the administration settings for the 'purchaseOrder' model
class PurchaseOrderAdmin(admin.ModelAdmin):
    """
    Customizes the appearance of the 'purchaseOrder' model in the Django admin interface.
    """
    list_display = ['poNumber', 'vendor', 'orderDate', 'issueDate']
    # Specifies the fields to be displayed in the change list view

# Register the 'Performance' model with the Django admin interface
admin.site.register(Performance)
# Registers the model without custom admin settings

# Register the 'vendor' model with the Django admin interface using the custom settings
admin.site.register(vendor, CompanyAdmin)
# Registers the model with custom admin settings

# Register the 'purchaseOrder' model with the Django admin interface using the custom settings
admin.site.register(purchaseOrder, PurchaseOrderAdmin)
# Registers the model with custom admin settings
