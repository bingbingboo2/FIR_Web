from django import forms
from .models import FIR  # Import the FIR model

class FIRForm(forms.ModelForm):
    class Meta:
        model = FIR
        fields = '__all__'  # You can specify the fields you want to include if needed

class FIRSearchForm(forms.Form):
    fir_number = forms.CharField(max_length=20, required=False, label='F.I.R. Number')
    ipc = forms.CharField(max_length=20, required=False, label='IPC')

class FIRUpdateIPCForm(forms.ModelForm):
    class Meta:
        model = FIR
        fields = ['ipc_applied']  # Specify the field(s) you want to update
