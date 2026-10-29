def update_buku(self, id_buku, judul, penulis, tahun):
    query = "UPDATE buku SET judul = %s, penulis = %s, tahun = %s WHERE id = %s"
    values = (judul, penulis, tahun, id_buku)
    
    # Eksekusi query menggunakan kursor database Anda
    self.cursor.execute(query, values)
    self.db.commit()