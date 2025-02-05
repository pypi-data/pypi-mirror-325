import cv2
import csv
import os

class IoTAnnotator:
    def __init__(self, folder_path, output_csv="annotations.csv"):
        self.folder_path = folder_path
        self.output_csv = output_csv
        self.annotations = []
        self.current_status = "On"
        self.current_type = "Appliance"
        self.drawing = False
        self.start_point = None

    def draw_rectangle(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.start_point = (x, y)
            self.drawing = True
        elif event == cv2.EVENT_MOUSEMOVE and self.drawing:
            temp_image = self.image.copy()
            color = (0, 255, 0) if self.current_status == "On" else (0, 0, 255)
            cv2.rectangle(temp_image, self.start_point, (x, y), color, 2)
            cv2.imshow("Annotate IoT Devices", temp_image)
        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False
            end_point = (x, y)
            color = (0, 255, 0) if self.current_status == "On" else (0, 0, 255)
            cv2.rectangle(self.image, self.start_point, end_point, color, 2)
            cv2.imshow("Annotate IoT Devices", self.image)
            self.annotations.append({
                "filename": self.current_filename,
                "appliance": self.current_type,
                "status": self.current_status,
                "coordinates": f"({min(self.start_point[0], end_point[0])}, {min(self.start_point[1], end_point[1])}) to ({max(self.start_point[0], end_point[0])}, {max(self.start_point[1], end_point[1])})"
            })

    def annotate_images(self):
        if not os.path.exists(self.folder_path):
            print("Error: Folder path does not exist.")
            return
        
        image_files = [f for f in os.listdir(self.folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        if not image_files:
            print("Error: No images found in the folder.")
            return
        
        for filename in image_files:
            self.current_filename = filename
            image_path = os.path.join(self.folder_path, filename)
            self.image = cv2.imread(image_path)
            if self.image is None:
                print(f"Error: Could not load image {filename}")
                continue
            
            cv2.namedWindow("Annotate IoT Devices")
            cv2.setMouseCallback("Annotate IoT Devices", self.draw_rectangle)
            print(f"Annotating {filename}... (Press 'o' for On, 'f' for Off, 't' for Type, 's' to Save)")
            
            while True:
                cv2.imshow("Annotate IoT Devices", self.image)
                key = cv2.waitKey(1) & 0xFF
                if key == ord('o'):
                    self.current_status = "On"
                elif key == ord('f'):
                    self.current_status = "Off"
                elif key == ord('t'):
                    self.current_type = input("Enter appliance type: ")
                elif key == ord('s'):
                    break
            
            cv2.destroyAllWindows()
        
        self.save_annotations()

    def save_annotations(self):
        with open(self.output_csv, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["filename", "appliance", "status", "coordinates"])
            writer.writeheader()
            writer.writerows(self.annotations)
        print(f"Annotations saved to {self.output_csv}")

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder containing images: ")
    IoTAnnotator(folder_path).annotate_images()
