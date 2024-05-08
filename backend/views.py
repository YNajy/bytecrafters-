from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserSignupForm, CustomersForm
from .models import Customers

@login_required
def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'shop/product_list.html', {'products': products})

def index(request):
    return render(request, 'index.html')

def mens(request):
    return render(request, 'men.html')

def women(request):
    return render(request, 'women.html')

def about(request):
    return render(request, 'about.html')

def registration(request):
    if request.method == 'POST':
        # Handle POST request for form submission
        user_form = UserSignupForm(request.POST)
        profile_form = CustomersForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_instance = user_form.save(commit=False)
            user_instance.set_password(user_form.cleaned_data['password'])
            user_instance.save()
            profile_instance = profile_form.save(commit=False)
            profile_instance.user = user_instance
            profile_instance.save()
            messages.success(request, 'You have successfully registered.')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        # Handle GET request to prefill form from URL parameters
        user_form = UserSignupForm()
        profile_form = CustomersForm()

        # Extract parameters from URL query string
        first_name = request.GET.get('firstname')
        last_name = request.GET.get('lastname')
        location = request.GET.get('location', None)  # Set default value to None if location is empty
        phone = request.GET.get('phone')
        email = request.GET.get('email')

        if first_name and last_name and phone and email:
            # Create a new customer instance with the provided parameters
            customer = Customers(
                first_name=first_name,
                last_name=last_name,
                city=location,
                phone=phone,
                email=email
            )
            customer.save()
            messages.success(request, 'Registration successful.')
            return redirect('index')

    return render(request, 'registration.html', {'user_form': user_form, 'profile_form': profile_form})
