import pandas as pd

def load_and_clean_data(): 
    df = pd.read_csv("survey_results_public.csv")
    df = df[['Country', 'EdLevel', 'YearsCodePro', 'Employment', 'ConvertedCompYearly']]
    df = df.rename(columns={'ConvertedCompYearly': 'Salary'})
    df = df.dropna()
    df = df[df['Employment'] == "Employed, full-time"]
    df = df.drop(columns=['Employment'])

    # Filter countries by the number of data points
    threshold = 400
    country_counts = df['Country'].value_counts()
    countries_to_other = country_counts[country_counts < threshold].index
    df['Country'] = df['Country'].apply(lambda x: 'Other' if x in countries_to_other else x)

    # Salary and Country filtering (although we could include Other)
    df = df[(df['Salary'] >= 10000) & (df['Salary'] <= 250000)]
    df = df[df['Country'] != 'Other']

    # Clean experience and education level fields
    df['YearsCodePro'] = df['YearsCodePro'].apply(clean_experience)
    df['EdLevel'] = df['EdLevel'].apply(clean_education)
    
    return df

def clean_experience(x):
    if x == 'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)

def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Post grad'
    return 'Less than a Bachelors'
