from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import webNote      
from .forms import webNoteForm   

def lst(request):       
    notes = webNote.objects.filter(published_date__lte=timezone.now()).order_by('published_date')   #
    return render(request, 'lst.html', {'notes': notes})       

def detail(request, pk):
    note = get_object_or_404(webNote, pk=pk)
    return render(request, 'detail.html', {'note': note})

def new(request):           
    if request.method == "POST":
        form = webNoteForm(request.POST)        
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.published_date = timezone.now()
            note.save()
            return redirect('detail', pk=note.pk)           
    else:
        form = webNoteForm()                    
    return render(request, 'edit.html', {'form': form})     

def edit(request, pk):      
    note = get_object_or_404(webNote, pk=pk)    
    if request.method == "POST":
        form = webNoteForm(request.POST, instance=note)     
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.published_date = timezone.now()
            note.save()
            return redirect('detail', pk=note.pk)           
    else:
        form = webNoteForm(instance=note)                   
    return render(request, 'edit.html', {'form': form})     
