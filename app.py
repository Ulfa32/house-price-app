import streamlit as st
import pandas as pd
import numpy as np
import joblib

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================
st.set_page_config(
    page_title="Prediksi Harga Rumah Bandung",
    layout="centered"
)

st.title("Prediksi Harga Rumah Kota Bandung")
st.write("Masukkan spesifikasi rumah, pilih kecamatan dan model, lalu prediksi harga.")

# LOAD DATA WILAYAH
df_wilayah = pd.read_csv("wilayah_all.csv")

# kolom: lokasi | wilayah | wilayah_encoded
daftar_kecamatan = sorted(df_wilayah["lokasi"].unique().tolist())
kecamatan_to_wilayah = dict(
    zip(df_wilayah["lokasi"], df_wilayah["wilayah_encoded"])
)

# INPUT USER
st.subheader("Spesifikasi Rumah")

kt = st.number_input("Jumlah Kamar Tidur", min_value=0, step=1)
km = st.number_input("Jumlah Kamar Mandi", min_value=0, step=1)

luas_bangunan = st.text_input(
    "Luas Bangunan (m²)",
    placeholder="contoh: 120"
)

luas_tanah = st.text_input(
    "Luas Tanah (m²)",
    placeholder="contoh: 150"
)

lokasi_pilih = st.selectbox(
    "Kecamatan",
    daftar_kecamatan,
    index=None,
    placeholder="Pilih Kecamatan"
)

# PILIH MODEL
st.subheader("Pilih Model")

model_dict = {
    "Baseline SVR": "baseline_svr.pkl",
    "Grid Search CV=3": "gs_cv3_svr.pkl",
    "Grid Search CV=5": "gs_cv5_svr.pkl",
    "Grid Search CV=10": "gs_cv10_svr.pkl",
    "Random Search CV=3": "rs_cv3_svr.pkl",
    "Random Search CV=5": "rs_cv5_svr.pkl",
    "Random Search CV=10": "rs_cv10_svr.pkl",
    "Bayesian Opt CV=3": "bo_cv3_svr.pkl",
    "Bayesian Opt CV=5": "bo_cv5_svr.pkl",
    "Bayesian Opt CV=10": "bo_cv10_svr.pkl"
}

model_name = st.selectbox(
    "Metode Pemodelan",
    list(model_dict.keys()),
    index=None,
    placeholder="Pilih Model"
)

# TOMBOL PREDIKSI
if st.button("Prediksi Harga"):

    if lokasi_pilih is None or model_name is None:
        st.warning("⚠️ Silakan pilih kecamatan dan model terlebih dahulu.")
        st.stop()

    try:
        luas_bangunan = float(luas_bangunan)
        luas_tanah = float(luas_tanah)
    except:
        st.error("⚠️ Luas bangunan dan luas tanah harus berupa angka.")
        st.stop()

    if luas_bangunan < 90 or luas_tanah < 90:
        st.error("⚠️ Luas bangunan dan luas tanah minimal 90 m².")
        st.stop()

    if luas_bangunan > luas_tanah:
        st.error("⚠️ Luas bangunan tidak boleh lebih besar dari luas tanah.")
        st.stop()

    # LOAD MODEL
    MODEL_DIR = "models/"
    model = joblib.load(MODEL_DIR + model_dict[model_name])

    wilayah_encoded = kecamatan_to_wilayah[lokasi_pilih]

    # FEATURE ENGINEERING
    total_rooms = kt + km
    kepadatan_kamar = total_rooms / luas_bangunan
    bangunan_log = np.log1p(luas_bangunan)

    X_input = pd.DataFrame([[ 
        kt,
        km,
        luas_bangunan,
        luas_tanah,
        total_rooms,
        kepadatan_kamar,
        bangunan_log,
        wilayah_encoded
    ]], columns=[
        'kt',
        'km',
        'luas_bangunan',
        'luas_tanah',
        'total_rooms',
        'kepadatan_kamar',
        'bangunan_log',
        'wilayah_encoded'
    ])

    # PREDIKSI 
    y_pred_log = model.predict(X_input)[0]
    harga_juta = np.expm1(y_pred_log)

    # FORMAT HARGA
    def format_harga(juta):
        if juta >= 1000:
            return f"Rp {juta/1000:.2f} Miliar"
        else:
            return f"Rp {juta:,.0f} Juta"

    # OUTPUT
    st.subheader("📊 Hasil Prediksi")
    st.success(f"Model: **{model_name}**")
    st.markdown(f"### 💰 {format_harga(harga_juta)}")
