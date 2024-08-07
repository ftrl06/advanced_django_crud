from django.shortcuts import render, redirect, get_object_or_404
from .models import Record
from .forms import RecordForm

def index(request):
    records = Record.objects.all()
    return render(request, 'myapp/index.html', {'records': records})

def add_record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RecordForm()
    return render(request, 'myapp/add_record.html', {'form': form})

def update_record(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RecordForm(instance=record)
    return render(request, 'myapp/update_record.html', {'form': form})

def delete_record(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('index')
    return render(request, 'myapp/delete_record.html', {'record': record})
