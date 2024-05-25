

def data_insertion(request):
  
  x = MemberTable(firstname = "Mahlet", lastname = 'Aweke', age = 16, joined_date = timezone.now())
  x.save()
  return HttpResponse("It is saved on the table!")

'''
from django.http import HttpResponse
from django.template import loader

 def display(request):
   template = loader.get_template('members/myfirst.html')
   return HttpResponse(template.render())
'''

from django.shortcuts import render
from django.http import HttpResponse
from members.models import MemberTable
from django.utils import timezone

def display(request):
  # my logic, logic 1
  return render(request,'members/myfirst.html')


def list_drink(request):
  return render(request, "members/smth.html" )

def product(request):
  x = 12
  y = 8
  a={'z': x * y}
  return render(request, 'members/product.html',a)



def all_member(request):
  a = MemberTable.objects.all()
  context ={'mymembers':a, 'z': "Yonas"}
  return render(request, 'all_members.html', context )


def members_details(request, id):
  b = MemberTable.objects.get(id=id)
  
  context = {'abi': b,}
  return render(request ,'details.html', context)

def main(request): 
  return render(request, 'main.html')


def debug(request):
  return render(request, '404.html')

def testing(request):
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return render(request, 'template.html',context)


def testing2(request):
  return render(request, 'template2.html')


def testing3(request):
  
  context = {
    'x': ['Apple', 'Banana', 'Cherry'], 
    'y': ['Apple', 'Banana', 'Cherry'], 
  }
  return render(request,'template3.html',context)  

def reversed_loop(request):
  c = MemberTable.objects.all()
  context ={'obje': c}
  return render(request, 'reversed_loop.html', context)
  
  
def include(request):
  return render(request,'django_includeTag.html')

def trying(request):
  mydata = MemberTable.objects.all()
  context = {
    'mymembers': mydata, }
  return render(request, 'trying.html',context )

def trying2(request):
  mydata = MemberTable.objects.values_list('firstname')
  context = { 'mymembers': mydata, }
  return render(request, 'trying2.html',context )

def filter1(request):
  mydata = MemberTable.objects.filter(firstname='Yonas').values()
  context = {'mymembers': mydata}
  return render(request,'filtering1.html',context)


def filter(request):
  mydata = MemberTable.objects.filter(firstname='Solomon', id= 6).values()
  context = {'mymembers': mydata}
  return render(request, 'filter_firstname.html', context)


def filter2(request):
  mydata = MemberTable.objects.filter(firstname='Solomon').values() | MemberTable.objects.filter(firstname='Markos').values()
  context = {'mymembers': mydata}
  return render(request, 'filtering2.html', context)

def startwith(request):
  mydata = MemberTable.objects.filter( firstname__startswith='M').values()
  context = {'mymembers': mydata}
  return render(request, 'startswith_keyword.html', context)


def order(request):
  mydatabase = MemberTable.objects.all().order_by('firstname').values()
  context = {'mymembers': mydatabase}
  return render(request, 'orderBy_keyword.html', context)

def descendingorder(request):
  mydatabase = MemberTable.objects.all().order_by('-firstname').values()
  context = {'mymembers': mydatabase}
  return render(request, 'descending_order.html', context)

def multipleOrder(request):
  mydatabase = MemberTable.objects.all().order_by('lastname', '-id').values()
  context = {'mymembers': mydatabase}
  return render(request, 'multiple_order.html', context)
