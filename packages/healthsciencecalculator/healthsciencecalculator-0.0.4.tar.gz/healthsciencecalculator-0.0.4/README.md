# Health Science Calculator

[![Documentation Status](https://readthedocs.org/projects/healthsciencecalculator/badge/?version=latest)](https://healthsciencecalculator.readthedocs.io/en/latest/?badge=latest)
[![CI/CD Workflow](https://github.com/UBC-MDS/HealthScienceCalculator/actions/workflows/ci-cd.yml/badge.svg?branch=main)](https://github.com/UBC-MDS/HealthScienceCalculator/actions)
[![codecov](https://codecov.io/gh/UBC-MDS/HealthScienceCalculator/branch/main/graph/badge.svg?token=lnZ6RUI3yh)](https://codecov.io/gh/UBC-MDS/HealthScienceCalculator)
[![PyPI version](https://img.shields.io/pypi/v/healthsciencecalculator.svg)](https://pypi.org/project/healthsciencecalculator/)
[![Python](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/github/license/UBC-MDS/HealthScienceCalculator.svg)](LICENSE)
[![semantic-release](https://img.shields.io/badge/semantic--release-✓-brightgreen.svg)](https://python-semantic-release.readthedocs.io/en/latest/)


## Summary 

This package healthsciencecalculator.py is designed to provide tools for calculating and analyzing important health metrics. It aims to support health professionals, researchers, and fitness enthusiasts by offering reliable functions to convert relevant units, compute Total Daily Energy Expenditure (TDEE), Basal Metabolic Rate (BMR), and Body Mass Index (BMI).


## Python Ecosystem Fit

The healthsciencecalculator.py package fits well within the broader Python ecosystem, complementing existing data science and health analysis libraries. There are several Python packages with similar functionalities, such as: 

[health-indicator](https://pypi.org/project/health-indicator/)
    
This package collects health indices like BMI and health indicators like birth rate

[health-records 0.0.7](https://pypi.org/project/health-records/)

This package maintains personal health records in a text file that can be privately stored in your computer.

The healthsciencecalculator.py package is unique in that it performs health-related calculations with high accuracy and precision, tailored specifically for healthcare professionals and data analysts.

## Functions 

**`get_tdee`**

Description: Calculates Total Daily Energy Expenditure (TDEE) based on BMR and activity level.

Inputs: BMR and activity level.

**`get_bmi`**

Description: Calculates Body Mass Index (BMI) and provides category classification.

Inputs: Weight and height.

**`get_bmr`**

Description: Computes Basal Metabolic Rate (BMR) using the Harris-Benedict equation.

Inputs: Weight, height, age, and sex.

**`unit_convert`**

Description: convert between various health-related units such as weight (kg to lbs), temperature (Celsius to Fahrenheit), and length (cm to inches). This function simplifies converting clinical data for international research or patient records.

Inputs: numeric value to be converted, unit of input value, the desired unit


## Installation

```bash
$ pip install healthsciencecalculator
```

## Usage

After installation, you can start using the various functions provided by the package. 


The **get_bmi** function calculates the Body Mass Index (BMI) and provides detailed classification information, including the BMI category and associated health risk level.

```
from healthsciencecalculator.healthsciencecalculator import get_bmi  

# Example usage
weight = 70.0  # Weight in kilograms
height = 1.75  # Height in meters

# Calculate BMI
bmi_result = get_bmi(weight, height)

# Access BMI details
print(f"BMI: {bmi_result.bmi:.2f}")
print(f"Category: {bmi_result.category}")
print(f"Risk Level: {bmi_result.risk_level}")
```

The **get_tdee** function calculates the Total Daily Energy Expenditure (TDEE) based on the Basal Metabolic Rate (BMR) and an individual's activity level.

```
from healthsciencecalculator.healthsciencecalculator import get_tdee  

# Example usage
bmr = 1500.0  # Basal Metabolic Rate in kilocalories
activity_level = 'moderately active'  # Choose from: 'sedentary', 'lightly active', 'moderately active', 'very active', 'extra active'

# Calculate TDEE
tdee = get_tdee(bmr, activity_level)

# Display TDEE
print(f"TDEE: {tdee:.2f} kcal/day")

```
The **unit_convert** function converts a value from one unit to another. It supports various units for weight, length, temperature, concentration, and volume.

```
from healthsciencecalculator.healthsciencecalculator import unit_convert

# Example usage

# Convert 1 meter to centimeters
value_in_meters = 1.0
converted_value = unit_convert(value_in_meters, "m", "cm")
print(f"1 meter is {converted_value} centimeters.")

# Convert 70 kilograms to pounds
value_in_kg = 70.0
converted_value = unit_convert(value_in_kg, "kg", "lb")
print(f"70 kilograms is {converted_value:.2f} pounds.")

# Convert 100 degrees Celsius to Fahrenheit
value_in_celsius = 100.0
converted_value = unit_convert(value_in_celsius, "C", "F")
print(f"100 degrees Celsius is {converted_value:.2f} degrees Fahrenheit.")

# Convert 5 liters to milliliters
value_in_liters = 5.0
converted_value = unit_convert(value_in_liters, "L", "mL")
print(f"5 liters is {converted_value:.0f} milliliters.")
```

The **get_bmr** function calculates the Basal Metabolic Rate (BMR) using the Harris-Benedict equation. BMR represents the number of calories required for basic life-sustaining functions.

```
from healthsciencecalculator.healthsciencecalculator import bmr

# Example usage

# Calculate BMR for a male
weight_male = 70.0  # Weight in kilograms
height_male = 175.0  # Height in centimeters
age_male = 25  # Age in years
sex_male = "male"

bmr_value_male = get_bmr(weight_male, height_male, age_male, sex_male)
print(f"BMR for a 25-year-old male (70 kg, 175 cm): {bmr_value_male:.2f} calories/day")

# Calculate BMR for a female
weight_female = 60.0  # Weight in kilograms
height_female = 165.0  # Height in centimeters
age_female = 30  # Age in years
sex_female = "female"

bmr_value_female = get_bmr(weight_female, height_female, age_female, sex_female)
print(f"BMR for a 30-year-old female (60 kg, 165 cm): {bmr_value_female:.2f} calories/day")
```

## Running the Test Suite

### Prerequisites

Before running the tests, make sure you have the following installed:

Python 3.x – You can check if you have Python installed by running:
```bash
python --version
```

pytest – The test suite uses the pytest testing framework. You can install pytest using pip:
```bash
pip install pytest

```

(Optional) pytest-cov – To check test coverage, you can install the pytest-cov plugin:
```bash
pip install pytest-cov
```

### Running the Tests

Once the prerequisites are installed, navigate to the root directory of the project (where pytest is located, and run the following command in your terminal:

```bash
pytest
```

This will automatically discover and run all tests in files starting with test_ and containing functions starting with test_.

### Runnin Specific Tests

To run a specific test file, use:

```bash
pytest path/to/test_file.py
```

To run a specific test function within a file, use:
```bash
pytest path/to/test_file.py::test_function_name
```

### Viewing Test Results

pytest will show the test results in your terminal, indicating which tests passed and which failed. If a test fails, pytest will display an error message to help with debugging.

### Checking Test Coverage (Optional)

If you have pytest-cov installed, you can check the test coverage with the following command:

```bash
pytest --cov=healthsciencecalculator
```

This will show you how much of your code is covered by tests and highlight areas that need more coverage.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`healthsciencecalculator` was created by Forgive Agbesi, Jiayi Li, Hala Arar, Tengwei Wang. It is licensed under the terms of the MIT license.

### Why MIT License?

The healthsciencecalculator.py package is released under the MIT license to promote widespread adoption and improvement of standardized health metric calculations in the medical and research communities. This choice reflects our commitment to:

- Scientific transparency: By using the MIT license, we ensure that the algorithms and methodologies behind the health metric calculations are openly accessible. This allows researchers to replicate the calculations, fostering trust and credibility in the results.
- Healthcare integration: The open license allows healthcare providers and organizations to adapt the package to their systems, improving patient care and decision-making through easy customization and integration.
- Educational use: The MIT license makes the package freely available for use in educational settings, supporting learning and innovation in healthcare, data science, and research.
- Quality improvement: By allowing unrestricted modification and redistribution, the research community can collectively improve these this tool and features they want to use. 

## Credits

`healthsciencecalculator` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

## Contributors

Forgive Agbesi
Hala Arar
Jiayi Li
Tengwei Wang
