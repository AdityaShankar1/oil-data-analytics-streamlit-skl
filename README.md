##🛢️ Oil & Gas Data Analytics Dashboard (Streamlit + Scikit-learn)

📌# Overview

This project is an interactive Oil & Gas analytics dashboard built using Streamlit.
It demonstrates an end-to-end data analytics workflow — from data ingestion and preprocessing to machine learning insights — all packaged in a web-based GUI.

Designed to simulate an internal tool for decision-making in the Oil & Gas industry, the dashboard follows a modular MVC-like structure and was developed in line with SDLC principles.


---

🎯 # Objectives

Provide exploratory data analysis and visual insights for Oil & Gas operational data.

Integrate machine learning (Scikit-learn) to detect patterns and predict key metrics.

Build a user-friendly web interface for non-technical stakeholders.



---

🏢 # Business Impact

While based on a synthetic dataset, this project models real-world Oil & Gas decision workflows.
The dashboard enables:

Faster decision-making by automating manual spreadsheet analysis.

Proactive maintenance planning through predictive insights.

Operational transparency via visual KPI tracking.

Data accessibility for teams without technical expertise.


Such a tool could reduce the analysis-to-action cycle time from hours to minutes, saving costs and improving uptime in large-scale operations.


---

🏗️ # Features

Interactive Visualizations: Dynamic charts and plots for data exploration.

ML Insights: Predictive analysis using Scikit-learn models.

Search & Filter: View data subsets on-demand.

Configurable Parameters: Adjust thresholds and model settings from the UI.

Secure Access: API Key–based authentication for basic access control.



---

🛠️ # Tech Stack

Layer	Technologies

Frontend UI	Streamlit
Data Processing	Pandas, NumPy
Visualization	Matplotlib, Seaborn
Machine Learning	Scikit-learn
Auth & Config	dotenv for API keys
Structure	MVC-inspired multi-file architecture


---

📂  Project Structure

📁 oil-gas-dashboard
│
├── 📄 app.py                  # Streamlit main app
├── 📁 data                    # Dataset(s)
├── 📁 modules                 # Core logic split into MVC layers
│   ├── model.py               # Data & ML processing
│   ├── view.py                # UI components
│   └── controller.py          # Interaction logic
├── 📁 assets                  # Images/icons
├── requirements.txt           # Python dependencies
└── README.md                  # This file


---

🔍 # Example Insights

Predictive maintenance indicators.

Production trend analysis.

Resource allocation efficiency metrics.

---

#🚀 Getting Started

1️⃣ Clone the Repository

git clone https://github.com/AdityaShankar1/oil-data-analytics-streamlit-skl.git
cd oil-data-analytics-streamlit-skl

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Set up API Key

Create a .env file in the root directory:

API_KEY=your_api_key_here

4️⃣ Run the App

streamlit run app.py


---

📈 Future Improvements (currently working on):

Add persistent storage (PostgreSQL / SQLite).

Implement CRUD operations for data management.

Integrate REST APIs for live data feeds.

Enhance role-based authentication.


---

🧑‍💻 Author:

Aditya Shankar

💼 LinkedIn: https://www.linkedin.com/in/aditya-shankar-35a85a247/
