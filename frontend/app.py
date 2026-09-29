import streamlit as st
import requests

st.set_page_config(
    page_title="LegalEase",
    page_icon="📄",
    layout="wide"
)

st.title("LegalEase")
st.write("AI-Powered Legal Document Generator")

document_type = st.selectbox(
    "Document Type",
    ["Employment Contract", "NDA", "Lease Agreement"]
)

parties = st.text_area("Parties")
terms = st.text_area("Terms and Conditions")
dates = st.text_area("Important Dates")

if st.button("Generate Document"):
    data = {
        "document_type": document_type,
        "parties": parties,
        "terms": terms,
        "dates": dates
    }

    try:
        response = requests.post(
            "http://localhost:8000/generate",
            json=data
        )

        if response.status_code == 200:
            document = response.json()["generated_document"]

            st.subheader("Generated Document")
            edited_document = st.text_area(
                "Edit your document",
                document,
                height=400
            )

            st.download_button(
                "Download as TXT",
                edited_document,
                file_name="legal_document.txt"
            )

        else:
            st.error("Document generation failed.")

    except Exception as e:
        st.error(f"Backend connection error: {e}")
