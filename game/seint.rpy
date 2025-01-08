label seint:
    scene pintu with fade
    voice "20.wav"
    g 3 "Sekarang kamu berada di Tantangan Kedua"
    voice "21.wav"
    g "Sekarang kamu harus menyelesaikan permainan terlebih dahulu sebelum melanjutkan"
    call game_2
    call lorong_ukiran
    return

label lorong_ukiran:
    scene lorong_ukiran with dissolve
    voice "suara.wav"
    "Kamu melangkah masuk dan menemukan lorong panjang dengan ukiran-ukiran kuno di dindingnya."
    voice "suara.wav"
    "Ukiran ini tampaknya menyimpan pesan tersembunyi, mungkin petunjuk untuk membuka pintu di ujung lorong."
    voice "suara.wav"
    "Namun, kamu hanya punya sedikit waktu sebelum lorong ini menjadi gelap sepenuhnya."
    voice "24.wav"
    g dua "Apa yang akan kamu lakukan ?"
    menu:
        "Memeriksa setiap ukiran satu per satu untuk menemukan pola.":
            $ S += 1
            voice "suara.wav"
            "Kamu memeriksa ukiran-ukiran itu dengan cermat, mencatat setiap detail kecil untuk menemukan pola tersembunyi."
        "Merenungkan keseluruhan arti ukiran dan mencoba memahami cerita besar di baliknya.":
            $ N += 1
            voice "suara.wav"
            "Kamu melangkah mundur dan mencoba memahami gambaran besar dari ukiran itu, berharap menemukan maknanya secara intuitif."
    voice "suara.wav"
    "Setelah beberapa saat, kamu mendengar suara pintu di ujung lorong terbuka perlahan."
    call jejak_lantai
    return

label jejak_lantai:
    scene jejak_lantai with dissolve
    voice "suara.wav"
    "Kamu tiba di ruangan berikutnya yang lantainya dipenuhi jejak-jejak kaki. Jejak itu bercabang menjadi dua arah."
    voice "suara.wav"
    "Satu jalur memiliki jejak-jejak yang jelas terlihat, sementara jalur lain terlihat kosong tanpa tanda apa pun."
    voice "24.wav"
    g dua "Apa yang akan kamu lakukan ?"
    menu:
        "Mengukur bentuk dan arah jejak untuk memilih jalur yang lebih logis.":
            $ S += 1
            voice "suara.wav"
            "Kamu mengamati bentuk jejak dan memeriksa arah yang paling masuk akal untuk dilewati."
        "Mengandalkan firasat untuk memilih jalan yang menurutmu benar.":
            $ N += 1
            voice "suara.wav"
            "Kamu mempercayai firasatmu dan memilih jalan kosong, berharap ini adalah pilihan yang benar."
    voice "suara.wav"
    "Setelah memilih jalur, kamu melangkah hati-hati ke depan. Jalan yang kamu pilih membawa kamu ke ruangan berikutnya."
    call ritual_cahaya
    return

label ritual_cahaya:
    scene ritual_cahaya with dissolve
    voice "suara.wav"
    "Kamu tiba di sebuah ruangan yang penuh dengan cahaya dari kristal-kristal besar di tengah dinding besar."
    voice "suara.wav"
    "Namun, pola cahaya tampaknya tidak lengkap. Beberapa kristal lainnya berserakan di lantai, dan kamu harus menyelesaikan pola ini agar pintu berikutnya terbuka."
    voice "24.wav"
    g dua "Apa yang akan kamu lakukan ?"
    menu:
        "Mengatur ulang kristal di lantai sesuai pola cahaya.":
            $ S += 1
            voice "suara.wav"
            "Kamu dengan hati-hati menyusun ulang kristal yang berserakan, mencoba mencocokkannya dengan pola yang terlihat."
        "Mencoba memahami hubungan pola cahaya dengan cerita atau makna di balik kuil ini.":
            $ N += 1
            voice "suara.wav"
            "Kamu merenungkan arti pola cahaya tersebut, mencoba mengaitkannya dengan cerita besar tentang kuil ini."
    voice "suara.wav"
    "Cahaya dari kristal bersinar lebih terang, dan sebuah pintu tersembunyi terbuka dengan suara gemuruh."
    call tumpukan_batu
    return

label tumpukan_batu:
    scene tumpukan_batu with dissolve
    voice "suara.wav"
    "Di tengah ruangan berikutnya, kamu menemukan tumpukan batu berbentuk piramida."
    voice "suara.wav"
    "Tumpukan ini tampaknya menyembunyikan mekanisme rahasia untuk membuka jalan keluar, tetapi kamu harus mencari cara untuk mengaktifkannya."
    voice "24.wav"
    g dua "Apa yang akan kamu lakukan ?"
    menu:
        "Memeriksa batu dengan teliti untuk menemukan mekanisme tersembunyi.":
            $ S += 1
            voice "suara.wav"
            "Kamu memeriksa setiap batu di piramida dengan cermat, mencoba menemukan celah atau tombol tersembunyi."
        "Mencoba menghubungkan simbol di batu dengan cerita atau legenda kuil ini.":
            $ N += 1
            voice "suara.wav"
            "Kamu mencoba memahami simbol-simbol di batu, berharap menemukan kaitannya dengan cerita kuil."
    voice "suara.wav"
    "Setelah kamu menyelesaikan teka-teki, sebuah jalan tersembunyi terbuka, membawa kamu ke tantangan terakhir."
    call puzzle_game
    return

label puzzle_game:
    scene peti_rahasia with dissolve
    voice "suara.wav"
    "Di ujung ruangan terakhir, kamu menemukan sebuah peti dengan tiga roda angka yang terkunci."
    voice "suara.wav"
    "Untuk membukanya, kamu harus memutar roda angka dengan benar. Pilihanmu akan menentukan apakah peti terbuka atau tetap terkunci."
    voice "24.wav"
    g dua "Apa yang akan kamu lakukan ?"
    menu:
        "Menganalisis pola angka untuk menemukan logikanya.":
            $ S += 1
            voice "suara.wav"
            "Kamu memeriksa roda angka dengan hati-hati, mencoba memahami logika di balik polanya."
        "Menebak angka berdasarkan intuisi.":
            $ N += 1
            voice "suara.wav"
            "Kamu mengikuti firasatmu dan memutar roda angka ke kombinasi yang menurutmu tepat."
    voice "suara.wav"
    "Setelah kamu memutar roda angka..."
    if S > N:
        scene peti_terbuka with dissolve
        voice "25.wav"
        g dua "Pilihan logikamu ternyata benar."
        voice "suara.wav"
        "Dan akhirnya tantangan kedua ini telah selesai dan kamu dapat melanjutkan ke tantangan berikutnya"
    else:
        scene peti_terbuka with dissolve
        voice "26.wav"
        g dua "Intuisimu berhasil membimbingmu ke kombinasi yang tepat."
        voice "suara.wav"
        "Dan akhirnya tantangan kedua ini telah selesai dan kamu dapat melanjutkan ke tantangan berikutnya"
    return