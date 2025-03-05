from fastapi import FastAPI, HTTPException
from v2.models import UserRegister, UserLogin, UserUpdate
from v2.supabase_config import supabase

app = FastAPI()

@app.post("/register")
def register_user(user: UserRegister):
    try:
        # Check if user already exists
        existing_user = supabase.table('users').select('*').eq('email', user.email).execute()
        if existing_user.data:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        # Insert new user
        response = supabase.table('users').insert({
            'name': user.name,
            'email': user.email,
            'password': user.password  # In production, hash the password
        }).execute()
        return {"message": f"{response} registered successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/login")
def login_user(user: UserLogin):
    try:
        # Check user credentials
        response = supabase.table('users').select('*').eq('email', user.email).eq('password', user.password).execute()
        
        if not response.data:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        user_data = response.data[0]
        return {
            "message": "Login successful",
            "user": {
                "id": user_data['id'],
                "name": user_data['name'],
                "email": user_data['email']
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/users/{user_id}")
def get_user_details(user_id: str):
    try:
        response = supabase.table('users').select('id, name, email').eq('id', user_id).execute()
        
        if not response.data:
            raise HTTPException(status_code=404, detail="User not found")
        
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/users/{user_id}")
def update_user_details(user_id: str, user: UserUpdate):
    try:
        # Check if user exists
        existing_user = supabase.table('users').select('*').eq('id', user_id).execute()
        if not existing_user.data:
            raise HTTPException(status_code=404, detail="User not found")
        
        # Update user details
        response = supabase.table('users').update({
            'name': user.name,
            'email': user.email
        }).eq('id', user_id).execute()
        
        return {
            "message": "User updated successfully",
            "user": response.data[0]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))