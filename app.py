from flask import Flask, render_template, request, send_file
import pandas as pd
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
PROCESSED_FOLDER = "processed"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return "Brak pliku", 400

        file = request.files["file"]
        option = request.form.get("option")

        if file.filename == "" or not option:
            return "Wybierz plik i opcję", 400

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        df = pd.read_excel(file_path)

        # Przekształcenia
        if option == "1":
            df = df.head(10)
        elif option == "2":
            df = df.sort_values(by=df.columns[0])
        elif option == "3":
            df = df.fillna(0)
        elif option == "4":
            df = df.iloc[::-1]
        elif option == "5":
            df = df.drop_duplicates()

        output_path = os.path.join(PROCESSED_FOLDER, "processed_" + file.filename)
        df.to_excel(output_path, index=False)

        return send_file(output_path, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
