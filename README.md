📝 To-Do List Application
Aplikasi ini adalah sistem manajemen tugas sederhana yang dibangun menggunakan FastAPI sebagai backend dan Streamlit sebagai frontend. Data disimpan secara lokal dalam file data.json.

📌 Deskripsi Proyek
Aplikasi ini memungkinkan pengguna untuk:

Melihat semua tugas yang tersimpan

Menambahkan tugas baru

Memperbarui detail tugas yang ada

Menghapus tugas

Semua fungsi tersebut dapat diakses melalui antarmuka pengguna berbasis web (Streamlit), yang berkomunikasi dengan backend FastAPI melalui HTTP API.

🗂️ Struktur Folder & File

.
├── app.py        # Frontend: Antarmuka pengguna dengan Streamlit
├── main.py       # Backend: REST API menggunakan FastAPI
├── data.json     # Penyimpanan data dalam format JSON
└── README.md     # Dokumentasi proyek

⚙️ Instalasi dan Menjalankan Aplikasi
1. Clone repositori (jika belum)
  git clone <URL-repo-anda>
  cd nama-folder-proyek

2. Buat dan aktifkan virtual environment (opsional tapi disarankan)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3.  Install semua dependensi
   pip install fastapi uvicorn streamlit requests pydantic

4.  Jalankan backend FastAPI
uvicorn main:app --reload

5. Jalankan frontend Streamlit
Buka terminal baru (jangan tutup yang menjalankan FastAPI), lalu jalankan:
streamlit run app.py
