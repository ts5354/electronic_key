from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# PostgreSQLへの接続情報
db_config = {
    'dbname': 'key',
    'user': 'postgres',
    'password': 'lucky0408',
    'host': 'localhost',
    'port': '5432'
}

# データベースに接続する関数
def connect_to_database():
    conn = psycopg2.connect(**db_config)
    return conn

# データベースにデータを挿入する関数
def insert_data(data):
    conn = connect_to_database()
    cur = conn.cursor()
    # テーブルにデータを挿入するSQLクエリ
    insert_query = "INSERT INTO test_table (name) VALUES (%s)"
    cur.execute(insert_query, (data['name'],))  # データをタプルとして渡す
    conn.commit()
    conn.close()

@app.route('/add_data', methods=['POST'])
def add_data():
    data = request.json  # POSTリクエストからデータを取得
    if 'name' not in data:
        return jsonify({'error': 'Name field is required'}), 400
    insert_data(data)  # データを挿入
    return 'Data added successfully'

if __name__ == '__main__':
    app.run(debug=True)
