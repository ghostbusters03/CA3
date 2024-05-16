from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Simple Calculator</h1>
    <form action="/calculate" method="post">
        <input type="number" name="num1" placeholder="Enter first number" required>
        <select name="operation">
            <option value="add">Add</option>
            <option value="subtract">Subtract</option>
        </select>
        <input type="number" name="num2" placeholder="Enter second number" required>
        <button type="submit">Calculate</button>
    </form>
    '''

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        else:
            return jsonify({"error": "Invalid operation"})

        return jsonify({"result": result})

    except (ValueError, KeyError) as e:
        return jsonify({"error": "Invalid input"})

if __name__ == '__main__':
    app.run(debug=True)
