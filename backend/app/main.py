# main.py
from fastapi import FastAPI, Depends
from app.db.database import get_db, AsyncSessionLocal
from sqlalchemy import text

app = FastAPI()

# Async route that uses the async session
@app.get("/")
async def root(db: AsyncSessionLocal = Depends(get_db)):
    # A tiny demo query – just check that we can talk to the DB
    result = await db.execute(text("SELECT 1"))
    value = result.scalar_one()          # should be 1
    return {"message": "Supabase DB is reachable!", "value": value}