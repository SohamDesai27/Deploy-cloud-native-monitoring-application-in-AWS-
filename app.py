# Import necessary modules
import psutil  # For system resource monitoring
from flask import Flask, render_template  # For creating a Flask web application and rendering HTML templates

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def index():
    # Get CPU and memory metrics using psutil library
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent
    
    # Initialize a variable to store the message
    message = None
    
    # Check if CPU or memory usage is above 80%
    if cpu_metric > 80 or mem_metric > 80:
        message = "High CPU or Memory Detected, scale up!!!"
    
    # Render the index.html template with CPU and memory metrics and the message
    return render_template("index.html", cpu_metric=cpu_metric, mem_metric=mem_metric, message=message)

# Start the Flask web application if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
