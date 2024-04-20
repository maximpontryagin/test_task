from django.contrib import admin
from django.urls import path
from customers.views import CustomersShowView, ExecutorsShowView, IndexView, ExecutorDetailView, CustomerDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('executors', ExecutorsShowView.as_view(), name='executors'),
    path('customers', CustomersShowView.as_view(), name='customers'),
    path('executor/<slug:name>', ExecutorDetailView.as_view(), name='executor'),
    path('customer/<slug:name>', CustomerDetailView.as_view(), name='customer'),
    
]
