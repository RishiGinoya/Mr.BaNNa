from django.shortcuts import render


def home(request):
    """Home page - displays single indicator "51 by GoldmanMrBaNNa" """
    return render(request, 'main/home.html')


def pricing(request):
    """Pricing page - $99/month and $999/yearly plans"""
    return render(request, 'main/pricing.html')


def contact(request):
    """Contact page - directs to Telegram admin bot"""
    return render(request, 'main/contact.html')


def faq(request):
    """FAQ page"""
    return render(request, 'main/faq.html')


def terms_conditions(request):
    """Terms and Conditions page view"""
    return render(request, 'main/terms_conditions.html')


def privacy_policy(request):
    """Privacy Policy page view"""
    return render(request, 'main/privacy_policy.html')

