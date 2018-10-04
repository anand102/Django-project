from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Social
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def social_list(request):
	social = Social.objects.all().order_by('date')
	return render(request, 'socio/social.html',{'social':social})

def social_detail(request,slug):
	#return HttpResponse(slug)
	social =Social.objects.get(slug=slug)
	return render(request , 'socio/details.html', {'social':social})

@login_required(login_url='/accounts/login')
def social_create(request):
    if request.method == 'POST':
        form =forms.CreateSocio(request.POST, request.FILES)
        if form.is_valid():
		# save data to db
            instance = form.save(commit=False)
            instance.profile = request.user
            instance.save()
            return redirect('socio:list')
    else:
        form = forms.CreateSocio()
    return render(request, 'socio/create.html',{'form':form})	
