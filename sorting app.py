import streamlit as st
import time

st.title ("visualisasi sorting")

#1. kontrol UI input data & Algoritma
col1, col2 = st.colums(2)
algo= col1.selecbox("pilihalgortima", ["bubble short", "seection sort", "insertion sort"])
user_input = col2.text_input ("input data(pisahkan koma)", "85, 60,92,75,88")

#2. keterangan algoritma dinamis 
if algo == "buble shprt":
    st.info ("🎈buble short**: membandingkan elemen bersebelahan & menukarnya jika salah urutan. elemen terbesar 'melembung' ke akhir.")
elif algo == "select sort":
    st.info(" 🎈 **selection sort**: memilih elemen terkecil dari bagian yang belum terurut, lalu menurkarnya ke posisi paling depan. ")
elif algo == "insertion sort":
    st. info("🎈** insertion sort**: bekerja seperti mengurutkan kartu; menyisipkan leemen satu per satu ke posisi yang tepat dibagian yang sudah terurut.")

#3. keamanaan input(parsing teks ke angka)
try:
    data = [int(x.strip()) for x in user_input.split(",") if x.strip()]
except ValueError:
    st.eror("gagal! pastikan anda hanya memasukan angka.")
    st.stop()

#4. area gambar grafik
chart = st.empty()
chart.bar_chart(data)

#5. tombol &logika sorting utama
if st.button("mulai urutkan", type="primary"):
    n = len(data)

    if algo== "buble short":
        for i in range(n):
            for j in range(0,n-i-1):
                if data [j]>data[j+1]:
                    data [j], data[j+1]= data[j+1],data[j]
                    #tukar posisi
                    chart.bar_chart(data)
                    time.sleep(0.2)

    elif algo == "select sort":
        for i in range(n):
            min_idx = i
            for j in range(i+1,n):
                if data[j]<data[min_idx]:
                    min_idx=j
            data[i], data[min_idx]= data [min_idx], data[i]
            #tukar kedepan 
            chart.bar_chart(data)
            time.sleep(0.2)

    elif algo == "insertion sort":
        for i in range(1,n):
            key = data[i]
            j = i-1
            while j>= 0 and data[j]>key:
                data[j+1]= data[j] #geser ke kanan 
                chart.bar_chart(data)
                time.sleep(0.2)
            data[j+1]= key
            chart.bar_chart(data)
            time.sleep(0.2)

    st.success(f"sorting selesai!hasil:{data}")
