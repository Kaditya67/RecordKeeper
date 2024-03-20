from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    customerName = models.CharField(max_length=100)
    CustomerUserId = models.CharField(max_length=100, unique=True)
    Password = models.CharField(max_length=100)  # You should hash passwords in production
    CustomerPhone = models.CharField(max_length=15)
    GovtFees = models.DecimalField(max_digits=10, decimal_places=2)
    ApplicationNo = models.CharField(max_length=100)

    APPROVED = 'approved'
    PENDIND='pending'
    STATUS_CHOICES=[
        (APPROVED,'Approved'),
        (PENDIND,"Pending")
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)  # Status of Document: Approved, Rejected, In Process, Pending
    FeesChargedToCustomer = models.DecimalField(max_digits=10, decimal_places=2)
    Tehsil = models.CharField(max_length=100)

    # Fields from Document class
    documentType = models.CharField(max_length=100)  # Types of Document
    dateUploaded = models.DateField()
    operator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    Referral = models.CharField(max_length=100)
    Comments = models.TextField(blank=True, null=True)
    approvedDate = models.DateField(null=True, blank=True)