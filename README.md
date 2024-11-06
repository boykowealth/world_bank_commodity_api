# World Bank Commodity Data Extraction

This Python module provides a streamlined approach to retrieve, clean, and format historical monthly commodity price data from the World Bank. The data includes various commodities like crude oil, natural gas, agricultural products, metals, and more, spanning multiple years.

## Features

- Downloads the latest World Bank commodity data.
- Cleans the data by normalizing column headers and filling missing values.
- Formats the date field for consistent analysis.
- Ready for use in time-series analysis, economic research, and commodity price tracking.

## Installation

1. Ensure you have Python 3.x installed.
2. Install required packages using pip:
   ```bash
   pip install pandas openpyxl
   ```

## Usage

The module contains a single class, `WORLD_BANK_COMMODITY`, with a `data()` method that returns a cleaned DataFrame of monthly commodity prices.

```python
from world_bank_commodity import WORLD_BANK_COMMODITY

# Fetch and display the cleaned data
data = WORLD_BANK_COMMODITY.data()
print(data.head())
```

## Code Overview

### `WORLD_BANK_COMMODITY` Class

- **`data()` Method**: 
   - Downloads the data from the World Bank URL.
   - Cleans the column headers by removing special characters and converting them to uppercase.
   - Converts the date column to a `datetime` object.
   - Returns the cleaned DataFrame.

### Sample Output

```
| DATE       | CRUDE_OIL_AVERAGE | NATURAL_GAS_US | SOYBEANS | ALUMINUM | ... |
|------------|--------------------|----------------|----------|----------|-----|
| 2022-01-01 | 85.52             | 4.24           | 1389.5   | 2568.5   | ... |
| 2022-02-01 | 92.13             | 4.95           | 1402.3   | 2610.0   | ... |
| ...        | ...               | ...            | ...      | ...      | ... |
```

## How Boyko Wealth Uses This Data

At **Boyko Wealth**, our team specializes in building advanced data model reports that analyze global economic trends, commodity markets, and investment risks. The World Bank commodity data is integral to these reports, providing us with reliable historical price trends across key commodities like crude oil, natural gas, metals, and agricultural products. This data serves as a foundation for:

- **Trend Analysis**: Tracking price movements over time to forecast market conditions and spot economic cycles.
- **Risk Modeling**: Integrating commodity price fluctuations into broader economic models that evaluate inflationary pressures and sector-specific risks.
- **Portfolio Strategy**: Using commodity data as a factor in asset allocation and hedging strategies, particularly in portfolios sensitive to energy, agriculture, and metals markets.

By incorporating this dataset, Boyko Wealth delivers precise insights for clients, supporting data-driven decisions in wealth management and strategic investment planning.

## Data Details

- **Data Source**: World Bank Commodity Price Data (Monthly).
- **Column Headers**: Converted to uppercase with spaces and commas replaced by underscores.
- **Data Cleaning**: Missing values are filled with zeros.

## Requirements

- **pandas**: For data manipulation.
- **openpyxl**: For reading Excel files.
