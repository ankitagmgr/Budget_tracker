from django.urls import path
from . import views

urlpatterns=[
    path('',views.transaction_list,name="transaction-list"),
    path('add/',views.add_transaction, name='add-transaction')
]