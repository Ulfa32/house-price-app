Aplikasi Prediksi Harga Rumah di Kota Bandung

Proyek machine learning untuk prediksi harga rumah di Kota Bandung menggunakan Support Vector Regression (SVR) dengan hyperparameter tuning:

Grid Search

Random Search

Bayesian Optimization

Proyek ini mencakup proses preprocessing data, pelatihan model, hyperparameter tuning, uji data eksternal, serta aplikasi prediksi berbasis Streamlit.

📂 Struktur Proyek
house-price-app/
├── .devcontainer/              # Konfigurasi development container
├── Code Colab/                 # Notebook Google Colab (ipynb & .py)
├── models/                     # Model hasil pelatihan
├── DATA_UJI_EKSTERNAL.csv      # Dataset uji eksternal
├── wilayah_all.csv             # Data wilayah/kecamatan Kota Bandung
├── app.py                      # Aplikasi prediksi (Streamlit)
├── requirements.txt            # Daftar library Python
└── README.md

🎯 Tujuan Proyek

Memprediksi harga rumah berdasarkan fitur properti dan lokasi

Membandingkan performa model baseline dan model hasil tuning

Menguji kemampuan generalisasi model menggunakan data uji eksternal

Menyediakan aplikasi prediksi interaktif berbasis Streamlit

🔹 Fitur yang Digunakan

Model menggunakan 8 fitur terpilih hasil feature selection:

kt

km

luas_bangunan

luas_tanah

total_rooms

kepadatan_kamar

bangunan_log

lokasi

Fitur lokasi disesuaikan agar konsisten antara data training dan data uji eksternal.

🔹 Model yang Digunakan

Baseline SVR (tanpa cross-validation)

Grid Search

CV = 3

CV = 5

CV = 10

Random Search

CV = 3

CV = 5

CV = 10

Bayesian Optimization

CV = 3

CV = 5

CV = 10

Total model yang diuji: 10 model

📊 Evaluasi Model

Setiap model dievaluasi menggunakan:

R² (Coefficient of Determination)

Mean Squared Error (MSE)

Root Mean Squared Error (RMSE)

Waktu komputasi

Ukuran model

🧪 Uji Data Eksternal

Dataset: DATA_UJI_EKSTERNAL.csv

Menggunakan alur preprocessing yang sama persis dengan data training

Digunakan untuk menguji generalisasi model terhadap data baru

🖥️ Aplikasi Streamlit

Aplikasi prediksi harga rumah dibuat menggunakan Streamlit (app.py).

Fitur Aplikasi:

Input fitur rumah secara interaktif

Prediksi harga rumah berdasarkan model terpilih

Output harga dalam format yang mudah dibaca

▶️ Menjalankan Aplikasi
pip install -r requirements.txt
streamlit run app.py

🎥 Rekaman Aplikasi (Streamlit App Record)

Tersedia rekaman penggunaan aplikasi Streamlit sebagai dokumentasi tambahan:

📁 Streamlit App Record

Berisi demo penggunaan aplikasi dan hasil prediksi

File berupa screen recording dari input hingga output prediksi

📦 Library yang Digunakan

Beberapa library utama:

pandas

numpy

scikit-learn

optuna

joblib

streamlit

📝 Catatan

Semua proses preprocessing pada data uji eksternal disamakan dengan data training

Proyek ini dibuat untuk keperluan akademik

👤 Penulis

Ulfa R
Prediksi Harga Rumah Menggunakan Support Vector Regression dengan Hyperparameter Tuning Grid Search, Random Search, dan Bayesian Optimization
