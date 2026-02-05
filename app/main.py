from fastapi import FastAPI 
from routes import router 

app = FastAPI(debug=True)

app.include_router(router)


if __name__ == "__main__":
    import uvicorn 
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)