# Project configuration
cmake_minimum_required(VERSION 3.15)
project(${SKBUILD_PROJECT_NAME} LANGUAGES CXX)

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE "Release")
    message(STATUS "Build type not specified, using Release by default")
endif()

if(MSVC)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /W3")
    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /O2 /EHsc")
else()
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wno-reorder")
    set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -pg -DLLVM_ENABLE_ASSERTIONS=ON")
    set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -O3")
endif()

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(PYBIND11_NEWPYTHON ON)
find_package(pybind11 CONFIG REQUIRED)

include_directories(${CMAKE_SOURCE_DIR}/nanoflann/include)

set(BINDINGS nanoflann_ext)
pybind11_add_module(${BINDINGS} src/pynanoflann.cpp)

install(TARGETS ${BINDINGS} LIBRARY DESTINATION pynanoflann)
