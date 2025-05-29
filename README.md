# Mental Well-Being Chatbot

A conversational AI assistant designed to promote mental well-being using Rasa for natural language understanding and dialogue management. The bot supports features like mood tracking, journaling, motivational quotes, and coping strategies. It is integrated with a Python frontend (e.g., Flask or FastAPI) for a web interface.

---

##  Features

- Daily mood check-ins
- Guided journaling prompts
- Mindfulness & breathing exercises
- Motivational quotes
- Crisis support messages
- Custom actions for personalized experiences

---

## Tech Stack

- **Backend**: [Rasa](https://rasa.com/)
- **Frontend**: Flask / FastAPI (Python)
---

## How to Run 

### 1. Clone the Repository
git clone https://github.com/Deadshot1831/rasa_chatbot

cd rasa_chatbot

### 2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt
### 4. Train the Rasa Model
rasa train

### 5. Start the Rasa Servers
Run the action server:
rasa run actions
Run the Rasa shell or HTTP API:
rasa run --enable-api --cors "*" --debug
### 6. Start the Frontend Server
If using Flask:
cd app
python main.py
Your chatbot UI will be available at: http://localhost:5000
