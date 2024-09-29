import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os


daydf = pd.read_csv(os.path.join(os.getcwd(), "Dashboard", "daydf.csv")) 

def trend_by_year(df):
    trend_by_year = df.groupby(by='yr').agg({
        'cnt':'sum'
    })
    trend_by_year = trend_by_year.reset_index()
    trend_by_year.rename(columns={
        "cnt": "jumlah_pengguna"
    }, inplace=True)
    return trend_by_year
    
def monthly_df_per_yr(df):
    df['mnth'] = pd.Categorical(df['mnth'], categories=
    ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    ordered=True)
    monthly_df_per_yr = df.groupby(by=["mnth","yr"]).agg({
    "cnt": "sum"
    }).reset_index()
    monthly_df_per_yr.rename(columns={
        "cnt": "jumlah_pengguna"
    }, inplace=True)
    return monthly_df_per_yr

def bike_rent_byseason(df):
    bike_rent_byseason = df.groupby(by='season').agg({
        'cnt':'sum'
    })
    bike_rent_byseason = bike_rent_byseason.reset_index()
    bike_rent_byseason.rename(columns={
        "cnt": "jumlah_pengguna"
    }, inplace=True)
    return bike_rent_byseason

def weeday_weekend_comparison(df):
    weeday_weekend_comparison = df.groupby(by='weekday').agg({
        'cnt':'sum'
    })
    weeday_weekend_comparison = weeday_weekend_comparison.reset_index()
    weeday_weekend_comparison.rename(columns={
        "cnt": "jumlah_pengguna"
    }, inplace=True)
    return weeday_weekend_comparison

def by_workingday(df):
    by_workingday = df.groupby(by='workingday').agg({
        'cnt':'sum'
    })
    by_workingday = by_workingday.reset_index()
    by_workingday.rename(columns={
        "cnt": "jumlah_pengguna"
    }, inplace=True)
    return by_workingday

with st.sidebar:
    st.image("Dashboard/city-bike.png")
    

st.title("Bike Sharing Analysis")

# 1. Trend by Year
st.header("1. Bagaimana tren jumlah pengguna sepeda beberapa tahun terakhir?")
monthly_df_per_yr = monthly_df_per_yr(daydf)
plt.figure(figsize=(10, 6))
sns.lineplot(data=monthly_df_per_yr, x="mnth", y="jumlah_pengguna", hue="yr")
plt.title('Tren Jumlah Penggunaan/Penyewaan Sepeda')
plt.xlabel(None)
plt.ylabel(None)
plt.legend(title='Tahun', loc='upper left')
st.pyplot(plt)

# 2. Bike Rental by Season
st.header("2. Bagaimana musim mempengaruhi persewaan sepeda?")
bike_rent_season_df = bike_rent_byseason(daydf)
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(
    y="jumlah_pengguna", 
    x="season",
    data=bike_rent_season_df.sort_values(by="season", ascending=False),
    ax=ax
)
ax.set_title("Pengaruh Musim Pada Bisnis Bike Sharing", loc="center", fontsize=15)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis="x", labelsize=12)
st.pyplot(fig)
st.write("Terlihat dari penyewaan sepeda terbanyak ada pada musim gugur")

# 3. Weekday/Weekend Comparison
st.header("3. Bagaimana perbandingan persewaan sepeda antara hari libur dan hari kerja")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(
    x='workingday',
    y='cnt', 
    data=daydf,
    ax=ax
)
ax.set_title('Perbandingan Penyewa Sepeda hari libur Dan hari kerja')
ax.set_xlabel(None)
ax.set_ylabel('Jumlah Penyewaan Sepeda')
st.pyplot(fig)
st.write("Terlihat dari jumlah penyewaan sepeda pada hari libur lebih sedikit daripada hari kerja")

# 4. Impact of Working Day
st.header("4. Bagaimana pengaruh hari kerja terhadap kinerja bisnis bike sharing?")
workingday_df = by_workingday(daydf)
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(
    y="jumlah_pengguna",
    x="workingday",
    data=workingday_df.sort_values(by="workingday", ascending=False),
    ax=ax
)
ax.set_title("Pengaruh Hari Kerja Pada Bisnis Bike Sharing", loc="center", fontsize=15)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis="x", labelsize=12)
st.pyplot(fig)
