cmake_minimum_required(VERSION 3.10)

# 프로젝트 이름과 C++ 표준 설정
project(AL_BACKEND_CPLUSPLUS VERSION 1.0 LANGUAGES CXX)

# C++ 표준 설정
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# 컴파일러 플래그 설정 (정적 링크 추가)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -static")

# 실행 파일 추가
add_executable(MyExecutable main.cpp)
