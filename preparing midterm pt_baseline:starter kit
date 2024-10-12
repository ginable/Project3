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

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/14b7775d-b6b5-40e1-be84-e9327f16fd78/089c4845-c149-46d2-8197-756c60dc4e8e/image.png)

train중에서 19.25%가 누락된 데이터 존재.

Unique value 확인

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/14b7775d-b6b5-40e1-be84-e9327f16fd78/3b4abf79-1cdb-4ea6-ad1c-15a1bea0b3c1/image.png)

가장 빈번한 레이블 확인

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/14b7775d-b6b5-40e1-be84-e9327f16fd78/ff067c04-50b1-4155-8b60-ee4a83e5fbd8/image.png)

가장 빈번한 원본 meawm~(6개)이고 Fake비율이 더 많음

Fake, Real 라밸 개수비교(19.25, 80.75)

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/14b7775d-b6b5-40e1-be84-e9327f16fd78/246c5aae-f772-48de-83ef-6163cb2efcac/image.png)

Fake 영상 샘플 확인

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/14b7775d-b6b5-40e1-be84-e9327f16fd78/226fa663-c93b-447b-951c-8550f7aa1300/image.png)

주로 얼굴쪽이 부자연스러운 현상 확인

Face Detection

OpenCV에서 얼굴(정면,측면), 눈, 웃음을 추출하는 기능 가져와서 활용.

- 정면 : 녹색 직사각형
- 눈 : 빨간색 원;
- 미소: 빨간색 사각형;
- 측면: 파란색 직사각형.
