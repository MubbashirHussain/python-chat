from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.auth import router as auth_router

app = FastAPI(
    title="Chat App Backend",
    description="Backend for the real-time chat application",
    version="1.0.0"
)

# CORS configuration (Crucial for SSR Integration)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this in production to match your SSR frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)

from app.utils.responses import res_success

@app.get("/")
async def root():
    return res_success("Welcome to the Chat App API!")
