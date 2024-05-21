from django.db import models

# Create your models here.
class FIR(models.Model):
    fir_number = models.CharField(max_length=20)
    complainant_name = models.CharField(max_length=100)
    time = models.DateTimeField()
    ipc_applied = models.CharField(max_length=20)
    pdf_fir = models.FileField(upload_to='fir_pdfs/')
    

    class Meta:
        app_label = 'dashboard'  