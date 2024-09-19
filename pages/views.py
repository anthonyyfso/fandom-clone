from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from .forms import PagesForm, DetailsForm

from .models import Pages, Details
# Create your views here.

@login_required(login_url='/register')
def pages_create(request):
    if request.method == 'POST':
        form = PagesForm(request.POST, request.FILES) 

        if form.is_valid():
            page = form.save(commit=False)
            page.user = request.user 
            page.save()

            return redirect('/pages')  
    else:
        form = PagesForm()

    return render(request, 'pages/pages_create.html', {'form': form})


@login_required(login_url='/register')
def pages_list(request):
    pages = Pages.objects.all()
    return render(request, 'pages/pages_list.html', {'pages': pages})

@login_required(login_url='/register')
def page_detail(request, slug):
    page = get_object_or_404(Pages, slug=slug)
    details = Details.objects.filter(title=page.title) 
    return render(request, 'pages/pages_detail.html', {'page': page, 'details': details})

def details_create(request, page_slug):
    if request.method == 'POST':
        form = DetailsForm(request.POST)
        if form.is_valid():
            detail = form.save(commit=False)
            detail.user = request.user
            page = get_object_or_404(Pages, slug=page_slug)
            detail.page = page
            detail.save()

            success_url = reverse('pages.detail', kwargs={'slug': page_slug})
            return HttpResponseRedirect(success_url)
    else:
        title = request.GET.get('title', '')
        form = DetailsForm(initial={'title': title})
    
    return render(request, 'pages/pages_details_create.html', {'form': form}) 


def pages_update(request, page_slug):
    page = get_object_or_404(Pages, slug=page_slug)
    if request.method == 'POST':
        form = PagesForm(request.POST, request.FILES, instance=page) 
        if form.is_valid():
            form.save()
            
            success_url = reverse('pages.detail', kwargs={'slug': page_slug})
            return HttpResponseRedirect(success_url)
    else:
        form = PagesForm(instance=page)
    return render(request, 'pages/pages_create.html', {'form': form})

def PageSearch(request):
    if request.method == 'POST':
        searched = request.POST.get('searched', '')
        OurPages = Pages.objects.filter(title__icontains=searched)
        if OurPages.count() == 1:
            single_page = OurPages.first()
            return redirect(reverse('pages.detail', kwargs={'slug': single_page.slug}))
        return render(request, 'pages/pages_searched.html', {'searched': searched, 'OurPages': OurPages})
    else:
        return render(request, 'pages/pages_searched.html', {})