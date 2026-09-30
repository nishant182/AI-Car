from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware

from routes import auth
from routes import vehicles
from routes import bookings
from routes import services
from routes import ai
from routes import history
from routes import notifications
from routes import upload


app = FastAPI(
    title="AI Vehicle Service API",
    description="Backend API for AI Vehicle Service",
    version="1.0.0"
)


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Authentication
app.include_router(
    auth.router,
    prefix="/api/auth",
    tags=["Authentication"]
)

app.include_router(
    history.router,
    prefix="/api/history",
    tags=["Service History"]
)


# Vehicles
app.include_router(
    vehicles.router,
    prefix="/api/vehicles",
    tags=["Vehicles"]
)


# Bookings
app.include_router(
    bookings.router,
    prefix="/api/bookings",
    tags=["Bookings"]
)


# Service Centers
app.include_router(
    services.router,
    prefix="/api/services",
    tags=["Service Centers"]
)


# AI
app.include_router(
    ai.router,
    prefix="/api/ai",
    tags=["AI"]
)
app.include_router(
    notifications.router,
    prefix="/api/notifications",
    tags=["Notifications"]
)

app.include_router(
    upload.router,
    prefix="/api/upload",
    tags=["Upload"]
)


@app.get("/")
def home():
    return {
        "message": "AI Vehicle Service Backend is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }