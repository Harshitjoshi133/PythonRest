create table users (
  id uuid default uuid_generate_v4() primary key,
  name text not null,
  email text unique not null,
  password text not null,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null
);


# Register a new user
curl -X POST http://localhost:8000/register -H "Content-Type: application/json" -d "{\"name\":\"John Doe\",\"email\":\"john@example.com\",\"password\":\"password123\"}"

# Login
curl -X POST http://localhost:8000/login -H "Content-Type: application/json" -d "{\"email\":\"john@example.com\",\"password\":\"password123\"}"

# Get user details (replace USER_ID with actual UUID)
curl -X GET http://localhost:8000/users/USER_ID

# Update user details (replace USER_ID with actual UUID)
curl -X PUT http://localhost:8000/users/USER_ID -H "Content-Type: application/json" -d "{\"name\":\"John Smith\",\"email\":\"john.smith@example.com\"}"