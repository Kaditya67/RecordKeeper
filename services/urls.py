from django.contrib import admin
from django.urls import path
from services import views


urlpatterns = [
    path('',views.login,name="login"),
    path('index/',views.index,name="index"),
    path('approved/',views.approved,name="approved"),
    path('pending/',views.pending,name="pending"),
    path('past_records/',views.past_records,name="past_records"),
    path('past-30-days-revenue/',views.past_30_days_revenue, name='past_30_days_revenue'),
    path('confirm-approval/<int:customer_id>/', views.confirm_approval, name='confirm_approval'),
    path('confirmation-page/<int:customer_id>/', views.confirmation_page, name='confirmation_page'),
]
 