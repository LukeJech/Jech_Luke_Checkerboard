from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def set_board():
    return render_template("index.html", columns=4, rows =8, color1="red", color2="black", )

@app.route('/<int:rows>')
def set_board_rows(rows):
    return render_template("index.html", columns=4, rows =rows, color1="red", color2="black", )

@app.route('/<int:rows>/<int:columns>')
def set_board_rows_columns(rows, columns):
    return render_template("index.html", columns=columns, rows =rows, color1="red", color2="black", )

@app.route('/<int:rows>/<int:columns>/<color1>/<color2>')
def set_board_colors(rows, columns, color1, color2):
    return render_template("index.html", columns=columns, rows =rows, color1=color1, color2=color2, )

if __name__ == "__main__":
    app.run(debug=True)