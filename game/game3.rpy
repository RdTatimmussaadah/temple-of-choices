# label game_3:
#     # Variabel awal
#     $ queue = ["Ali", "Budi", "Cici", "Deni", "Eka"]  # Daftar pelanggan yang mengantri
#     $ max_queue = 5  # Maksimal panjang antrian
#     $ current_customer_index = 0  # Untuk melacak pelanggan yang dilayani
#     voice "28.wav"
#     g semangat "Nama permainannya yaitu Atur Antrian!"
#     voice "29.wav"
#     g "Tugas kamu adalah melayani pelanggan sesuai urutan yang benar."
#     "Perhatikan urutan mengantrinya !!!"
    
#     # Loop permainan
#     while queue:
#         # Menampilkan antrian saat ini
#         voice "suara.wav"
#         "Orang yang mengantri saat ini adalah: [', '.join(queue)]."
#         voice "suara.wav"
#         "Perhatikan Huruf kapital dan huruf kecilnya !"
        
#         # Menanyakan nama pelanggan yang akan dilayani pertama
#         voice "suara.wav"
#         $ pelanggan = renpy.input("Masukkan nama pelanggan yang akan dilayani pertama:").strip()

#         # Memeriksa apakah pelanggan yang dimasukkan sesuai dengan urutan pertama
#         if pelanggan == queue[0]:
#             # Melayani pelanggan yang sesuai urutan
#             $ queue.pop(0)  # Mengeluarkan pelanggan pertama dari antrian
#             voice "suara.wav"
#             "Pelanggan [pelanggan] telah dilayani dan keluar dari antrian."
#         else:
#             voice "suara.wav"
#             "Salah! Kamu harus melayani [queue[0]] terlebih dahulu."
#     voice "suara.wav"
#     "Semua pelanggan telah dilayani!"
#     voice "suara.wav"
#     "Terima kasih telah bermain!"

#     return
image ali = "images/ali.png"
image budi = "images/budi.png"
image cici = "images/cici.png"
image deni = "images/deni.png"
image eka = "images/eka.png"
image selesai = "images/selesai.png"

label game_3:
    # Variabel awal
    $ queue = ["Ali", "Budi", "Cici", "Deni", "Eka"]  # Daftar pelanggan yang mengantri
    $ max_queue = 5  # Maksimal panjang antrian
    voice "28.wav"
    g semangat "Nama permainannya yaitu Atur Antrian!"
    voice "29.wav"
    g "Tugas kamu adalah melayani pelanggan sesuai urutan yang benar."
    voice "suara.wav"
    "Perhatikan urutan mengantrinya !!!"
    
    # Loop permainan
    while queue:
        $ i = 0
        window hide
        
        # Menampilkan gambar pelanggan satu per satu berdasarkan antrian
        if queue[i] == "Ali":
            scene ali
        elif queue[i] == "Budi":
            scene budi
        elif queue[i] == "Cici":
            scene cici
        elif queue[i] == "Deni":
            scene deni
        elif queue[i] == "Eka":
            scene eka

        voice "suara.wav"
        "Orang yang mengantri saat ini adalah: [', '.join(queue)]."
        voice "suara.wav"
        "Perhatikan huruf kapital dan huruf kecilnya!"
        
        # Menanyakan nama pelanggan yang akan dilayani pertama
        voice "suara.wav"
        $ pelanggan = renpy.input("Masukkan nama pelanggan yang akan dilayani pertama:").strip()

        # Memeriksa apakah pelanggan yang dimasukkan sesuai dengan urutan pertama
        if pelanggan == queue[0]:
            # Mengeluarkan pelanggan dari antrian dan menghilangkan gambarnya
            $ queue.pop(0)  # Mengeluarkan pelanggan pertama dari antrian
            # window hide  # Menyembunyikan gambar yang sudah dilayani
            voice "suara.wav"
            "Pelanggan [pelanggan] telah dilayani dan keluar dari antrian."
            scene selesai
        else:
            voice "suara.wav"
            "Salah! Kamu harus melayani [queue[0]] terlebih dahulu."

    # Permainan selesai
    scene selesai
    voice "suara.wav"
    "Semua pelanggan telah dilayani!"
    voice "suara.wav"
    "Game ini dapat melatih kemampuan kamu untuk mematuhi urutan, mengatur prioritas, dan mengikuti instruksi dengan teliti."
    voice "suara.wav"
    "Biasanya, orang yang menikmati permainan ini dan mengikuti urutan dengan disiplin memiliki kepribadian yang lebih terstruktur, cenderung memiliki sifat Judging (J) dalam MBTI."
    voice "suara.wav"
    "Mereka lebih suka mengikuti aturan, menyelesaikan tugas sesuai urutan, dan merasa nyaman dengan jadwal yang teratur."
    voice "suara.wav"
    "Di sisi lain, orang yang kurang menikmati permainan ini mungkin lebih suka fleksibilitas dan spontanitas."
    voice "suara.wav"
    "Terima kasih telah bermain!"

    return
