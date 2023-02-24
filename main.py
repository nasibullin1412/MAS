from server.victim_server import app, user_db

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, use_reloader=True)
