from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world"

@app.route("/demo", methods=['POST'])
def math_opertation():
    if (request.method == 'POST'):
        operation = request.json['operation']
        num1 = request.json['num1']
        num2 = request.json['num2']
        results = num1 + num2

        if operation == 'add':
            results = num1 + num2
        elif operation == 'subtract':
            results =  num1 - num2
        elif operation == 'mul':
            results =  num1 * num2
        elif operation == 'div':
            results = num1 / num2
        else:
            return "Error"
         
    return "The operation is {} and the results is {}".format(operation, results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)