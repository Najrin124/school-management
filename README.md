# school-management
school-management-App

```bash
mkdir school-management
cd school-management

python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

```bash
pip install fastapi[standard]
pip install uvicorn[standard]
pip install sqlalchemy
pip install psycopg2-binary
pip install python-jose
pip install passlib[bcrypt]
pip install python-dotenv
pip install pydantic-settings
```

```bash
pip freeze > requirements.txt
```

### RUN

```bash
uvicorn main:app --reload
```

### TEST:
- Open browser: http://localhost:8000/docs