from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from course_data import course_map, course_detail_map
from gemini_service import get_career_advice

app = Flask(__name__)
CORS(app)

# Normalize keys to avoid mismatch
normalized_course_map = {k.strip().lower(): v for k, v in course_map.items()}
normalized_course_detail_map = {k.strip().lower(): v for k, v in course_detail_map.items()}

# 🧭 Get list of courses based on subtopic
@app.route('/courses', methods=['GET'])
def get_courses():
    interest = request.args.get('interest', '').strip().lower()
    matched_courses = normalized_course_map.get(interest)
    if not matched_courses:
        return jsonify({"error": f"No courses found for interest '{interest}'"}), 404
    return jsonify(matched_courses), 200

# 📘 Get full course details including roadmap
@app.route('/course-details', methods=['GET'])
def get_course_details():
    name = request.args.get('name', '').strip().lower()
    details = normalized_course_detail_map.get(name)
    if not details:
        return jsonify({"error": f"Course '{name}' not found"}), 404
    return jsonify(details), 200

# 🗺️ Get only the roadmap section of a course
@app.route('/course-roadmap', methods=['GET'])
def get_course_roadmap():
    name = request.args.get('name', '').strip().lower()
    details = normalized_course_detail_map.get(name)
    if not details or 'roadmap' not in details:
        return jsonify({"error": f"Roadmap not available for '{name}'"}), 404
    return jsonify(details['roadmap']), 200

# 🧩 Get list of available categories (for dropdowns)
@app.route('/categories', methods=['GET'])
def get_categories():
    return jsonify([k.title() for k in normalized_course_map.keys()]), 200

# 🤖 Get dynamic career advice from Gemini
@app.route('/api/advise', methods=['POST'])
def advise():
    user_data = request.json
    required_keys = ['interests', 'skills', 'education', 'career_category']
    if not all(k in user_data for k in required_keys):
        return jsonify({"error": "Incomplete user profile"}), 400

    advice = get_career_advice(user_data)
    if advice is None:
        return jsonify({"error": "Failed to generate advice"}), 500
    return jsonify(advice), 200

# 🩺 Health check
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Career Advisor API is running"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
