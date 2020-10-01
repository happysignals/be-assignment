from django import forms

from .models import Survey, Factor, Response

class UnvalidatedMultipleChoiceField(forms.MultipleChoiceField):
  def validate(self, value):
    pass # Don't require the value to be one of the listed choices like the default MultipleChoiceField requires

class ResponseForm(forms.ModelForm):
  factors = UnvalidatedMultipleChoiceField()
  comment = forms.CharField(widget=forms.Textarea)

  # TODO: (2) Validate the value parameter is between 0 and 10 (inclusive)
  # TODO: (3) Ensure comment doesn't mention "banana", "pear", "lemon"

  class Meta:
    model = Response
    fields = ["value", "comment", "factors"]
