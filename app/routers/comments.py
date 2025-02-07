# -*- coding: utf-8 -*-
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.Comment)
def create_comment(comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    db_comment = models.Comment(
        content=comment.content,
        owner_id=comment.owner_id,
        article_id=comment.article_id
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


@router.get("/article/{article_id}", response_model=list[schemas.Comment])
def get_comments_by_article(article_id: int, db: Session = Depends(get_db)):
    comments = db.query(models.Comment).filter(models.Comment.article_id == article_id).all()
    if not comments:
        raise HTTPException(status_code=404, detail="No comments found for this article")
    return comments
