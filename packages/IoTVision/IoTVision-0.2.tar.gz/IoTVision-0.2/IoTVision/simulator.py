import cv2
import csv
import os
import threading

class IoTSimulator:
    def __init__(self, csv_file, image_folder):
        self.csv_file = csv_file
        self.image_folder = image_folder
        self.annotations = self.load_annotations()
    
    def load_annotations(self):
        annotations = {}
        with open(self.csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                filename = row['filename']
                appliance = row['appliance']
                status = row['status']
                coords = row['coordinates'].replace("(", "").replace(")", "").replace("to", ",").split(",")
                coords = [int(coord.strip()) for coord in coords]
                if filename not in annotations:
                    annotations[filename] = []
                annotations[filename].append({"appliance": appliance, "status": status, "coords": tuple(coords)})
        return annotations
    
    def draw_annotations(self, image, annotations):
        for annotation in annotations:
            x_min, y_min, x_max, y_max = annotation['coords']
            color = (0, 255, 0) if annotation['status'] == "On" else (0, 0, 255)
            label = f"{annotation['appliance']} ({annotation['status']})"
            cv2.rectangle(image, (x_min, y_min), (x_max, y_max), color, 2)
            cv2.putText(image, label, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
        return image
    
    def update_status(self, command):
        try:
            appliance, status = command.split()
            status = status.capitalize()
            for filename in self.annotations:
                for annotation in self.annotations[filename]:
                    if annotation['appliance'] == appliance:
                        annotation['status'] = status
                        print(f"Updated {appliance} to {status}")
                        return
            print(f"Appliance '{appliance}' not found.")
        except ValueError:
            print("Invalid format. Use '<appliance> <status>' (e.g., 'fan1 On').")
    
    def display_images(self):
        for filename in self.annotations:
            image_path = os.path.join(self.image_folder, filename)
            image = cv2.imread(image_path)
            if image is None:
                print(f"Error: Could not load image {filename}")
                continue
            while True:
                annotated_image = self.draw_annotations(image.copy(), self.annotations[filename])
                cv2.imshow("IoT Simulator", annotated_image)
                key = cv2.waitKey(100) & 0xFF
                if key == ord('q'):
                    break
        cv2.destroyAllWindows()
    
    def start(self):
        threading.Thread(target=self.command_listener, daemon=True).start()
        self.display_images()
    
    def command_listener(self):
        print("Enter commands like '<appliance> <status>' (e.g., 'fan1 On'). Type 'exit' to quit.")
        while True:
            command = input("> ")
            if command.lower() == 'exit':
                break
            self.update_status(command)

if __name__ == "__main__":
    image_folder = input("Enter the image folder path: ")
    simulator = IoTSimulator("annotations.csv", image_folder)
    simulator.start()
