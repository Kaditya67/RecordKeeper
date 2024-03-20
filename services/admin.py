# admin.py

from django.contrib import admin
from .models import Customer  # Import the Admin model


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_user_id', 'customer_phone', 'comments', 'govt_fees', 'application_no',
                    'fees_charged_to_customer', 'tehsil', 'referral', 'document_type', 'date_uploaded', 'status',
                    'operator')

    def customer_name(self, obj):
        return obj.customerName

    def customer_user_id(self, obj):
        return obj.CustomerUserId

    def customer_phone(self, obj):
        return obj.CustomerPhone

    def comments(self, obj):
        return obj.Comments

    def govt_fees(self, obj):
        return obj.GovtFees

    def application_no(self, obj):
        return obj.ApplicationNo

    def fees_charged_to_customer(self, obj):
        return obj.FeesChargedToCustomer

    def tehsil(self, obj):
        return obj.Tehsil

    def referral(self, obj):
        return obj.Referral

    def document_type(self, obj):
        return obj.documentType

    def date_uploaded(self, obj):
        return obj.dateUploaded

    def status(self, obj):
        return obj.status

    def operator(self, obj):
        return obj.operator


# Register the Admin model
admin.site.register(Customer, CustomerAdmin)

