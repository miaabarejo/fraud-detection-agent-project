import streamlit as st
from fraud_detector import flag_anomalies
from transaction_data import generate_transactions
from explain_fraud import explain_transaction

# Set up global session state variables to persist data across page reruns
if 'df' not in st.session_state:
    st.session_state.df = None
if 'flagged_df' not in st.session_state:
    st.session_state.flagged_df = None
if 'initial_selection' not in st.session_state:
    st.session_state.initial_selection = None
if 'current_selection' not in st.session_state:
    st.session_state.current_selection = None
    
st.title("🛡️ Fraud Detection Agent")


def run_analysis_and_store():
    """Generates data, flags anomalies, and stores results in session state."""
    
    df = generate_transactions()
    flagged_df = flag_anomalies(df)

    # Store analysis results in session state
    st.session_state.df = df
    st.session_state.flagged_df = flagged_df
    
    # Set the initial selection to the first flagged ID
    if not flagged_df.empty:
        st.session_state.initial_selection = flagged_df[flagged_df["Flagged"] == True]["Transaction ID"].tolist()[0]
    else:
        st.session_state.initial_selection = None
        
        
if st.button("Run Analysis"):
    run_analysis_and_store()


# Display results only if data is present in the session state
if st.session_state.df is not None:
    st.subheader("🔍 All Transactions")
    st.dataframe(st.session_state.df)

    # Check the persisted data, not the locally created variable
    if not st.session_state.flagged_df.empty:
        st.subheader("🚨 Flagged Transactions")
        
        # Display the correctly filtered DataFrame (Only Flagged=True rows)
        # We must filter this *DataFrame* for display purposes.
        flagged_for_display = st.session_state.flagged_df[st.session_state.flagged_df["Flagged"] == True]
        st.dataframe(flagged_for_display)
        
        
        st.subheader("💬 AI Explanation")
        
        # --- FIX IS HERE: The list of IDs must be generated ONLY from the flagged rows ---
        id_list = flagged_for_display["Transaction ID"].tolist()
        
        # Find the index of the previously selected item to prevent reset
        if 'current_selection' in st.session_state and st.session_state.current_selection in id_list:
            default_index = id_list.index(st.session_state.current_selection)
        elif st.session_state.initial_selection in id_list:
            default_index = id_list.index(st.session_state.initial_selection)
        else:
            default_index = 0

        selected_id = st.selectbox(
            "Choose a flagged Transaction ID",  
            id_list, # Now uses the clean, filtered list
            index=default_index,
            key='select_id_key' 
        )
        
        # Store the current selection for the next rerun
        st.session_state.current_selection = selected_id
        
        # --- AI GENERATION BLOCK ---
        if selected_id:
            # Locate the row of the selected transaction from the persisted DataFrame
            # Since 'flagged_df' still holds ALL rows but with the 'Flagged' column, we use the original state variable for access
            row = st.session_state.flagged_df[st.session_state.flagged_df["Transaction ID"] == selected_id].iloc[0]

            # Use a container for stable output display
            explanation_container = st.empty()
            
            with explanation_container.container():
                with st.spinner(f"Generating forensic explanation for {selected_id}..."):
                    explanation = explain_transaction(row)
                    
                st.write(explanation)