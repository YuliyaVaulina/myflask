from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import date
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv('.env')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('PG_USER')}:{os.getenv('PG_PASSWORD')}@127.0.0.1:5432/{os.getenv('PG_DATABASE')}"

db = SQLAlchemy(app)


class Advertisement(db.Model):
    __tablename__ = 'advertisements'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.Date, nullable=False)
    owner = db.Column(db.String(100), nullable=False)

    def __init__(self, title, description, date_created, owner):
        self.title = title
        self.description = description
        self.date_created = date_created
        self.owner = owner


# Создание базы данных и таблицы
with app.app_context():
    db.create_all()

# Получение всех объявлений
@app.route('/advertisements', methods=['GET'])
def get_advertisements():
    advertisements = Advertisement.query.all()
    results = [
        {
            'id': ad.id,
            'title': ad.title,
            'description': ad.description,
            'date_created': ad.date_created.strftime('%Y-%m-%d'),
            'owner': ad.owner
        }
        for ad in advertisements
    ]
    return jsonify(results)

# Получение объявления по идентификатору
@app.route('/advertisements/<int:ad_id>', methods=['GET'])
def get_advertisement(ad_id):
    ad = Advertisement.query.get(ad_id)
    if ad:
        result = {
            'id': ad.id,
            'title': ad.title,
            'description': ad.description,
            'date_created': ad.date_created.strftime('%Y-%m-%d'),
            'owner': ad.owner
        }
        return jsonify(result)
    else:
        return jsonify({'error': 'Объявление не найдено'}), 404

# Создание объявления
@app.route('/advertisements', methods=['POST'])
def create_advertisement():
    data = request.json
    title = data.get('title')
    description = data.get('description')
    date_created_str = data.get('date_created')
    owner = data.get('owner')

    # Преобразуем строку с датой в объект date
    date_created = date.fromisoformat(date_created_str)

    ad = Advertisement(title=title, description=description, date_created=date_created, owner=owner)
    db.session.add(ad)
    db.session.commit()

    return jsonify({
        'id': ad.id,
        'title': ad.title,
        'description': ad.description,
        'date_created': ad.date_created.strftime('%Y-%m-%d'),
        'owner': ad.owner
    }), 201


# Удаление объявления
@app.route('/advertisements/<int:ad_id>', methods=['DELETE'])
def delete_advertisement(ad_id):
    ad = Advertisement.query.get(ad_id)
    if ad:
        db.session.delete(ad)
        db.session.commit()
        return jsonify({'message': 'Объявление удалено'})
    else:
        return jsonify({'error': 'Объявление не найдено'}), 404


if __name__ == '__main__':
    app.run()
