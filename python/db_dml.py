def insert():
    db = get_db()
    cursor = db.execute("INSERT INTO messages (author, content) VALUES (?, ?)", (author, content))
    db.commit()
    return cursor.lastrowid

def select():
    db = get_db()
    rows = db.execute("SELECT author, content FROM messages").fetchall()
    return rows

def update():
    db = get_db()
    cursor = db.execute("UPDATE messages SET content = ? WHERE id = ?", (new_text, msg_id))
    db.commit()
    return cursor.rowcount

def delete():
    db = get_db()
    cursor = db.execute("DELETE FROM messages WHERE id = ?", (msg_id))
    db.commit()
    return cursor.rowcount
