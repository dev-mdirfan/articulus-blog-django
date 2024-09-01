from django.shortcuts import render

def user_details(request, pk):
    return render(request, 'users/user_details.html')