from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import (
    Event, EventType, Venue, AddOn, Payment
)


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