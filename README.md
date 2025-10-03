# mHealth-EmSarc-Framework

This repository contains the source code and replication package for the paper: "A Fine-Grained Emotion and Sarcasm Detection Framework in mHealth App Review Analysis for Understanding Patient Frustration, Trust, and Joy."

This project provides a web-based tool to analyze mHealth app reviews for both fine-grained emotion and sarcasm, implementing the multi-task learning framework described in the paper.

## Features
-   **Sarcasm Detection:** Classifies review text as Sarcastic or Not Sarcastic.
-   **Fine-Grained Emotion Analysis:** Identifies patient emotions such as Frustration, Distrust, Joy, and more.
-   **Web Interface:** A simple Django-based UI for easy interaction and demonstration.

## Tech Stack
-   **Backend Model:** PyTorch with Hugging Face Transformers (XLM-RoBERTa)
-   **Web Framework:** Django
-   **Data Handling:** Pandas, NumPy
-   **Language:** Python 3.8+

## Setup and Installation

Follow these steps to set up the project locally.

**1. Clone the repository:**
```bash
git clone https://github.com/massenon/mHealth-EmSarc-Framework.git
cd mHealth-EmSarc-Framework
```

**2. Create and activate a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Run the Django development server:**
Navigate into the `mhealth_analyzer` directory and run the server.
```bash
cd mhealth_analyzer
python manage.py runserver
```

## Usage
1.  Once the server is running, open your web browser and go to `http://127.0.0.1:8000/`.
2.  Enter an mHealth app review into the text box.
3.  Click the "Analyze Review" button.
4.  The results for Sarcasm and Emotion detection will be displayed below the form.

## Replication
The replication package contains:
-   The source code for the MTL framework in `analysis_engine/`.
-   The Django web application in `mhealth_analyzer/`.
-   The annotated dataset (or a sample) can be found in the `data/` directory.