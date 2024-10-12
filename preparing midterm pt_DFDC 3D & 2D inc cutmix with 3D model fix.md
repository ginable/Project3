**성적 높은 모델 분석 : 1.DFDC 3D & 2D inc cutmix with 3D model fix**

https://www.kaggle.com/code/kkkkksw/dfdc-3d-2d-inc-cutmix-with-3d-model-fix/edit ← 직접

https://www.kaggle.com/code/vaillant/dfdc-3d-2d-inc-cutmix-with-3d-model-fix ← 기존

 주어진 비디오에서 얼굴을 탐지하고, 사전 학습된 3D 및 2D 모델들을 사용하여 각 프레임의 진위 여부를 예측

1. 설치 라이브러리
    
    ```python
    import os
    import math
    import pickle #모델 저장 및 로드
    from functools import partial #함수에서 인자를 미리 고정하여 다른 함수처럼 사용
    from collections import defaultdict #모델의 예측 값을 여러 영상 파일에서 누적하고 저장
    
    from PIL import Image
    from glob import glob
    
    import cv2
    import numpy as np
    import skimage.measure
    import albumentations as A #이미지 증강
    from tqdm.notebook import tqdm 
    from albumentations.pytorch import ToTensor 
    
    import torch
    import torch.nn as nn
    import torch.nn.functional as F
    from torch.autograd import Variable
    from torchvision.models.video import mc3_18, r2plus1d_18
    
    from facenet_pytorch import MTCNN #얼굴탐지
    ```
    

2. 영상 처리 및 얼굴 탐지

- **`MTCNN`을 사용한 얼굴 탐지**: 영상에서 얼굴을 탐지하기 위해 MTCNN(FaceNet-PyTorch)을 사용. 얼굴을 탐지하는 다단계 네트워크로, 얼굴이 포함된 프레임에서 얼굴의 위치를 파악. 
영상에서 프레임을 추출한 후, MTCNN 모델을 통해 얼굴 영역을 탐지하고 그 영역을 반환.
- **프레임 로딩**: `load_video` 함수는 주어진 비디오 파일에서 특정 프레임을 추출하여 RGB로 변환하고 필요한 경우 리스케일링도 수행.
 메모리 에러 방지를 위해 프레임의 수를 제한하고, 다운샘플링하여 프레임을 로드.

3. 3D CNN 모델 준비 및 적용

- **pretrained 3D 모델 로드**: I3D, ResNet, MC3, R2Plus1D 등 다양한 3D CNN 모델을 사용. 
이 모델들은 pretrained 상태로 제공, 각 모델은 얼굴이 포함된 영상의 특정 부분을 분석해 딥페이크 여부를 예측.
- **앙상블**: 각 영상에 대해 모델들의 예측 값을 평균내어 최종 예측 값을 계산. 
예측 값이 0에 가까우면 딥페이크일 가능성이 낮고, 1에 가까우면 딥페이크일 가능성이 높음.

### 4. 2D CNN 모델 적용

- **Ian의 2D 모델 적용**: Ian이라는 이름의 2D CNN 모델을 사용하여 추가적인 예측을 수행. 
2D 프레임 기반으로 동작하며, 모델을 통해 각 프레임에서 딥페이크 여부를 예측.

### 5.결론

딥페이크 탐지를 위해 pretrained된 여러 3D CNN 모델과 MTCNN을 사용하여 영상을 처리하고, 각 영상에서 얼굴을 추출한 후, 딥페이크 여부를 예측. 여러 모델을 사용하여 앙상블 방식으로 최종 예측 값을 도출.
