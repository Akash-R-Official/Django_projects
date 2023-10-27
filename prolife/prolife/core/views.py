from django.http import JsonResponse
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'core/index.html')

@csrf_exempt
def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # Send an email (You need to configure email settings in Django)
        send_mail('New Subscriber', 'Email: ' + email, 'your@example.com', ['your@example.com'])

        return JsonResponse({'success': True})
    return JsonResponse({'success': False})