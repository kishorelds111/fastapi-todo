from sqlalchemy.orm import Session
from models import Task

def get_tasks(db: Session):
    return db.query(Task).all()

def create_task(db: Session, task_name: str):
    task = Task(name=task_name)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return task
