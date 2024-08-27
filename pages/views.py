from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseRedirect

from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import PagesForm
from .models import Pages
# Create your views here.

class PagesCreateView(LoginRequiredMixin, CreateView):
    model = Pages
    success_url = ''
    form_class = PagesForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    
class PagesListView(LoginRequiredMixin, ListView):
    model = Pages
    context_object_name = 'pages'
    template_name = 'pages_list.html'

def page_detail(request, slug):
    page = get_object_or_404(Pages, slug=slug)
    return render(request, 'pages/page_detail.html', {'page': page})

