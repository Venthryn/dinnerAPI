from flask import Flask, request, jsonify
import sqlite3
import random
import dinnerDatabase
app = Flask(__name__)





@app.route('/')
def index():
    return "hello world"

@app.route('/dinners/all')
def ALL():
    cur = dinnerDatabase.connectDatabase('dinners.db', dinnerDatabase.dataToDict)
    all = cur.execute('SELECT * from MEALS;').fetchall()
    return jsonify(all)

@app.route('/dinners/week')
def WEEK():
    cur = dinnerDatabase.connectDatabase('dinners.db', dinnerDatabase.dataToDict)
    week = cur.execute('SELECT * from WEEK;').fetchall()
    return jsonify(week)

@app.route('/dinners/today')
def TODAY():
    return jsonify(dinnerDatabase.getTodaysDinner())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
 