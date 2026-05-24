from django.conf import settings
from django.shortcuts import redirect, render


def home_page(request):
    demo_sites = [
        {
            "title": "Restaurant Website",
            "subtitle": "Menu and bookings demo",
            "description": "A hospitality-style landing page built to highlight food, ambience, reservations, and contact details.",
            "url_name": "demo_website_restaurant_1",
            "icon": "fa-utensils",
            "accent": "linear-gradient(135deg, rgba(214,108,43,0.95), rgba(252,187,92,0.78))",
            "highlights": ["Menu", "Reservations", "Events"],
        },
        {
            "title": "Real Estate Website",
            "subtitle": "Property showcase demo",
            "description": "A clean property presentation page for featured listings, trust signals, and location-led browsing.",
            "url_name": "demo_website_realstate_1",
            "icon": "fa-building",
            "accent": "linear-gradient(135deg, rgba(94,122,168,0.95), rgba(132,164,208,0.78))",
            "highlights": ["Properties", "Search", "Lead capture"],
        },
        {
            "title": "Gym Website",
            "subtitle": "Fitness brand demo",
            "description": "A bold, action-driven layout for memberships, trainers, programs, and high-energy conversion points.",
            "url_name": "demo_website_gym_1",
            "icon": "fa-dumbbell",
            "accent": "linear-gradient(135deg, rgba(24,112,82,0.96), rgba(62,186,125,0.8))",
            "highlights": ["Programs", "Pricing", "Trainers"],
        },
    ]
    template_gallery = [
        {
            "title": "Restaurant Template",
            "category": "Dining and hospitality",
            "image": "images/template-previews/restaurant-template.png",
            "alt": "Restaurant website template preview image",
        },
        {
            "title": "Real Estate Template",
            "category": "Property and listings",
            "image": "images/template-previews/real-estate-template.png",
            "alt": "Real estate website template preview image",
        },
        {
            "title": "Gym Template",
            "category": "Fitness and memberships",
            "image": "images/template-previews/gym-template.png",
            "alt": "Gym website template preview image",
        },
        {
            "title": "Ecommerce Template",
            "category": "Online store and catalog",
            "image": "images/template-previews/ecommerce-template.png",
            "alt": "Ecommerce website template preview image",
        },
    ]
    return render(
        request,
        "homepage.html",
        {
            "demo_sites": demo_sites,
            "template_gallery": template_gallery,
        },
    )


def chat_redirect(request):
    return redirect(settings.CHATDORA_CHAT_URL)


def privacy_policy(request):
    return render(
        request,
        "simple_page.html",
        {
            "title": "Privacy Policy",
            "body": "This brochure site only serves the ChatDORA homepage content and static assets. Update this page later with your final privacy policy before production launch.",
        },
    )


def terms_of_use(request):
    return render(
        request,
        "simple_page.html",
        {
            "title": "Terms of Service",
            "body": "This brochure site is a lightweight public-facing landing page. Update this page later with your final terms of service before production launch.",
        },
    )


def demo_placeholder(request, demo_name):
    return render(
        request,
        "simple_page.html",
        {
            "title": f"{demo_name} Demo",
            "body": "This brochure project only includes the homepage. The demo page itself was intentionally not copied from the main project.",
        },
    )
