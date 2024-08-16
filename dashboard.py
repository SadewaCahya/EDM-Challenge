import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

data = pd.read_csv("data_pendidikan_newss.csv")

st.title("Analisis pengangguran pada tingkat pendidikan")
st.subheader("Tren tingkat pengangguran dalam 4 tahun terakhir")

total = data[['2020', '2021', '2022', '2023']].sum()
periode = ['2020', '2021', '2022', '2023']

fig, ax = plt.subplots(figsize=(20, 10))
ax.plot(total.rename("tingkat pengangguran"), marker='o', linewidth=2, color="#72BCD4")
ax.set_xticklabels(periode, fontsize=10)
st.pyplot(fig)

st.subheader("jumlah pengangguran berdasarkan tingkat pendidikan")

fig, ax = plt.subplots(figsize=(20, 10))
option = st.selectbox(
    "What year you want to see?",
    ['2020', '2021', '2022', '2023'],
)

st.write("You selected:", option)    
ax = sns.barplot(
    x=data[option], 
    y=data["tingkat pendidikan"],
    ax=ax
)
for container in ax.containers:
    ax.bar_label(container, fmt='%d', padding=3, fontsize=10)

ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(20, 10))
option = st.selectbox(
    "What educational level you want to see?",
    data['tingkat pendidikan']
)       
st.write("You selected:", option)
data_option = data[data['tingkat pendidikan'] == option].drop("tingkat pendidikan", axis=1)
data_option = data_option.T
data_option.columns = [option]
ax = sns.barplot(
    x=periode, 
    y=data_option[option],
    ax=ax
)
for container in ax.containers:
    ax.bar_label(container, fmt='%d', padding=3, fontsize=10)

ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)


