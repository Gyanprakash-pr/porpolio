from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .forms import ProfileForm, ProjectForm
from .models import Project, Resume
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def project_list(request):
    projects = Project.objects.all()
    return render(request, "projects.html", {"projects": projects})


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        
        try:
            send_mail(
                subject=f"New Contact Query from {name}",
                message=full_message,
                from_email=email,  # The sender's email
                recipient_list=["gyanbabu193@gmail.com"],  # Replace with your email
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, "Failed to send your message. Please try again later.")

        return redirect("contact")  # Redirect to the contact page after submission

    return render(request, "contact.html")

def resume(request):
    resume_entry = Resume.objects.last()  # Latest uploaded resume fetch karega
    return render(request, 'resume.html', {'resume_entry': resume_entry})



def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your resume has been uploaded successfully!')
            return redirect('resume')
        else:
            messages.error(request, 'Error uploading resume. Please check the details.')
    else:
        form = ProfileForm()

    return render(request, 'profile.html', {'form': form})

@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')  # Redirect to project list
    else:
        form = ProjectForm()

    return render(request, 'create_project.html', {'form': form})


@login_required(login_url='/login/')  # Force login before accessing edit page
def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    # Check if the user is the owner of the project
    if request.user != project.owner:
        messages.warning(request, "🚫 You are not authorized to edit this project!")
        return redirect('/admin/')  # Redirect unauthorized users to admin

    if request.method == "POST":
        project.title = request.POST.get("title")
        project.description = request.POST.get("description")
        project.github_link = request.POST.get("github_link")
        project.save()
        messages.success(request, "✅ Project updated successfully!")
        return redirect("projects")  # ✅ Corrected redirection


    return render(request, "edit_project.html", {"project": project})