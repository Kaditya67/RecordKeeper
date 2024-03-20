from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Customer
from django.urls import resolve
from datetime import date
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum

def index(request):
    current_path = resolve(request.path_info).url_name
    current_date = timezone.now().date()
    customers = Customer.objects.filter(dateUploaded=current_date)
    context = {'customers': customers, 'current_date': current_date, 'current_path': current_path}
    return render(request, 'index.html', context)

def approved(request):
    current_path = resolve(request.path_info).url_name
    customers = Customer.objects.filter(status='approved').order_by('-approvedDate')
    context = {'customers': customers, 'current_path': current_path}
    return render(request, 'approved.html', context)

def pending(request):
    current_path = resolve(request.path_info).url_name
    customers = Customer.objects.filter(status='pending').order_by('dateUploaded')
    context = {'customers': customers, 'current_path': current_path}
    return render(request, 'pending.html', context)

def confirm_approval(request, customer_id):
    current_path = resolve(request.path_info).url_name
    customer = Customer.objects.get(pk=customer_id)
    if request.method == 'POST':
        customer.status = 'approved'
        customer.approvedDate = date.today()
        customer.save()
        messages.success(request, 'Record has been successfully approved.')
        return redirect('approved')
    return render(request, 'confirm_approval.html', {'customer': customer, 'current_path': current_path})

def confirmation_page(request, customer_id):
        
    customer = Customer.objects.get(pk=customer_id)
    return render(request, 'confirmation_page.html', {'customer': customer, 'current_path': current_path})

def past_records(request):
    current_path = resolve(request.path_info).url_name
    current_date = timezone.now().date()
    yesterday = current_date - timedelta(days=1)
    past_records = Customer.objects.exclude(dateUploaded=current_date).order_by('-dateUploaded')
    context = {'past_records': past_records, 'current_date': current_date, 'yesterday': yesterday, 'current_path': current_path}
    return render(request, 'past_records.html', context)

def past_30_days_revenue(request):
    current_path = resolve(request.path_info).url_name
    thirty_days_ago = timezone.now().date() - timedelta(days=30)
    past_30_days_approved_records = Customer.objects.filter(status='approved', dateUploaded__gte=thirty_days_ago)
    total_fees_charged = past_30_days_approved_records.aggregate(total_fees_charged=Sum('FeesChargedToCustomer'))['total_fees_charged']
    total_govt_fees = past_30_days_approved_records.aggregate(total_govt_fees=Sum('GovtFees'))['total_govt_fees']
    context = {
        'past_30_days_approved_records': past_30_days_approved_records,
        'total_fees_charged': total_fees_charged if total_fees_charged else 0,
        'total_govt_fees': total_govt_fees if total_govt_fees else 0,
        'current_path': current_path
    }
    return render(request, 'past_30_days_revenue.html', context)
