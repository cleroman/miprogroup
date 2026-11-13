from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SiteSettings, Service, Partner, ProjectRequest, TeamMember, News


def index(request):
    # Gestion du formulaire de contact
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        profile = request.POST.get('profile')
        domain = request.POST.get('domain')
        message_text = request.POST.get('message')
        
        if name and email and domain and message_text:
            ProjectRequest.objects.create(
                name=name,
                email=email,
                company=profile,
                domain=domain,
                description=message_text
            )
            messages.success(request, "Votre demande a bien été enregistrée. Nous vous contacterons sous 24h.")
            return redirect('website:index')

    # Recuperation des donnees
    settings_obj = SiteSettings.objects.first()
    services = Service.objects.all()
    partners = Partner.objects.all()
    
    # Logique de l'equipe
    ceo = TeamMember.objects.filter(role_type='CEO').first()
    if not ceo:
        ceo = TeamMember.objects.filter(is_ceo=True).first()
        
    directors = TeamMember.objects.filter(role_type__in=['DG', 'PRESIDENT', 'DIRECTEUR']).exclude(role_type='CEO').order_by('order')
    team_members = TeamMember.objects.exclude(role_type__in=['CEO', 'DG', 'PRESIDENT', 'DIRECTEUR']).order_by('order')
    
    context = {
        'settings': settings_obj,
        'services': services,
        'partners': partners,
        'ceo': ceo,
        'directors': directors,
        'team_members': team_members,
    }
    return render(request, 'website/index.html', context)


def demande_projet(request):
    # Cette vue redirige simplement vers l'accueil (qui contient le formulaire)
    return redirect('website:index')