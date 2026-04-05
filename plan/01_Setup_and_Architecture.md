# Step 1: Initial Setup & Architecture

## Objective
Initialize the project, set up the folder structure, and configure environment variables securely.

## Actions to Take
1. **Initialize the Backend Project**: 
   - Based on our chosen tech stack (e.g., Python FastAPI/Django or Node.js Express).
   - Set up the dependency manager (`requirements.txt`, `Pipfile`, or `package.json`).
2. **Install Core Dependencies**:
   - Web framework.
   - MongoDB driver (e.g., Motor, PyMongo, or Mongoose).
   - Authentication libraries (e.g., bcrypt, PyJWT).
   - WebSocket handler.
   - Cloudinary SDK.
3. **Folder Structure Setup**:
   - `controllers/` - Route logic
   - `models/` - Database schemas
   - `routes/` - API endpoints
   - `services/` - Business logic (e.g., Socket connections, Cloudinary tasks)
   - `middlewares/` - Auth verification
   - `config/` - Database and API keys setup
4. **Environment Variables**:
   - Create a `.env` template file for securing MongoDB URI, JWT Secret, and Cloudinary keys.

## Questions for the User
- Since this directory is named `backend/python`, do you want to build this in **Python** (e.g., FastAPI, which is great for WebSockets) or **Node.js** (Express)?
