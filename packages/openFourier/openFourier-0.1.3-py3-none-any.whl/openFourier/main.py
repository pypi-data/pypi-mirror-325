# -*- coding: utf-8 -*-

import numpy as np

def ww_amplitude_spectrum(image):
    """
    입력 이미지의 2D 푸리에 변환을 수행하고 진폭 스펙트럼을 반환합니다.
    
    Parameters:
        image (numpy.ndarray): 입력 이미지 배열 (2D grayscale 또는 3D RGB)
        
    Returns:
        numpy.ndarray: 정규화된 진폭 스펙트럼 이미지
    """
    # 입력 이미지가 3D(RGB)인 경우 grayscale로 변환
    if len(image.shape) == 3:
        image = np.mean(image, axis=2)
    
    # 2D 푸리에 변환 수행
    f_transform = np.fft.fft2(image)
    
    # 주파수 성분을 중앙으로 이동
    f_shift = np.fft.fftshift(f_transform)
    
    # 진폭 스펙트럼 계산
    amplitude_spectrum = np.abs(f_shift)
    
    # log scale로 변환하여 시각화 개선
    amplitude_spectrum = np.log1p(amplitude_spectrum)
    
    # 0-1 범위로 정규화
    amplitude_spectrum = (amplitude_spectrum - np.min(amplitude_spectrum)) / \
                        (np.max(amplitude_spectrum) - np.min(amplitude_spectrum))
    
    return amplitude_spectrum