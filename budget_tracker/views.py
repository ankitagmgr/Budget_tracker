from django.shortcuts import render
from budget_tracker.models import Transaction
from django.http import HttpResponseRedirect

def transaction_list(request):
    return render(
        request,
        'transaction.html',
    )
