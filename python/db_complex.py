@app.route("/db")
def db():
    db = get_db()
    rows = db.execute("""
    SELECT
     points.id AS id,
     student.name AS student_name,
     course.title AS course_title,
     course.semester AS semester,
     points.value AS points
    FROM points
    INNER JOIN student ON points.id_student = student.id 
    INNER JOIN course ON points.id_course = course.id
    ORDER BY semester ASC, student_name ASC
    """).fetchall()
    return render_template("table.html.j2", rows=rows)

@app.route("/student/<student_id>/points")
def student_points(student_id):
    db = get_db()
    rows = db.execute("""
    SELECT
     points.id AS id,
     student.name AS student_name,
     course.title AS course_title,
     course.semester AS semester,
     points.value AS points
    FROM points
    INNER JOIN student ON points.id_student = student.id 
    INNER JOIN course ON points.id_course = course.id
    WHERE student.id = ?
    ORDER BY semester ASC, student_name ASC
    """, [student_id]).fetchall()
    return render_template("table.html.j2", rows=rows)
