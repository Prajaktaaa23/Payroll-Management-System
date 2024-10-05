# accounts/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 
from .views import payroll_management
from .views import send_salary_email
from .views import password_reset_request


urlpatterns = [
    path('register/employee/', views.register_employee, name='register_employee'),
    path('register/hr/', views.register_hr, name='register_hr'),
    path('login/', views.login_view, name='login'),
    path('employee/dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('hr/dashboard/', views.hr_dashboard, name='hr_dashboard'),
    path('employee/leave/', views.employee_leave_management, name='employee_leave_management'),
    path('hr/leave/', views.hr_leave_management, name='hr_leave_management'),
    path('payroll_management/', payroll_management, name='payroll_management'),
    path('calculate_salary/', views.calculate_salary, name='calculate_salary'),
    path('send_salary_email/', send_salary_email, name='send_salary_email'),
    path('user-management/', views.user_management, name='user_management'),
    path('user-management/edit/', views.user_management, name='user_management'),
    path('password_reset/', password_reset_request, name='password_reset_request'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
]



    




    

