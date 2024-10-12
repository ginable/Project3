딥페이크 연구동향

![image](https://github.com/user-attachments/assets/bd6b21aa-2de3-44b4-9f19-c9d7f5d48462)


가상의 얼굴 생성하여 합성

![image](https://github.com/user-attachments/assets/843c7c7c-d16f-4d9b-9fae-4fda68f63d02)

GAN을 활용한 생성

Style GAN으로 학습된 이미지를 이용한 가짜이미지 생성

기존의 얼굴에 특정 속성만 바꿈(안경, 머리숱, 피부색 등

![image](https://github.com/user-attachments/assets/acfdf43d-1d09-4302-9674-bb5bdadc1efc)


이역시도 GAN기반의 생생 ex) Star Gan

표정바꿈*실질적이용

![image](https://github.com/user-attachments/assets/4fc85d15-2e5d-4037-b2bf-9c0343dc9f85)

source: 피해 얼굴

target:x참고할 얼굴(표정 등)

Fake생성

특정 사람 + 어떠한 사람이 한 표정이나 행동→ 특정사람이 어떤 표정이나 행동하도록 생성

ex:Face3face, synthesizing obama

서로다른 두사람 얼굴 교체*실질적이용

![image](https://github.com/user-attachments/assets/d2322186-dc26-498e-8339-cdc70f3cd37d)


특정한 사람과 다른사람의 얼굴의 교체

피해자 사진의 특성을 소스 비디오에 입힘

ex: faceswap, deepfacelab과 같은 라이브러리

![image](https://github.com/user-attachments/assets/2c8e1159-a68b-42a6-ba54-2e3ab6a7f9dc)


2가지 접근법: 

1. 컴퓨터 그래픽에 기반한 기법: 
2. 딥러닝 기반의 기법: 1) few shot: 비디오에  삽입하고자하는 이미지가 몇장밖에 없을때, 
2)multi shot: 삽입하고자 하는 사진이 여러장 있을때

오토인코더

![image](https://github.com/user-attachments/assets/eb7194c5-f642-4bf5-ae18-f84875017136)


DNN구조의 딥러닝 모델 이미지의 특징(눈코입)과 같은 내용을 비지도학습

인코더: 인풋 입력받아 특성값 z 생성

디코더: z값을 받아서 원본이미지와 비슷한 아웃풋 만듬

딥페이크 생성 과정

extraction 학습을 위한 얼굴의 이미지를 추출

![image](https://github.com/user-attachments/assets/b74e9cd6-ac75-493a-82de-6b1e5fb4cf70)

주요 랜드마크 alignment파일을 생성

랜드마크 파일을 잏용해서 학습 및 변환 과정에서 도움을 받음

training

![image](https://github.com/user-attachments/assets/db747a96-ebbc-4860-88bf-55714b1ce7e8)


텐서플로우 기반으로 동작,

오토인코더를 기반으로 학습

인코더 파트 공유, 디코더 파트는 서로 다르게 설정

각 이미지의 특성 추출 → 공유함으로써 두 비디오의 공유되고 있는 특성이 학습됨.

여기서 공유되고 있는 특성: 눈코입위치, 유사한 특성이 학습되도록 유도

디코더에서는 피해자와 소스 특성이 각각 따로 학습되도록유도→ 각 얼굴의 눈 생김새 코생김새 등

latent에서는 외곽이나 눈코입 위치만 학습

converting

![image](https://github.com/user-attachments/assets/1beaf0a3-4dd4-4294-b84f-8f9b89bcb9fd)


피해자의 얼굴 변환하여

오리지널 의 눈코입 위치 확인하고, 

피해자의 특성을 삽입

피해자의 얼굴이 바뀌어 들어감

![image](https://github.com/user-attachments/assets/77ad67b2-e44b-4ce1-b142-59310cc3ca3a)


1000장에서 만장의 이미지

얼굴파트의 각도와 조명이 다양해야 결과가 좋아짐** 각도와 조명을 보면 좋을듯

deepfakedetection현황

![image](https://github.com/user-attachments/assets/9c2b2bd8-d35e-4251-91f3-e77c287b80f7)

매프래임마다 얼굴위치를 찾아서 판별- deepclasifier: FaceForensics ICCV

Temporal 비디오에서 프래임간의 연결관계 시간적 특성 탐지 : 프레임간의 연결을 확인하는것 -CVPR Recurrent Convolutional Strategies for Face~ 

![image](https://github.com/user-attachments/assets/c3cc506a-7c85-4d90-96da-4c1b0486ccef)


faceforencsic: 각 프래임마다 effnet넣어서 성능

recurrent: cnn+rnn

![image](https://github.com/user-attachments/assets/e41ed145-6bb1-4376-9db1-1db7835643a1)


xceoptionNet 이 결과가 괜찮은편
