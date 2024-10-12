직접 Edit 및 수행 
https://www.kaggle.com/code/kkkkksw/deepfake-starter-kit/edit

EDA

파일유형 확인

```
Train samples: 401
Test samples: 400
Extensions: ['mp4', 'json']
```

누락 데이터 확인

![image](https://github.com/user-attachments/assets/729bf4b7-3f67-4a10-a22d-99ed399da25d)


train중에서 19.25%가 누락된 데이터 존재.

Unique value 확인
![image](https://github.com/user-attachments/assets/134aedae-bab9-4700-baaa-731182d1571c)

가장 빈번한 레이블 확인
![image](https://github.com/user-attachments/assets/b9aa629a-d45d-45b8-932c-b2aea6aee71f)


가장 빈번한 원본 meawm~(6개)이고 Fake비율이 더 많음

![image](https://github.com/user-attachments/assets/d7f8de1f-5f36-4e52-81a0-c9b08aaf87d7)

Fake, Real 라밸 개수비교(19.25, 80.75)


Fake 영상 샘플 확인

![image](https://github.com/user-attachments/assets/ebd61bd9-8fe3-4cf9-9d81-3db1942274e5)

얼굴쪽 부자연스러운 현상 확인

Face Detection

OpenCV에서 얼굴(정면,측면), 눈, 웃음을 추출하는 기능 가져와서 활용.
![image](https://github.com/user-attachments/assets/2abd7b4f-c1ee-4c45-8d70-6a4a679327ae)

- 정면 : 녹색 직사각형
- 눈 : 빨간색 원;
- 미소: 빨간색 사각형;
- 측면: 파란색 직사각형.
