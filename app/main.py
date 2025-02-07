# -*- coding: utf-8 -*-
import uvicorn
from fastapi import FastAPI

from routers.articles import router as articles_router
from routers.users import router as users_router
from routers.comments import router as comments_router

app = FastAPI()

app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(articles_router, prefix="/articles", tags=["articles"])
app.include_router(comments_router, prefix="/comments", tags=["comments"])


@app.get("/", tags=["home"])
async def index():
    return 'hello fastAPI'


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8888)
