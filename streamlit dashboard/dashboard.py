#importing libraries
import streamlit as st
import numpy as np  
import pandas as pd 

#data visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns
 #adding the title
st.title('Telecom Dashboard')


#importing the dataset
df = pd.read_csv('telecom.csv')
#displaying 5 rows of the dataset
st.subheader('First 5 rows of the data')
st.dataframe(df.head())


st.subheader("Dataset Information")
info_data = {
    "Number of Rows": [df.shape[0]],
    "Number of Columns": [df.shape[1]],
    "Number of Missing Values": [df.isnull().sum().sum()]
}

st.table(pd.DataFrame(info_data))

# Display the data types of columns in a table
st.subheader("Column Data Types")
data_types = df.dtypes.reset_index()
data_types.columns = ['Column', 'Data Type']
st.table(data_types)

#displaying the statistical summary of data
st.sidebar.header("Statistical Summary")
stat_summary = df.describe().T
stat_summary = stat_summary.round(2)
st.sidebar.table(stat_summary)

# Function to fill numeric missing values with the mean
def fill_na(df):
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            col_mean = df[col].mean()
            df[col].fillna(value=col_mean, inplace=True)
    return df

# Fill missing values with the mean
df = fill_na(df)

# Display the dataset after filling missing values
st.subheader("Dataset after Filling Missing Values with Mean")
st.dataframe(df.head())

st.title("Bar Plot Analysis")

# Select a column for bar plot
selected_column = st.selectbox("Select a column for bar plot", df.columns)

# Plot the bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x=df[selected_column].value_counts().index, y=df[selected_column].value_counts())
plt.title(f"Bar Plot of {selected_column}")
plt.xlabel(selected_column)
plt.ylabel("Count")

# Display the bar plot in Streamlit
st.subheader(f"Bar Plot of {selected_column}")
st.pyplot()

st.subheader('Bivariet analysis')
df['all_tot'] = df['Total DL (Bytes)'] + df['Total UL (Bytes)']
df.head()



# Select x and y columns for the scatter plot
x_column = st.selectbox("Select X-axis Column", df.columns)
y_column = st.selectbox("Select Y-axis Column", df.columns)

# Plot the scatter plot
fig, ax = plt.subplots(figsize=(7, 5))
sns.scatterplot(data=df, x=x_column, y=y_column, hue=y_column, ax=ax)
plt.title(f"Scatter Plot: {y_column} vs {x_column}")
plt.xlabel(x_column)
plt.ylabel(y_column)
st.pyplot(fig)

#getting the variables we need
df_sess = df[['MSISDN/Number','Dur. (ms)', 'all_tot']]
#grouping by msisdn
sess_group = pd.DataFrame(df_sess.groupby('MSISDN/Number')['Dur. (ms)'].sum())

#performing the decile cut
sess_group['decile'] = pd.qcut(sess_group['Dur. (ms)'], q = [0.1, 0.2,0.3,0.4,0.5,1], labels=False)
print(sess_group)
# Displaying the result in Streamlit
st.subheader("Decile Cut Analysis Result")
#st.dataframe(sess_group)
# Merging the two dataframes to get the variables we need
df_merg = pd.merge(sess_group, df_sess[['all_tot', 'MSISDN/Number']], on='MSISDN/Number')
#displaying on streamlit
st.dataframe(df_merg.head())

#grouping the df_merge per class
df_merg_sum = pd.DataFrame(df_merg.groupby('decile')['all_tot'].sum())
st.subheader('grouping the dataframe per the decile cut')
st.dataframe(df_merg_sum)

# #selection of columns
# #df_corr = df[['Social Media DL (Bytes)', 'Social Media UL (Bytes)',
#        'Google DL (Bytes)', 'Google UL (Bytes)', 'Email DL (Bytes)',
#        'Email UL (Bytes)', 'Youtube DL (Bytes)', 'Youtube UL (Bytes)',
#        'Netflix DL (Bytes)', 'Netflix UL (Bytes)', 'Gaming DL (Bytes)',
#        'Gaming UL (Bytes)', 'Other DL (Bytes)', 'Other UL (Bytes)',
#        'Total UL (Bytes)', 'Total DL (Bytes)']]



# Selection of columns
selected_columns = st.multiselect("Select columns for correlation analysis(you can select more than 2 columns. Please select column to remove the error showing)", df.columns)
df_corr = df[selected_columns]

# Getting the correlation
correl = df_corr.corr()

# Displaying the correlation matrix in Streamlit
st.subheader("Correlation Matrix of Selected Columns")
st.dataframe(correl)



# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correl, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')

# Display the heatmap in Streamlit
st.subheader("Correlation Heatmap")
st.pyplot()
