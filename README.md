Aplikasi Prediksi Harga Rumah di Kota Bandung
Proyek machine learning untuk prediksi harga rumah menggunakan Support Vector Regression (SVR) dengan hyperparameter tuning Grid Search, Random Search, dan Bayesian Optimization.
Proyek ini mencakup proses preprocessing data, pelatihan model, hyperparameter tuning, uji data eksternal, serta aplikasi prediksi berbasis Streamlit.

📂 Struktur Proyek
    house-price-app/
    │
    ├── .devcontainer/              # Konfigurasi development container
    ├── Code Colab/                 # Notebook Google Colab (ipynb & py)
    ├── models/                     # Model hasil 
    │
    ├── DATA_UJI_EKSTERNAL.csv      # Dataset uji eksternal
    ├── wilayah_all.csv             # Data wilayah/lokasi kecamatan di Kota Bandung
    │
    ├── app.py                      # Aplikasi prediksi (Streamlit)
    ├── requirements.txt            # Daftar library Python
    └── README.md

🎯 Tujuan Proyek
    Memprediksi harga rumah berdasarkan fitur properti dan lokasi
    Membandingkan performa model baseline dan model hasil tuning
    Menguji kemampuan generalisasi model menggunakan data uji eksternal
    Menyediakan aplikasi prediksi interaktif menggunakan Streamlit

🔹 Fitur
    Menggunakan 8 fitur terpilih hasil feature selection:
    (kt, km, luas_bangunan, luas_tanah, total_rooms, kepadatan_kamar, bangunan_log, lokasi)
    Fitur lokasi disesuaikan agar konsisten antara data training dan data uji eksternal

🔹 Model
    Baseline SVR (tanpa cross-validation)
    Grid Search CV (CV = 3, 5, 10)
    Random Search CV (CV = 3, 5, 10)
    Bayesian Optimization (CV = 3, 5, 10)

📊 Evaluasi Model
    Setiap model dievaluasi menggunakan:
    R² (Coefficient of Determination)
    Mean Squared Error (MSE)
    Root Mean Squared Error (RMSE)
    Waktu komputasi

🧪 Uji Data Eksternal
    Dataset: DATA_UJI_EKSTERNAL.csv
    Menggunakan alur preprocessing yang sama persis dengan data training
    Digunakan untuk menguji generalisasi model terhadap data baru

🖥️ Aplikasi Streamlit
    Aplikasi prediksi harga rumah dibuat menggunakan Streamlit (app.py)
    Fitur aplikasi:
    Input fitur rumah secara interaktif
    Prediksi harga rumah berdasarkan model
    Output harga dalam format yang mudah dibaca.

▶️ Menjalankan aplikasi:
    pip install -r requirements.txt
    streamlit run app.py

🎥 Rekaman Aplikasi (Streamlit App Record)
    Rekaman penggunaan aplikasi Streamlit tersedia sebagai dokumentasi tambahan:
    📁 Streamlit App Record
    Berisi demo penggunaan aplikasi dan hasil prediksi
    File rekaman berupa screen record yang menunjukkan alur input hingga output prediksi.

📦 Library
    Beberapa library utama yang digunakan:
    pandas
    numpy
    scikit-learn
    optuna
    joblib
    streamlit

📝 Catatan
    Semua proses preprocessing pada data uji eksternal disamakan dengan data training
    Proyek ini dibuat untuk keperluan akademik 

Ulfa R
Prediksi Harga Rumah Menggunakan Support Vector Regression dengan hyperparameter tuning Grid Search, Random Search, dan Bayesian Optimization.
