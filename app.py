import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("📋 Aplikasi To-Do List")

menu = ["Lihat Tugas", "Tambah Tugas", "Ubah Tugas", "Hapus Tugas"]
pilihan = st.sidebar.selectbox("Menu", menu)

if pilihan == "Lihat Tugas":
    try:
        r = requests.get(f"{API_URL}/tasks")
        if r.status_code == 200:
            tasks = r.json()
            if not tasks:  # Jika daftar tugas kosong
                st.warning("Belum ada tugas yang tersimpan.")
            else:
                st.write("## 📝 Daftar Tugas")
                for task in tasks:
                    with st.expander(f"🔹 {task['judul']} (ID: {task['id']})"):
                        st.write(f"**Deskripsi:** {task['deskripsi']}")
        else:
            st.error(f"Gagal memuat tugas. Kode status: {r.status_code}")
    except requests.exceptions.RequestException as e:
        st.error(f"Tidak dapat terhubung ke server: {e}")

elif pilihan == "Tambah Tugas":
    id = st.number_input("ID", min_value=1, step=1)
    judul = st.text_input("Judul")
    deskripsi = st.text_area("Deskripsi")
    if st.button("Tambah"):
        r = requests.post(f"{API_URL}/tasks", json={"id": id, "judul": judul, "deskripsi": deskripsi})
        st.success("Tugas berhasil ditambahkan!")

elif pilihan == "Ubah Tugas":
    id = st.number_input("ID Task yang akan diubah", min_value=1, step=1)
    judul = st.text_input("Judul Baru")
    deskripsi = st.text_area("Deskripsi Baru")
    if st.button("Perbarui"):
        r = requests.put(f"{API_URL}/tasks/{id}", json={"id": id, "judul": judul, "deskripsi": deskripsi})
        if r.status_code == 200:
            st.success("Tugas diperbarui!")
        else:
            st.error("Gagal memperbarui tugas!")

elif pilihan == "Hapus Tugas":
    id = st.number_input("ID Task yang akan dihapus", min_value=1, step=1)
    if st.button("Hapus"):
        r = requests.delete(f"{API_URL}/tasks/{id}")
        st.success("Tugas dihapus!")
