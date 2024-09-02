#include <pybind11/pybind11.h>
#include <pybind11/stl.h>  // 이 헤더 파일을 추가합니다.
#include <vector>

std::vector<int> add_vectors(const std::vector<int>& vec1, const std::vector<int>& vec2) {
    std::vector<int> result;
    if (vec1.size() == vec2.size()) {
        result.reserve(vec1.size());
        for (size_t i = 0; i < vec1.size(); ++i) {
            result.push_back(vec1[i] + vec2[i]);
        }
    }
    return result;
}

PYBIND11_MODULE(vector_add, m) {
    m.def("add_vectors", &add_vectors, "A function that adds two vectors");
}
