#////////////////////////////////////////////////////////////////////////////
#//
#//  This file is part of RTIMULib
#//
#//  Copyright (c) 2014, richards-tech
#//
#//  Permission is hereby granted, free of charge, to any person obtaining a copy of
#//  this software and associated documentation files (the "Software"), to deal in
#//  the Software without restriction, including without limitation the rights to use,
#//  copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
#//  Software, and to permit persons to whom the Software is furnished to do so,
#//  subject to the following conditions:
#//
#//  The above copyright notice and this permission notice shall be included in all
#//  copies or substantial portions of the Software.
#//
#//  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
#//  INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
#//  PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#//  HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
#//  OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#//  SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

#// The cmake support was based on work by Moritz Fischer at ettus.com.
#// Original copyright notice:
#
# Copyright 2014 Ettus Research LLC
#

# Set target system name.
SET (CMAKE_SYSTEM_NAME Linux)

# Set compiler name.
SET (CMAKE_C_COMPILER aarch64-linux-gnu-gcc)
SET (CMAKE_CXX_COMPILER /usr/bin/aarch64-linux-gnu-g++)


# search for programs in the build host directories
SET(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
# for libraries and headers in the target directories
SET(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
SET(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)

# Set output/install directory to safe place.
SET (CMAKE_INSTALL_PREFIX ${CMAKE_BINARY_DIR}/output)

#set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -rpath-link=/lib/arm-linux-gnueabihf")
set(THREADS_PTHREAD_ARG 0)
#set(CMAKE_CROSSCOMPILING ON CACHE BOOL "Cross-compiling" FORCE)

########################################################################
IF(${CMAKE_SOURCE_DIR} STREQUAL ${CMAKE_BINARY_DIR})
    MESSAGE(FATAL_ERROR "Prevented in-tree built. This is bad practice.")
ENDIF(${CMAKE_SOURCE_DIR} STREQUAL ${CMAKE_BINARY_DIR})

INCLUDE(CMakeDependentOption)
INCLUDE(FeatureSummary)

########################################################################
# Project setup
########################################################################
CMAKE_MINIMUM_REQUIRED(VERSION 2.8.9)
PROJECT(RTIMULib CXX)
# Set minimum cmake version required for cross-compiling to work.
cmake_minimum_required(VERSION 2.6)
# Build with rm CMakeCache.txt; cmake -DCMAKE_TOOLCHAIN_FILE=/home/crosscompile/dev/raspberry_pi/CMakeCross.txt .. 

OPTION(BUILD_GL "Build RTIMULibGL" OFF)
OPTION(BUILD_DRIVE "Build RTIMULibDrive" ON)
OPTION(BUILD_DRIVE10 "Build RTIMULibDrive10" ON)
OPTION(BUILD_DRIVE11 "Build RTIMULibDrive11" ON)
OPTION(BUILD_CAL "Build RTIMULibCal" ON)
OPTION(BUILD_DEMO "Build RTIMULibDemo" OFF)
CMAKE_DEPENDENT_OPTION(BUILD_DEMOGL "Build RTIMULibDemoGL" OFF
                       "BUILD_GL" OFF)

ADD_FEATURE_INFO(RTIMULibGL BUILD_GL "")
ADD_FEATURE_INFO(RTIMULibDrive BUILD_DRIVE "App that shows how to use the RTIMULib library in a basic way.")
ADD_FEATURE_INFO(RTIMULibDrive10 BUILD_DRIVE10 "App that shows to use  pressure/temperature sensors.")
ADD_FEATURE_INFO(RTIMULibDrive11 BUILD_DRIVE11 "App that shows to use  pressure/temperature/humidity sensors.")
ADD_FEATURE_INFO(RTIMULibCal BUILD_CAL "Command line calibration tool for the magnetometers and accelerometers.")
ADD_FEATURE_INFO(RTIMULibDemo BUILD_DEMO "GUI app that displays the fused IMU data in real-time")
ADD_FEATURE_INFO(RTIMULibDemoGL BUILD_DEMOGL "RTIMULibDemo with OpenGL visualization")

INCLUDE_DIRECTORIES(${CMAKE_CURRENT_SOURCE_DIR}/../RTIMULib)

ADD_SUBDIRECTORY(${CMAKE_CURRENT_SOURCE_DIR}/../RTIMULib RTIMULib)

IF(BUILD_GL)
    INCLUDE_DIRECTORIES(${CMAKE_CURRENT_SOURCE_DIR}/RTIMULibGL)
    INCLUDE_DIRECTORIES(${CMAKE_CURRENT_SOURCE_DIR}/RTIMULibGL/QtGLLib)
    INCLUDE_DIRECTORIES(${CMAKE_CURRENT_SOURCE_DIR}/RTIMULibGL/VRWidgetLib)
    ADD_SUBDIRECTORY(${CMAKE_CURRENT_SOURCE_DIR}/RTIMULibGL)
ENDIF(BUILD_GL)

IF(BUILD_DRIVE)
    ADD_SUBDIRECTORY(RTIMULibDrive)
ENDIF(BUILD_DRIVE)

IF(BUILD_DRIVE10)
    ADD_SUBDIRECTORY(RTIMULibDrive10)
ENDIF(BUILD_DRIVE10)

IF(BUILD_DRIVE11)
    ADD_SUBDIRECTORY(RTIMULibDrive11)
ENDIF(BUILD_DRIVE11)

IF(BUILD_CAL)
# Set path(s) to search for libraries/binaries/headers.
SET (CMAKE_FIND_ROOT_PATH /home/crosscompile/dev/raspberry_pi/rootfs/)

# Ensure only cross-compiler directories are searched.
SET (ONLY_CMAKE_FIND_ROOT_PATH TRUE)
    ADD_SUBDIRECTORY(RTIMULibCal)
ENDIF(BUILD_CAL)

IF(BUILD_DEMO)
    ADD_SUBDIRECTORY(RTIMULibDemo)
ENDIF(BUILD_DEMO)

IF(BUILD_DEMOGL)
    ADD_SUBDIRECTORY(RTIMULibDemoGL)
ENDIF(BUILD_DEMOGL)

PRINT_ENABLED_FEATURES()

MESSAGE(STATUS "Using install prefix: ${CMAKE_INSTALL_PREFIX}")
