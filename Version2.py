import streamlit as st
import pandas as pd
import plotly.express as px

# Title and Introduction
st.title("Business Dashboard")
st.write("This dashboard provides insights into sales, customer demographics, and product performance.")

# Data Input
file_path = '/content/drive/MyDrive/Lastclass/sales.csv'
data = pd.read_csv(file_path)

# Display data preview
st.header("Preview of the Uploaded Data")
st.dataframe(data.head())

# Sales Insights
st.header("Sales Insights")
sales_fig = px.line(data, x='sales_date', y='sales_amount', title='Sales Over Time')
st.plotly_chart(sales_fig)

# Customer Segmentation by Region
st.header("Customer Segmentation by Region")
segmentation_fig = px.pie(data, names='region', values='sales_amount', title="Customer Segmentation by Region")
st.plotly_chart(segmentation_fig)

# Product Analysis
st.header("Product Analysis")
top_products_df = data.groupby('product').sum()['sales_amount'].nlargest(10).reset_index()
product_fig = px.bar(top_products_df, x='product', y='sales_amount', title="Top Products By Sales", text='sales_amount')
st.plotly_chart(product_fig)

# Footer
st.markdown("---")
st.write("This business dashboard template is flexible. Expand upon it based on your specific business needs.")
