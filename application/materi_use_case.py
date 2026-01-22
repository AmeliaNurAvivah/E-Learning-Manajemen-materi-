from .services.id_generator_services import generate_id
from datetime import datetime
from domain.repositories.materi_repository import MateriRepository
from infrastructure.services.materi_repository_impl import MateriRepositoryImpl

class MateriUseCase:
    def __init__(self):
        self.repo: MateriRepository = MateriRepositoryImpl()

    def list_materi(self):
        return self.repo.get_all()

    def tambah_materi(self, judul, deskripsi, file_path):
        self.repo.add(judul, deskripsi, file_path)

    def hapus_materi(self, materi_id):
        self.repo.delete(materi_id)

