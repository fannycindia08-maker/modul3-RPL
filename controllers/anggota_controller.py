
import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView


class AnggotaController:
    def __init__(self):ds
        self.model = AnggotaModel()
        self.view = AnggotaView()

        # Binding tombol
        self.view.btn_simpan.configure(
            command=self.simpan_data
        )
        self.view.btn_update.configure(
            command=self.update_data
        )
        self.view.btn_delete.configure(
            command=self.hapus_data
        )

        # Mengisi form saat baris tabel diklik
        self.view.tabel.bind(
            "<<TreeviewSelect>>",
            self.pilih_anggota
        )

        # Muat data saat aplikasi dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_anggota = self.model.get_all_anggota()

        for anggota in data_anggota:
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    anggota["id_anggota"],
                    anggota["nama_anggota"],
                    anggota["alamat"]
                )
            )

    def pilih_anggota(self, event=None):
        pilihan = self.view.tabel.selection()

        if not pilihan:
            return

        data = self.view.tabel.item(
            pilihan[0], "values"
        )

        self.bersihkan_form()

        self.view.entry_nama.insert(0, data[1])
        self.view.entry_alamat.insert(0, data[2])

    def ambil_id_anggota(self):
        pilihan = self.view.tabel.selection()

        if not pilihan:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data anggota terlebih dahulu!"
            )
            return None

        data = self.view.tabel.item(
            pilihan[0], "values"
        )

        return data[0]

    def simpan_data(self):
        nama = self.view.entry_nama.get().strip()
        alamat = self.view.entry_alamat.get().strip()

        if not nama or not alamat:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!"
            )
            return

        # Sesuaikan dengan nama method di AnggotaModel
        berhasil = self.model.tambah_anggota(
            nama, alamat
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data anggota berhasil disimpan!"
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Data anggota gagal disimpan."
            )

    def update_data(self):
        id_anggota = self.ambil_id_anggota()

        if id_anggota is None:
            return

        nama = self.view.entry_nama.get().strip()
        alamat = self.view.entry_alamat.get().strip()

        if not nama or not alamat:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!"
            )
            return

        # Sesuaikan dengan method di AnggotaModel
        berhasil = self.model.update_anggota(
            id_anggota, nama, alamat
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data anggota berhasil diperbarui!"
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Data anggota gagal diperbarui."
            )

    def hapus_data(self):
        id_anggota = self.ambil_id_anggota()

        if id_anggota is None:
            return

        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            "Apakah kamu yakin ingin menghapus anggota ini?"
        )

        if not konfirmasi:
            return

        # Sesuaikan dengan method di AnggotaModel
        berhasil = self.model.hapus_anggota(
            id_anggota
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data anggota berhasil dihapus!"
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Data anggota gagal dihapus."
            )

    def bersihkan_form(self):
        self.view.entry_nama.delete(0, "end")
        self.view.entry_alamat.delete(0, "end")

    def run(self):
        self.view.mainloop()
