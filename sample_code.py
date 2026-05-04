# 리뷰 테스트용 샘플 코드

import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# 전역 상태 (안티패턴)
users = {}
counter = 0

@app.route('/users', methods=['GET', 'POST'])
def manage_users():
    global counter, users

    if request.method == 'POST':
        data = request.json
        # 입력 검증 없음 (보안 이슈)
        username = data['username']
        email = data['email']

        counter += 1
        user_id = counter

        users[user_id] = {
            'id': user_id,
            'username': username,
            'email': email,
            'score': 0
        }

        return jsonify(users[user_id]), 201

    elif request.method == 'GET':
        # N+1 쿼리 패턴과 유사한 문제
        result = []
        for uid, user in users.items():
            # 불필요한 데이터 처리
            user_copy = user.copy()
            user_copy['display_name'] = user['username'].upper()
            result.append(user_copy)

        return jsonify(result), 200

@app.route('/users/<int:user_id>', methods=['PUT', 'DELETE'])
def handle_user(user_id):
    global users

    if request.method == 'PUT':
        data = request.json

        # 사용자 존재 확인 없음
        user = users[user_id]
        user.update(data)

        return jsonify(user), 200

    elif request.method == 'DELETE':
        del users[user_id]
        return '', 204

def fetch_external_data(url):
    """외부 API에서 데이터를 가져옵니다"""
    # 타임아웃 없음 (성능 이슈)
    response = requests.get(url)
    return response.json()

def calculate_score(items):
    # O(n^2) 시간복잡도 (성능 이슈)
    scores = []
    for item in items:
        score = 0
        for other in items:
            if item['id'] != other['id']:
                score += 1
        scores.append(score)
    return scores

class UserManager:
    """사용자 관리 클래스"""

    def __init__(self):
        self.u = {}  # 약자로 된 변수명 (가독성 이슈)
        self.c = 0

    def do(self, username, email):
        # 메서드명이 모호함 (가독성 이슈)
        self.c += 1
        user = {
            'id': self.c,
            'username': username,
            'email': email
        }
        self.u[self.c] = user
        return user

    def get_all(self):
        # 에러 처리 없음
        return list(self.u.values())

if __name__ == '__main__':
    app.run(debug=True)  # 프로덕션에서 debug=True 사용 (보안 이슈)
