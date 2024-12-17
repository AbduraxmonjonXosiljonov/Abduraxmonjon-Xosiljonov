from flask import Flask, render_template
import psycopg2

app = Flask(name)

DB_CONFIG = {
    "dbname": "postgres",  
    "user": "postgres",       
    "password": "postgres",  
    "host": "postgres.clwqowmk696o.eu-west-3.rds.amazonaws.com",
    "port": 5432
}

def get_courses():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        cur.execute("""
            SELECT course_name, year, start_date, title, instructor 
            FROM courses;
        """)
        courses = cur.fetchall()

        cur.close()
        conn.close()

        return courses
    except Exception as e:
        print(f"Error fetching courses: {e}")
        return []

@app.route('/')
def index():
    courses = get_courses()
    return render_template('index.html', courses=courses)

if name == 'main':
    app.run(debug=True, host='0.0.0.0', port=5000)
