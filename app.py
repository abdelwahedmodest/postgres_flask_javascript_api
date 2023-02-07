# >export FLASK_APP=flask_app.py
# >flask run




from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect("dbname=video_database user=postgres password=secret")
cur = conn.cursor()

@app.route("/videos", methods=["GET"])
def get_videos():
    cur.execute("SELECT name, path FROM videos")
    rows = cur.fetchall()
    videos = []
    for row in rows:
        videos.append({"name": row[0], "path": row[1]})
    return jsonify(videos)

if __name__ == "__main__":
    app.run()
