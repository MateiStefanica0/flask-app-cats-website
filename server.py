from flask import Flask, request, render_template, redirect, session, flash, url_for, send_from_directory
import os
from werkzeug.utils import secure_filename
from PIL import Image

extensii = {'png', 'jpg', 'jpeg'}

app = Flask(__name__, static_folder="static")
app.secret_key = "cheiefoartesecretapisicifericite"

admins = {
    "admin": "admin123",
    "a": "a",
}


@app.route("/")
def index():
    folder_angry = 'static/angry'
    files_angry = os.listdir(folder_angry)
    thumb_files_angry = [element for element in files_angry if "thumb" in element]
    #happy
    folder_happy = 'static/happy'
    files_happy = os.listdir(folder_happy)
    thumb_files_happy = [element for element in files_happy if "thumb" in element]
    #lazy
    folder_lazy = 'static/lazy'
    files_lazy = os.listdir(folder_lazy)
    thumb_files_lazy = [element for element in files_lazy if "thumb" in element]
    #sad
    folder_sad = 'static/sad'
    files_sad = os.listdir(folder_sad)
    thumb_files_sad = [element for element in files_sad if "thumb" in element]
    return render_template('index.html', files_angry=thumb_files_angry, files_happy=thumb_files_happy, files_lazy=thumb_files_lazy, files_sad=thumb_files_sad)

@app.route("/about")
def about():
    return render_template("/about.html")

@app.route('/uploads/angry/<name>')
def download_file_angry(name):
    return send_from_directory(app.config["folder_angry"], name)

@app.route('/uploads/happy/<name>')
def download_file_happy(name):
    return send_from_directory(app.config["folder_happy"], name)

@app.route('/uploads/lazy/<name>')
def download_file_lazy(name):
    return send_from_directory(app.config["folder_lazy"], name)

@app.route('/uploads/sad/<name>')
def download_file_sad(name):
    return send_from_directory(app.config["folder_sad"], name)


@app.route("/login", methods=["GET", "POST"])
def login():
    error_msg = "Login failed"
    username = request.form.get("username", "")
    password = request.form.get("password", "")
    if username in admins and password==admins[username]:
        session["username"] = username
        session["auth"] = True
        return redirect("/index_logged", code=302)
    return render_template("login.html", error=error_msg)


@app.route("/index_logged")
def index_logged():
    # angry
    folder_angry = 'static/angry'
    files_angry = os.listdir(folder_angry)
    thumb_files_angry = [element for element in files_angry if "thumb" in element]
    #happy
    folder_happy = 'static/happy'
    files_happy = os.listdir(folder_happy)
    thumb_files_happy = [element for element in files_happy if "thumb" in element]
    #lazy
    folder_lazy = 'static/lazy'
    files_lazy = os.listdir(folder_lazy)
    thumb_files_lazy = [element for element in files_lazy if "thumb" in element]
    #sad
    folder_sad = 'static/sad'
    files_sad = os.listdir(folder_sad)
    thumb_files_sad = [element for element in files_sad if "thumb" in element]
    return render_template('index_logged.html', files_angry=thumb_files_angry, files_happy=thumb_files_happy, files_lazy=thumb_files_lazy, files_sad=thumb_files_sad)


@app.route("/view_photo_angry/<filename>")
def view_photo_angry(filename): #ruta este cu thumb, dar imaginea afisata nu
    folder = os.path.join(app.root_path, 'static', 'angry')
    filename, extension = filename.rsplit('.', 1)
    filename, discard = filename.rsplit('.', 1)
    filename = filename + '.' + extension
    return send_from_directory(folder, filename)

@app.route("/view_photo_happy/<filename>")
def view_photo_happy(filename): #ruta este cu thumb, dar imaginea afisata nu
    folder = os.path.join(app.root_path, 'static', 'happy')
    filename, extension = filename.rsplit('.', 1)
    filename, discard = filename.rsplit('.', 1)
    filename = filename + '.' + extension
    return send_from_directory(folder, filename)

@app.route("/view_photo_lazy/<filename>")
def view_photo_lazy(filename): #ruta este cu thumb, dar imaginea afisata nu
    folder = os.path.join(app.root_path, 'static', 'lazy')
    filename, extension = filename.rsplit('.', 1)
    filename, discard = filename.rsplit('.', 1)
    filename = filename + '.' + extension
    return send_from_directory(folder, filename)

@app.route("/view_photo_sad/<filename>")
def view_photo_sad(filename): #ruta este cu thumb, dar imaginea afisata nu
    folder = os.path.join(app.root_path, 'static', 'sad')
    filename, extension = filename.rsplit('.', 1)
    filename, discard = filename.rsplit('.', 1)
    filename = filename + '.' + extension
    return send_from_directory(folder, filename)


@app.route("/upload")
def upload():
    return render_template("/upload.html")
    
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in extensii

@app.route("/upload_logged", methods=['GET', 'POST'])
def upload_logged():
    if request.method == 'POST':
        # adaugat de mine
        name = request.form.get("name", "")
        category = request.form.get("category", "")
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            base_name, extension = filename.rsplit('.', 1)
            filename = name + '.' + extension
            thumbnail_name = name + '.thumb.' + extension
            if category == '1':
                folder_angry = 'static/angry'
                app.config['folder_angry'] = folder_angry
                file.save(os.path.join(app.config['folder_angry'], filename))
                #creare thumbnail
                path = 'static/angry/' + filename
                thmb = Image.open(path)
                size = (200, 200)
                thmb.thumbnail(size)
                thmb.save(os.path.join(app.config['folder_angry'], thumbnail_name))
            if category == '2':
                folder_happy = 'static/happy'
                app.config['folder_happy'] = folder_happy
                file.save(os.path.join(app.config['folder_happy'], filename))
                #creare thumbnail
                path = 'static/happy/' + filename
                thmb = Image.open(path)
                size = (200, 200)
                thmb.thumbnail(size)
                thmb.save(os.path.join(app.config['folder_happy'], thumbnail_name))
            if category == '3':
                folder_lazy = 'static/lazy'
                app.config['folder_lazy'] = folder_lazy
                file.save(os.path.join(app.config['folder_lazy'], filename))
                #creare thumbnail
                path = 'static/lazy/' + filename
                thmb = Image.open(path)
                size = (200, 200)
                thmb.thumbnail(size)
                thmb.save(os.path.join(app.config['folder_lazy'], thumbnail_name))
            if category == '4':
                folder_sad = 'static/sad'
                app.config['folder_sad'] = folder_sad
                file.save(os.path.join(app.config['folder_sad'], filename))
                #creare thumbnail
                path = 'static/sad/' + filename
                thmb = Image.open(path)
                size = (200, 200)
                thmb.thumbnail(size)
                thmb.save(os.path.join(app.config['folder_sad'], thumbnail_name))
    return render_template("/upload_logged.html")

@app.route("/about_logged")
def about_logged():
    return render_template("/about_logged.html")

@app.route("/logout")
def logout():
    session["authenticated"] = False
    return redirect("/login")

@app.errorhandler(404)
def error404(code):
    return "HTTP Error 404 - Page Not Found"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)