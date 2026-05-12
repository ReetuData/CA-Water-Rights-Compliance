# CA-Water-Rights-Compliance
A Python and ArcGIS-based tool designed to automate the identification of water diversion points within California's Fully Appropriated Stream Systems (FASS). This project supports regulatory compliance and environmental protection by flagging potential water right violations.


# CA-Water-Rights-Compliance 🌊
**Automated Geospatial Tool for Stream Flow Monitoring & Regulatory Compliance**

## 📌 Project Overview
In California, many water diversions occur on "Fully Appropriated Stream Systems" (FASS)—waterways where no new water rights are currently available. Monitoring these for compliance is a manual, data-intensive task. 

This project leverages **Python (ArcPy)** and **ArcGIS Pro** to automate the identification of Points of Diversion (PODs) that overlap with restricted stream systems. This ensures environmental protection for instream flows and public trust resources.

## 🚀 Key Features
* **Automated Screening:** Uses spatial joins to flag diversions on closed streams.
* **Data Integration:** Combines real-time USGS stream gage data with eWRIMS water right records.
* **Compliance Reporting:** Generates automated alerts for regulatory teams during restricted seasons.

## 🛠️ Technologies Used
* **Languages:** Python (ArcPy)
* **Software:** ArcGIS Pro 3.x
* **Data Science:** Data cleaning, Spatial Join, Buffer Analysis
* **Data Sources:** [California State Water Board (eWRIMS)](https://www.waterboards.ca.gov/), [FASS Dataset](https://gis.data.ca.gov/)

## 📂 Project Structure
* `/scripts`: Python scripts for automation.
* `/data`: Sample shapefiles and links to state datasets.
* `/docs`: Project methodology and regulatory context.

## 🧪 Methodology
1. **Acquisition:** Pulling POD and FASS layers from the CA Open Data Portal.
2. **Spatial Join:** Linking diversions to restricted stream segments.
3. **Python Automation:** Scripting the filtering process to identify "At Risk" diversions based on seasonality.

---
*Created by Reetu Sharma | Senior Chemist & Data Scientist*
