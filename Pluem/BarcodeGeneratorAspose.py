# -------------------- โค้ดใหม่สำหรับ Aspose Barcode --------------------
import pandas as pd
import os
import aspose.barcode.generation as barcodegen

excel_file_path = r"E:\Download\CAI CAMP 2025\July\7.July\สรุปบัญชี คูปอง รอบ ก.ค.68 (Line)โอม.xlsx"
output_dir = r"E:\Download\CAI CAMP 2025\July\7.July\Barcodes_Aspose"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

df_excel = pd.read_excel(excel_file_path)

for index, row in df_excel.iterrows():
    coupon_id = str(row['Coupon ID']).zfill(13)
    promotion_code = str(row['Promotion Code'])
    receipt_promotion_name = str(row['Receipt Promotion Name'])

    if len(coupon_id) == 13 and coupon_id.isdigit():
        try:
            builder = barcodegen.BarcodeGenerator(barcodegen.EncodeTypes.EAN13, coupon_id)
            builder.parameters.barcode.x_dimension.pixels = 2
            builder.parameters.barcode.bar_height.pixels = 80
            builder.parameters.barcode.padding.left.pixels = 0
            builder.parameters.barcode.padding.right.pixels = 10
            builder.parameters.barcode.padding.top.pixels = 0
            builder.parameters.barcode.padding.bottom.pixels = 0
            builder.parameters.caption_above.text = ""
            builder.parameters.caption_below.text = ""
            builder.parameters.barcode.code_text_parameters.location = barcodegen.CodeLocation.BELOW

            filename = f"{promotion_code}_{receipt_promotion_name}.png"
            filepath = os.path.join(output_dir, filename)
            builder.save(filepath)
            print(f"Generated barcode for {filename}")

        except Exception as e:
            print(f"Error generating barcode for Coupon ID {coupon_id}: {e}")
    else:
        print(f"Skipping invalid Coupon ID length: {coupon_id} (length {len(coupon_id)})")

print("Barcode generation complete.")

# -------------------- โค้ด Aspose Barcode แบบเดิม --------------------
'''
import pandas as pd
import os
import aspose.barcode as barcode

excel_file_path = r"E:\Download\CAI CAMP 2025\July\7.July\สรุปบัญชี คูปอง รอบ ก.ค.68 (Line)โอม.xlsx"
output_dir = r"E:\Download\CAI CAMP 2025\July\7.July\Barcodes_Aspose"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

df_excel = pd.read_excel(excel_file_path)

for index, row in df_excel.iterrows():
    coupon_id = str(row['Coupon ID']).zfill(13)
    promotion_code = str(row['Promotion Code'])
    receipt_promotion_name = str(row['Receipt Promotion Name'])

    # Use the 13-digit Coupon ID directly for EAN-13
    if len(coupon_id) == 13 and coupon_id.isdigit():
        try:
            # Create the EAN-13 barcode with Aspose
            builder = barcode.generation.BarcodeGenerator(barcode.generation.EncodeTypes.EAN13, coupon_id)
            
            builder.parameters.barcode.x_dimension.pixels = 2
            builder.parameters.barcode.bar_height.pixels = 80
            builder.parameters.barcode.padding.left.pixels = 15
            builder.parameters.barcode.padding.right.pixels = 15
            builder.parameters.barcode.padding.top.pixels = 10
            builder.parameters.barcode.padding.bottom.pixels = 10

            builder.parameters.caption_above.text = ""
            builder.parameters.caption_below.text = ""
            builder.parameters.barcode.code_text_parameters.location = barcode.generation.CodeLocation.BELOW

            filename = f"{promotion_code}_{receipt_promotion_name}.png"
            filepath = os.path.join(output_dir, filename)
            builder.save(filepath)
            print(f"Generated barcode for {filename}")

        except Exception as e:
            print(f"Error generating barcode for Coupon ID {coupon_id}: {e}")
    else:
        print(f"Skipping invalid Coupon ID length: {coupon_id} (length {len(coupon_id)})")

print("Barcode generation complete.")
'''