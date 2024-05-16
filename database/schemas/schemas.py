from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class AccountCreate(BaseModel):
    full_name: str
    phone_number: str
    email: str
    contact_info: str