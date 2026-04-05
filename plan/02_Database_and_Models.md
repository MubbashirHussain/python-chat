# Step 2: Database and Models

## Objective
Connect to MongoDB and define the necessary data models/schemas.

## Actions to Take
1. **Database Connection**: 
   - Write a module to securely connect to MongoDB using the URI from `.env`.
2. **Define User Schema**:
   - `userId`
   - `username` / `identifier`
   - `password` (hashed)
   - `profilePicture` (Cloudinary URL)
   - `bio` or other profile details you might want.
3. **Define Chat Room Schema**:
   - `roomId`
   - `isGroup` (boolean)
   - `name` (for group chats)
   - `participants` (list of User IDs)
4. **Define Message Schema**:
   - `messageId`
   - `roomId` (reference to Chat Room)
   - `senderId` (reference to User)
   - `content` (text)
   - `mediaUrl` (optional Cloudinary URL)
   - `createdAt`

## Questions for the User
- Do you already have a MongoDB Atlas cloud database set up, or should we use a local MongoDB instance for development?
