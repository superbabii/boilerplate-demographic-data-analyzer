import pandas as pd

def calculate_demographic_data(print_data=False):
    # Load the data
    df = pd.read_csv('adult.data.csv')

    # Number of each race represented in the dataset
    race_count = df['race'].value_counts()

    # Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Percentage of people with a Bachelor's degree
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # Advanced education (Bachelors, Masters, or Doctorate) making >50K
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round((df[higher_education]['salary'] == '>50K').mean() * 100, 1)

    # People without advanced education making >50K
    # People without advanced education making >50K
    lower_education = df[~higher_education]
    lower_education_rich = round((lower_education['salary'] == '>50K').mean() * 100, 1)

    # Minimum number of hours worked per week
    min_work_hours = df['hours-per-week'].min()

    # Percentage of people who work minimum hours and have salary >50K
    min_hours_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((min_hours_workers['salary'] == '>50K').mean() * 100, 1)

    # Country with the highest percentage of people earning >50K
    countries_earning_above_50k = df[df['salary'] == '>50K']['native-country'].value_counts()
    countries_total = df['native-country'].value_counts()
    highest_earning_country = (countries_earning_above_50k / countries_total * 100).idxmax()
    highest_earning_country_percentage = round((countries_earning_above_50k / countries_total * 100).max(), 1)

    # Most popular occupation for those who earn >50K in India
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    # Compile the results
    result = {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

    # Optionally print the data
    if print_data:
        for key, value in result.items():
            print(f"{key}: {value}")

    return result
