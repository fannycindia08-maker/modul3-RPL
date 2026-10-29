def handle_update_buku(self):
    # Mengambil baris yang sedang dipilih/disorot pada tabel
    selected_item = self.view.table.currentItem()
    if not selected_item:
        print("Pilih baris data buku yang ingin diperbarui!")
        return
    
    row = selected_item.row()
    # Mengambil ID dari kolom ke-0 (Kolom ID)
    id_buku = self.view.table.item(row, 0).text()
    
    # Mengambil inputan terbaru dari form di View
    judul = self.view.input_judul.text()     # Sesuaikan dengan nama variabel input judul Anda
    penulis = self.view.input_penulis.text() # Sesuaikan dengan nama variabel input penulis Anda
    tahun = self.view.input_tahun.text()     # Sesuaikan jika ada input tahun
    
    # Kirim data ke model untuk melakukan update ke database
    try:
        self.model.update_buku(id_buku, judul, penulis, tahun)
        print("Data buku berhasil diperbarui!")
        self.load_data() # Memuat ulang tabel agar data terbaru langsung tampil
    except Exception as e:
        print(f"Error saat update: {e}")