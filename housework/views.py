from django.shortcuts import render
from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy
from .models import HouseworkModel,HOUSEWORK_CATEGORY

# Create your views here.


def listview(request):
    object_list = HouseworkModel.objects.all()
    ans_list = []
    #print('------------test-------------')
    #print(type(object_list))

    for key in HOUSEWORK_CATEGORY:
        getobject = object_list.filter(category = key[0]).order_by('postdate').reverse()[0]
        if(getobject is not None):
            ans_list.append(getobject)
    return render(request,'list.html',{'object_list':ans_list})

class CreateClass(CreateView):
    template_name = 'create.html'
    model = HouseworkModel
    fields = ('postdate','category','username','suntext')
    success_url = reverse_lazy('list')

def detailview(request,ck):
    object_list = HouseworkModel.objects.all().filter(category = ck).order_by('postdate').reverse()
    dct = dict((x, y) for x, y in HOUSEWORK_CATEGORY)
    return render(request,'detail.html',{'object_list':object_list,'category_name':dct[ck]})


class DeleteClass(DeleteView):
    template_name = 'delete.html'
    model = HouseworkModel
    success_url = reverse_lazy('list')


