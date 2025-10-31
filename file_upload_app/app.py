from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["UPLOAD_FOLDER"] = os.path.join("static", "uploads")
app.config["MAX_CONTENT_LENGTH"] = 500 * 1024  # 500 KB limit

db = SQLAlchemy(app)

# -------------------------
# Database Model
# -------------------------
class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255))
    status = db.Column(db.String(20), default="pending")  # pending/saved

with app.app_context():
    db.create_all()

# -------------------------
# Routes
# -------------------------
@app.route("/")
def index():
    """Render upload page."""
    return render_template("index.html")

@app.route("/get_files", methods=["GET"])
def get_files():
    """Return all uploaded files (for page refresh)"""
    docs = Document.query.all()
    files = [{"id": d.id, "filename": d.filename, "status": d.status} for d in docs]
    return jsonify(files)

@app.route("/upload", methods=["POST"])
def upload_file():
    """Upload a single file (one-by-one)"""
    file = request.files.get("file")

    if not file or file.filename == "":
        return jsonify({"error": "No file uploaded"}), 400

    # Check file size
    file.seek(0, os.SEEK_END)
    size = file.tell()
    file.seek(0)
    if size > 500 * 1024:
        return jsonify({"error": "File exceeds 500KB limit"}), 400

    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
    path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(path)

    new_doc = Document(filename=file.filename)
    db.session.add(new_doc)
    db.session.commit()

    return jsonify({"message": "File uploaded", "id": new_doc.id, "filename": new_doc.filename})

@app.route("/remove/<int:file_id>", methods=["DELETE"])
def remove_file(file_id):
    """Remove a specific uploaded file"""
    doc = Document.query.get(file_id)
    if not doc:
        return jsonify({"error": "File not found"}), 404

    try:
        os.remove(os.path.join(app.config["UPLOAD_FOLDER"], doc.filename))
    except FileNotFoundError:
        pass

    db.session.delete(doc)
    db.session.commit()
    return jsonify({"message": f"File '{doc.filename}' removed successfully"})

@app.route("/submit", methods=["POST"])
def submit_all():
    """Mark all files as saved"""
    docs = Document.query.all()
    for doc in docs:
        doc.status = "saved"
    db.session.commit()
    return jsonify({"message": "All files marked as saved on server"})

@app.route("/cancel", methods=["POST"])
def cancel_upload():
    """Cancel all uploads and delete files"""
    docs = Document.query.all()
    for doc in docs:
        try:
            os.remove(os.path.join(app.config["UPLOAD_FOLDER"], doc.filename))
        except FileNotFoundError:
            pass
        db.session.delete(doc)
    db.session.commit()
    return jsonify({"message": "All uploaded files removed (cancelled)"})

# -------------------------
# Run App
# -------------------------
if __name__ == "__main__":
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
    app.run(debug=True)
