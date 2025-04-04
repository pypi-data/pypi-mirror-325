from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, validator

class ErrorNumber(BaseModel):
    """نموذج لرقم به خطأ"""
    number: str
    country: Optional[str] = None
    error: str

class MessageRequest(BaseModel):
    """نموذج لطلب إرسال الرسالة"""
    text: str
    numbers: List[str]
    sender: str

class MessageResponse(BaseModel):
    """نموذج للرد على الرسالة"""
    inserted_numbers: int
    message: Dict[str, Any]
    error_numbers: Optional[List[ErrorNumber]] = None
    no_package: Optional[List[str]] = None
    has_more_iso_code: Optional[List[str]] = None

class SMSRequest(BaseModel):
    """نموذج لطلب إرسال الرسائل"""
    messages: List[MessageRequest]

class SMSResponse(BaseModel):
    """نموذج للرد على طلب إرسال الرسائل"""
    job_id: str
    messages: List[MessageResponse]
    code: int
    message: str
    success: bool = True
    total_success: int = 0
    total_failed: int = 0

    @validator('success')
    def validate_success(cls, v, values):
        """التحقق من نجاح الإرسال بناءً على وجود معرف المهمة"""
        if 'job_id' in values and values['job_id']:
            return True
        return False

class Package(BaseModel):
    """نموذج لباقة الرسائل"""
    id: int
    package_points: int = Field(alias='package_points')
    current_points: int = Field(alias='current_points')
    expire_at: str = Field(alias='expire_at')
    is_active: bool = Field(alias='is_active')

class BalanceResponse(BaseModel):
    """نموذج للرد على طلب الرصيد"""
    code: int
    message: str
    total_balance: int
    packages: Optional[List[Package]] = None

class SenderNameItem(BaseModel):
    """نموذج لاسم المرسل"""
    id: int
    sender_name: str
    status: int
    note: Optional[str] = None
    sabah_request_id: Optional[int] = None

class SenderNamesResponse(BaseModel):
    """نموذج للرد على طلب أسماء المرسلين"""
    code: int
    message: str
    items: List[SenderNameItem]
