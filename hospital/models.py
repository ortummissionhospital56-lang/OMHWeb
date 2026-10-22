from django.db import models
from django.utils import timezone


class SiteSettings(models.Model):
    """One record that controls the logo, name, texts and contact details."""
    hospital_name = models.CharField(max_length=150, default="Your Hospital Name")
    tagline = models.CharField(max_length=200, blank=True, default="Caring for you and your family")
    logo = models.ImageField(upload_to="logo/", blank=True)
    hero_image = models.ImageField(upload_to="hero/", blank=True,
                                   help_text="Large banner image on the home page (optional).")
    intro_title = models.CharField(max_length=150, default="Welcome to our hospital")
    intro_text = models.TextField(default="Write a short introduction to your facility here.")
    about_text = models.TextField(blank=True, help_text="Main text of the About us page.")
    mission = models.TextField(blank=True)
    vision = models.TextField(blank=True)
    address = models.CharField(max_length=250, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    emergency_phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    working_hours = models.CharField(max_length=200, blank=True, default="Open 24 hours")

    class Meta:
        verbose_name = "Site settings"
        verbose_name_plural = "Site settings"

    def __str__(self):
        return self.hospital_name


class Service(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=8, blank=True, default="✚",
                            help_text="A single emoji or symbol, e.g. 🩺 or 🚑")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    image = models.ImageField(upload_to="gallery/")
    caption = models.CharField(max_length=150, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-id"]

    def __str__(self):
        return self.caption or f"Image {self.pk}"


class StaffMember(models.Model):
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=150)
    photo = models.ImageField(upload_to="staff/", blank=True)
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first.")

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "management staff member"

    def __str__(self):
        return f"{self.name} - {self.role}"


class NewsPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.CharField(max_length=300, blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to="news/", blank=True)
    published_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title


class JobPosting(models.Model):
    title = models.CharField(max_length=150)
    department = models.CharField(max_length=120, blank=True)
    description = models.TextField()
    requirements = models.TextField(blank=True)
    deadline = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class DownloadItem(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300, blank=True)
    file = models.FileField(upload_to="downloads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self):
        return self.title


class Feedback(models.Model):
    RATINGS = [(5, "Excellent"), (4, "Good"), (3, "Average"), (2, "Poor"), (1, "Very poor")]
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    rating = models.PositiveSmallIntegerField(choices=RATINGS, default=5)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "feedback"

    def __str__(self):
        return f"{self.name or 'Anonymous'} ({self.created_at:%Y-%m-%d})"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name}: {self.subject or 'No subject'}"
