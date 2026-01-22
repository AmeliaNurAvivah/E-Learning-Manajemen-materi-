from abc import ABC, abstractmethod

class MateriRepository(ABC):

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def add(self, judul, deskripsi, file_path):
        pass

    @abstractmethod
    def get_by_id(self, materi_id):
        pass

    @abstractmethod
    def delete(self, materi_id):
        pass
