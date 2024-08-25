from flask import Flask, request, jsonify
import datetime
from collections import OrderedDict


def generate_user_id(full_name, dob):
    dob_formatted = dob.strftime("%d%m%Y")
    return f"{full_name}_{dob_formatted}"


def process_data(data):
    numbers = []
    alphabets = []
    highest_lowercase = []

    for item in data:
        try:
            if item.isdigit():  # Check if the item is a digit string
                numbers.append(int(item))
            elif item.isalpha():  # Check if the item is an alphabet string
                alphabets.append(item.lower())
                if item.islower():
                    highest_lowercase.append(item)
            else:
                print(f"Warning: Unexpected data type for item: {item}")
        except TypeError as e:
            print(f"Error processing item: {item}, {e}")

    highest_lowercase.sort(reverse=True)
    return numbers, alphabets, highest_lowercase[0] if highest_lowercase else []


app = Flask(__name__)


@app.route("/bfhl", methods=["POST"])
def handle_post():
    try:
        data = request.get_json()["data"]
        numbers, alphabets, highest_lowercase = process_data(data)
        response_data = OrderedDict([
            ("is_success", True),
            ("user_id", generate_user_id("Aditya Ramguru", datetime.datetime(year=2003, month=11, day=9))),
            ("email", "aditya.ramguru2021@vitstudent.ac.in"),  # Replace with your email
            ("roll_number", "21BCB0004"),  # Replace with your roll number (optional)
            ("numbers", numbers),
            ("alphabets", alphabets),
            ("highest_lowercase_alphabet", highest_lowercase),
        ])
    except Exception as e:
        response_data = {"is_success": False, "error": str(e)}
    return jsonify(response_data)


@app.route("/bfhl", methods=["GET"])
def handle_get():
    return jsonify({"operation_code": 1})


if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Specify the port here
