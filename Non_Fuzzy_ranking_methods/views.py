from django.shortcuts import render
from models import Request, Indicator, Choice, MatrixData
from django.shortcuts import render, redirect, get_object_or_404
from forms import MethodForm, IndicatorForm, ChoiceForm
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
import json
from django.http import JsonResponse
import numpy as np
from pyDecision.algorithm import topsis_method, codas_method, aras_method, waspas_method


def create_request(request):
    if request.method == 'POST':
        method_form = MethodForm(request.POST, prefix='method')
        if method_form.is_valid():
            method = method_form.save(commit=False)
            method.save()

            indicator_names = request.POST.getlist('indicators-name')
            indicator_types = request.POST.getlist('indicators-type')
            indicator_weights = request.POST.getlist('indicators-weight')
            choice_names = request.POST.getlist('choices-name')

            indicators = []
            for name, type, weight in zip(indicator_names, indicator_types, indicator_weights):
                indicator = Indicator.objects.create(name=name, type=type, weight=weight, method=method)
                indicators.append(indicator)

            choices = []
            for name in choice_names:
                choice = Choice.objects.create(name=name, method=method)
                choices.append(choice)

            request_instance = Request.objects.create(method=method)
            request_instance.indicators.add(*indicators)
            request_instance.choices.add(*choices)

            return redirect('success3', request_id=request_instance.id)  # Redirect to a success page or any other page
    else:
        method_form = MethodForm(prefix='method')
    return render(request, './Non_Fuzzy_ranking_methods/Non_Fuzzy_inputs.html', {'method_form': method_form})

def success(request, request_id):
    request_instance = get_object_or_404(Request, pk=request_id)
    method = request_instance.method
    indicators = request_instance.indicators.all()
    choices = request_instance.choices.all()

    # Serialize indicators and choices to JSON
    indicators_json = json.dumps([{'name': indicator.name, 'type': indicator.type, 'weight': indicator.weight} for indicator in indicators])
    choices_json = json.dumps([{'name': choice.name} for choice in choices])

    # Render the HTML template with the data
    html_content = render_to_string('./Non_Fuzzy_ranking_methods/Non_Fuzzy_success.html', {
        'method': method,
        'indicators_json': mark_safe(indicators_json),
        'choices_json': mark_safe(choices_json),
    })

    # Return the HTML content as an HTTP response
    return HttpResponse(html_content)

def save_matrix_data(request):
    if request.method == 'POST':
        try:
            # Retrieve matrix data from POST request
            data = json.loads(request.body)
            matrix_data = data.get('matrix_data')
            request_id = data.get('request_id')

            # Validate that both matrix data and request ID are present
            if not matrix_data or not request_id:
                return JsonResponse({'success': False, 'error': 'Missing matrix data or request ID'})

            # Convert matrix data from strings to integers
            matrix_data = [[int(val) if val.isdigit() else float(val) for val in row] for row in matrix_data]

            # Create or update MatrixData object
            matrix_data_obj, created = MatrixData.objects.update_or_create(
                request_id=request_id,
                defaults={'data': matrix_data}
            )

            # Return response based on whether matrix data was successfully saved or updated
            if created:
                return JsonResponse({'success': True, 'message': 'Matrix data saved successfully'})
            else:
                return JsonResponse({'success': True, 'message': 'Matrix data updated successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON format in request body'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})


def calculate_method(matrix_data, indicator_weights, indicator_types, method_name):
    # Convert matrix data to numpy array
    dataset = np.array(matrix_data)

    # Initialize lists to store weights and criterion types
    weights = []
    criterion_type = []

    # Iterate through indicator weights and types
    for weight, indicator_type in zip(indicator_weights, indicator_types):
        weights.append(weight)
        if indicator_type == 'Positive':
            criterion_type.append('max')
        elif indicator_type == 'Negative':
            criterion_type.append('min')

    # Call the corresponding method based on the method_name argument
    if method_name == 'method-ARAS':
        from pyDecision.algorithm import aras_method
        rank = aras_method(dataset, weights, criterion_type, graph=True, verbose=True)
    elif method_name == 'method-Borda':
        from pyDecision.algorithm import borda_method
        rank = borda_method(dataset, weights, criterion_type, graph=True, verbose=True)
    elif method_name == 'method-CoCoSo':
        from pyDecision.algorithm import cocoso_method
        rank = cocoso_method(dataset, weights, criterion_type, L=0.5, graph=True, verbose=True)
    elif method_name == 'method-CODAS':
        from pyDecision.algorithm import codas_method
        rank = codas_method(dataset, weights, criterion_type, lmbd=0.02, graph=True, verbose=True)
    elif method_name == 'method-Copeland':
        from pyDecision.algorithm import copeland_method
        rank = copeland_method(dataset, criterion_type, graph=True, verbose=True)
    elif method_name == 'method-COPRAS':
        from pyDecision.algorithm import copras_method
        rank = copras_method(dataset, weights, criterion_type, graph=True, verbose=True)
    elif method_name == 'method-CRADIS':
        from pyDecision.algorithm import cradis_method
        rank = cradis_method(dataset, weights, criterion_type, graph=True, verbose=True)
    elif method_name == 'method-EDAS':
        from pyDecision.algorithm import edas_method
        rank = edas_method(dataset, weights, criterion_type, graph=True, verbose=True)
    elif method_name == 'method-GRA':
        from pyDecision.algorithm import gra_method
        rank = gra_method(dataset, weights, criterion_type, epsilon=0.5, graph=True, verbose=True)
    elif method_name == 'method-MABAC':
        from pyDecision.algorithm import mabac_method
        rank = mabac_method(dataset, criterion_type, graph=True, verbose=True)
    elif method_name == 'method-MACBETH':
        from pyDecision.algorithm import macbeth_method
        rank = macbeth_method(dataset, weights, criterion_type, graph=True, verbose=True)
    elif method_name == 'method-MAIRCA':
        from pyDecision.algorithm import mairca_method
        rank = mairca_method(dataset, weights, criterion_type, graph=True, verbose=True)
    elif method_name == 'method-MARA':
        from pyDecision.algorithm import mara_method
        rank = mara_method(dataset, weights, criterion_type, graph=True, verbose=True)
    elif method_name == 'method-MARCOS':
        from pyDecision.algorithm import marcos_method
        rank = marcos_method(dataset, weights, criterion_type, graph=True, verbose=True)
    elif method_name == 'method-MOORA':
        from pyDecision.algorithm import moora_method
        rank = moora_method(dataset, weights, criterion_type, graph=True, verbose=True)
    elif method_name == 'method-MOOSRA':
        from pyDecision.algorithm import moosra_method
        rank = moosra_method(dataset, weights, criterion_type, graph=True, verbose=True)
    elif method_name == 'method-OCRA':
        from pyDecision.algorithm import ocra_method
        rank = ocra_method(dataset, weights, criterion_type, graph=True, verbose=True)
    elif method_name == 'method-ORESTE':
        from pyDecision.algorithm import oreste_method
        rank = oreste_method(dataset, weights, criterion_type, alpha=0.4, graph=True, verbose=True)
    elif method_name == 'method-PIV':
        from pyDecision.algorithm import piv_method
        rank = piv_method(dataset, weights, criterion_type, graph=True, verbose=True)
    elif method_name == 'method-PSI':
        from pyDecision.algorithm import psi_method
        rank = psi_method(dataset, criterion_type, graph=True, verbose=True)
    elif method_name == 'method-REGIME':
        from pyDecision.algorithm import regime_method
        rank = regime_method(dataset, weights, criterion_type, graph=True, verbose=True)
    elif method_name == 'method-ROV':
        from pyDecision.algorithm import rov_method
        rank = rov_method(dataset, weights, criterion_type, graph=True, verbose=True)
    elif method_name == 'method-SAW':
        from pyDecision.algorithm import saw_method
        rank = saw_method(dataset, criterion_type, weights, graph=True, verbose=True)
    elif method_name == 'method-TODIM':
        from pyDecision.algorithm import todim_method
        rank = todim_method(dataset, criterion_type, weights, teta=1, graph=True, verbose=True)
    elif method_name == 'method-TOPSIS':
        from pyDecision.algorithm import topsis_method
        rank = topsis_method(dataset, weights, criterion_type, graph=True, verbose=True)
    elif method_name == 'method-WSM':
        from pyDecision.algorithm import waspas_method
        wsm, wpm, waspas = waspas_method(dataset, weights, criterion_type, lambda_value=0.5, graph=True)
        rank = wsm
    elif method_name == 'method-WPM':
        from pyDecision.algorithm import waspas_method
        wsm, wpm, waspas = waspas_method(dataset, weights, criterion_type, lambda_value=0.5, graph=True)
        rank = wpm
    elif method_name == 'method-WASPAS':
        from pyDecision.algorithm import waspas_method
        wsm, wpm, waspas = waspas_method(dataset, weights, criterion_type, lambda_value=0.5, graph=True)
        rank = waspas
    elif method_name == 'Simple WISP':
        from pyDecision.algorithm import wisp_method
        rank = wisp_method(dataset, criterion_type, weights, simplified=True, graph=True, verbose=True)
    elif method_name == 'method-WISP':
        from pyDecision.algorithm import wisp_method
        rank = wisp_method(dataset, criterion_type, weights, simplified=False, graph=True, verbose=True)
    else:
        raise ValueError("Invalid method name.")

    # Convert rank array to a dictionary with option names as keys
    option_names = [f'rank{i+1}' for i in range(len(rank))]
    result_dict = {option_name: rank_val for option_name, rank_val in zip(option_names, rank)}

    # Return the ranking output
    return result_dict

method_calculations = {
    'method-ARAS': 'ARAS',
    'method-Borda': 'Borda',
    'method-CoCoSo': 'CoCoSo',
    'method-CODAS': 'CODAS',
    'method-Copeland': 'Copeland',
    'method-COPRAS': 'COPRAS',
    'method-CRADIS': 'CRADIS',
    'method-EDAS': 'EDAS',
    'method-GRA': 'GRA',
    'method-MABAC': 'MABAC',
    'method-MACBETH': 'MACBETH',
    'method-MAIRCA': 'MAIRCA',
    'method-MARA': 'MARA',
    'method-MARCOS': 'MARCOS',
    'method-MOORA': 'MOORA',
    'method-MOOSRA': 'MOOSRA',
    'method-OCRA': 'OCRA',
    'method-ORESTE': 'ORESTE',
    'method-PIV': 'PIV',
    'method-PSI': 'PSI',
    'method-REGIME': 'REGIME',
    'method-ROV': 'ROV',
    'method-SAW': 'SAW',
    'method-TODIM': 'TODIM',
    'method-TOPSIS': 'TOPSIS',
    'method-WSM': 'WSM',
    'method-WPM': 'WPM',
    'method-WASPAS': 'WASPAS',
    'method-Simple WISP': 'Simple WISP',
    'method-WISP': 'WISP',
}

def results(request, request_id):
    # Retrieve the corresponding Request object
    request_instance = get_object_or_404(Request, pk=request_id)

    # Retrieve the associated MatrixData object
    matrix_data_obj = MatrixData.objects.filter(request=request_instance).first()

    # Retrieve indicator weights and types associated with the request
    indicators = request_instance.indicators.all()
    indicator_weights = [indicator.weight for indicator in indicators]
    indicator_types = [indicator.type for indicator in indicators]

    # Debugging expressions
    print("Indicator Weights:", indicator_weights)
    print("Indicator Types:", indicator_types)

    # Get the selected method and method name
    selected_method = request_instance.method.name
    method_name = f'{selected_method}'  # Assuming selected_method is an integer

    # Initialize calculation_result with a default value
    calculation_result = None

    # Check if the selected method exists in the dictionary
    if method_name in method_calculations:
        # Execute the appropriate calculation function based on the selected method
        calculation_function = method_calculations[method_name]
        calculation_result = calculation_function(matrix_data_obj.data, indicator_weights, indicator_types, method_name)
        if calculation_result is None:
            # Handle case where calculation result is None
            calculation_result = "Calculation result is not available"
    else:
        # Handle the case where the selected method is not found
        calculation_result = "Selected method is not supported"

    # Pass the necessary data to the template
    return render(request, './Non_Fuzzy_ranking_methods/Non_Fuzzy_results.html', {
        'matrix_data_obj': matrix_data_obj,
        'request_id': request_id,
        'selected_method': selected_method,
        'indicator_weights': indicator_weights,
        'indicator_types': indicator_types,
        'calculation_result': calculation_result,  # Pass the calculation result to the template if needed
    })