from django.shortcuts import render
from .models import Company
from .forms import CompanyForm
from .bulk_upload import handle_uploaded_file

def single_entry(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CompanyForm()
    return render(request, 'company/single_entry.html', {'form': form})

def bulk_upload(request):
    if request.method == 'POST' and request.FILES['file']:
        handle_uploaded_file(request.FILES['file'])
    return render(request, 'company/bulk_upload.html')

from django.shortcuts import render
from .models import Employee

def search_employees(request):
    query = request.GET.get('q')
    employees = Employee.objects.filter(name__icontains=query)
    return render(request, 'employee/search_results.html', {'employees': employees})

