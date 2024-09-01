from django.shortcuts import render

def settings(request):
    return render(request, 'settings/info.html')

def notifications(request):
    return render(request, 'settings/notifications.html')

def activity(request):
    return render(request, 'settings/activity.html')

def security(request):
    return render(request, 'settings/security.html')