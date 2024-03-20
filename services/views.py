from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Customer
from django.urls import resolve
from datetime import date
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    current_path = resolve(request.path_info).url_name
    current_date = timezone.now().date()
    customers = Customer.objects.filter(dateUploaded=current_date)
    context = {'customers': customers, 'current_date': current_date, 'current_path': current_path}
    return render(request, 'index.html', context)

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Changed to auth_login to avoid conflict
            # messages.success(request, "Successfully Logged In")
            return redirect('index')  # Redirect to the home page or any other desired page
        else:
            print(f"Failed login attempt for user: {username}")
            messages.error(request, "Invalid credentials! Please try again")
            return render(request, "login.html")
    return render(request, 'login.html')

@login_required
def approved(request):
    current_path = resolve(request.path_info).url_name
    customers = Customer.objects.filter(status='approved').order_by('-approvedDate')
    context = {'customers': customers, 'current_path': current_path}
    return render(request, 'approved.html', context)

@login_required
def pending(request):
    current_path = resolve(request.path_info).url_name
    customers = Customer.objects.filter(status='pending').order_by('dateUploaded')
    context = {'customers': customers, 'current_path': current_path}
    return render(request, 'pending.html', context)

@login_required
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

@login_required
def confirmation_page(request, customer_id):
        
    customer = Customer.objects.get(pk=customer_id)
    return render(request, 'confirmation_page.html', {'customer': customer, 'current_path': current_path})

from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Customer  # Import your Customer model here

@login_required
def past_records(request):
    current_path = resolve(request.path_info).url_name
    customers = Customer.objects.exclude(dateUploaded=timezone.now().date())
    context = {'customers': customers,'current_path': current_path}
    return render(request, 'past_records.html', context)

@login_required
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
