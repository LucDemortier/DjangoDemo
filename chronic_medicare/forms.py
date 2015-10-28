from django import forms
from .models import AnalysisFile
from .constants import CHRONIC_COLUMN_NAMES


class ChronicConditionAnalysisQueryForm(forms.Form):
    '''
    This form validates that valid query choices have been made
    '''
    features = forms.MultipleChoiceField(choices=CHRONIC_COLUMN_NAMES,
        widget=forms.CheckboxSelectMultiple())
    target = forms.ChoiceField(choices=CHRONIC_COLUMN_NAMES)
    input_file = forms.ModelChoiceField(queryset=AnalysisFile.objects.all())

    def clean_input_file(self):
        return self.cleaned_data['input_file'].csv_file