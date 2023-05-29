#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 17:22:45 2020

@author: fernanda
"""

import sys
import cv2

def main ():

    img = cv2.imread ("entrada.png")
    if img is None:
        print ("Não consegui abrir o arquivo: ", img)
        return
        
    
    
main ()