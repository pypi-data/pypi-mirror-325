
# openFourier

A Python package for computing 2D Fourier transform amplitude spectrum of images.

## Installation

You can install the package using pip:

```bash
pip install openFourier

## Usage

import cv2
import openFourier as of

# 이미지 로드
image = cv2.imread('example.png')

# 진폭 스펙트럼 계산
spectrum = of.ww_amplitude_spectrum(image)

# 결과 저장
cv2.imwrite('amplitude_spectrum.png', spectrum * 255)
