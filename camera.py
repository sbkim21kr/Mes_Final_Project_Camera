import cv2
import os
from datetime import datetime

def main():
    # Base /photos folder
    base_photos_dir = os.path.join(os.getcwd(), "photos")
    os.makedirs(base_photos_dir, exist_ok=True)

    # Today's date folder
    today_str = datetime.now().strftime("%Y-%m-%d")
    date_dir = os.path.join(base_photos_dir, today_str)
    os.makedirs(date_dir, exist_ok=True)

    # Subfolder named by initiated time (HHhMMmSSs → e.g. 15h18m42s)
    run_time = datetime.now().strftime("%Hh%Mm%Ss")
    photos_dir = os.path.join(date_dir, run_time)
    os.makedirs(photos_dir, exist_ok=True)

    # Print session folder info
    print(f"Session folder created: {photos_dir}")

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        print("Could not open camera.")
        return

    counter = 0  # photo index within this run

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Frame read failed.")
            break

        # Overlay info on preview
        overlay_text = f"{today_str}/{run_time} | Next photo: _{counter:02d}.jpg"
        cv2.putText(frame, overlay_text, (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.imshow("Logitech Camera", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == 27:  # ESC to quit
            break

        elif key == 32:  # Space bar pressed
            filename = f"_{counter:02d}.jpg"
            filepath = os.path.join(photos_dir, filename)
            cv2.imwrite(filepath, frame)
            print(f"Saved photo: {run_time}/{filename}")
            counter += 1

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
