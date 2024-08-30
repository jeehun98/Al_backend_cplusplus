# C++ BACKEND 파일

## Keras 동작 과정

Keras 는 고수준의 신경망 라이브러리, 주로 Python 으로 작성, TensorFlow 와 같은 백엔드를 활용하여 작업한다. 

Keras 자체는 백엔드와 직접적으로 상호작용하지 않고, Keras API 를 통해 백엔드 엔진을 호출한다. 

백엔드 동작을 이해하기 위해 백엔드의 C++ 코드 베이스를 살펴보는 것이 필요하다.

### TensorFlow 백엔드 예시

- Core Components (tensorflow/core/) : TensorFlow 의 코어 컴포넌트, 텐서 조작, 그래프 실행, 연산자 등의 코드가 있음

- Operations (tensorflow/core/ops/) : 다양한 텐서 연산의 정의

- Kernels (tensorflw/core/kernels/) : 특정 연산이 CPU 나 GPU 에서 어떻게 실행되는지 정의

## Keras 와 C++ 연관성

Keras 의 API 는 TensorFlow 와 같은 백엔드에 종속적이다. TensorFlow 의 Python API 를 통해서 간접적으로 호출하게 된다. 


## PyTorch 의 계산방법

동적 계산 그래프 dynamic computation graph 를 기반, 자동 미분 엔진, 동일하게 C++ 백엔드


# CUDA(C++) 를 이용한 GPU 연산

- CUDA 장치 선택

- 텐서와 모델의 GPU 이동

- 멀티 GPU 연산

- CUDA 스트림과 동기화

- 메모리 관리

- 혼합 정밀도 학습