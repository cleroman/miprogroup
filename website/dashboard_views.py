from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .models import SiteSettings, Service, Partner, ProjectRequest, News, TeamMember
from .dashboard_forms import SiteSettingsForm, ServiceForm, PartnerForm, NewsForm, TeamMemberForm

# Mixin pour s'assurer que seul le personnel (admin) peut acceder
class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class DashboardIndexView(StaffRequiredMixin, TemplateView):
    template_name = 'website/dashboard/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services_count'] = Service.objects.count()
        context['partners_count'] = Partner.objects.count()
        context['requests_count'] = ProjectRequest.objects.count()
        context['recent_requests'] = ProjectRequest.objects.order_by('-created_at')[:5]
        return context

# --- PARAMETRES DU SITE ---
class SettingsUpdateView(StaffRequiredMixin, UpdateView):
    model = SiteSettings
    form_class = SiteSettingsForm
    template_name = 'website/dashboard/form.html'
    success_url = reverse_lazy('dashboard_settings')
    
    def get_object(self, queryset=None):
        return SiteSettings.objects.first() or SiteSettings.objects.create()
        
    def form_valid(self, form):
        messages.success(self.request, "Les paramètres du site ont été mis à jour avec succès.")
        return super().form_valid(form)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Paramètres du Site"
        return context

# --- SERVICES ---
class ServiceListView(StaffRequiredMixin, ListView):
    model = Service
    template_name = 'website/dashboard/service_list.html'
    context_object_name = 'services'

class ServiceCreateView(StaffRequiredMixin, CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'website/dashboard/form.html'
    success_url = reverse_lazy('dashboard_services')
    
    def form_valid(self, form):
        messages.success(self.request, "Le service a été ajouté.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Ajouter un Service"
        return context

class ServiceUpdateView(StaffRequiredMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'website/dashboard/form.html'
    success_url = reverse_lazy('dashboard_services')
    
    def form_valid(self, form):
        messages.success(self.request, "Le service a été modifié.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Modifier le Service"
        return context

class ServiceDeleteView(StaffRequiredMixin, DeleteView):
    model = Service
    success_url = reverse_lazy('dashboard_services')
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            if self.object.image:
                self.object.image.delete(save=False)
        except Exception:
            pass
        self.object.delete()
        messages.success(self.request, "Le service a ete supprime.")
        return HttpResponseRedirect(success_url)

class PartnerListView(StaffRequiredMixin, ListView):
    model = Partner
    template_name = 'website/dashboard/partner_list.html'
    context_object_name = 'partners'

class PartnerCreateView(StaffRequiredMixin, CreateView):
    model = Partner
    form_class = PartnerForm
    template_name = 'website/dashboard/form.html'
    success_url = reverse_lazy('dashboard_partners')
    
    def form_valid(self, form):
        messages.success(self.request, "Le partenaire a été ajouté.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Ajouter un Partenaire"
        return context

class PartnerUpdateView(StaffRequiredMixin, UpdateView):
    model = Partner
    form_class = PartnerForm
    template_name = 'website/dashboard/form.html'
    success_url = reverse_lazy('dashboard_partners')
    
    def form_valid(self, form):
        messages.success(self.request, "Le partenaire a été modifié.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Modifier le Partenaire"
        return context

class PartnerDeleteView(StaffRequiredMixin, DeleteView):
    model = Partner
    success_url = reverse_lazy('dashboard_partners')
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            if self.object.logo:
                self.object.logo.delete(save=False)
        except Exception:
            pass
        self.object.delete()
        messages.success(self.request, "Le partenaire a ete supprime.")
        return HttpResponseRedirect(success_url)

class RequestListView(StaffRequiredMixin, ListView):
    model = ProjectRequest
    template_name = 'website/dashboard/request_list.html'
    context_object_name = 'requests'

# --- EQUIPE ---
class TeamListView(StaffRequiredMixin, ListView):
    model = TeamMember
    template_name = 'website/dashboard/team_list.html'
    context_object_name = 'team_members'

class TeamCreateView(StaffRequiredMixin, CreateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'website/dashboard/form.html'
    success_url = reverse_lazy('dashboard_team')
    
    def form_valid(self, form):
        messages.success(self.request, "Le membre de l'equipe a ete ajoute.")
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Ajouter un membre"
        return context

class TeamUpdateView(StaffRequiredMixin, UpdateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'website/dashboard/form.html'
    success_url = reverse_lazy('dashboard_team')
    
    def form_valid(self, form):
        messages.success(self.request, "Le membre a ete modifie.")
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Modifier le membre"
        return context

class TeamDeleteView(StaffRequiredMixin, DeleteView):
    model = TeamMember
    success_url = reverse_lazy('dashboard_team')
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            if self.object.image:
                self.object.image.delete(save=False)
            if self.object.cv:
                self.object.cv.delete(save=False)
        except Exception:
            pass
        self.object.delete()
        messages.success(self.request, "Le membre a ete supprime.")
        return HttpResponseRedirect(success_url)

