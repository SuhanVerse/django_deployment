from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Registration


def registration_form(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            try:
                Registration.objects.create(
                    name=form.cleaned_data['name'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password']
                )
                return render(request, 'registration/form.html',{
                    'form': RegistrationForm(),
                    'success': 'Registration successful!'
                })
            except Exception as e:
                form.add_error(None, 'An error occurred during registration. Please try again.')
    else:
        form = RegistrationForm()

    return render(request, 'registration/form.html', {'form': form})