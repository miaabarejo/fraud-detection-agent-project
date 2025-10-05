# 🛡️ Fraud Detection AI Agent

**Portfolio Alignment:** Analytics, Operational Risk, Process Automation

---

## Project Goal & Business Value

This project designs and implements an automated workflow to support compliance and operational risk teams in a high-volume digital payments environment.

* **Objective:** To automatically screen financial transactions to identify severe statistical outliers (potential fraud or error) and generate an instant, actionable forensic report.
* **Operational Efficiency:** Replaces time-consuming manual data review by providing a real-time risk score and translating complex data into clear, human-readable instructions.
* **Core Value:** Directly tackles a core problem, minimizing financial losses and enhancing compliance processes.

---

## Analytical Methodology

The agent's logic is structured in three modular steps:

### 1. Statistical Anomaly Scoring (Z-Score)
* **Method:** The core logic calculates the **Z-Score** for every transaction amount.
* **Logic:** A transaction is flagged as high-risk if its Z-Score is greater than **3.0** (or less than -3.0). This threshold is standard practice for flagging significant statistical outliers.
* **Skills:** Python (Pandas/NumPy), Statistical Analysis, Data Filtering.

### 2. AI-Powered Forensic Explanation
* **Integration:** Uses the **LangChain/OpenAI** stack to provide a layer of Business Intelligence over the raw statistics.
* **Process:** The system feeds the flagged transaction's raw data (ID, Z-Score, Amount) into an LLM instructed to act as a "forensic accountant."
* **Result:** Generates a narrative summary of *why* the transaction is risky and recommends actionable next steps (e.g., "verify source documentation," "freeze the account").

### 3. Interactive BI Dashboard
* **Platform:** Streamlit is used to build a stable, interactive dashboard that visualizes all transactions and clearly isolates only the high-risk anomalies, allowing analysts to triage their work efficiently.

---

## Working Demonstration
The application is hosted live via Streamlit Cloud, allowing immediate interaction with the dashboard and the AI explanation features.

🌐 Live Demo: [Fraud Detection AI Agent on Streamlit](https://fraud-detection-agent-project.streamlit.app/)

<img width="771" height="851" alt="image" src="https://github.com/user-attachments/assets/6507d737-47d5-478a-99ac-5f9bdbcc95c1" />





**Sample AI Explanation for TX-XXXX (Z-Score: 3.94):**
> *This transaction might be suspicious due to the high Z-Score of 3.94, which indicates that it is significantly outside the normal range of transactions for account A102. A Z-Score above 3 typically suggests that the transaction is an outlier and may be fraudulent or erroneous.*
> *The finance team should investigate this transaction further by reviewing the details of the payment, such as the recipient, purpose, and any supporting documentation. They should also verify the legitimacy of the transaction with the account holder and potentially freeze the account temporarily to prevent any further suspicious activity.*

---

## Installation & Setup

To run this agent locally, you need Python 3.9+ and your OpenAI API Key.

1.  **Clone the Repository:**
    ```bash
    git clone [YOUR-REPOSITORY-LINK-HERE]
    cd fraud-detection-agent
    ```
2.  **Install Dependencies:** All required packages (Streamlit, LangChain, OpenAI, Pandas) are listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```
3.  **Set Environment Variable:** Set your OpenAI secret key securely in your terminal session:
    ```bash
    $env:OPENAI_API_KEY='YOUR_SECRET_KEY_HERE'  # PowerShell/Anaconda Prompt
    # OR
    export OPENAI_API_KEY='YOUR_SECRET_KEY_HERE' # macOS/Linux
    ```
4.  **Run the App:**
    ```bash
    streamlit run app.py
    ```

---

## Future BI Enhancements

* **Contextual Z-Score:** The next phase would be to refine the anomaly detection by calculating Z-scores based on **transaction type** (e.g., comparing a 'Transfer' only against other 'Transfers') for higher accuracy and fewer false positives.
* **Next-Step Automation:** Integrate the system to automatically trigger an email alert or open a ticket in a platform like JIRA or Salesforce, streamlining the operational response.
