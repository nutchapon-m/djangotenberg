# Djangotenberg

Djangotenberg คือ Library สำหรับเชื่อมต่อและใช้งาน Gotenberg PDF generator ภายในโปรเจค Django ช่วยให้สามารถแปลง HTML เป็น PDF และจัดการไฟล์ PDF ได้อย่างง่ายดาย

## Supported Tools

ปัจจุบัน Djangotenberg รองรับเครื่องมือ (Tools) หลักของ Gotenberg ดังนี้:

*   **Chromium**: สำหรับแปลง HTML code ให้เป็นไฟล์ PDF
*   **PDF Engines**: สำหรับจัดการไฟล์ PDF
    *   Merge PDFs: รวมไฟล์ PDF หลายไฟล์เข้าด้วยกัน
    *   Read Metadata: อ่านค่า Metadata ของไฟล์ PDF
    *   Write Metadata: แก้ไขหรือเพิ่ม Metadata ให้กับไฟล์ PDF

## Requirements

*   Python >= 3.9
*   Django >= 4.2
*   djangorestframework >= 3.16
*   requests >= 2.32
*   **Gotenberg Server**: จำเป็นต้องมี Gotenberg server รันอยู่ (แนะนำให้รันผ่าน Docker)

## Installation

ติดตั้ง Library ผ่าน pip:
(สมมติว่า package ชื่อ `djangotenberg`)

```bash
pip install djangotenberg
```

หรือติดตั้งจาก Source code:

```bash
pip install .
```

## Setup & Configuration

1.  เพิ่ม `djangotenberg` เข้าไปใน `INSTALLED_APPS` ในไฟล์ `settings.py` ของคุณ:

    ```python
    # settings.py

    INSTALLED_APPS = [
        # ...
        'rest_framework',
        'djangotenberg',
        # ...
    ]
    ```

2.  กำหนดค่า `GOTENBERG_CONFIG` ใน `settings.py` เพื่อระบุตำแหน่งของ Gotenberg server:

    ```python
    # settings.py

    GOTENBERG_CONFIG = {
        # URL ของ Gotenberg server ที่คุณรันอยู่ (Required)
        "GOTENBERG_URL": "http://localhost:3000",
        
        # เวลา Time out สำหรับเรียก API หน่วยเป็นวินาที (Optional, Default: 10)
        "GOTENBERG_API_TIMEOUT": 10,
    }
    ```

## Usage

### 1. ใช้งานผ่าน Client (Python Code)

คุณสามารถเรียกใช้ `APIClient` เพื่อส่งคำสั่งไปยัง Gotenberg โดยตรง

```python
from djangotenberg.client import APIClient

client = APIClient()

# Example: Convert HTML string to PDF
html_content = "<h1>Hello, Djangotenberg!</h1>"
response = client.html_to_pdf(html_content)

if response.ok:
    with open("output.pdf", "wb") as f:
        f.write(response.content)
```

### 2. ใช้งานผ่าน Django Views (REST Framework)

Djangotenberg เตรียม `PDFView` มาให้ ซึ่งคุณสามารถนำไป register กับ Router ของ DRF ได้ทันที

**urls.py**

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from djangotenberg.views.pdf import PDFView

router = DefaultRouter()
# Register endpoint สำหรับ PDF
router.register(r'pdf', PDFView, basename='pdf')

urlpatterns = [
    path('api/', include(router.urls)),
]
```

**Available Endpoints:**

เมื่อติดตั้งแล้ว คุณจะสามารถเรียกใช้ API ได้ดังนี้ (สมมติ base url คือ `/api/pdf/`):

*   `POST /api/pdf/html-to-pdf/`: แปลง HTML string เป็น PDF
    *   Body: `{ "html": "<h1>Content</h1>" }`
*   `POST /api/pdf/merge/`: รวมไฟล์ PDF
*   `POST /api/pdf/read-metadata/`: อ่าน Metadata
*   `POST /api/pdf/write-metadata/`: เขียน Metadata
