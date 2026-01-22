from flask import Blueprint, render_template, request, redirect, url_for
from application.materi_use_case import MateriUseCase
from werkzeug.utils import secure_filename
import os

materi_bp = Blueprint("materi", __name__, url_prefix="/")

materi_uc = MateriUseCase()
UPLOAD_FOLDER = "flask_app/static/uploads/materi"


@materi_bp.route("/")
def dashboard_dosen():
    materi_list = materi_uc.list_materi()
    return render_template("materi/dosen/dashboard.html", materi_list=materi_list)


@materi_bp.route("/dosen/tambah")
def form_tambah_materi():
    return render_template("materi/dosen/tambah_materi.html")


@materi_bp.route("/dosen/simpan", methods=["POST"])
def simpan_materi():
    judul = request.form.get("judul")
    deskripsi = request.form.get("deskripsi")

    file = request.files.get("file")
    filename = None

    if file and file.filename:
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        file_path = f"uploads/materi/{filename}"
    else:
        file_path = None

    materi_uc.tambah_materi(
        judul=judul,
        deskripsi=deskripsi,
        file_path=file_path
    )

    return redirect(url_for("materi.dashboard_dosen"))

@materi_bp.route("/dosen/hapus/<int:materi_id>")
def hapus_materi(materi_id):
    materi_uc.hapus_materi(materi_id)
    return redirect(url_for("materi.dashboard_dosen"))


@materi_bp.route("/mahasiswa")
def dashboard_mahasiswa():
    materi_list = materi_uc.list_materi()
    return render_template("materi/mahasiswa/dashboard.html", materi_list=materi_list)
