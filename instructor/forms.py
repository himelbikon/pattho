from django import forms
from . import models as instructor_models


class InstructorForm(forms.ModelForm):
    class Meta:
        model = instructor_models.Instructor
        fields = ['categories']