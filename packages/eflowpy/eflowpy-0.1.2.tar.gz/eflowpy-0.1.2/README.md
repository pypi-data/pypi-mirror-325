# eflowpy
### A Python Package for Estimating Environmental Flow Requirements in Rivers

`eflowpy` is a Python package for estimating environmental flow requirements using **hydrological methods**. It provides methods such as **Flow Duration Curve (FDC), 7Q10, GEFC, and Tennant Method** to analyze river flow conditions for environmental assessments.

## Features
✔ Calculate Flow Duration Curve (FDC) with exceedance probabilities  
✔ Compute **7Q10 low-flow values** for drought analysis  
✔ Apply the **Tennant Method** for environmental flow assessments  
✔ Use **GEFC (Generalized Environmental Flow Criteria)** for water resource planning  
✔ Easily visualize FDC plots with **Q-value markers** (Q1, Q5, Q10, Q50, Q90, Q95)  
✔ Support for both **daily and monthly streamflow data**
✔ Handling missing data

---

## Installation
To install `eflowpy` from PyPI:
```bash
pip install eflowpy
```
To install the development version:
```bash
git clone https://github.com/gokhancuceloglu/eflowpy.git
cd eflowpy
pip install -e .
```

---

## How to Use

### ** Load Streamflow Data**
```python
from eflowpy.utils.data_reader import read_streamflow_data

df = read_streamflow_data("gauge_12013059_daily.csv")
print(df.head())
```

### ** Calculate Flow Duration Curve (FDC)**
```python
from eflowpy.hydrological.fdc import FlowDurationCurve

flow_series = df.iloc[:, 0]  # Extract flow column
fdc_method = FlowDurationCurve(flow_series)
fdc = fdc_method.calculate_fdc()

print(fdc.head())  # Show first few rows
```

### ** Get Specific Q-Values from FDC**
```python
q10 = fdc_method.get_flow_at_percentile(10)  # Q10 flow
q50 = fdc_method.get_flow_at_percentile(50)  # Median flow
q90 = fdc_method.get_flow_at_percentile(90)  # Low flow

print(f"Q10: {q10} m³/s, Q50: {q50} m³/s, Q90: {q90} m³/s")
```

### ** Plot FDC with Optional Q-Values**
```python
from eflowpy.utils.plotting import plot_fdc

plot_fdc(fdc, q_values=[1, 5, 10, 50, 90, 95])
```

---

## Folder Structure
```
eflowpy/
├── eflowpy/
│   ├── __init__.py
│   ├── core.py                # Base class for Environmental Flow methods
│   ├── hydrological/          # Hydrological methods directory
│   │   ├── __init__.py
│   │   ├── tennant.py         # Tennant Method
│   │   ├── fdc.py             # Flow Duration Curve (FDC)
│   │   ├── sevenq10.py        # 7Q10 Method
│   │   ├── gefc.py            # GEFC Method
│   ├── hydraulic/             # Hydraulic methods directory
│   │   ├── __init__.py
│   ├── utils/                 # Utility functions
│   │   ├── __init__.py
│   │   ├── data_reader.py     # Reads streamflow data
│   │   ├── plotting.py        # FDC Plotting functions
│   ├── setup.py               # Package configuration
├── examples/                  # Example usage scripts
│   ├── test_fdc.py
│   ├── test_tennant.py
├── README.md                   # Documentation
└── requirements.txt             # Dependencies
```

---

## License
This project is licensed under the **MIT License**.
