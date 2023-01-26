from django.shortcuts import render
from  store.models import Prdouct
from  django.db.models import Q
# Create your views here.

def SearchResult(request):
    products=None
    query=None
    if 'q' in request.GET:
        query= request.GET.get('q')
        products=Prdouct.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
        return render(request,'search.html',{'query':query,'products':products})