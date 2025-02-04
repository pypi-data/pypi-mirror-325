import cv2
import numpy as np
from typing import List, Optional, Union
from dataclasses import dataclass
import os, time

@dataclass
class QRResult:
    """คลาสสำหรับเก็บผลลัพธ์จากการอ่าน QR code"""
    data: bytes
    def decode(self, encoding: str = 'utf-8') -> Optional[str]:
        """แปลงข้อมูลไบต์เป็นสตริง"""
        try:
            return self.data.decode(encoding)
        except UnicodeDecodeError:
            return None

class QRDetectorError(Exception):
    """คลาสสำหรับข้อผิดพลาดที่เกิดในโมดูล QR Detector"""
    pass

class QRDetector:
    def __init__(self, debug: bool = False):
        self.qr_detector = cv2.QRCodeDetector()
        self.debug = debug

    def preprocess_image(self, img: np.ndarray, scale: float = 2.0) -> np.ndarray:
        """ขยายและปรับแต่งภาพเพื่อเพิ่มประสิทธิภาพการตรวจจับ QR Code"""
        # แปลงเป็นภาพขาวดำ
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # ปรับความคมชัด
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        gray = clahe.apply(gray)
        
        # ลดสัญญาณรบกวน
        gray = cv2.medianBlur(gray, 3)
        
        # แปลงเป็นภาพขาวดำแบบไบนารี
        _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        # ขยายภาพ
        height, width = binary.shape[:2]
        resized = cv2.resize(binary, (int(width * scale), int(height * scale)), interpolation=cv2.INTER_LINEAR)
        
        return resized

    def rotate_image(self, img: np.ndarray, angle: float) -> np.ndarray:
        """หมุนภาพเพื่อแก้ไข QR Code ที่เอียง"""
        height, width = img.shape[:2]
        rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
        return cv2.warpAffine(img, rotation_matrix, (width, height))

    def decode(self, img: np.ndarray) -> List[QRResult]:
        """ถอดรหัส QR Code จากภาพ พร้อมการตรวจสอบหลายมุม"""
        try:
            if img is None or img.size == 0:
                raise QRDetectorError("รูปภาพไม่ถูกต้อง")
            
            # มุมที่จะลองหมุน
            rotation_angles = [0, 45, -45, 90, -90]
            all_results = []

            for angle in rotation_angles:
                # หมุนภาพ
                rotated_img = self.rotate_image(img, angle)
                
                # เตรียมภาพ
                preprocessed_img = self.preprocess_image(rotated_img, scale=2.0)
                
                # ตรวจจับและถอดรหัส QR Code
                retval, decoded_info, points, _ = self.qr_detector.detectAndDecodeMulti(preprocessed_img)
                
                # เก็บผลลัพธ์
                results = [QRResult(data.encode('utf-8')) for data in decoded_info if data]
                all_results.extend(results)

                # หากพบ QR Code แล้ว จะไม่ลองมุมอื่นต่อ
                if results:
                    break

            return all_results
        except Exception as e:
            if self.debug:
                print(f"เกิดข้อผิดพลาดในการถอดรหัส: {str(e)}")
            raise QRDetectorError(f"เกิดข้อผิดพลาดในการถอดรหัส: {str(e)}")

    def read_from_file(self, file_path: str) -> List[QRResult]:
        """อ่าน QR code จากไฟล์รูปภาพ"""
        try:
            if not os.path.exists(file_path):
                raise QRDetectorError(f"ไม่พบไฟล์: {file_path}")
            
            img = cv2.imread(file_path)
            if img is None:
                raise QRDetectorError(f"ไม่สามารถอ่านไฟล์รูปภาพได้: {file_path}")
            
            return self.decode(img)
        except QRDetectorError:
            raise
        except Exception as e:
            if self.debug:
                print(f"เกิดข้อผิดพลาดในการอ่านไฟล์: {str(e)}")
            raise QRDetectorError(f"เกิดข้อผิดพลาดในการอ่านไฟล์: {str(e)}")

    async def read_from_bytes(self, img_bytes: bytes) -> List[QRResult]:
        """อ่าน QR code จากข้อมูลไบต์ของรูปภาพ"""
        try:
            if not img_bytes:
                raise QRDetectorError("ไม่พบข้อมูลรูปภาพ")
            
            nparr = np.frombuffer(img_bytes, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            if img is None:
                raise QRDetectorError("ไม่สามารถแปลงข้อมูลไบต์เป็นรูปภาพได้")
            
            return self.decode(img)
        except QRDetectorError:
            raise
        except Exception as e:
            if self.debug:
                print(f"เกิดข้อผิดพลาดในการอ่านข้อมูลไบต์: {str(e)}")
            raise QRDetectorError(f"เกิดข้อผิดพลาดในการอ่านข้อมูลไบต์: {str(e)}")

 
    def scan_qr(self, camera_id: int = 0):
        """
        สแกน QR code จากกล้องแบบเรียลไทม์และแสดงผล
        Args:
            camera_id: ID ของกล้องที่ต้องการใช้ (default: 0)
        """
        cap = cv2.VideoCapture(camera_id)
        
        if not cap.isOpened():
            print("❌ ไม่สามารถเปิดกล้องได้")
            return
            
        print("✅ เปิดกล้องสำเร็จ - กำลังเริ่มสแกน")
        
        last_result = None
        
        try:
            while True:
                ret, frame = cap.read()
                if not ret or frame is None:
                    print("❌ ไม่สามารถอ่านภาพจากกล้องได้")
                    break

                # แสดงขนาดเฟรม
                height, width = frame.shape[:2]
                print(f"📸 ขนาดภาพ: {width}x{height}", end='\r')

                # ตรวจจับ QR Code
                try:
                    results = self.decode(frame)
                    
                    # ถ้าพบ QR Code และผลลัพธ์ไม่ซ้ำกับครั้งก่อน
                    for result in results:
                        decoded = result.decode()
                        if decoded and decoded != last_result:
                            last_result = decoded
                            print(f"\n🎯 ผลการสแกน: {decoded}")
                except Exception as e:
                    if self.debug:
                        print(f"\n⚠️ เกิดข้อผิดพลาดในการสแกน: {str(e)}")

                # แสดงภาพจากกล้อง
                try:
                    cv2.imshow("QR Scanner (Press 'q' to quit)", frame)
                except Exception as e:
                    if self.debug:
                        print(f"\n⚠️ ไม่สามารถแสดงภาพได้: {str(e)}")
                    continue

                # หน่วงเวลาเล็กน้อย
                time.sleep(0.1)

                # กด 'q' เพื่อออก
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    print("\n👋 ปิดโปรแกรม")
                    break
        finally:
            cap.release()
            cv2.destroyAllWindows()

    def scan_single(self, camera_id: int = 0) -> Optional[str]:
        """
        สแกน QR code ครั้งเดียวและคืนค่าผลลัพธ์
        Args:
            camera_id: ID ของกล้องที่ต้องการใช้ (default: 0)
        Returns:
            Optional[str]: ข้อความที่อ่านได้จาก QR code หรือ None ถ้าไม่พบ
        """
        cap = cv2.VideoCapture(camera_id)
        
        if not cap.isOpened():
            print("❌ ไม่สามารถเปิดกล้องได้")
            return None
            
        print("✅ เปิดกล้องสำเร็จ - กำลังสแกน...")
        
        # วนลูปสักครู่เพื่อให้กล้องปรับแสง
        for _ in range(5):
            cap.read()
            time.sleep(0.1)
        
        try:
            while True:
                ret, frame = cap.read()
                if not ret or frame is None:
                    print("❌ ไม่สามารถอ่านภาพจากกล้องได้")
                    return None

                # ตรวจจับ QR Code
                try:
                    results = self.decode(frame)
                    
                    # ถ้าพบ QR Code
                    for result in results:
                        decoded = result.decode()
                        if decoded:
                            print(f"🎯 ผลการสแกน: {decoded}")
                            return decoded
                    
                    # ถ้ายังไม่พบ QR Code
                    print("⏳ กำลังค้นหา QR Code...", end='\r')
                    
                except Exception as e:
                    if self.debug:
                        print(f"⚠️ เกิดข้อผิดพลาดในการสแกน: {str(e)}")

                # หน่วงเวลาเล็กน้อย
                time.sleep(0.1)
                    
        finally:
            cap.release()
            print("\n👋 ปิดโปรแกรม")