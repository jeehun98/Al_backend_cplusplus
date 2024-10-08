# CPP, PY, PYD 파일간 관계

## Pybind11

C++ 코드를 Pythno 에서 쉽게 호출할 수 있도록 해주는 라이브러리, C++ 에서 작성된 고성능 코드를 Python 에서 바로 사용할 수 있다. 

### 역할 및 관계

- C++ 파일 (cpp 파일):

    - C++ 로 작성된 소스 코드가 들어있다. 이 파일에는 Python 에서 사용할 함수나 클래스가 구현되어 있다. 

    - Pybind11 을 사용하여 이 C++ 함수나 클래스를 Python 에서 사용할 수 있도록 바인딩하는 코드도 이 파일에 포함된다.

- Pybind11

    - C++ 코드를 Python 에서 호출할 수 있도록 바인딩을 생성해 준다. 이를 통해 C++ 함수나 클래스를 Pythno 모듈로 변환한다. 

    - Pybind11 을 사용하면 C++ 코드에 추가적인 바인딩 코드를 작성하고 이를 통해 C++ 함수가 Python 에서 직접 호출될 수 있게 된다.

- PYD 파일

    - Window 에서 사용하는 Python 확장 모듈 파일, 컴파일된 C++ 코드로, Python 에서 모듈처럼 import 하여 사용할 수 있다.

    - PYD 파일은 CPP 파일을 컴파일한 결과물로, Pybind11 을 사용해 생성된다. 이 파일은 Python 모듈처럼 동작하며, Python 코드에서 import 하여 C++ 함수를 사용할 수 있다.

- Python 파일

    - Python 코드가 들어 있는 파일, PYD 파일을 import 하여 C++ 에서 작성된 함수를 호출할 수 있다.

    