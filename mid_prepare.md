# Exploratory Data Analysis (EDA) - 탐색적 데이터 분석

- EDA는 이처럼 데이터를 탐구하면서 문제점과 패턴을 발견하는 과정.
- 이를 통해 후속 데이터 전처리와 모델링의 방향성을 잡는 것.

1. 데이터 로드 및 기본 구조 파악
    - 비디오 파일, 이미지 파일 또는 프레임을 먼저 로드합니다. 딥페이크 탐지 프로젝트에서 데이터는 주로 비디오와 메타데이터로 구성됩니다.
    - 데이터셋의 파일 개수, 각 비디오의 길이, 프레임 수, 해상도와 같은 기본적인 통계를 확인합니다.

```python
import os
import cv2

# 비디오 파일 경로 설정
data_dir = "/path/to/video/dataset"
video_files = [f for f in os.listdir(data_dir) if f.endswith('.mp4')]

# 데이터 통계 확인
print(f"Number of videos: {len(video_files)}")
```

1. 비디오에서 샘플 프레임 추출 및 시각화
    - 각 비디오에서 랜덤으로 몇 개의 프레임을 추출하고 시각화하여 데이터 품질을 확인합니다. 실제 얼굴이 잘 보이는지, 데이터가 잘 구성되어 있는지 확인합니다.
    
    ```python
    import matplotlib.pyplot as plt
    
    # 비디오에서 랜덤 프레임 추출
    def extract_frame(video_path, frame_num=10):
        cap = cv2.VideoCapture(video_path)
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
        ret, frame = cap.read()
        cap.release()
        return frame
    
    # 첫 번째 비디오의 10번째 프레임 시각화
    sample_frame = extract_frame(os.path.join(data_dir, video_files[0]))
    plt.imshow(cv2.cvtColor(sample_frame, cv2.COLOR_BGR2RGB))
    plt.show()
    ```
    

1. 라벨 분포 확인
    - 딥페이크 탐지에서 중요하게 다룰 라벨의 분포를 파악합니다. 얼마나 많은 데이터가 ‘딥페이크’인지 ‘정상’인지 확인하여 데이터의 불균형 여부를 파악할 수 있습니다.

```python
import pandas as pd

# 메타데이터 로드 (라벨 정보 포함)
metadata = pd.read_json('/path/to/metadata.json')

# 라벨 분포 시각화
metadata['label'].value_counts().plot(kind='bar')
plt.title('Distribution of Deepfake vs Real')
plt.show()
```

1. 프레임 간 얼굴 탐지
    - 각 프레임에서 얼굴이 제대로 탐지되고 있는지 확인합니다. 얼굴이 없는 경우가 있는지, 잘못된 탐지 결과가 있는지 파악하여 후속 데이터 전처리 방향을 설정합니다.
    
    ```python
    import face_recognition
    
    # 프레임에서 얼굴 탐지
    def detect_faces_in_frame(frame):
        face_locations = face_recognition.face_locations(frame)
        return len(face_locations), face_locations
    
    # 샘플 프레임에서 얼굴 탐지
    num_faces, face_locations = detect_faces_in_frame(sample_frame)
    print(f"Number of faces detected: {num_faces}")
    ```
    

1. 비디오 길이 및 해상도 분석
    - 각 비디오의 길이와 해상도를 분석하여 전처리 과정에서의 균일한 크기 조정 등의 작업을 미리 계획합니다.

```python
# 비디오 길이 및 해상도 분석
def analyze_video_properties(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cap.release()
    return frame_count, frame_width, frame_height

# 샘플 비디오 속성 확인
frame_count, width, height = analyze_video_properties(os.path.join(data_dir, video_files[0]))
print(f"Video has {frame_count} frames, with resolution {width}x{height}")
```

1. 데이터 불균형 및 해결 전략 파악
    - 라벨 분포에서 데이터가 불균형한 경우, 이를 해결하기 위한 전략을 고려해야 합니다. 데이터 증강기법이나 샘플링 방법 등을 검토

# 데이터 전처리 (Data Preprocessing)

- 데이터의 품질의 높이고, 모델에 적합한 형식으로 변환
    1. **결측값 처리**: 누락된 데이터를 처리하거나 채움.
    2. **중복 제거**: 중복된 데이터 제거.
    3. **정규화/표준화**: 데이터 범위를 일정하게 조정하여 학습 안정성 향상.
    4. **레이블 인코딩**: 범주형 데이터를 수치형으로 변환.
    5. **데이터 정렬 및 클리닝**: 이상치, 노이즈 데이터 제거.
    6. **리샘플링**: 데이터의 균형을 맞추기 위해 과소/과대 샘플링 수행.
    
- 이미지를 모델에 입력하기 전에 **크기 조정**, **회전**, **필터 적용** 등으로 데이터를 통일.

# 데이터 증강 (Data Augmentation)

- 모델이 다양한 데이터 변형에 잘 대응할 수 있도록, **인위적으로 데이터를 늘리는 과정.**
- 특히 딥러닝에서 데이터가 부족할 때, 모델의 **일반화 성능**을 향상시키기 위해 사용.

1. **회전, 확대, 축소**: 이미지를 약간 회전시키거나 확대/축소해 새로운 데이터를 생성.
2. **뒤집기**: 이미지를 좌우 혹은 상하로 반전.
3. **노이즈 추가**: 약간의 노이즈를 추가하여 새로운 데이터 생성.
4. **컬러 조정**: 밝기, 대조, 채도를 변경.
5. **데이터 합성**: 기존 데이터에 합성을 통해 새로운 데이터를 만듦.

- 혁신적인 데이터 증강 기법
    1. **Generative Adversarial Networks (GANs)**
        - GAN은 두 개의 신경망(생성자와 판별자) 간의 경쟁을 통해 데이터를 생성하는 방법입니다. GAN을 사용하여 기존 데이터의 변형뿐만 아니라 완전히 새로운 데이터를 생성할 수 있습니다. 이를 통해 데이터의 다양성을 높이고 모델의 성능을 향상시킬 수 있습니다.
    2.  **CutMix**
        - CutMix는 이미지의 일부를 잘라서 다른 이미지와 합치는 방법입니다. 이렇게 하면 두 개의 이미지에서 특성이 혼합되어 새로운 데이터 샘플을 생성합니다. 이 기법은 다양한 시각적 특성을 모델이 학습할 수 있도록 도와줍니다 .
    3. **Mixup**
        - Mixup은 두 개의 이미지를 서로 섞어 새로운 이미지를 생성하는 기법으로, 두 개의 이미지를 선형 조합하여 하나의 새로운 이미지를 생성합니다. 이 방법은 모델이 다양한 데이터 포인트 사이의 연속성을 학습할 수 있도록 하여 일반화 능력을 높입니다 .
    4.  **Augmented Data via Style Transfer**
        - 스타일 전이 기법을 사용하여 기존 이미지의 스타일을 다른 이미지에 적용하는 방법입니다. 예를 들어, 유명한 화가의 스타일을 사용하여 새로운 이미지로 변환함으로써 다양한 스타일의 데이터를 생성할 수 있습니다 .
    5.  **Random Erasing**
        - Random Erasing은 이미지의 일부를 무작위로 지우는 방법으로, 이를 통해 모델이 손실된 정보를 견딜 수 있도록 합니다. 이 기법은 다양한 상황에서 모델의 견고함을 높이는 데 도움을 줍니다 .
    6. **AutoAugment**
        - AutoAugment는 다양한 데이터 증강 전략을 자동으로 검색하는 방법입니다. 이를 통해 최적의 증강 기법을 발견하고 적용하여 모델 성능을 극대화할 수 있습니다 .
        
        **참고 자료**
        
        1.	[CutMix: Regularization Strategy to Train Stronger Models](https://arxiv.org/abs/1905.04899)
        
        2.	[Mixup: Beyond Empirical Risk Minimization](https://arxiv.org/abs/1710.09412)\
        
        3.	[A Neural Algorithm of Artistic Style](https://arxiv.org/abs/1508.06576)
        
        4.	[Random Erasing Data Augmentation](https://arxiv.org/abs/1708.04896)
        
        5.	[AutoAugment: Learning Augmentation Strategies from Data](https://arxiv.org/abs/1805.09501)
        

# 앙상블 기법

- 여러 모델을 결합하여 성능을 향상시키는 머신러닝 및 딥러닝 방법.

1.  **Bagging (Bootstrap Aggregating)**
    1. **원리**: 데이터셋의 여러 부트스트랩 샘플을 생성하고, 각각의 샘플에 대해 독립적으로 모델을 학습합니다. 마지막 결과는 각 모델의 예측을 평균하거나 다수결 투표를 통해 결정합니다.
    2. **예시**: 랜덤 포레스트(Random Forest)가 대표적인 Bagging 기법입니다. 이는 여러 결정 트리를 결합하여 더 강력한 예측 성능을 얻습니다.
2. **Boosting**
    1. **원리**: 이전 모델의 오차를 줄이기 위해 순차적으로 모델을 학습하는 방법입니다. 각 모델은 이전 모델이 잘못 예측한 샘플에 더 많은 가중치를 부여하여 학습합니다.
    2. **예시**: AdaBoost, Gradient Boosting, XGBoost 등이 있으며, 각 모델의 성능을 단계적으로 개선합니다. Boosting은 일반적으로 높은 성능을 보여주는 기법입니다.
3. **Stacking (Stacked Generalization)**
    1. **원리**: 여러 모델을 학습한 후, 이들의 예측 결과를 새로운 데이터셋으로 사용하여 또 다른 모델을 학습합니다. 이를 통해 다양한 모델의 장점을 결합할 수 있습니다.
    2. **예시**: 여러 서로 다른 모델(예: SVM, 결정 트리, 신경망)의 출력을 입력으로 사용하여 메타 모델(예: 로지스틱 회귀)을 학습합니다.
4. **Voting**
    1. **원리**: 여러 모델이 각기 다른 예측을 할 때, 가장 많이 예측된 클래스를 선택하는 방법입니다. 보통 하드 보팅과 소프트 보팅으로 나뉩니다. 하드 보팅은 다수결에 따라 결정되고, 소프트 보팅은 클래스 확률의 평균을 사용합니다.
    2. **예시**: KNN(K-Nearest Neighbors)와 같은 간단한 모델을 여러 개 결합하여 사용하거나, 다른 복잡한 모델과 조합할 수 있습니다.
5. **Blending**
    1. **원리**: Stacking과 비슷하지만, 전체 데이터셋을 학습하는 대신 일부 데이터를 검증 세트로 사용합니다. 각각의 기본 모델의 예측값을 사용하여 메타 모델을 학습합니다.
    2. **예시**: 테스트 데이터셋의 일부를 블렌딩용으로 사용하여 메타 모델을 최적화합니다.
