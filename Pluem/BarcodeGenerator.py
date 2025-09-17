import pandas as pd
import os
from barcode import EAN13
from barcode.writer import ImageWriter

# Path ของไฟล์ Excel
excel_file_path = r"E:\Download\CAI CAMP 2025\July\7.July\สรุปบัญชี คูปอง รอบ ก.ค.68 (Line)โอม.xlsx"
# โฟลเดอร์สำหรับเก็บไฟล์บาร์โค้ด

# ใช้ path Windows และสร้างโฟลเดอร์ถ้ายังไม่มี
output_dir = r"E:\Download\CAI CAMP 2025\July\7.July\Barcodes"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# อ่านข้อมูลจาก Excel
df_excel = pd.read_excel(excel_file_path)


for index, row in df_excel.iterrows():
    coupon_id = str(row['Coupon ID']).zfill(13)
    promotion_code = str(row['Promotion Code'])
    receipt_promotion_name = str(row['Receipt Promotion Name'])

    # Use the 13-digit Coupon ID directly for EAN-13
    if len(coupon_id) == 13 and coupon_id.isdigit():
        try:
            # Create the EAN-13 barcode
            # We need to use a custom writer to add text
            from barcode.writer import ImageWriter
            from PIL import Image, ImageDraw, ImageFont

            class CustomImageWriter(ImageWriter):
                def __init__(self):
                    ImageWriter.__init__(self)
                    self.text = ""
                    self.font_path = "C:/Windows/Fonts/arial.ttf"  # ใช้ฟอนต์ Windows
                    try:
                        self.font = ImageFont.truetype(self.font_path, 20) # Adjust font size as needed
                    except IOError:
                        self.font = ImageFont.load_default()
                        print(f"Warning: Font not found at {self.font_path}, using default font.")

                def create_image(self, text):
                    """Creates the image with the barcode and the text below."""
                    barcode_image = ImageWriter.create_image(self, text)
                    img_width, img_height = barcode_image.size

                    # Calculate text size
                    try:
                         text_width, text_height = self.font.getbbox(self.text)[2:]
                    except AttributeError:
                         text_width, text_height = self.font.getsize(self.text)


                    # Create a new image with extra space for text
                    new_img_height = img_height + text_height + 10 # Add some padding
                    new_img = Image.new('RGB', (max(img_width, text_width), new_img_height), 'white')

                    # Paste the barcode image
                    new_img.paste(barcode_image, (int((new_img.size[0] - img_width) / 2), 0))

                    # Add the text below the barcode
                    draw = ImageDraw.Draw(new_img)
                    text_x = (new_img.size[0] - text_width) / 2
                    text_y = img_height + 5 # Add some padding
                    draw.text((text_x, text_y), self.text, fill="black", font=self.font)

                    return new_img


            custom_writer = CustomImageWriter()
            custom_writer.text = f"Promotion Code: {promotion_code}\nReceipt Promotion Name: {receipt_promotion_name}\nCoupon ID: {coupon_id}"

            # Adjusting writer options for better visual appearance (experimentation might be needed)
            writer_options = {
                "format": "JPEG",
                "module_height": 10, # Adjust module height (height of the bars)
                "module_width": 0.3, # Adjust module width (width of the narrowest bar)
                "font_size": 10,     # Adjust font size for the numbers below the barcode (if not using custom writer text)
                "text_distance": 5,  # Adjust distance between barcode and numbers (if not using custom writer text)
                "quiet_zone": 6.5    # Adjust quiet zone (whitespace around the barcode)
            }


            ean = EAN13(coupon_id, writer=custom_writer)

            # Define the filename

            filename = f"{promotion_code}_{receipt_promotion_name}.jpg"
            filepath = os.path.join(output_dir, filename)

            # Save the barcode as a JPEG image with adjusted options
            ean.save(filepath[:-4], options=writer_options)  # python-barcode จะเติม .jpg ให้เอง
            print(f"Generated barcode for {filename}")

        except Exception as e:
            print(f"Error generating barcode for Coupon ID {coupon_id}: {e}")
    else:
        print(f"Skipping invalid Coupon ID length: {coupon_id} (length {len(coupon_id)})")

print("Barcode generation complete.")