from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hello')
def hello():
    return "Hello C$E 15"

@app.route("/tuan/<name>")
def hello_tuan(name):
    return "Hi " + name

@app.route("/sum/<int:x>/<int:y>")
def sum(x, y):
    return str(x + y)

@app.route("/html")
def heading():
    return "<h1>Gì cũng được<h1>"

@app.route("/blog")
def blog():
    article_name = "Thơ con cóc"
    posts = [
        {
        "content": "Phấn khởi",
        "author": "Nguyên"
        },
        {
        "content": "Táo bao tử",
        "author": "Tuấn"
        },
        {
        "content": "Tứ bao tải",
        "author": "A"}
    ]
    return render_template("blog.html",
        article_title=article_name,
        posts=posts)


@app.route("/user/<name>")
def profile(name):
    users = [
    {
    "user_name": "tuan",
    "tuoi": "30",
    "gioi_tinh": "Nam"
    },
    {
    "user_name": "a",
    "tuoi": "28",
    "gioi_tinh": "Nu"
    }
    ]
    if name == users["user_name"]:
        return render_template("profile.html", users=users)
    else:
        return "not found"

if __name__ == '__main__':
  app.run(debug=True)
