## This project aims to create a user-friendly platform for students to buy, sell, and exchange educational resources such as textbooks, instruments, and other study materials.

# Setting up a Python Django Project

## Step 1: Create a Virtual Environment
```bash
# On Windows
python -m venv env

# Activate the virtual environment
myenv\Scripts\activate

# On Linux/Mac
python3 -m venv myenv

# Activate the virtual environment
source env/bin/activate
```
## Step 2: Setup the Environment
```
# Navigate to the project folder
cd path/to/your/project

# Install project dependencies
pip install -r requirements.txt

# Run Django development server
python manage.py runserver

```

## File Structure
```
├───conversation
│   ├───migrations
│   │   └───__pycache__
│   ├───templates
│   │   └───conversation
│   └───__pycache__
├───core
│   ├───migrations
│   │   └───__pycache__
│   ├───static
│   ├───templates
│   │   └───core
│   └───__pycache__
├───dashboard
│   ├───migrations
│   │   └───__pycache__
│   ├───templates
│   │   └───dashboard
│   └───__pycache__
├───item
│   ├───migrations
│   │   └───__pycache__
│   ├───templates
│   │   └───item
│   └───__pycache__
├───media
│   └───item_images
└───mproj
    └───__pycache__
```
