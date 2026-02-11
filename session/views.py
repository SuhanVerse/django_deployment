from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from .models import Student

def student_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            student = Student.objects.get(username=username)
            if check_password(password, student.password):
                request.session['student_id'] = student.id
                request.session['username'] = student.username
                return redirect('dashboard')
            else:
                return render(request, 'session/login.html', {'error': 'Invalid password'})
        except Student.DoesNotExist:
            return render(request, 'session/login.html', {'error': 'Username does not exist'})
    
    return render(request, 'session/login.html')


def dashboard(request):
    if 'student_id' not in request.session:
        return redirect('login')
    
    student_id = request.session.get('student_id')
    student = Student.objects.get(id=student_id)
    return render(request, 'session/dashboard.html', {'student': student})


def logout(request):
    request.session.flush()
    return redirect('login')


def student_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        name = request.POST.get('name')
        email = request.POST.get('email')

        if password != confirm_password:
            return render(request, 'session/register.html', {'error': 'Passwords do not match'})

        if Student.objects.filter(username=username).exists():
            return render(request, 'session/register.html', {'error': 'Username already exists'})

        if Student.objects.filter(email=email).exists():
            return render(request, 'session/register.html', {'error': 'Email already registered'})

        Student.objects.create(
            username=username,
            password=make_password(password),
            name=name,
            email=email
        )
        return render(request, 'session/register.html', {'success': 'Account created successfully!'})
    return render(request, 'session/register.html')
