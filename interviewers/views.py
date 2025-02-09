from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from candidates.models import CandidateProfile
from django.contrib.auth.views import LoginView
from .forms import InterviewerSignUpForm
from django.urls import reverse_lazy

@login_required
def interviewer_dashboard(request):
    resumes = CandidateProfile.objects.exclude(
        resume__isnull=True).exclude(resume__exact='')
    return render(request, 'interviewers/dashboard.html', {'resumes': resumes})


class InterviewerLoginView(LoginView):
    template_name = 'interviewers/login.html'

    def get_success_url(self):
        # Ensures redirection to dashboard
        return reverse_lazy('interviewer_dashboard')


def interviewer_signup(request):
    if request.method == 'POST':
        form = InterviewerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after sign-up (optional)
            from django.contrib.auth import login
            login(request, user)
            # Redirect to interviewer dashboard
            return redirect('interviewer_dashboard')
    else:
        form = InterviewerSignUpForm()
    return render(request, 'interviewers/signup.html', {'form': form})
