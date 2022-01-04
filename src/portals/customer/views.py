from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, CreateView
from src.portals.admins.models import Event
from src.portals.customer.bll import calculate_price


class DashboardView(TemplateView):
    template_name = 'customer/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['events_all'] = Event.objects.filter(user=self.request.user).count()
        context['events_paid'] = Event.objects.filter(user=self.request.user, is_paid=True).count()
        context['events_un_paid'] = Event.objects.filter(user=self.request.user, is_paid=False).count()
        return context


class EventsListView(ListView):
    template_name = 'customer/event_list.html'

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)


class EventDetailView(DetailView):
    template_name = 'customer/event_detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Event.objects.filter(user=self.request.user), pk=self.kwargs['pk'])


class EventDeleteView(DeleteView):
    template_name = 'customer/event_confirm_delete.html'
    model = Event
    success_url = reverse_lazy("customer-portal:event-list")

    def get_object(self, queryset=None):
        return get_object_or_404(Event.objects.filter(user=self.request.user), pk=self.kwargs['pk'])


class EventCreateView(CreateView):
    template_name = 'customer/event_form.html'
    model = Event
    fields = [
        'name', 'event_type', 'venue', 'add_ons', 'no_of_persons',
        'event_date', 'transaction_id'
    ]
    success_url = reverse_lazy("customer-portal:event-list")

    def form_valid(self, form):
        # TODO: Calculate according to your pricing setup >>
        calculate_price(form, self.request.user)
        form.instance.user = self.request.user
        return super(EventCreateView, self).form_valid(form)
