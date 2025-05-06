import os
import logging
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash
from diet_generator import calculate_bmr, adjust_calories, generate_diet_plan

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask application
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "diet-plan-generator-secret")

# Add context processor to provide current year to all templates
@app.context_processor
def inject_current_year():
    return {'current_year': datetime.now().year}

@app.route('/', methods=['GET'])
def index():
    """Render the main page with the input form."""
    return render_template('index.html')

@app.route('/generate_plan', methods=['POST'])
def generate_plan():
    """Process the form data and generate a diet plan."""
    try:
        # Extract form data
        height = float(request.form.get('height'))
        weight = float(request.form.get('weight'))
        gender = request.form.get('gender')
        age = int(request.form.get('age'))
        fitness_goal = request.form.get('fitness_goal')
        
        # Validate input
        if height <= 0 or weight <= 0 or age <= 0:
            flash("Please enter valid values for height, weight, and age.", "danger")
            return redirect(url_for('index'))
        
        # Calculate BMR
        bmr = calculate_bmr(weight, height, age, gender)
        
        # Adjust calories based on fitness goal
        adjusted_calories = adjust_calories(bmr, fitness_goal)
        
        # Generate diet plan
        diet_plan = generate_diet_plan(adjusted_calories)
        
        # Store data in session for display
        session['user_data'] = {
            'height': height,
            'weight': weight,
            'gender': gender,
            'age': age,
            'fitness_goal': fitness_goal,
            'bmr': round(bmr),
            'adjusted_calories': round(adjusted_calories),
            'diet_plan': diet_plan
        }
        
        return render_template('diet_plan.html', user_data=session['user_data'])
    
    except ValueError as e:
        flash(f"Invalid input: {str(e)}", "danger")
        return redirect(url_for('index'))
    except Exception as e:
        logging.error(f"Error generating diet plan: {str(e)}")
        flash("An error occurred while generating your diet plan. Please try again.", "danger")
        return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('index.html'), 404

@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors."""
    logging.error(f"Server error: {str(e)}")
    return render_template('index.html'), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
