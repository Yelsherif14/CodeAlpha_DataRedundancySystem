from flask import Flask, render_template, request
from database.db import get_connection, init_db
import re

app = Flask(__name__)

init_db()


def is_valid_email(email):
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return re.match(pattern, email) is not None


@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    message_type = ""

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()

        # 1. Check empty fields
        if not name or not email:
            message = "❌ Name and email are required."
            message_type = "error"

        # 2. Check email format
        elif not is_valid_email(email):
            message = "❌ Please enter a valid email address."
            message_type = "error"

        else:
            connection = get_connection()

            # 3. Check if email already exists
            existing_user = connection.execute(
                "SELECT id FROM users WHERE email = ?",
                (email,)
            ).fetchone()

            if existing_user:
                message = "❌ Duplicate data! This email already exists."
                message_type = "error"

            else:
                # 4. Save unique data
                connection.execute(
                    "INSERT INTO users (name, email) VALUES (?, ?)",
                    (name, email)
                )

                connection.commit()

                message = "✅ Unique data added successfully."
                message_type = "success"

            connection.close()

    connection = get_connection()

    users = connection.execute(
        "SELECT id, name, email FROM users ORDER BY id DESC"
    ).fetchall()

    connection.close()

    return render_template(
        "index.html",
        message=message,
        message_type=message_type,
        users=users
    )


if __name__ == "__main__":
    app.run(debug=True)