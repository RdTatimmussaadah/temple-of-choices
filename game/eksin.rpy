label eksin:
    scene pintu
    voice "7.wav"
    g dua "Sekarang kamu berada di Tantangan Pertama"
    voice "8.wav"
    g "Tapi sebelum kamu bisa masuk ke stage ini, kamu harus menyelesaikan permainan terlebih dahulu"
    call game_1
    voice "11.wav"
    g dua "Sekarang kamu bisa melanjutkan perjalananmu !"
    jump ruang_cermin
label ruang_cermin:
    scene ruang_cermin with dissolve
    voice "suara.wav"
    "Kamu melangkah ke dalam ruangan dengan dinding penuh cermin. Refleksi di setiap cermin menunjukkan sisi berbeda dari dirimu."
    voice "suara.wav"
    "Beberapa cermin memantulkan dirimu yang energik dan penuh semangat, sementara yang lain menunjukkan dirimu yang tenang dan pendiam."
    voice "12.wav"
    g dua "Bagaimana kau bereaksi terhadap refleksimu?"
    menu:
        "Mendekati cermin yang menunjukkan dirimu yang bersemangat dan percaya diri.":
            $ E += 1
            voice "suara.wav"
            "Kamu tersenyum lebar pada refleksimu, merasa siap untuk menghadapi apa pun."
        "Merenung di depan cermin yang menunjukkan dirimu yang tenang dan introspektif.":
            $ I += 1
            voice "suara.wav"
            "Kamu memandang dalam-dalam pada refleksimu, mencoba memahami dirimu lebih jauh."
    voice "suara.wav"
    "Cermin di depanmu memudar, dan pintu menuju tantangan berikutnya terbuka."
    jump taman_bunga

label taman_bunga:
    scene taman_bunga with dissolve
    voice "suara.wav"
    "Kamu melangkah ke taman yang indah. Jalan setapak yang dihiasi bunga-bunga yang berbeda."
    voice "13.wav"
    g dua "Bagaimana kamu memilih jalanmu?"
    menu:
        "Berjalan cepat di setiap jalan setapak, menikmati keindahan taman sepenuhnya.":
            $ E += 1
            voice "suara.wav"
            "Kamu bersemangat menjelajahi seluruh taman, mencium aroma bunga yang beragam."
        "Memilih satu jalan setapak dan menikmati keindahan bunga secara perlahan.":
            $ I += 1
            voice "suara.wav"
            "Kamu berjalan perlahan, menikmati setiap detail bunga di sepanjang jalan."
    voice "suara.wav"
    "Setelah beberapa waktu, kamu tiba di sebuah ruangan lain dengan batu-batu besar."
    jump ruang_batu

label ruang_batu:
    scene ruang_batu with dissolve
    voice "suara.wav"
    "Ruangan ini dipenuhi dengan batu-batu besar, beberapa membentuk pola yang jelas, sementara yang lain terlihat acak."
    voice "14.wav"
    g dua "Bagaimana kamu menghadapi tantangan ini?"
    menu:
        "Menyusun batu dengan cepat, mencoba berbagai kombinasi secara spontan.":
            $ E += 1
            voice "suara.wav"
            "Kamu langsung bergerak, mencoba kombinasi yang terasa paling masuk akal."
        "Mengamati batu-batu dengan hati-hati untuk menemukan pola yang tersembunyi.":
            $ I += 1
            voice "suara.wav"
            "Kamu memeriksa setiap batu, memastikan pola yang kamu pilih benar-benar logis."
    voice "suara.wav"
    "Dengan usaha keras, pintu lain terbuka, dan kamu melangkah ke dalam labirin suara."
    jump labirin_suara

label labirin_suara:
    scene labirin_suara with dissolve
    voice "suara.wav"
    "Labirin ini penuh dengan suara-suara aneh, dari bisikan ramah hingga gema yang mengganggu."
    voice "15.wav"
    g dua "Bagaimana kamu menavigasi labirin ini?"
    menu:
        "Mengikuti suara-suara ramah dengan antusias, percaya diri bahwa itu adalah petunjuk.":
            $ E += 1
            voice "suara.wav"
            "Kamu mengikuti suara-suara yang terasa nyaman dan akrab, melangkah dengan percaya diri."
        "Menghindari suara-suara mengganggu, mencari jalan yang paling tenang dan damai.":
            $ I += 1
            voice "suara.wav"
            "Kamu menghindari suara-suara yang terlalu keras, mencari ketenangan di tengah kebingungan."
    voice "suara.wav"
    "Setelah perjalanan yang penuh tantangan, kamu mencapai ruangan terakhir."
    jump ruang_akhir_intro_extro

label ruang_akhir_intro_extro:
    scene ruang_akhir with dissolve
    voice "suara.wav"
    "Di ruangan terakhir, sebuah peti tertutup menunggumu."
    voice "16.wav"
    g dua "Apa yang paling penting bagimu?"
    menu:
        "Hubungan dengan orang lain dan pengalaman baru.":
            $ E += 1
            voice "suara.wav"
            "Kamu menyadari betapa pentingnya interaksi sosial dan petualangan bagi dirimu."
        "Waktu untuk merenung dan kedamaian batin.":
            $ I += 1
            voice "suara.wav"
            "Kamu merasa bahwa momen-momen introspektif adalah hal yang paling berharga."
    voice "suara.wav"
    "Peti itu terbuka, dan cahaya keluar darinya"
    if E > I:
        voice "17.wav"
        g dua "Kamu merupakan seseorang yang lebih condong bersemangat dan menyukai interaksi sosial."
        voice "18.wav"
        g dua "Namun, perjalananmu belum selesai. Ada tantangan lain yang menunggumu untuk memahami dirimu lebih jauh."
    else:
        voice "19.wav"
        g dua "Kamu merupakan seseorang yang lebih condong tenang dan menikmati kedamaian batin."
        voice "18.wav"
        g dua "Namun, perjalananmu belum selesai. Ada tantangan lain yang menunggumu untuk memahami dirimu lebih jauh."
    return


