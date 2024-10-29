# World Bank Commodity Price Reports API
_Tool For World Banks Commodity Price Reports_

## How It Works
Boyko Wealth utilizes the official monthly commodity price reports released in excel format each month. This tool automatically converts the most recent data release into a usable Pandas DataFrame. 
To return the data, simply reference: WORLD_BANK_COMMODITY.data() in your script. **Please Note: Heading names have been converted into format: "DATA_HERE", which allows for concistency among our other applications.** The dates provided by the world bank are in format "YYYYMmm", we have converted this into "YYYY-MM-DD" format for concistency.

### Output Example
![image](https://github.com/user-attachments/assets/09cf0da8-af7c-499e-a3cb-c7b48d861412)

