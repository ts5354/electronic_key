from flask import Flask, request, jsonify , render_template
from flask_sqlalchemy import SQLAlchemy
import datetime
import datetime
from flask_cors import CORS
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)
CORS(
    app,
    supports_credentials=True
)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://your_username:your_password@db/your_database_name"

db = SQLAlchemy(app)
# PostgreSQLへの接続情報
class return_name(db.Model):
    __tablename__ = 'return_names'
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(255))
    date=db.Column(db.String(255))
    time=db.Column(db.String(255))


# データベースに接続する関数


# データベースにデータを挿入する関数

# データベースからデータを取得する関数

@app.route('/add_data', methods=['POST'])#アプリ内における特定の操作によって実行される
def add_data():
    data = request.json 
    print(type(data), data)
    name = data.get("name") 
    date=data.get("date")
    time=data.get("time")
    if 'name' not in data:
            return jsonify({'error': 'Name field is required'}), 400
    new_user = return_name(name=name,date=date,time=time)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"id": new_user.id, "name": new_user.name, "date": new_user.date, "time": new_user.time})

@app.route('/return_data', methods=['GET'])
def get_points():
    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')  # UTCから9時間差の「JST」タイムゾーン
    dt = datetime.datetime.now(JST)  
    d_today = dt.date()

    print(d_today,flush=True)
    points = return_name.query.filter_by(date=str(d_today)).all()
    print(points,flush=True)
    if not points:
        # 今日のデータが見つからない場合
        return jsonify({"error": "No data found for today."}), 404

    # 最初のデータを返す例（要件に応じて調整してください）
    points_list=[{"id": point.id, "name": point.name, "date": point.date, "time": point.time} for point in points]
    return jsonify(points_list)


with app.app_context():
    db.create_all()
if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=5001)