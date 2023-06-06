from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Items
from django.template import loader
from .forms import Itemform
# Create your views here.

def index(request):
    queryset=Items.objects.all()
    template=loader.get_template('food/index.html')
    context={
        'queryset':queryset,
    }

    return HttpResponse(template.render(context,request))
def item_detail(request,item_id):
    item=Items.objects.get(pk=item_id)
    context={
        'item':item,
    }
    return render(request,'food/details.html',context)

def add_item(request):
    form =Itemform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/add.html',{'form':form})

def update_item(request,item_id):
    item=Items.objects.get(id=item_id)
    form =Itemform(request.POST or None,instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/add.html',{'form':form,'item':item})

def delete_item(request,item_id):
    item=Items.objects.get(id=item_id)
    if request.method=='POST':
        item.delete()
        return redirect('food:index')
    return render(request,'food/delete.html',{'item':item})

