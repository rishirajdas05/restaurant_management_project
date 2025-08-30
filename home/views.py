from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FeedbackForm

def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Thank you! Your feedback has been submitted.")
                return redirect("feedback")
            except Exception as e:
                messages.error(request, "Sorry, we couldn't save your feedback. Please try again.")
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = FeedbackForm()

    return render(request, "feedback.html", {"form": form})