from django.shortcuts import render, redirect
from .mlapp import data_preprocessor, visualize_confidence_level, model
from .templatetags.templatetags import plot_to_base64
import pandas as pd

def wine_input_form(request):
    if request.method == 'POST':
        # Process the form data
        wine_type = request.POST.get('wine_type')
        fixed_acidity = float(request.POST.get('fixed_acidity'))
        volatile_acidity = float(request.POST.get('volatile_acidity'))
        citric_acid = float(request.POST.get('citric_acid'))
        residual_sugar = float(request.POST.get('residual_sugar'))
        chlorides = float(request.POST.get('chlorides'))
        free_sulfur_dioxide = float(request.POST.get('free_sulfur_dioxide'))
        total_sulfur_dioxide = float(request.POST.get('total_sulfur_dioxide'))
        density = float(request.POST.get('density'))
        pH = float(request.POST.get('pH'))
        sulphates = float(request.POST.get('sulphates'))
        alcohol = float(request.POST.get('alcohol'))

        # Create a dictionary with the form data
        form_data = {
            'wine_type': wine_type,
            'fixed_acidity': fixed_acidity,
            'volatile_acidity': volatile_acidity,
            'citric_acid': citric_acid,
            'residual_sugar': residual_sugar,
            'chlorides': chlorides,
            'free_sulfur_dioxide': free_sulfur_dioxide,
            'total_sulfur_dioxide': total_sulfur_dioxide,
            'density': density,
            'pH': pH,
            'sulphates': sulphates,
            'alcohol': alcohol
        }

        # Create a DataFrame from the form data
        user_input_df = pd.DataFrame(form_data, index=[0])

        # Preprocess the user input
        processed_user_input = data_preprocessor(user_input_df)

        # Predict using the model
        prediction_proba = model.predict_proba(processed_user_input)

        # Visualize the confidence level
        fig = visualize_confidence_level(prediction_proba)

        # Convert the plot to base64 for rendering in HTML
        plot_data = plot_to_base64(fig)

        # Pass the plot data to the template for rendering
        return render(request, 'wine_prediction.html', {'plot_data': plot_data})
    else:
        # Render the input form template for GET requests
        return render(request, 'input_form.html')
