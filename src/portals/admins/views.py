from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, TemplateView

from src.accounts.models import User
from .models import (
    Event, EventType, Venue, AddOn
)


class DashboardView(TemplateView):
    template_name = 'admins/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.count()
        context['users'] = User.objects.filter().count()
        context['admins'] = User.objects.filter(is_staff=True, is_active=True).count()
        context['customer'] = User.objects.filter(is_customer=True, is_active=True).count()
        return context


""" ADD ON """


class AddonListView(ListView):
    queryset = AddOn.objects.all()


class AddonUpdateView(UpdateView):
    queryset = AddOn.objects.all()
    fields = ['name', 'price', 'is_active']
    success_url = reverse_lazy('admin-portal:addon-list-view')


class AddonCreateView(CreateView):
    model = AddOn
    fields = ['name', 'price', 'is_active']
    success_url = reverse_lazy('admin-portal:addon-list-view')


class AddonDeleteView(DeleteView):
    model = AddOn
    success_url = reverse_lazy('admin-portal:addon-list-view')


""" EVENT TYPES """


class EventTypeListView(ListView):
    queryset = EventType.objects.all()


class EventTypeUpdateView(UpdateView):
    queryset = EventType.objects.all()
    fields = ['name', 'description', 'is_active']
    success_url = reverse_lazy('admin-portal:eventtype-list-view')


class EventTypeCreateView(CreateView):
    model = EventType
    fields = ['name', 'description', 'is_active']
    success_url = reverse_lazy('admin-portal:eventtype-list-view')


class EventTypeDeleteView(DeleteView):
    model = EventType
    success_url = reverse_lazy('admin-portal:eventtype-list-view')


""" VENUES """


class VenueListView(ListView):
    queryset = Venue.objects.all()


class VenueUpdateView(UpdateView):
    queryset = Venue.objects.all()
    fields = ['name', 'description', 'is_active']
    success_url = reverse_lazy('admin-portal:venue-list-view')


class VenueCreateView(CreateView):
    model = Venue
    fields = ['name', 'description', 'is_active']
    success_url = reverse_lazy('admin-portal:venue-list-view')


class VenueDeleteView(DeleteView):
    model = Venue
    success_url = reverse_lazy('admin-portal:venue-list-view')


""" EVENT """


class EventListView(ListView):
    queryset = Event.objects.all()


class EventDetailView(DetailView):
    model = Event


class EventUpdateView(UpdateView):
    model = Event
    fields = '__all__'
    success_url = reverse_lazy('admin-portal:event-list-view')


class EventDeleteView(DeleteView):
    model = Event
    success_url = reverse_lazy('admin-portal:event-list-view')


""" PAYMENT VERIFICATION """


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class PaymentVerificationEasyPaisa(View):

    def get(self, request):
        return render(request=request, template_name="admins/easypaisa_payment_verification.html")

    def post(self, request):

        transaction_id = request.POST['transaction_id']
        transaction = Event.objects.filter(transaction_id=transaction_id)

        # IF TRANSACTION ID EXISTS OR NOT
        if transaction:
            transaction = transaction[0]

            # IF TRANSACTION ALREADY EXISTS
            if not transaction.is_paid:

                transaction.is_paid = True
                transaction.save()
                messages.success(
                    request, f"Transaction {transaction.pk} amount {transaction.event_charge} paid by "
                             f"{transaction.user} verified successfully, and event is reserved")
            else:
                messages.error(request, "This transaction is  already verified.")
        else:
            messages.error(request, "No transaction record available with requested ID.")

        return render(request=request, template_name="admins/easypaisa_payment_verification.html")
