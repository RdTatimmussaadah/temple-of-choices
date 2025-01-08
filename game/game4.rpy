label game_4:
    # Inisialisasi Variabel
    $ low = 1  # Rentang bawah tetap
    $ high = 100  # Rentang atas tetap
    $ attempts = 0
    # Menggunakan input tanpa validasi
    voice "40.wav"
    g "Aku akan menebak angka rahasiamu yang tersembunyi."
    voice "suara.wav"
    $ max_attempts = renpy.input("Berikan saja berapa langkah maksimal yang boleh digunakan saya untuk menebak angka rahasiamu? (Rekomendasi: 7-10)").strip()
    voice "suara.wav"
    "Baik kalau begitu, 'Pilihlah angka rahasiamu dalam rentang 1 hingga 100, dan hanya ada [max_attempts] langkah untuk menebaknya.'"

    # Loop untuk proses binary search oleh kuil
    while attempts < int(max_attempts):  # Menggunakan max_attempts sebagai integer
        $ mid = (low + high) // 2  # Binary search langkah
        $ attempts += 1
        voice "suara.wav"
        "'Langkah ke-[attempts], pencari angka! Apakah angka rahasiamu [mid]?'"

        menu:
            "Lebih besar":
                $ low = mid + 1
                voice "suara.wav"
                "Baiklah, ternyata angka rahasiamu lebih besar dari [mid]. Berarti harus mencari lebih tinggi lagi."
            "Lebih kecil":
                $ high = mid - 1
                voice "suara.wav"
                "Baiklah, ternyata angka rahasiamu lebih kecil dari [mid]. Berarti harus mencari lebih rendah lagi."
            "Ya Benar":
                voice "suara.wav"
                # Pengguna menentukan apakah tebakan benar
                "Yey akhirnya angkamu tertebak dengan [attempts] langkah ! Angka rahasiamu adalah [mid] !!"
                return
    # Jika kuil gagal menebak dalam langkah yang ditentukan
    voice "suara.wav"
    "Sayang sekali, aku gagal menebak angka rahasiamu dalam [max_attempts] langkah."
    voice "suara.wav"
    "Aku akan bermain lagi nanti untuk menguji keberanian dan kebijaksanaanku."
    voice "suara.wav"
    "Game ini menguji ketepatanmu dalam memberikan petunjuk kepada sistem untuk menebak angka rahasiamu."
    voice "suara.wav"
    "Jika kamu merasa nyaman memberikan jawaban yang cepat, artinya kamu lebih memilih proses yang terstruktur dan jelas. Tipe Judging (J)"
    voice "suara.wav"
    "Namun, jika kamu merasa lebih fleksibel dalam memberi petunjuk atau tidak terlalu memikirkan langkah-langkahnya secara mendetail berarti kamu bisa jadi lebih condong ke tipe Perceiving (P)"
    voice "suara.wav"
    "Terima kasih telah bermain"
    return
