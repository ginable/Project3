딥페이크 연구동향

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/14b7775d-b6b5-40e1-be84-e9327f16fd78/16196ace-c937-4bb6-94bc-fc5ae559ece1/image.png)

가상의 얼굴 생성하여 합성

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/14b7775d-b6b5-40e1-be84-e9327f16fd78/f999ad39-0023-420f-a5b7-090e1fcf59ae/image.png)

GAN을 활용한 생성

Style GAN으로 학습된 이미지를 이용한 가짜이미지 생성

기존의 얼굴에 특정 속성만 바꿈(안경, 머리숱, 피부색 등

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/14b7775d-b6b5-40e1-be84-e9327f16fd78/28aa28ea-552f-4be9-8cb7-d506c4985c4a/image.png)

이역시도 GAN기반의 생생 ex) Star Gan

표정바꿈*실질적이용

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/14b7775d-b6b5-40e1-be84-e9327f16fd78/7fe90021-4ba1-482a-88fd-a6b880e8faa3/image.png)

source: 피해 얼굴

target:x참고할 얼굴(표정 등)

Fake생성

특정 사람 + 어떠한 사람이 한 표정이나 행동→ 특정사람이 어떤 표정이나 행동하도록 생성

ex:Face3face, synthesizing obama

서로다른 두사람 얼굴 교체*실질적이용

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/14b7775d-b6b5-40e1-be84-e9327f16fd78/3e0ed62e-b075-4f34-ae47-9f00c999cc60/image.png)

특정한 사람과 다른사람의 얼굴의 교체

피해자 사진의 특성을 소스 비디오에 입힘

ex: faceswap, deepfacelab과 같은 라이브러리

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/14b7775d-b6b5-40e1-be84-e9327f16fd78/59f787c1-8f53-4c41-af51-5ce5b2f838fd/image.png)

2가지 접근법: 

1. 컴퓨터 그래픽에 기반한 기법: 
2. 딥러닝 기반의 기법: 1) few shot: 비디오에  삽입하고자하는 이미지가 몇장밖에 없을때, 
2)multi shot: 삽입하고자 하는 사진이 여러장 있을때

오토인코더

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/14b7775d-b6b5-40e1-be84-e9327f16fd78/bb8111ad-d76e-438f-845a-f46cb62011c0/image.png)

DNN구조의 딥러닝 모델 이미지의 특징(눈코입)과 같은 내용을 비지도학습

인코더: 인풋 입력받아 특성값 z 생성

디코더: z값을 받아서 원본이미지와 비슷한 아웃풋 만듬

딥페이크 생성 과정

extraction 학습을 위한 얼굴의 이미지를 추출

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/14b7775d-b6b5-40e1-be84-e9327f16fd78/5145b434-78cf-4661-b0ff-8d1701f125ba/image.png)

주요 랜드마크 alignment파일을 생성

랜드마크 파일을 잏용해서 학습 및 변환 과정에서 도움을 받음

training

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/14b7775d-b6b5-40e1-be84-e9327f16fd78/48bbd516-e757-4ce8-b7ba-a66ad02b729b/image.png)

텐서플로우 기반으로 동작,

오토인코더를 기반으로 학습

인코더 파트 공유, 디코더 파트는 서로 다르게 설정

각 이미지의 특성 추출 → 공유함으로써 두 비디오의 공유되고 있는 특성이 학습됨.

여기서 공유되고 있는 특성: 눈코입위치, 유사한 특성이 학습되도록 유도

디코더에서는 피해자와 소스 특성이 각각 따로 학습되도록유도→ 각 얼굴의 눈 생김새 코생김새 등

latent에서는 외곽이나 눈코입 위치만 학습

converting

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/14b7775d-b6b5-40e1-be84-e9327f16fd78/3a283181-dc98-4169-a32a-04ec88c59838/image.png)

피해자의 얼굴 변환하여

오리지널 의 눈코입 위치 확인하고, 

피해자의 특성을 삽입

피해자의 얼굴이 바뀌어 들어감

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/14b7775d-b6b5-40e1-be84-e9327f16fd78/cfa628f4-b248-43ca-b13f-5f73853b9454/image.png)

1000장에서 만장의 이미지

얼굴파트의 각도와 조명이 다양해야 결과가 좋아짐** 각도와 조명을 보면 좋을듯

deepfakedetection현황

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/14b7775d-b6b5-40e1-be84-e9327f16fd78/a90b29f0-d914-489d-9c95-a29ea65ffe26/image.png)

매프래임마다 얼굴위치를 찾아서 판별- deepclasifier: FaceForensics ICCV

Temporal 비디오에서 프래임간의 연결관계 시간적 특성 탐지 : 프레임간의 연결을 확인하는것 -CVPR Recurrent Convolutional Strategies for Face~ 

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/14b7775d-b6b5-40e1-be84-e9327f16fd78/5eddf820-d275-481c-a82d-b445b1c80642/image.png)

faceforencsic: 각 프래임마다 effnet넣어서 성능

recurrent: cnn+rnn

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/14b7775d-b6b5-40e1-be84-e9327f16fd78/67b22173-13ec-45bf-b607-2a76c5215429/image.png)

xceoptionNet 이 결과가 괜찮은편
