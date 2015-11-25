from django.shortcuts import render
from . models import Entry

# Create your views here.
from django.shortcuts import get_list_or_404, get_object_or_404, render

def index(request):
   entry = get_list_or_404(Entry.objects.order_by('-modified'))
   context = {'entry': entry}   
   return render(request, 'todaylearned/index.html', context)

def details(request, entry_id):
   entry = get_object_or_404(Entry, pk=entry_id)
   context = {'entry': entry}   
   return render(request, 'todaylearned/details.html', context)
