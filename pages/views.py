from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .forms import PagesForm, DetailsForm
from .models import Pages, Details
# Create your views here.

class PagesCreateView(LoginRequiredMixin, CreateView):
    model = Pages
    success_url = '/pages'
    form_class = PagesForm
    template_name = 'pages/pages_create.html'
    login_url = "/register"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    
class PagesListView(LoginRequiredMixin, ListView):
    model = Pages
    context_object_name = 'pages'
    template_name = 'pages_list.html'
    login_url = "/register"

@login_required(login_url='/register')
def page_detail(request, slug):
    page = get_object_or_404(Pages, slug=slug)
    details = Details.objects.filter(title=page.title)  # Filter details by page title
    return render(request, 'pages/pages_detail.html', {'page': page, 'details': details})


class DetailsCreateView(LoginRequiredMixin, CreateView):
    model = Details
    success_url = '/pages'
    form_class = DetailsForm
    template_name = 'pages/pages_details_create.html'
    login_url = "/register"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    

class PagesUpdateView (LoginRequiredMixin, UpdateView):
    model = Pages
    success_url = '/pages'
    form_class = PagesForm
    template_name = 'pages/pages_create.html'
    login_url = "/register"

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