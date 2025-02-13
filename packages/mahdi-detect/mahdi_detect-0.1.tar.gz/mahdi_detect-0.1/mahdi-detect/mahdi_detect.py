from ultralytics import YOLO
import cv2
import os
import util  # فرض بر این است که توابع read_license_plate و get_car در این ماژول موجود است

class VehicleAndPlateDetector:
    def __init__(self, vehicle_model_path='yolov8n.pt', plate_model_path='license_plate_detector.pt'):
        # تعریف مدل‌ها
        self.coco_model = YOLO(vehicle_model_path)  # مدل تشخیص عمومی (خودروها و سایر اشیاء)
        self.license_plate_detector = YOLO(plate_model_path)  # مدل تشخیص پلاک

        # لیست کلاس‌های خودرو (مطابق دیتاست COCO: مثلا 2: car, 3: motorcycle, 5: bus, 7: truck)
        self.vehicles = [2, 3, 5, 7]

    def detect(self, image_path):
        """
        تابع اصلی برای تشخیص خودروها و پلاک‌ها در تصویر
        """
        # بارگذاری تصویر
        image = cv2.imread(image_path)
        if image is None:
            print("تصویر خوانده نشد. لطفاً آدرس تصویر را بررسی کنید.")
            return

        # تشخیص خودروها در تصویر
        results_vehicle = self.coco_model(image)[0]  # اجرای مدل روی تصویر
        vehicle_detections = []  # لیستی برای ذخیره دتکسیون‌های خودرو

        for detection in results_vehicle.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = detection
            if int(class_id) in self.vehicles:
                vehicle_detections.append([x1, y1, x2, y2, score])

        # تشخیص پلاک خودرو در تصویر
        results_lp = self.license_plate_detector(image)[0]  # اجرای مدل پلاک روی تصویر

        # دایرکتوری‌های ذخیره خروجی برای پلاک‌ها و خودروها
        output_dir_plate = 'plates'
        output_dir_car = 'cars'
        os.makedirs(output_dir_plate, exist_ok=True)
        os.makedirs(output_dir_car, exist_ok=True)

        plate_count = 0  # شمارنده برای نامگذاری تصاویر پلاک
        for detection in results_lp.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = detection

            # رسم کادر پلاک روی تصویر (به رنگ قرمز)
            cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
            cv2.putText(image, f"{score:.2f}", (int(x1), int(y1)-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)

            # کراپ دقیق پلاک
            plate_crop = image[int(y1):int(y2), int(x1):int(x2)]
            
            # ذخیره تصویر پلاک کراپ شده
            plate_filename = os.path.join(output_dir_plate, f"plate_{plate_count}.jpg")
            cv2.imwrite(plate_filename, plate_crop)
            print(f"تصویر پلاک در {plate_filename} ذخیره شد.")

            # تعیین خودرو مربوط به پلاک با استفاده از تابع get_car
            car_bbox = util.get_car([x1, y1, x2, y2], vehicle_detections)
            
            if car_bbox is not None:
                car_x1, car_y1, car_x2, car_y2, car_score = car_bbox
                # کراپ خودرو از تصویر اصلی
                car_crop = image[int(car_y1):int(car_y2), int(car_x1):int(car_x2)]
                car_filename = os.path.join(output_dir_car, f"car_{plate_count}.jpg")
                cv2.imwrite(car_filename, car_crop)
                print(f"تصویر خودرو مربوط به پلاک در {car_filename} ذخیره شد.")
            else:
                print("خودروی مرتبط با پلاک یافت نشد.")
            
            plate_count += 1

        # نمایش تصویر اصلی با کادرهای پلاک کشیده شده
        cv2.imshow("Detected License Plates", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # ذخیره تصویر نهایی در صورت نیاز
        output_path = 'output.jpg'
        cv2.imwrite(output_path, image)
        print(f"تصویر نهایی در {output_path} ذخیره شد.")

# اجرای تشخیص
if __name__ == "__main__":
    detector = VehicleAndPlateDetector('yolov8n.pt', 'license_plate_detector.pt')
    image_path = 'car.jpg'  # آدرس تصویر مورد نظر خود را قرار دهید
    detector.detect(image_path)
