from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Sample data to simulate a database
data = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"}
]

# Route to render the HTML page for the root ("/") route
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', items=data)

# Route to create a new item
@app.route('/create', methods=['POST'])
def create_item():
    new_item_name = request.form.get('new_item')
    if new_item_name:
        new_item = {"id": len(data) + 1, "name": new_item_name}
        data.append(new_item)
        message = f"Item '{new_item_name}' created successfully!"
    else:
        message = "Please provide a valid item name."
    return render_template('index.html', items=data, message=message)

# Route to edit an existing item
@app.route('/edit/<int:item_id>', methods=['GET'])
def edit_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    if item:
        return render_template('edit.html', item=item)
    else:
        return jsonify({"message": "Item not found"}), 404

# Route to update an existing item
@app.route('/update/<int:item_id>', methods=['POST'])
def update_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    if item:
        item['name'] = request.form.get('updated_item_name')
        message = f"Item '{item['name']}' updated successfully!"
    else:
        message = "Item not found."
    return render_template('index.html', items=data, message=message)

# Route to delete an item by ID
@app.route('/delete/<int:item_id>', methods=['GET'])
def delete_item(item_id):
    global data
    data = [item for item in data if item['id'] != item_id]
    message = "Item deleted successfully!"
    return render_template('index.html', items=data, message=message)

if __name__ == '__main__':
    app.run(debug=True,port=9000)
