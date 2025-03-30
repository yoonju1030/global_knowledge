from sqlalchemy.orm import Session
from src.global_knowledge.models import Setting
import datetime
from uuid import UUID, uuid4

class AdminService:
    def __init__(self):
        pass

    def set_page(self, page: int, db: Session):
        try:
            page_setting = Setting(
                id=str(uuid4()),
                category = "page",
                value = page,
                set_date = datetime.datetime.now()
            )
            db.add(page_setting)
            db.commit()
            return True
        except Exception as e:
            raise e