# Step 3: Authentication System

## Objective
Allow users to register, log in securely with an ID and password, and receive a Token (JWT) for authorization.

## Actions to Take
1. **Registration Endpoint**:
   - Validate incoming ID and password.
   - Hash the password before saving to the database.
   - Create the User record in MongoDB.
2. **Login Endpoint**:
   - Verify the ID and compare the hashed password.
   - Generate a JSON Web Token (JWT) containing the user's ID.
   - Return the token to the client.
3. **Auth Middleware/Dependency**:
   - Create a reusable function to protect routes.
   - It will intercept incoming requests, extract the token from headers or cookies, and verify it before allowing access to chat features.

## Questions for the User
- Because we are integrating with an SSR frontend, do you want to pass the token back as an `HttpOnly` cookie (for better security) or as a standard JSON response?
