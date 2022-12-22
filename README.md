# P2_Komnum_E11

Praktikum 2 Komputasi Numerik (Implementasi Integrasi Romberg)

Kelompok 11

1. Fathan Abi Karami (5025211156)
2. Vito Febrian Ananta (5025211224)


Praktikum ini merupakan implementasi metode integrasi romberg pada program python. Metode integrasi romberg ini bergantung terhadap metode integrasi trapezoida. Metode ini dilakukan dengan cara menggabungkan 2 aproksimasi integrasi level sebelumnya. Berikut adalah persamaan unik yang membuat aproksimasi metode integrasi romberg lebih baik dibandingkan metode integrasi trapezoida. 
![rumusromberg](https://user-images.githubusercontent.com/115033527/209135783-5609cc7d-e571-4040-8007-3b5ce42bec66.png

Metode integrasi trapezoida dipakai dalam program ini untuk menentukan nilai aproksimasi level pertama (kolom pertama). Berikut adalah ilustrasi matriks dari metode integrasi romberg.
![rumusromberg2](https://user-images.githubusercontent.com/115033527/209138156-dd4c09e5-1d8b-4144-b4d6-c84dcddd283e.png)

Selain itu, pada progam ini metode integrasi trapezoida juga digunakan sebagai perbandingan dengan metode integrasi romberg. Output berupa hasil integrasi dari sebuah fungsi dengan batas atas, batas bawah, dan iterasi tertentu beserta hasil tiap iterasinya. Output juga menampilkan perbandingan antara metode trapezoid dan metode romberg berserta Er-nya masing-masing.

contoh output pada terminal
![Screenshot_20221222_164226](https://user-images.githubusercontent.com/90834092/209105737-2e1ada32-a87a-4dcb-8218-bde468adec05.png)
