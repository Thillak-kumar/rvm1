from django.shortcuts import render,redirect
from django.http import HttpResponse
from database.models import student
from database.forms import Reg


# Create your views here.
def register(request):
	if request.method == 'POST':
		formdata = Reg(request.POST)
		if formdata.is_valid():
			formdata.save()
			return redirect('http://127.0.0.1:8000/details/')
	formdata = Reg()
	return render(request,'database/register.html',{'data':formdata})
def details(request):
	if 'q' in request.GET:
		q=request.GET['q']
		posts=student.objects.filter(Name__icontains=q)
	else:
		posts=student.objects.all()
	data = student.objects.all()
	return render(request,'database/details.html',{'data':data})
def update(request,id):
	a = student.objects.get(id=id)
	if request.method == 'POST':
		u = Reg(request.POST,instance=a)
		if u.is_valid():
			u.save()
			return redirect('http://127.0.0.1:8000/details/')
	u = Reg(instance=a)
	return render(request,'database/update.html',{'u':u})
def delete(request,id):
	ob = student.objects.get(id=id)
	ob.delete()
	return redirect('http://127.0.0.1:8000/details/')
	return render(request,'database/delete.html',{'info':ob})
def index(request):
	
	return render(request,'database/index.html')

def display(request,P):
	data = student.objects.filter(Roll_No=P)
	return render(request,'database/display.html',{'data':data})
	
def search(request):
	if request.method == 'POST':
		q = request.POST['q']
		a=student.objects.filter(Roll_No=q)
		return render(request,'database/search.html',{'q':q},{'a':a})
	

	

   