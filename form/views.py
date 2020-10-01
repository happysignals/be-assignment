from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

from .models import Survey, Factor, Response
from .forms import ResponseForm

def form_default(request):
  survey = Survey.objects.first()
  return Http404 if not survey else HttpResponseRedirect(reverse("form", args=(survey.slug,)))

def form_done(request, id):
  response = Response.objects.get(pk=id)
  return render(request, "thankyou.html", {
    "value": response.value,
    # TODO: (5) Pass comment and selected factors to the template
  })

def form(request, slug):
  """ Render a form that allows the user to submit a response, and save the response once submitted """
  survey = Survey.objects.get(slug=slug)

  if request.method!="POST":
    response_form = ResponseForm()
  else:
    response_form = ResponseForm(request.POST)
    if response_form.is_valid():
      response = response_form.save(commit=False) # Don't commit since factors are not properly mapped
      response.save()

      # TODO: (4) Save the factors to the response, their slugs are listed in `response_form.cleaned_data["factors"]`

    return HttpResponseRedirect(reverse("thank_you", args=[response.pk]))

  return render(request, "form.html", {
    "question": survey.question,
    "value_range": [str(i) for i in range(0,11)],
    "factors": list(survey.factors.all()),
    "form": response_form
  })