from django.shortcuts import render

# Create your views here.

def display(request):
    context = {
        "balance":"4000"
    }
    return render(request, 'accounts/account.html', context)