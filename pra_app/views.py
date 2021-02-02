from django.shortcuts import render
from django.http import HttpResponse
from pra_app import forms
# Create your views here.
def index(request):
	return render(request, 'index.html', {"name1":'Prabhat', 'name2':'Sudha' })

def bye(request):
	return render(request, 'add.html')

def form_view(request):
	form = forms.FormObj()
	if request.method == "POST":
		form = forms.FormObj(request.POST)
		if form.is_valid():
			print(form.cleaned_data['full_name'])
			print(form.cleaned_data['email'])
			print(form.cleaned_data['number'])
			print("Success!")

	return render(request, 'contact_us.html', {'form':form})
