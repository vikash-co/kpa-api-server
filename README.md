# kpa-api-server

This is a backend implementation for a sample KPA ERP system built using Django REST Framework and PostgreSQL.

✅ Implemented two fully working API endpoints from the provided Swagger/Postman collection, connected to PostgreSQL, and tested using Postman.

📦 Tech Stack

Language	- Python 3.11+
Framework - 	Django REST Framework
Database -	PostgreSQL
Env management -	.env using python-decouple


🚀 Setup Instructions

1. Clone the project
bash
git clone https://github.com/<your-username>/kpa-backend-assignment.git
cd kpa-backend-assignment

3. Create and activate virtual environment
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

5. Install dependencies
bash
pip install -r requirements.txt
6. Create .env file
   
At the root of the project, create a .env file and configure your PostgreSQL details:

text
DEBUG=True
DB_NAME=kpa_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

5. Apply Migrations
bash
python manage.py makemigrations
python manage.py migrate

6. Run the server
bash
python manage.py runserver
API will be available at:
http://127.0.0.1:8000/api/forms/...

📬 APIs Implemented
1. POST /api/forms/bogie-checksheet
Description: Create a new bogie form entry.

Sample Body
json
{
  "formNumber": "BOGIE-2025-001",
  "inspectionBy": "user_id_456",
  "inspectionDate": "2025-07-03",
  "bogieDetails": {
    "bogieNo": "BG1234",
    "dateOfIOH": "2025-07-01",
    "deficitComponents": "None",
    "incomingDivAndDate": "NR / 2025-06-25",
    "makerYearBuilt": "RDSO/2018"
  },
  "bogieChecksheet": {
    "axleGuide": "Worn",
    "bogieFrameCondition": "Good",
    "bolster": "Good",
    "bolsterSuspensionBracket": "Cracked",
    "lowerSpringSeat": "Good"
  },
  "bmbcChecksheet": {
    "adjustingTube": "DAMAGED",
    "cylinderBody": "WORN OUT",
    "pistonTrunnion": "GOOD",
    "plungerSpring": "GOOD"
  }
}
Sample Success Response: 201 Created
json
{
  "success": true,
  "message": "Bogie checksheet submitted successfully.",
  "data": { ... }
}

2. GET /api/forms/wheel-specifications
Description: Fetch wheel specs. Filter by formNumber, submittedBy, or submittedDate.

Example URL:
text
/api/forms/wheel-specifications?formNumber=WHEEL-2025-001
Sample Response: 200 OK
json
{
  "success": true,
  "message": "Filtered wheel specification forms fetched successfully.",
  "data": [
    {
      "formNumber": "WHEEL-2025-001",
      "submittedBy": "user_id_123",
      "submittedDate": "2025-07-03",
      "fields": {
        "condemningDia": "825 (800-900)",
        "lastShopIssueSize": "837 (800-900)",
        "treadDiameterNew": "915 (900-1000)",
        "wheelGauge": "1600 (+2,-1)"
      }
    }
  ]
}

📂 File Structure Overview
bash
kpa_backend_project/
│
├── api/                  # Django app
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── kpa_backend/          # Django project core
│   ├── settings.py
│   └── urls.py
├── .env
├── requirements.txt
├── manage.py
└── README.md

🧪 Testing
Tested using Postman with both:

✅ Successful form creation (POST)

✅ Filtered data retrieval (GET)

Postman collection is included as kpa_postman_collection.json.
