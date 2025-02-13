# 4jawaly SMS Gateway SDK for Python

مكتبة Python لإرسال الرسائل النصية القصيرة عبر بوابة 4jawaly للرسائل

## المتطلبات

- Python 3.7 أو أحدث
- requests >= 2.25.0
- pydantic >= 1.8.0

## التثبيت

```bash
pip install fourjawaly-sms
```

## الاستخدام

### تهيئة المكتبة

```python
from fourjawaly_sms import SMSGateway

client = SMSGateway(
    api_key='your_api_key',
    api_secret='your_api_secret',
    sender='YOUR_SENDER_NAME'
)
```

### إرسال رسالة SMS

```python
try:
    # إرسال لرقم واحد
    response = client.send_single_sms(
        number='966500000000',
        message='مرحباً من 4jawaly!'
    )
    
    if response.success:
        print('تم إرسال الرسالة بنجاح!')
        print(f'معرفات المهام: {", ".join(response.job_ids)}')
    
    # إرسال لعدة أرقام
    numbers = ['966500000000', '966500000001']
    bulk_response = client.send_sms(
        numbers=numbers,
        message='رسالة جماعية من 4jawaly!'
    )
    
    print(f'تم إرسال: {bulk_response.total_success}')
    print(f'فشل إرسال: {bulk_response.total_failed}')

except SMSGatewayError as e:
    print(f'حدث خطأ: {e}')
```

### الاستعلام عن الرصيد

```python
try:
    balance = client.get_balance(is_active=1)
    print(f'الرصيد: {balance.balance}')
    
    if balance.packages:
        for package in balance.packages:
            print(f'الباقة {package.id}:')
            print(f'  النقاط: {package.package_points}')
            print(f'  النقاط المتبقية: {package.current_points}')
            print(f'  تاريخ الانتهاء: {package.expire_at}')

except SMSGatewayError as e:
    print(f'حدث خطأ: {e}')
```

### استخدام Context Manager

```python
with SMSGateway('your_api_key', 'your_api_secret', 'YOUR_SENDER_NAME') as client:
    response = client.send_single_sms('966500000000', 'مرحباً من 4jawaly!')
    # سيتم إغلاق الجلسة تلقائياً عند الخروج من الـ with block
```

## التطوير

```bash
# تثبيت المتطلبات
pip install -e ".[dev]"

# تشغيل الاختبارات
pytest

# تشغيل التحقق من التنسيق
black .
flake8 .

# بناء الحزمة
python setup.py sdist bdist_wheel
```

## المساهمة

1. Fork المشروع
2. إنشاء فرع للميزة (`git checkout -b feature/amazing-feature`)
3. Commit التغييرات (`git commit -m 'Add some amazing feature'`)
4. Push إلى الفرع (`git push origin feature/amazing-feature`)
5. فتح Pull Request

## الترخيص

MIT License
