from django.shortcuts import render, redirect
from .models import FIR
from .forms import FIRForm, FIRSearchForm, FIRUpdateIPCForm

def dashboard(request):
    # Get a list of FIR records
    fir_list = FIR.objects.all()
    
    # Initialize the search form
    search_form = FIRSearchForm(request.GET)
    
    if search_form.is_valid():
        fir_number = search_form.cleaned_data.get('fir_number')
        ipc = search_form.cleaned_data.get('ipc')
        fir_list = FIR.objects.filter(fir_number__icontains=fir_number, ipc_applied__icontains=ipc)
    
    context = {'fir_list': fir_list, 'search_form': search_form}
    return render(request, 'dashboard/dashboard.html', context)

def add_fir(request):
    if request.method == 'POST':
        form = FIRForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = FIRForm()
    
    context = {'form': form}
    return render(request, 'dashboard/add_fir.html', context)

def update_ipc(request, fir_id):
    fir = FIR.objects.get(id=fir_id)
    
    if request.method == 'POST':
        form = FIRUpdateIPCForm(request.POST, instance=fir)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = FIRUpdateIPCForm(instance=fir)
    
    context = {'form': form, 'fir': fir}
    return render(request, 'dashboard/update_ipc.html', context)
