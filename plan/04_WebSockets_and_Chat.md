# Step 4: WebSockets and Chat Logic

## Objective
Enable real-time communication between users using rooms and REST API endpoints to fetch chat history.

## Actions to Take
1. **Initialize WebSocket Server**: 
   - Tie the WebSocket server to our main HTTP server.
2. **Socket Authentication**: 
   - Before upgrading a user's connection to a WebSocket, verify their Token.
3. **Room Logic**:
   - Implement `join_room` events. When a user opens a chat, their socket joins the specific Room ID.
   - Implement `leave_room` events.
4. **Messaging Logic**:
   - Endpoint to create a 1-on-1 chat or a group chat.
   - `send_message` socket event: 
     - Save the message to MongoDB.
     - Broadcast the message to all active participants in that room.
5. **Chat History**:
   - REST API route to fetch previous messages from a Room ID (paginated).

## Questions for the User
- How do you want to handle user presence? (e.g., displaying if a user is "online" or "offline")
