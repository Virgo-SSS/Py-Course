#Soal
#Posisi sebuah benda dinyatakan dengan persamaan: r = {7ti + (9t + 3tÂ²)j} m. 
#Setelah benda bergerak selama 2,5 sekon, kelajuannya menjadi. . . .
# A. 15 m/s
# B. 20 m/s
# C. 25 m/s
# D. 30 m/s
# E. 35 m/s

# Harus install numpy & sympy pakai : 
# pip install sympy
# pip install numpy

import math
from sympy import *
import numpy as np
def menu():
        menu =  '''
Program GLB 2 Dimensi
================================
1. Menghitung GLB
2. Keluar
================================
'''
        return menu

simpan_t = []
simpan_i = []
simpan_j = []

while True:
    print(menu())        
    pilihan = input("Masukkan Pilihan: ")
    if pilihan == "1":
        print("===================================================================")
        s = input("Masukkan Simbol Aritmatika (+/-): ")
        t = symbols('t')
        a = input("Masukkan Suku i: ")
        ski = diff(a)
        ai = parse_expr(a)
        b = input("Masukkan Suku j: ")
        skj = diff(b)
        bj = parse_expr(b)

        print1 = (f"Hasil Turunannya adalah: ({ski})i {s} ({skj})j")
        print(print1)
        print("===================================================================")
        waktu = float(input("Masukkan Nilai Batas Waktu (t): "))

        str_expr1 = (ski)
        expr1 = sympify(str_expr1)
        pr1 = expr1.subs(t, waktu)
        m = ('%f' % pr1).rstrip('0').rstrip('.')
        
        str_expr2 = (skj)
        expr2 = sympify(str_expr2)
        pr2 = expr2.subs(t, waktu)
        n = ('%f' % pr2).rstrip('0').rstrip('.')
        
        print(m,'i',s,n,'j')

        pow1 = pow(pr1,2)
        pow2 = pow(pr2,2)

        plus = pow1 + pow2
        print("Hasil Kecepatannya adalah ",math.sqrt(plus),'m/s')
        print("===================================================================")
        
        for i in np.arange(1,waktu+0.5,0.5):
            simpan_t.append(i)

            expr1 = (ai)
            pr1 = expr1.subs(t, i)
            round1 = float(round(pr1,2))
            simpan_i.append(round1)
    
            expr2 = (bj)
            pr2 = expr2.subs(t, i)
            round2 = float(round(pr2,2))
            simpan_j.append(round2)

        for waktu in range (len(simpan_i)):
            print('Pada t =',simpan_t[waktu],'Posisi benda adalah',simpan_i[waktu],'x',s,simpan_j[waktu],'y')

        print()
        print("Posisi benda pada t =",i,"adalah",round1,'x',s,round2,'y')
        print("===================================================================")

    else: break