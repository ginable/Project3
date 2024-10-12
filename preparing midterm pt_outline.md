- Deepfake detection challenge (DFDC)

**개요**

- 2020년 facebook 주관 kaggle에서 개최된 challenge
- https://www.kaggle.com/c/deepfake-detection-challenge
- 생성형 모델 (generative model)로부터 생성되는 영상 또는 동영상을 검출하는 목적
- 당시 generative adversarial network (GAN), variational auto-encoder (VAE), flow model 등을 활용하여 생성된 동영상

**Data**

- Training dataset: 470GB 크기의 데이터
- Public validation dataset: 10초 분량의 400개 동영상
- Public test dataset
- Private test dataset
- Sample 동영상

Easy sample

![image](https://github.com/user-attachments/assets/f1911f5c-f095-4d39-aebe-139632d9f4dd)


Hard sample

![image](https://github.com/user-attachments/assets/edcffd47-a544-45a1-9750-328ceb786a2f)


제약조건

CPU/GPU notebook에서 9 시간 이내 동작

인터넷 없는 환경에서 동작

외부 데이터 1GB까지 허용, pre-trained model 허용

평가 방법

![image](https://github.com/user-attachments/assets/b5524019-aa39-490b-a5de-6e0c5d7bf15f)


- **n**: 예측하는 비디오의 수 (전체 샘플 수)
- **y^i**: i번째 비디오가 **FAKE**일 확률에 대한 예측값 (모델의 예측 확률, 0과 1 사이의 값)
- **yi**: i번째 비디오가 실제로 **FAKE**인지 여부 (정답값, FAKE이면 1, REAL이면 0)
- **log()**: 자연 로그, 밑(base)이 **e**인 로그
    
    
    Log Loss는 모델이 얼마나 확률적으로 정확하게 예측하는지, 특히 **확률 예측에서의 신뢰도**를 기반으로 평가하는 방법
    

제출 방법

Format에 맞는 제출 파일을 생성하여 Kaggle에 업로드

Comma separated variables (CSV) file 제출

![image](https://github.com/user-attachments/assets/01a9107b-6fc3-4547-bc32-d1fc8a897f98)


Video는 image를 매우 짧은 간격으로 연결한 미디어

일반적으로 초당 25 frame (1초에 25개의 image)으로 재생되면, 끊기는 걸 눈치채기 어려움

고품질의 video는 초당 30 frame == 30 fps (frame per second)

30fps의 10초 길이 video는 900개의 image로 구성
