import pandas as pd
import os
import aspose_barcode_cloud
from aspose_barcode_cloud.rest import ApiException

# กำหนด API Key ของคุณที่นี่
client_id = "910ab854-5651-4660-aa80-2b2359cda6aa"
client_secret = "d945c8909ef4e578e99afaae5644a8a7"

# Pa
# th ของไฟล์ Excel
excel_file_path = r"E:\Download\CAI CAMP 2025\July\7.July\สรุปบัญชี คูปอง รอบ ก.ค.68 (Line)โอม.xlsx"
output_dir = r"E:\Download\CAI CAMP 2025\July\7.July\Barcodes_AsposeCloud"
os.makedirs(output_dir, exist_ok=True)

df = pd.read_excel(excel_file_path)

# ตั้งค่า API Client
api_client = aspose_barcode_cloud.ApiClient(
    client_id="910ab854-5651-4660-aa80-2b2359cda6aa",
    client_secret="d945c8909ef4e578e99afaae5644a8a7"
)
barcode_api = aspose_barcode_cloud.BarcodeApi(api_client)

for idx, row in df.iterrows():
    code = str(row['Coupon ID']).zfill(13)
    promo_code = str(row['Promotion Code'])
    receipt_name = str(row['Receipt Promotion Name'])
    if len(code) != 13 or not code.isdigit():
        print(f"Skipping invalid Coupon ID: {code}")
        continue

    try:
        barcode_info = aspose_barcode_cloud.BarcodeInfo(
            type="EAN13",
            text=code
        )
        response = barcode_api.generate_barcode(barcode_info)
        filename = f"{promo_code}_{receipt_name}.png"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "wb") as f:
            f.write(response)
        print(f"Generated barcode for {filename}")
    except ApiException as e:
        print(f"Exception when calling BarcodeApi->generate_barcode for {code}: {e}")

print("Barcode generation complete.")
