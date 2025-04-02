from django.shortcuts import render, redirect
from budget_tracker.models import Transaction
from django.http import HttpResponseRedirect

def transaction_list(request):
    transactions=Transaction.objects.all()
    return render(
        request,
        'transaction.html',
        {"transactions":transactions}
    )
def add_transaction(request):
    if request.method == "POST":
        title = request.POST.get("title")
        amount = request.POST.get("amount")
        type_ = request.POST.get("type")
        category = request.POST.get("category")

        if title and amount and type_ and category:  # Ensure required fields are provided
            Transaction.objects.create(
                title=title,
                amount=amount,
                type=type_,
                category=category
            )
            return redirect("transaction_list")  # Redirect to transaction list after adding

    return render(request, "add_transaction.html")
