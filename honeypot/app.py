from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)
LOG_FILE = "honeypot_log.txt"


def log_attempt(username, password):
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user_agent = request.headers.get('User-Agent', 'unknown')
    entry = f"[{timestamp}] IP={ip} | username='{username}' | password='{password}' | agent='{user_agent}'\n"
    with open(LOG_FILE, "a") as f:
        f.write(entry)
    print("HONEYPOT ALERT:", entry.strip())


@app.route("/admin", methods=["GET", "POST"])
def fake_admin():
    message = ""
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        log_attempt(username, password)
        message = "Invalid credentials. Please try again."
    return render_template("admin.html", message=message)


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
