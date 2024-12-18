import sys
import cv2
import torch
import timm  # Xception 모델을 불러오기 위해 timm 사용
import torchvision.transforms as transforms
from PIL import Image
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QFileDialog

# DeepFakeModel 클래스 정의
class DeepFakeModel:
    def __init__(self, model_path):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        # Xception 모델 로드 (timm 라이브러리 사용)
        self.model = timm.create_model('xception', pretrained=False, num_classes=2)  # 2개 클래스 출력 설정

        # 가중치 로드
        checkpoint = torch.load(model_path, map_location=self.device)

        # 키 이름 수정: 'model.' 접두사 제거 및 'last_linear.1' -> 'fc'
        state_dict = {key.replace("model.", "").replace("last_linear.1", "fc"): value
                      for key, value in checkpoint['model_state_dict'].items()}

        # 수정된 state_dict를 모델에 적용
        self.model.load_state_dict(state_dict)
        self.model.to(self.device)
        self.model.eval()

        # 이미지 전처리 (Xception 입력에 맞게 설정)
        self.transform = transforms.Compose([
            transforms.Resize((299, 299)),  # Xception 모델은 299x299 입력 사용
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])  # 정규화 설정
        ])

    def predict(self, frames):
        """동영상에서 추출한 프레임 리스트를 받아 예측."""
        inputs = torch.stack([self.transform(frame) for frame in frames]).to(self.device)
        with torch.no_grad():
            outputs = self.model(inputs)  # Xception 모델 예측
            probabilities = torch.softmax(outputs, dim=1).cpu().numpy()[:, 1]  # 두 번째 클래스 확률만 가져오기

            # 디버깅: 각 프레임별 확률 출력
            print("Frame-wise probabilities:", probabilities)

        mean_probability = probabilities.mean()
        print("Mean Probability:", mean_probability)  # 평균 확률 출력
        return mean_probability  # 평균 확률 반환


# GUI 메인 윈도우 정의
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # PyQt5 GUI 설정
        self.setWindowTitle("Deepfake Detection")
        self.setGeometry(300, 300, 600, 400)

        # Upload Video 버튼
        self.upload_button = QPushButton("Upload Video", self)
        self.upload_button.setGeometry(50, 50, 120, 30)
        self.upload_button.clicked.connect(self.upload_video)

        # Analyze 버튼
        self.analyze_button = QPushButton("Analyze", self)
        self.analyze_button.setGeometry(200, 50, 120, 30)
        self.analyze_button.clicked.connect(self.analyze_video)

        # 동영상 경로 표시
        self.video_path = QLineEdit(self)
        self.video_path.setGeometry(50, 100, 400, 30)

        # 결과 표시 라벨
        self.result_label = QLabel("Result will be shown here", self)
        self.result_label.setGeometry(50, 150, 400, 30)

        # 딥페이크 모델 로드
        self.model = DeepFakeModel("best_model_epoch_11.pth")

    def upload_video(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Upload Video", "", "Video Files (*.mp4 *.avi)")
        if file_name:
            self.video_path.setText(file_name)

    def analyze_video(self):
        video_path = self.video_path.text()
        if not video_path:
            self.result_label.setText("Please upload a video first!")
            return

        # 동영상 처리
        print(f"Processing video: {video_path}")  # 동영상 경로 출력
        frames = self.process_video(video_path)
        print(f"Total extracted frames: {len(frames)}")  # 추출된 프레임 수 출력

        if not frames:
            self.result_label.setText("No frames extracted from video!")
            return

        # 모델 예측
        result = self.model.predict(frames)
        print(f"Final Prediction Result: {result:.2f}")  # 최종 예측값 출력

        # 결과 표시
        result = round(result, 2)

        if result > 0.3:
            self.result_label.setText(f"DeepFake Detected! ({result:.2f})")
        else:
            self.result_label.setText(f"Real Video! ({result:.2f})")

    def process_video(self, video_path, frame_count=10):
        cap = cv2.VideoCapture(video_path)
        frames = []
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        step = max(total_frames // frame_count, 1)

        for i in range(0, total_frames, step):
            cap.set(cv2.CAP_PROP_POS_FRAMES, i)
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frames.append(Image.fromarray(frame))
            if len(frames) >= frame_count:
                break

        cap.release()
        return frames


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())