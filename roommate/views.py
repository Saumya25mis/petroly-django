from django.shortcuts import render
from .models import Bid
from django.views.generic import (
    TemplateView,
    ListView,
    DeleteView,
    DetailView,
    CreateView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse


class BidCreateView(LoginRequiredMixin, CreateView):
    model = Bid
    fields = [
        'name', 'phone', 'smoking', 
        'staying_up', 'temperature', 'region'
    ]

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class BidDeleteView(DeleteView):
    model = Bid
    success_url = reverse_lazy('roommate:bid_list')


class BidUpdateView(UpdateView):
    model = Bid
    fields = [
        'name', 'phone', 'smoking', 
        'staying_up', 'temperature', 'region'
    ]


class BidDetailView(DetailView):
    model = Bid


class BidListView(ListView):
    model = Bid
