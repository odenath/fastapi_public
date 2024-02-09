from fastapi import FastAPI
from routes import router as routes_router
# from scheduling import job

app = FastAPI()

app.include_router(routes_router)

# job()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)










# from fastapi import FastAPI
# ## import models
# ##from routes import router
# from config import engine
# ## models.Base.metadata.create_all(bind=engine)
# app = FastAPI()
# ## app.include_router(router='/', prefix="/book", tags=["book"])