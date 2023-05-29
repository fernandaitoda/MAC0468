#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 16:49:29 2020

@author: fernanda
"""




import cv2 
import numpy as np
import sys

sobelxy = None

def main():
    global sobelxy

    # leia uma imagem
    if len(sys.argv) != 2:
        print("Para usar digite: python rgb.py arq_imagem")
        return
    fname = sys.argv[1]
    img   = cv2.imread(fname)
    
    # mostra imagem
    cv2.imshow("Entrada", img)

    # cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Cinza", gray)

    # suavização
    gblur = cv2.GaussianBlur( gray, (5,5), 0 )

    # sobelx 
    # sobely 
    sobelx = np.abs(cv2.Sobel( gblur, cv2.CV_64F, 1, 0, ksize=5  ))
    sobely = np.abs(cv2.Sobel( gblur, cv2.CV_64F, 0, 1, ksize=5  ))
    sobelxy  = sobelx + sobely

    if 0:
        # usando numpy para normalizar o resultado para o intervalo 0-1
        sobelx = sobelx * (1 / np.max(sobelx))
        sobely = sobely * (1 / np.max(sobely))
        sobelxy = sobelxy * (1 / np.max(sobelxy))
    else:
        # usando opencv para normalizar para 8 bits
        sobelx = cv2.convertScaleAbs( sobelx )
        sobely = cv2.convertScaleAbs( sobely )
        sobelxy = cv2.convertScaleAbs( sobelxy )

    cv2.imshow("Sobel x", sobelx)
    cv2.imshow("Sobel y", sobely)
    cv2.imshow("Sobel xy", sobelxy)

    # binaria
    valor = 70
    r, imgBinX = cv2.threshold( sobelx, valor, 255, cv2.THRESH_BINARY)
    r, imgBinY = cv2.threshold( sobely, valor, 255, cv2.THRESH_BINARY)
    r, imgBinXY = cv2.threshold( sobelxy, valor, 255, cv2.THRESH_BINARY)

    cv2.imshow("Sobel bin x", imgBinX)
    cv2.imshow("Sobel bin y", imgBinY)
    cv2.imshow("Sobel bin xy", imgBinXY)

    cv2.createTrackbar( "trackbar", "Sobel bin xy", valor, 255, on_tracker)
    cv2.waitKey()

def on_tracker( valor ):
    global sobelxy
    r, imgBinXY = cv2.threshold( sobelxy, valor, 255, cv2.THRESH_BINARY)
    cv2.imshow("Sobel bin xy", imgBinXY)

main()