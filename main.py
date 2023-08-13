from fastapi import FastAPI
from routers import books
from services.db import init_db


app = FastAPI()

app.include_router(books.router)


@app.on_event("startup")
async def on_startup():
    await init_db()

# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()
