from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SiteSettings, Service, Partner, ProjectRequest, TeamMember, News

def index(request):
    # Si le formulaire de contact de la page d'accueil est soumis
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
                company=profile, # On stocke le profil ici
                domain=domain,
                description=message_text
            )
            messages.success(request, "Votre demande a bien été enregistrée. Nous vous contacterons sous 24h.")
            return redirect('website:index')

    # Recuperation des donnees
    settings_obj = SiteSettings.objects.first()
    services = Service.objects.all()
    partners = Partner.objects.all()
    ceo = TeamMember.objects.filter(is_ceo=True).first()
    team_members = TeamMember.objects.filter(is_ceo=False)
    
    context = {
        'settings': settings_obj,
        'services': services,
        'partners': partners,
        'ceo': ceo,
        'team_members': team_members,
    }
    return render(request, 'website/index.html', context)


# LA FONCTION MANQUANTE :
def demande_projet(request):
    # Cette vue redirige simplement vers l'accueil (qui contient le formulaire)
    return redirect('website:index')