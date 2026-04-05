# Step 5: Media Uploads and Profile Sharing

## Objective
Enable the uploading and sharing of small media files and profile pictures using Cloudinary.

## Actions to Take
1. **Cloudinary Configuration**:
   - Set up API credentials in `.env`.
   - Initialize the Cloudinary SDK.
2. **File Upload Middleware**:
   - Create a system to temporarily accept files in memory.
3. **Upload Service**:
   - Upload the file directly from memory to Cloudinary securely.
   - Intercept the returned secure URL for our database.
4. **Profile Management**:
   - Create an endpoint for a user to upload/update their profile picture.
   - Create an endpoint to fetch and view another user's profile.
5. **Media in Chats**:
   - Create an endpoint specifically for uploading media destined for a chat.
   - The user will upload the file -> get the Cloudinary URL -> include the URL in the `send_message` WebSocket payload.

## Questions for the User
- What size limit should we enforce on "small media files" (e.g., 5MB, 10MB)?
