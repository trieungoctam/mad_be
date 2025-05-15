import hashlib
import hmac
import urllib.parse
import json
import datetime
import random
import requests
from typing import Dict, Any, Optional


def direct_card_payment(
    card_number: str,
    card_holder_name: str,
    cvv: str,
    expiry_date: str,
    amount: int,
    bank_code: Optional[str] = None,
    description: str = "Thanh toán"
) -> Dict[str, Any]:
    """
    Hàm thực hiện thanh toán trực tiếp với thông tin thẻ qua VNPay Sandbox

    Args:
        card_number (str): Số thẻ ngân hàng
        card_holder_name (str): Tên chủ thẻ
        cvv (str): Mã CVV/CVC
        expiry_date (str): Ngày hết hạn theo định dạng MM/YY
        amount (int): Số tiền cần thanh toán (VND)
        bank_code (str, optional): Mã ngân hàng (NCB, VIETCOMBANK, VIETINBANK, BIDV, v.v.)
        description (str, optional): Mô tả giao dịch. Mặc định là "Thanh toán"

    Returns:
        Dict[str, Any]: Kết quả giao dịch
    """
    # Cấu hình VNPay Sandbox
    vnp_tmn_code = "84JIGDIU"  # Mã website của bạn tại VNPay
    vnp_hash_secret = "MX7U8PWTHDTK6LBK5J6X90JSQMV2KZTS"  # Chuỗi bí mật
    vnp_api_url = "https://sandbox.vnpayment.vn/paymentv2/vpcpay.html"

    # Tạo mã giao dịch
    order_id = f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}{random.randint(10000, 99999)}"

    # Chuẩn bị dữ liệu thanh toán
    expiry_month, expiry_year = expiry_date.split('/')

    # Định dạng ngày theo yêu cầu của VNPay
    create_date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # Chuẩn bị dữ liệu gửi đi
    payment_data = {
        "vnp_Version": "2.1.0",
        "vnp_Command": "pay",
        "vnp_TmnCode": vnp_tmn_code,
        "vnp_Amount": amount * 100,  # VNPay yêu cầu nhân 100 (đơn vị xu)
        "vnp_CreateDate": create_date,
        "vnp_CurrCode": "VND",
        "vnp_IpAddr": "127.0.0.1",
        "vnp_Locale": "vn",
        "vnp_OrderInfo": description,
        "vnp_OrderType": "billpayment",
        "vnp_TxnRef": order_id,

        # Thông tin thẻ
        "vnp_CardNumber": card_number,
        "vnp_CardHolderName": card_holder_name,
        "vnp_CardCvv": cvv,
        "vnp_CardExpiryMonth": expiry_month,
        "vnp_CardExpiryYear": "20" + expiry_year,  # VNPay yêu cầu định dạng 4 chữ số

        # Phương thức thanh toán trực tiếp (không chuyển hướng)
        "vnp_PaymentMethod": "direct",
    }

    # Thêm bank code nếu được cung cấp
    if bank_code:
        payment_data["vnp_BankCode"] = bank_code

    # Kiểm tra định dạng thẻ
    if not card_number.isdigit() or len(card_number) < 13 or len(card_number) > 19:
        return {
            "status": "error",
            "message": "Số thẻ không hợp lệ",
            "data": None
        }

    if not cvv.isdigit() or len(cvv) < 3 or len(cvv) > 4:
        return {
            "status": "error",
            "message": "Mã CVV không hợp lệ",
            "data": None
        }

    # Sắp xếp các tham số theo thứ tự a-z
    sorted_params = sorted(payment_data.items())

    # Tạo chuỗi ký
    hash_data = "&".join([f"{urllib.parse.quote_plus(str(key))}={urllib.parse.quote_plus(str(value))}" for key, value in sorted_params])

    # Tạo chữ ký HMAC-SHA512
    secure_hash = hmac.new(
        vnp_hash_secret.encode('utf-8'),
        hash_data.encode('utf-8'),
        hashlib.sha512
    ).hexdigest()

    # Thêm chữ ký vào dữ liệu
    payment_data["vnp_SecureHash"] = secure_hash

    try:
        # Gửi yêu cầu thanh toán trực tiếp tới VNPay API
        response = requests.post(
            vnp_api_url,
            data=payment_data,
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )

        # Phân tích kết quả
        if response.status_code == 200:
            # Phân tích query string từ response
            result_params = {}
            query_string = response.text.split('?')[1] if '?' in response.text else response.text
            for param in query_string.split('&'):
                if '=' in param:
                    key, value = param.split('=', 1)
                    result_params[key] = urllib.parse.unquote_plus(value)

            if result_params.get("vnp_ResponseCode") == "00":
                return {
                    "status": "success",
                    "message": "Thanh toán thành công",
                    "transaction_id": order_id,
                    "amount": amount,
                    "data": result_params
                }
            else:
                return {
                    "status": "error",
                    "message": f"Thanh toán thất bại: {result_params.get('vnp_Message', 'Lỗi không xác định')}",
                    "data": result_params
                }
        else:
            return {
                "status": "error",
                "message": f"Lỗi kết nối: {response.status_code}",
                "data": response.text
            }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Lỗi khi xử lý thanh toán: {str(e)}",
            "data": None
        }
