import streamlit as st
import pandas as pd
import plotly.express as px

# Title and Introduction with a colorful header
st.markdown("<h1 style='color: #4A90E2;'>Business Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #4A90E2;'>This dashboard provides insights into sales, customer demographics, and product performance.</p>", unsafe_allow_html=True)

# Data Input
file_path = ("choose a csv file", type="csv")
data = pd.read_csv(file_path)

# Display data preview
st.markdown("<h2 style='color: #FF5733;'>Preview of the Uploaded Data</h2>", unsafe_allow_html=True)
st.dataframe(data.head())

# Sales Insights
st.markdown("<h2 style='color: #33C3F0;'>Sales Insights</h2>", unsafe_allow_html=True)
sales_fig = px.line(data, x='sales_date', y='sales_amount', title='Sales Over Time', line_shape='spline')
sales_fig.update_layout(plot_bgcolor="#F0F0F0", title_font=dict(size=20), title_font_color='#33C3F0')
st.plotly_chart(sales_fig)

# Customer Segmentation by Region
st.markdown("<h2 style='color: #FF6347;'>Customer Segmentation by Region</h2>", unsafe_allow_html=True)
segmentation_fig = px.pie(data, names='region', values='sales_amount', title="Customer Segmentation by Region", color_discrete_sequence=px.colors.sequential.RdBu)
segmentation_fig.update_layout(title_font=dict(size=20), title_font_color='#FF6347')
st.plotly_chart(segmentation_fig)

# Product Analysis
st.markdown("<h2 style='color: #32CD32;'>Product Analysis</h2>", unsafe_allow_html=True)
top_products_df = data.groupby('product').sum()['sales_amount'].nlargest(10).reset_index()
product_fig = px.bar(top_products_df, x='product', y='sales_amount', title="Top Products By Sales", text='sales_amount', color='sales_amount', color_continuous_scale=px.colors.sequential.Viridis)
product_fig.update_layout(plot_bgcolor="#F7FBFF", title_font=dict(size=20), title_font_color='#32CD32')
st.plotly_chart(product_fig)

# Footer
st.markdown("<hr style='border: 1px solid #4A90E2;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #4A90E2;'>This business dashboard template is flexible. Expand upon it based on your specific business needs.</p>", unsafe_allow_html=True)
