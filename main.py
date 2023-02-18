from server.victim_server import app, user_db

if __name__ == "__main__":
    query = f"CREATE TABLE IF NOT EXISTS sql_assert(id integer primary key, request_id integer not null, value varchar not null);"
    user_db.execute(query)
    app.run(host="0.0.0.0", port=8080, use_reloader=True)

