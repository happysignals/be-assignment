from django.urls import path, include

from .views import form, form_done, form_default

urlpatterns = [
  path("form/thankyou/<int:id>", form_done, name="thank_you"),
  path("form/<slug>", form, name="form"),
  path("form", form_default)
]