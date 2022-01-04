from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, CreateView

from src.portals.admins.models import Event


class DashboardView(TemplateView):
    template_name = 'customer/dashboard.html'


class EventsList(ListView):
    template_name = 'customer/event_list.html'

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)


class EventDetail(DetailView):
    template_name = 'customer/event_detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Event.objects.filter(user=self.request.user), pk=self.kwargs['pk'])


class EventDelete(DeleteView):
    template_name = 'customer/event_confirm_delete.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Event.objects.filter(user=self.request.user), pk=self.kwargs['pk'])


class EventCreateView(CreateView):
    template_name = 'customer/event_form.html'

    def form_valid(self, form):
        form.save()
