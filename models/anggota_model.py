
from config.database import Database


class AnggotaModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "anggota"

    def get_all_anggota(self):
        if not self.conn:
            return []

        cursor = None
        try:
            cursor = self.conn.cursor(dictionary=True)
            query = """
                SELECT id_anggota, nama, alamat
                FROM anggota
                ORDER BY id_anggota ASC
            """
            cursor.execute(query)
            return cursor.fetchall()

        except Exception as e:
            print("Error mengambil data anggota:", e)
            return []

        finally:
            if cursor:
                cursor.close()

    def create_anggota(self, nama, alamat):
        if not self.conn:
            return False

        cursor = None
        try:
            cursor = self.conn.cursor()
            query = """
                INSERT INTO anggota (nama, alamat)
                VALUES (%s, %s)
            """
            cursor.execute(query, (nama, alamat))
            self.conn.commit()
            return True

        except Exception as e:
            self.conn.rollback()
            print("Error menambah anggota:", e)
            return False

        finally:
            if cursor:
                cursor.close()

    def update_anggota(self, id_anggota, nama, alamat):
        if not self.conn:
            return False

        cursor = None
        try:
            cursor = self.conn.cursor()
            query = """
                UPDATE anggota
                SET nama = %s, alamat = %s
                WHERE id_anggota = %s
            """
            cursor.execute(query, (nama, alamat, id_anggota))

            if cursor.rowcount == 0:
                cursor.execute(
                    "SELECT id_anggota FROM anggota WHERE id_anggota = %s",
                    (id_anggota,)
                )

                if not cursor.fetchone():
                    self.conn.rollback()
                    return False

            self.conn.commit()
            return True

        except Exception as e:
            self.conn.rollback()
            print("Error memperbarui anggota:", e)
            return False

        finally:
            if cursor:
                cursor.close()

    def delete_anggota(self, id_anggota):
        if not self.conn:
            return False

        cursor = None
        try:
            cursor = self.conn.cursor()
            query = """
                DELETE FROM anggota
                WHERE id_anggota = %s
            """
            cursor.execute(query, (id_anggota,))

            if cursor.rowcount == 0:
                self.conn.rollback()
                return False

            self.conn.commit()
            return True

        except Exception as e:
            self.conn.rollback()
            print("Error menghapus anggota:", e)
            return False

        finally:
            if cursor:
                cursor.close()
