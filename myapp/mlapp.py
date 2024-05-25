import pandas as pd
import joblib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

# Load the machine learning model
model = joblib.load(open("myapp/model-v1.joblib", "rb"))

def data_preprocessor(df):
    """
    Preprocesses the user input data.
    
    Parameters:
    - df: pandas DataFrame containing user input
    
    Returns:
    - df: preprocessed pandas DataFrame
    """
    df.wine_type = df.wine_type.map({'white': 0, 'red': 1})
    return df

def visualize_confidence_level(prediction_proba):
    """
    Creates a Matplotlib figure to visualize the prediction confidence level.

    Parameters:
    - prediction_proba: array-like, prediction probabilities

    Returns:
    - fig: matplotlib figure object
    """
    data = (prediction_proba[0] * 100).round(2)
    grad_percentage = pd.DataFrame(data=data, columns=['Percentage'], index=['Low', 'Ave', 'High'])

    fig = Figure(figsize=(7, 4))
    ax = fig.subplots()
    grad_percentage.plot(kind='barh', ax=ax, color='#722f37', zorder=10, width=0.5)
    ax.legend().set_visible(False)
    ax.set_xlim(xmin=0, xmax=100)

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(True)
    ax.spines['bottom'].set_visible(True)

    ax.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")

    vals = ax.get_xticks()
    for tick in vals:
        ax.axvline(x=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)

    ax.set_xlabel(" Percentage(%) Confidence Level", labelpad=2, weight='bold', size=12)
    ax.set_ylabel("Wine Quality", labelpad=10, weight='bold', size=12)
    ax.set_title('Prediction Confidence Level', fontdict=None, loc='center', pad=None, weight='bold')

    return fig
