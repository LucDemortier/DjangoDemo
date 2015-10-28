from django.shortcuts import render, get_object_or_404, redirect
from .models import ChronicConditionRegression
from .forms import ChronicConditionAnalysisQueryForm
from .regression import CSVRegression, DEFAULT_TARGET


def home(request):
    return render(request, 'index.html')


def results_list(request):
    results = ChronicConditionRegression.objects.all()
    return render(request, 'chronic_medicare/results_list.html', {'results': results})


def results_detail(request, pk):
    result = get_object_or_404(ChronicConditionRegression, pk=pk)
    return render(request, 'chronic_medicare/results_detail.html', {'result': result})


def query_view(request):
    if request.method == 'POST':
        form = ChronicConditionAnalysisQueryForm(request.POST)
        if form.is_valid():
            regression = CSVRegression(form.cleaned_data['input_file'])
            features_list = []
            for feature in form.cleaned_data['features']:
                unique_values = len(regression.df[feature].unique())
                # Dangerous (but maybe reasonable) assumption:
                # features with less than 10 unique values are ordinal
                if unique_values < 10:
                    data_type = "ordinal"
                else:
                    data_type = "ratio"
                # TODO: Allow dynamic labels
                features_list.append({
                    'csv_column': feature,
                    'label': feature,
                    'data_type': data_type,
                    })
            regression.generate_model_data(features_list, form.cleaned_data['target'])
            regression.run_ols_regression()
            regression.generate_summary_dict()
            analysis_file = AnalysisFile.objects.get(csv_file=regression.source_file)
            regression.summary_dict['source_file'] = analysis_file
            saved_regression, created = ChronicConditionRegression.objects.get_or_create(
                **regression.summary_dict)
            return redirect('chronic:results_detail', pk=saved_regression.pk)
    else:
        form = ChronicConditionAnalysisQueryForm(initial={'target': DEFAULT_TARGET})
    return render(request, 'chronic_medicare/query.html', {'form': form})