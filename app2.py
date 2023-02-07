# install flask
pip install flask

# flask_app.py
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_videos():
    conn = psycopg2.connect(database="videos", user="video_user", password="password", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("SELECT video_id, video_name, video_path FROM videos")
    videos = cur.fetchall()
    cur.close()
    conn.close()
    return videos

@app.route("/videos", methods=["GET"])
def all_videos():
    videos = get_videos()
    return jsonify([{"video_id": vid, "video_name": vname, "video_path": vpath} for vid, vname, vpath in videos])

if __name__ == '__main__':
    app.run()
