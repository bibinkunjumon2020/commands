import random

def generate_math_problem():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operation = random.choice(['+', '-'])
    if operation == '+':
        answer = num1 + num2
    else:
        answer = num1 - num2
    problem = f"{num1} {operation} {num2}"
    return problem, answer

#========== CAPTCHA =============#
from app.captcha import generate_math_problem
from flask import jsonify


@webapp.route("/generate-math-captcha", methods=["GET"])
def generate_math_captcha():
    problem, answer = generate_math_problem()
    return jsonify({"problem": problem, "answer": answer})


@webapp.route("/validate-math-captcha", methods=["POST"])
def validate_math_captcha():
    user_answer = int(request.json.get("user_answer"))
    correct_answer = int(request.json.get("correct_answer"))
    if user_answer == correct_answer:
        return jsonify({"result": "success"})
    else:
        return jsonify({"result": "failure"})
    
#========== CAPTCHA END