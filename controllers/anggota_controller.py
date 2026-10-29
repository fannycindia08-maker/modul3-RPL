
import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView


class AnggotaController:
    def __init__(self):
        self.model = AnggotaModel()
        self.view = AnggotaView()

        # Hubungkan tombol dengan fungsi
        self.view.btn_simpan.configure(
            command=self.simpan_data
        )
        self.view.btn_update.configure(
            command=self.perbarui_data
        )
        self.view.btn_delete.configure(
            command=self.hapus_data
        )

        # Event ketika baris tabel dipilih
        self.view.tabel.bind(
            "<<TreeviewSelect>>",
            self.isi_form_dari_tabel
        )

        # Tampilkan data saat program dibuka
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
                    anggota["nama"],
                    anggota["alamat"] or ""
                )
            )

    def bersihkan_form(self):
        self.view.entry_nama.delete(0, "end")
        self.view.entry_alamat.delete(0, "end")

        for item in self.view.tabel.selection():
            self.view.tabel.selection_remove(item)

    def get_id_terpilih(self):
        pilihan = self.view.tabel.selection()

        if not pilihan:
            messagebox.showwarning(
                "Peringatan",
                "Pilih baris anggota di tabel terlebih dahulu!"
            )
            return None

        values = self.view.tabel.item(
            pilihan[0], "values"
        )

        if not values:
            return None

        return values[0]

    def isi_form_dari_tabel(self, event=None):
        pilihan = self.view.tabel.selection()

        if not pilihan:
            return

        values = self.view.tabel.item(
            pilihan[0], "values"
        )

        if len(values) < 3:
            return

        _, nama, alamat = values

        self.view.entry_nama.delete(0, "end")
        self.view.entry_nama.insert(0, nama)

        self.view.entry_alamat.delete(0, "end")
        self.view.entry_alamat.insert(0, alamat)

    def simpan_data(self):
        nama = self.view.entry_nama.get().strip()
        alamat = self.view.entry_alamat.get().strip()

        if not nama or not alamat:
            messagebox.showwarning(
                "Peringatan",
                "Nama dan alamat wajib diisi!"
            )
            return

        if self.model.create_anggota(nama, alamat):
            messagebox.showinfo(
                "Sukses",
                "Data anggota berhasil disimpan!"
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Data gagal disimpan. Periksa pesan error di terminal."
            )

    def perbarui_data(self):
        id_anggota = self.get_id_terpilih()

        if id_anggota is None:
            return

        nama = self.view.entry_nama.get().strip()
        alamat = self.view.entry_alamat.get().strip()

        if not nama or not alamat:
            messagebox.showwarning(
                "Peringatan",
                "Nama dan alamat wajib diisi!"
            )
            return

        if self.model.update_anggota(
            id_anggota, nama, alamat
        ):
            messagebox.showinfo(
                "Sukses",
                "Data anggota berhasil diperbarui!"
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Data gagal diperbarui. Periksa pesan error di terminal."
            )

    def hapus_data(self):
        id_anggota = self.get_id_terpilih()

        if id_anggota is None:
            return

        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            "Yakin ingin menghapus data anggota ini?"
        )

        if not konfirmasi:
            return

        if self.model.delete_anggota(id_anggota):
            messagebox.showinfo(
                "Sukses",
                "Data anggota berhasil dihapus!"
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Data gagal dihapus. Periksa pesan error di terminal."
            )

    def run(self):
        self.view.mainloop()


if __name__ == "__main__":
    app = AnggotaController()
    app.run()
