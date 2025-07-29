📋 Aplikasi To-Do List
Aplikasi To-Do List sederhana yang dibangun dengan FastAPI (backend) dan Streamlit (frontend). Aplikasi ini memungkinkan pengguna untuk melihat, menambah, mengubah, dan menghapus tugas.

🛠️ Teknologi yang Digunakan
Backend: FastAPI

Frontend: Streamlit

Penyimpanan Data: JSON (data.json)

📂 Struktur Proyek
.
├── app.py          # Aplikasi Streamlit (frontend)
├── main.py         # Aplikasi FastAPI (backend)
├── data.json       # Database penyimpanan tugas
└── README.md       # Dokumentasi proyek

🚀 Cara Menjalankan Aplikasi
Pastikan Python terinstall (versi 3.7 atau lebih baru)

Install dependencies:
pip install fastapi uvicorn streamlit requests

Jalankan backend (FastAPI):
uvicorn main:app --reload
Backend akan berjalan di http://localhost:8000

Jalankan frontend (Streamlit) di terminal terpisah:
streamlit run app.py
Frontend akan terbuka di browser pada http://localhost:8501

🎯 Fitur Aplikasi
a. Lihat Tugas:

Menampilkan daftar semua tugas yang tersimpan

b. Tambah Tugas:

Menambahkan tugas baru dengan ID, judul, dan deskripsi

c. Ubah Tugas:

Memperbarui judul dan deskripsi tugas berdasarkan ID

d. Hapus Tugas:

Menghapus tugas berdasarkan ID
