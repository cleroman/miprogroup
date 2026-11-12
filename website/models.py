from django.db import models

class SiteSettings(models.Model):
    hero_title = models.CharField(max_length=200, default="Bâtir l'avenir énergétique et infrastructurel de la RDC")
    hero_subtitle = models.TextField(default="De l'ingénierie conseil à la réalisation de projets BTP et Énergies Renouvelables...")
    hero_video_url = models.URLField(default="https://cdn.pixabay.com/video/2022/07/12/124204-729684643_large.mp4")
    logo = models.ImageField(upload_to='site/', blank=True, null=True)
    
    address = models.TextField(default="16 eme Etage, Local C, Nouvelles Gal. Presidentielles, Q/Revolution, C/Gombe, Kinshasa, RDC")
    email1 = models.EmailField(default="mipro.ngoie@gmail.com")
    email2 = models.EmailField(default="direction@miprogroup.cd", blank=True)
    phone1 = models.CharField(max_length=50, default="+243 813 949 891")
    phone2 = models.CharField(max_length=50, default="+243 997 278 348", blank=True)
    hours = models.CharField(max_length=100, default="Lundi - Vendredi : 8h00 - 17h00")
    
    youtube_url = models.URLField(blank=True, null=True, verbose_name="Lien YouTube")
    tiktok_url = models.URLField(blank=True, null=True, verbose_name="Lien TikTok")
    instagram_url = models.URLField(blank=True, null=True, verbose_name="Lien Instagram")
    facebook_url = models.URLField(blank=True, null=True, verbose_name="Lien Facebook")
    whatsapp_url = models.URLField(blank=True, null=True, verbose_name="Lien WhatsApp")
    linkedin_url = models.URLField(blank=True, null=True, verbose_name="Lien LinkedIn")
    
    rccm = models.CharField(max_length=100, default="CD/KNG/RCCM/21-B-01330")
    impots = models.CharField(max_length=100, default="A2164852Q")
    id_nat = models.CharField(max_length=100, default="01-F4300-N80931E")
    arsp = models.CharField(max_length=100, default="5885434406")
    cnss = models.CharField(max_length=100, default="1015341800")

    class Meta:
        verbose_name = "Parametre du site"
        verbose_name_plural = "Parametres du site"

    def __str__(self):
        return "Configuration Globale du Site"

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    order = models.IntegerField(default=0, help_text="Ordre d affichage (0, 1, 2...)")

    class Meta:
        ordering = ['order']
        verbose_name = "Service (Expertise)"
        verbose_name_plural = "Services (Expertises)"

    def __str__(self):
        return self.title

class ProcessStep(models.Model):
    step_number = models.CharField(max_length=2, help_text="Ex: 01, 02...")
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='process/', blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Etape de Processus"
        verbose_name_plural = "Processus d Ingenierie"

    def __str__(self):
        return f"{self.step_number} - {self.title}"

class Partner(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='partners/', blank=True, null=True, help_text="Uploadez le logo officiel du partenaire")
    order = models.IntegerField(default=0, help_text="Ordre d affichage")
    
    class Meta:
        ordering = ['order']
        verbose_name = "Partenaire"
        verbose_name_plural = "Partenaires"

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Actualite"
        verbose_name_plural = "Actualites"

    def __str__(self):
        return self.title

class ProjectRequest(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    domain = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    budget = models.CharField(max_length=50, blank=True)
    timeline = models.CharField(max_length=50, blank=True)
    document = models.FileField(upload_to='requests/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Demande de Projet"
        verbose_name_plural = "Demandes de Projet"

    def __str__(self):
        return f"{self.name} - {self.domain}"

class TeamMember(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom complet")
    role = models.CharField(max_length=100, verbose_name="Fonction / Role")
    image = models.ImageField(upload_to='team/', blank=True, null=True, verbose_name="Photo de profil")
    cv = models.FileField(upload_to='team/cv/', blank=True, null=True, verbose_name="CV (PDF)")
    
    details = models.TextField(verbose_name="Biographie / Details")
    comments = models.TextField(blank=True, null=True, verbose_name="Commentaires / Citations")
    
    email1 = models.EmailField(blank=True, null=True, verbose_name="Email 1")
    email2 = models.EmailField(blank=True, null=True, verbose_name="Email 2")
    email3 = models.EmailField(blank=True, null=True, verbose_name="Email 3")
    
    phone1 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Telephone 1")
    phone2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Telephone 2")
    phone3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Telephone 3")
    
    address1 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Adresse 1")
    address2 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Adresse 2")
    address3 = models.CharField(max_length=255, blank=True, null=True, verbose_name="Adresse 3")

    linkedin = models.URLField(blank=True, null=True, verbose_name="Lien LinkedIn")
    is_ceo = models.BooleanField(default=False, verbose_name="Est-ce le CEO ?")
    order = models.IntegerField(default=0, verbose_name="Ordre d'affichage")

    class Meta:
        ordering = ['-is_ceo', 'order']
        verbose_name = "Membre de l'equipe"
        verbose_name_plural = "Membres de l'equipe"

    def __str__(self):
        return f"{self.name} - {self.role}"