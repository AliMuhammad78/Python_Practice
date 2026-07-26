# a= ['apples' , 'bananas' , 'mangoes']

# result = "-".join(a)
# print(result)

from flask import Flask

app = Flask(__name__)

# Define a route
@app.route('/')
def home():
    return "Hello, World!"

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
