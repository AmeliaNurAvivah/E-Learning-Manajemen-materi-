from infrastructure.sqlite_db.db_settings import get_connection
from domain.entities.entities import Materi

class MateriRepositoryImpl:

    def get_all(self):
        conn = get_connection()
        rows = conn.execute("""
            SELECT * FROM materi ORDER BY tanggal_upload DESC
        """).fetchall()
        conn.close()

        return [
            Materi(
                id=r["id"],
                judul=r["judul"],
                deskripsi=r["deskripsi"],
                file_path=r["file_path"]
             )
            for r in rows
        ]

    def add(self, judul, deskripsi, file_path):
        conn = get_connection()
        conn.execute("""
            INSERT INTO materi (judul, deskripsi, file_path)
            VALUES (?, ?, ?)
        """, (judul, deskripsi, file_path))
        conn.commit()
        conn.close()

    def get_by_id(self, materi_id):
        conn = get_connection()
        r = conn.execute("""
            SELECT * FROM materi WHERE id = ?
        """, (materi_id,)).fetchone()
        conn.close()

        if not r:
            return None

        return Materi(
            id=r["id"],
            judul=r["judul"],
            deskripsi=r["deskripsi"],
            file_path=r["file_path"]
           
        )

    def delete(self, materi_id):
        conn = get_connection()
        conn.execute("DELETE FROM materi WHERE id = ?", (materi_id,))
        conn.commit()
        conn.close()
