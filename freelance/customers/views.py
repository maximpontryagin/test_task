from django.shortcuts import render
from . import models
from django.views.generic import DetailView, TemplateView, ListView


class IndexView(TemplateView):
    """View класс для отображения начальной страницы."""

    template_name = 'index.html'


class CustomersShowView(ListView):
    """View класс для отображения списка покупателей."""

    model = models.CustomerProfile
    template_name = 'customers_list.html'
    context_object_name = 'customers'


class ExecutorsShowView(ListView):
    """View класс для отображения списка исполнителей."""

    model = models.ExecutorProfile
    template_name = 'executors_list.html'
    context_object_name = 'executors'


class ExecutorDetailView(DetailView):
    """View класс для отображения кабинета исполнителя."""

    model = models.ExecutorProfile
    template_name = 'executor_detail.html'
    slug_url_kwarg = 'name'
    slug_field = 'name'
    context_object_name = 'executor'


class CustomerDetailView(DetailView):
    """View класс для отображения кабинета заказчика."""

    model = models.CustomerProfile
    template_name = 'customer_detail.html'
    slug_url_kwarg = 'name'
    slug_field = 'name'
    context_object_name = 'customer'
