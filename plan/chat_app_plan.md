# Chat Application Development Plan

This document outlines the step-by-step plan for building a Server-Side Rendered (SSR) Chat Application with FastAPI. The application will feature robust user authentication, MongoDB for data storage, and Cloudinary for media management (profile pictures).

---

## Phase 1: Environment and Dependencies
1. **Environment Variables**: Create a `.env` file to securely store credentials.
    - `MONGODB_URL`
    - `JWT_SECRET_KEY`
    - `CLOUDINARY_CLOUD_NAME`
    - `CLOUDINARY_API_KEY`
    - `CLOUDINARY_API_SECRET`
2. **Install Required Libraries**:
    - `motor`: Asynchronous MongoDB driver.
    - `passlib[bcrypt]`: For password hashing.
    - `python-jose[cryptography]`: For JWT token creation and verification.
    - `python-multipart`: For form data and file uploads.
    - `cloudinary`: Official Cloudinary Python SDK.
    - `jinja2`: For Server-Side Rendering (SSR) templates.

## Phase 2: Database Configuration (MongoDB)
1. **Database Client (`app/db/mongodb.py`)**:
    - Establish an asynchronous connection to MongoDB using `motor`.
    - Set up application startup and shutdown events in `main.py` to manage the DB lifecycle.
2. **User Schema (`app/models/user.py` / PyDantic)**:
    - **Schema Fields**:
        - `username` (string, unique)
        - `password` (string, hashed)
        - `first_name` (string)
        - `last_name` / `surname` (string)
        - `status` (string, e.g., "Available", "Away")
        - `profile_picture_url` (string, maps to Cloudinary URL)
        - `created_at` (datetime)

## Phase 3: Cloudinary Integration (Media)
1. **Cloudinary Service (`app/services/cloudinary_service.py`)**:
    - Configure the Cloudinary library using variables from the `.env` file.
    - Create a function: `upload_profile_picture(file)` which takes a FastAPI `UploadFile`, streams it to Cloudinary, and returns the public URL.

## Phase 4: Authentication & Security Core
1. **Security Utilities (`app/core/security.py`)**:
    - `get_password_hash(password: str) -> str`: Hashes plain text passwords.
    - `verify_password(plain_password: str, hashed_password: str) -> bool`: Checks passwords.
    - `create_access_token(data: dict) -> str`: Generates JWT tokens.
2. **Authentication Dependency (`app/api/deps.py`)**:
    - Create a `get_current_user` dependency that reads the JWT token (presumably stored in HTTP-only cookies for SSR), verifies it, and fetches the user object from MongoDB.

## Phase 5: User & Authentication Endpoints
1. **Auth Router (`app/api/v1/auth.py`)**:
    - `POST /auth/register`: Takes user info, hashes password, saves to MongoDB.
    - `POST /auth/login`: Checks credentials, returns JWT (sets cookie).
    - `POST /auth/logout`: Clears the JWT cookie.
2. **User Router (`app/api/v1/user.py`)**:
    - `GET /users/me`: Return authenticated user info.
    - `PUT /users/me`: Update `first_name`, `last_name`, and `status`.
    - `POST /users/me/profile_picture`: Uploads image to Cloudinary and updates user DB record with the new URL.

## Phase 6: SSR Frontend Integration (Jinja2)
1. **Template Setup**:
    - Create a `templates/` directory in the project root.
    - Configure FastAPI's `Jinja2Templates`.
2. **Page Routes (`app/routers/pages.py`)**:
    - `GET /`: Renders the landing/login/registration page.
    - `GET /chat`: Requires authentication. Renders the main chat application. Injects user profile data (name, picture, status) into the HTML template.

## Phase 7: Real-Time Chat (WebSockets)
1. **WebSocket Endpoint (`app/api/ws/chat.py`)**:
    - Create a WebSocket route: `ws://.../ws/chat`.
    - Require JWT token verification on the WebSocket connection.
2. **Connection Manager**:
    - Keep track of active connections and user statuses.
    - Handle broadcasting messages to connected users.
3. **Message Schema (MongoDB)**:
    - Create a schema/collection for Chat Messages to persist history.

---

### Next Action Items:
Review this plan. Once approved, we will begin with Phase 1 by installing dependencies and configuring the `.env` file and basic MongoDB connection.

## Implementation Notes
- **Standardized Response Format**: All API endpoints use custom response functions defined in `app/utils/responses.py` (e.g. `res_success`, `res_created`, `res_bad_request`) to maintain a consistent JSON response structure: `{ "status": true|false, "code": HTTP_STATUS_CODE, "message": "...", "data": {...} | "error": "..." }`.
