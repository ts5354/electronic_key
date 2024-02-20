from flask import Flask, request, jsonify , render_template
import psycopg2

app = Flask(__name__)

# PostgreSQLへの接続情報
db_config = {
    'dbname': 'your_database_name',
    'user': 'your_username',
    'password': 'your_password',
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

# データベースからデータを取得する関数
def get_data_from_database():
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()
    cur.execute("SELECT * FROM your_table_name")
    data = cur.fetchall()
    conn.close()
    return data

@app.route('/add_data', methods=['POST'])#アプリ内における特定の操作によって実行される
def add_data():
    data = request.json  # POSTリクエストからデータを取得
    if 'name' not in data:
        return jsonify({'error': 'Name field is required'}), 400
    insert_data(data)  # データを挿入
    return 'Data added successfully'

@app.route('/')#アプリ内における特定の操作によって実行される
def index():
    # データベースからデータを取得
    data = get_data_from_database()
    # テンプレートにデータを渡してレンダリング
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
