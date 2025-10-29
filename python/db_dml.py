def insert():
    db = get_db()
    db.execute("INSERT INTO messages (author, content) VALUES (?, ?)", (author, content))
    db.commit()

def select():
    db = get_db()
    rows = db.execute("SELECT author, content FROM messages").fetchall()
    return rows

def update():
    db = get_db()
    db.execute("UPDATE messages SET content = ? WHERE id = ?", (new_text, msg_id))
    db.commit()

def delete():
    db = get_db()
    db.execute("DELETE FROM messages WHERE id = ?", (msg_id))
    db.commit()
