# -*- coding: utf-8 -*-
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    username: str
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class ArticleBase(BaseModel):
    title: str
    content: str


class ArticleCreate(ArticleBase):
    owner_id:int


class Article(ArticleBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class CommentBase(BaseModel):
    content: str


class CommentCreate(CommentBase):
    owner_id: int
    article_id: int


class Comment(CommentBase):
    id: int
    owner_id: int
    article_id: int

    class Config:
        orm_mode = True
