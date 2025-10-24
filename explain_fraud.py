from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import streamlit as st

explanation_prompt = PromptTemplate.from_template("""
You are a forensic accountant AI. A financial transaction has been flagged for possible fraud:

Transaction ID: {transaction_id}
Amount: ${amount}
Type: {type}
Account: {account}
Z-Score: {z_score}

Explain why this transaction might be suspicious and what actions a finance team should take.
""")

def explain_transaction(row):
    # Load key directly from Streamlit secrets
    # The key is securely retrieved from the Streamlit Cloud dashboard settings.
    api_key_value = st.secrets["secrets"]["API_KEY"]
    
    # Initialize the LLM. It securely looks for the OPENAI_API_KEY environment variable.
    llm = ChatOpenAI(temperature=0.3, model="gpt-3.5-turbo", api_key=api_key_value) # Explicitly set model for stability
    
    # Format the prompt with the transaction data
    prompt_string = explanation_prompt.format(
        transaction_id=row["Transaction ID"],
        amount=row["Amount"],
        type=row["Type"],
        account=row["Account"],
        z_score=round(row["Z-Score"], 2)
    )
    
    # Execute the LLM call using the modern .invoke() method
    response = llm.invoke(prompt_string)
    
    # CRITICAL FIX: Return the text content from the response object
    return response.content
