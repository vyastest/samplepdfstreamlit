import pandas as pd
import streamlit as st
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Sample marketing data
data = {
    'Category': ['Category A', 'Category B', 'Category A', 'Category C', 'Category B'],
    'Clicks': [100, 150, 120, 80, 90],
    'Impressions': [1000, 1200, 800, 600, 700]
}

df = pd.DataFrame(data)

# Calculate the sum of clicks and total impressions by category
clicks_by_category = df.groupby('Category')['Clicks'].sum().reset_index()
impressions_by_category = df.groupby('Category')['Impressions'].sum().reset_index()

# Create a Streamlit app
st.title('Marketing Data Analysis')
st.write('Sample Marketing Data:')

# Display the sample marketing data
st.write(df)

# Create a function to generate a PDF with the calculations
def generate_pdf():
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    
    p.drawString(100, 750, "Clicks by Category")
    p.drawString(100, 725, clicks_by_category.to_string())
    
    p.drawString(100, 625, "Impressions by Category")
    p.drawString(100, 600, impressions_by_category.to_string())
    
    p.showPage()
    p.save()
    
    buffer.seek(0)
    return buffer

# Create a downloadable link for the PDF
st.markdown("### Download PDF with Calculations")
pdf_buffer = generate_pdf()
st.download_button(
    label="Download PDF",
    data=pdf_buffer,
    key="pdf",
    on_click=None,
)

