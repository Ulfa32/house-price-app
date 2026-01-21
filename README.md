Aplikasi Prediksi Harga Rumah di Kota Bandung<br>
Proyek machine learning untuk prediksi harga rumah menggunakan Support Vector Regression (SVR) dengan hyperparameter tuning Grid Search, Random Search, dan Bayesian Optimization.<br>
Proyek ini mencakup proses preprocessing data, pelatihan model, hyperparameter tuning, uji data eksternal, serta aplikasi prediksi berbasis Streamlit.<br>

📂 Struktur Proyek<br>
    house-price-app/<br>
    │<br>
    ├── .devcontainer/              # Konfigurasi development container<br>
    ├── Code Colab/                 # Notebook Google Colab (ipynb & py)<br>
    ├── models/                     # Model hasil <br>
    │<br>
    ├── DATA_UJI_EKSTERNAL.csv      # Dataset uji eksternal<br>
    ├── wilayah_all.csv             # Data wilayah/lokasi kecamatan di Kota Bandung<br>
    │<br>
    ├── app.py                      # Aplikasi prediksi (Streamlit)<br>
    ├── requirements.txt            # Daftar library Python<br>
    └── README.md<br>
<br>
🎯 Tujuan Proyek<br>
    Memprediksi harga rumah berdasarkan fitur properti dan lokasi<br>
    Membandingkan performa model baseline dan model hasil tuning<br>
    Menguji kemampuan generalisasi model menggunakan data uji eksternal<br>
    Menyediakan aplikasi prediksi interaktif menggunakan Streamlit<br>
<br>
🔹 Fitur<br>
    Menggunakan 8 fitur terpilih hasil feature selection:<br>
    (kt, km, luas_bangunan, luas_tanah, total_rooms, kepadatan_kamar, bangunan_log, lokasi)<br>
    Fitur lokasi disesuaikan agar konsisten antara data training dan data uji eksternal<br>
<br>
🔹 Model<br>
    Baseline SVR (tanpa cross-validation)<br>
    Grid Search CV (CV = 3, 5, 10)<br>
    Random Search CV (CV = 3, 5, 10)<br>
    Bayesian Optimization (CV = 3, 5, 10)<br>
<br>
📊 Evaluasi Model<br>
    Setiap model dievaluasi menggunakan:<br>
    R² (Coefficient of Determination)<br>
    Mean Squared Error (MSE)<br>
    Root Mean Squared Error (RMSE)<br>
    Waktu komputasi<br>
<br>
🧪 Uji Data Eksternal<br>
    Dataset: DATA_UJI_EKSTERNAL.csv<br>
    Menggunakan alur preprocessing yang sama persis dengan data training<br>
    Digunakan untuk menguji generalisasi model terhadap data baru<br>
<br>
🖥️ Aplikasi Streamlit<br>
    Aplikasi prediksi harga rumah dibuat menggunakan Streamlit (app.py)<br>
    Fitur aplikasi:<br>
    Input fitur rumah secara interaktif<br>
    Prediksi harga rumah berdasarkan model<br>
    Output harga dalam format yang mudah dibaca.<br>
<br>
▶️ Menjalankan aplikasi:<br>
    pip install -r requirements.txt<br>
    streamlit run app.py<br>
<br>
🎥 Rekaman Aplikasi (Streamlit App Record)<br>
    Rekaman penggunaan aplikasi Streamlit tersedia sebagai dokumentasi tambahan:<br>
    📁 Streamlit App Record<br>
    Berisi demo penggunaan aplikasi dan hasil prediksi<br>
    File rekaman berupa screen record yang menunjukkan alur input hingga output prediksi.<br>
<br>
📦 Library<br>
    Beberapa library utama yang digunakan:<br>
    pandas<br>
    numpy<br>
    scikit-learn<br>
    optuna<br>
    joblib<br>
    streamlit<br>
<br>
📝 Catatan<br>
    Semua proses preprocessing pada data uji eksternal disamakan dengan data training<br>
    Proyek ini dibuat untuk keperluan akademik <br>
<br>
Ulfa R<br>
Prediksi Harga Rumah Menggunakan Support Vector Regression dengan hyperparameter tuning Grid Search, Random Search, dan Bayesian Optimization.
