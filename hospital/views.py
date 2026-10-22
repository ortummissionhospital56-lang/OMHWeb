from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm, FeedbackForm
from .models import (DownloadItem, GalleryImage, JobPosting, NewsPost,
                     Service, StaffMember)


def home(request):
    return render(request, "home.html", {
        "services": Service.objects.filter(is_active=True),
        "gallery": GalleryImage.objects.all()[:12],
        "staff": StaffMember.objects.all(),
        "latest_news": NewsPost.objects.filter(is_published=True)[:3],
    })


def about(request):
    return render(request, "about.html")


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Thank you. Your message has been sent.")
        return redirect("contact")
    return render(request, "contact.html", {"form": form})


def careers(request):
    jobs = JobPosting.objects.filter(is_active=True)
    return render(request, "careers.html", {"jobs": jobs})


def news_list(request):
    posts = NewsPost.objects.filter(is_published=True)
    page = Paginator(posts, 6).get_page(request.GET.get("page"))
    return render(request, "news_list.html", {"page": page})


def news_detail(request, slug):
    post = get_object_or_404(NewsPost, slug=slug, is_published=True)
    return render(request, "news_detail.html", {"post": post})


def downloads(request):
    return render(request, "downloads.html", {"items": DownloadItem.objects.all()})


def feedback(request):
    form = FeedbackForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Thank you for your feedback. It helps us improve our care.")
        return redirect("feedback")
    return render(request, "feedback.html", {"form": form})
