from fastapi import FastAPI 
import routes 

app = FastAPI()

app.include_router(routes.router)


if __name__ == "__main__":
    import uvicorn 
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)