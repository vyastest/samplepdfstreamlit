import streamlit as st
import pandas as pd
from io import BytesIO
import matplotlib.pyplot as plt

# Sample data
clicks_data = pd.DataFrame({'Category': ['A', 'B', 'A', 'B', 'C'],
                            'Clicks': [100, 150, 120, 80, 90]})
impressions_data = pd.DataFrame({'Campaign': ['X', 'Y', 'X', 'Y', 'Z'],
                                 'Impressions': [1000, 1200, 800, 900, 700]})

# Group clicks by category
clicks_grouped = clicks_data.groupby('Category').sum()

# Create a Streamlit app
st.title('Clicks and Impressions')

st.subheader('Clicks by Category')
st.write(clicks_grouped)

st.subheader('Impressions by Campaign')
st.write(impressions_data)

# Download as PDF
if st.button("Download as PDF"):
    # Create a PDF document
    pdf_buffer = BytesIO()
    plt.figure(figsize=(8, 6))
    plt.subplot(2, 1, 1)
    plt.bar(clicks_grouped.index, clicks_grouped['Clicks'])
    plt.title('Clicks by Category')
    
    plt.subplot(2, 1, 2)
    plt.bar(impressions_data['Campaign'], impressions_data['Impressions'])
    plt.title('Impressions by Campaign')

    plt.tight_layout()
    plt.savefig(pdf_buffer, format='pdf')
    pdf_buffer.seek(0)

    # Offer the PDF for download
    import base64


    # Assuming you have a PDF file in a bytes variable called pdf_buffer
    pdf_base64 = base64.b64encode(pdf_buffer).decode('utf-8')
    link = f'<a href="data:application/pdf;base64,{pdf_base64}" download="report.pdf">Download PDF</a>'
    st.markdown(link, unsafe_allow_html=True)


    st.write('You can click the button to download the report as a PDF.')
