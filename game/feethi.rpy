label feethi:
    scene pintu
    voice "27.wav"
    g 4 "Sekarang kamu berada di Tantangan Ketiga"
    voice "8.wav"
    g 4 "Tapi sebelum kamu bisa masuk ke stage ini, kamu harus menyelesaikan permainan terlebih dahulu"
    call game_3 from _call_game_3
    call ruang_penilaian from _call_ruang_penilaian
    return

label ruang_penilaian:
    scene ruangan_kuil with fade
    voice "suara.wav"
    "Kamu tiba di sebuah ruangan yang didalamnya terdapat timbangan yang bersinar lembut, seolah menunggu keputusan yang akan kamu buat." 
    voice "suara.wav"
    "Sebuah pintu di belakangmu tertutup rapat, sementara pintu lain di depanmu terkunci, hanya akan terbuka setelah kamu menyelesaikan tantangan ini."
    voice "30.wav"
    g 4 "Jawablah pertanyaan di setiap sudut ruangan ini, dan biarkan timbangan mengungkapkan pilihan hatimu."
    voice "suara.wav"
    "Dengan napas dalam, kamu melangkah lebih jauh ke dalam ruangan, bersiap menghadapi pertanyaan yang akan menguji hatimu dan pikiranmu."
    call konflik_kelompok from _call_konflik_kelompok
    return

label konflik_kelompok:
    scene konflik_kelompok with dissolve
    voice "suara.wav"
    "Di satu sudut ruangan, sebuah bayangan muncul, memperlihatkan adegan konflik dalam kelompok kerja."
    voice "31.wav"
    g 4 "Bayangkan kamu adalah pemimpin kelompok ini. Apa yang akan kamu lakukan?"
    menu:
        "Menganalisis masalah secara logis dan mencari solusi terbaik untuk semua pihak.": 
            $ T += 1
            voice "suara.wav"
            "Kamu mencoba memahami akar masalah, mengevaluasi solusi yang mungkin, dan menyusun strategi untuk menyelesaikan konflik dengan efisien."
        "Berbicara dengan setiap anggota kelompok, mencoba memahami perasaan mereka dan membangun harmoni.": 
            $ F += 1
            voice "suara.wav"
            "Kamu fokus mendengarkan setiap anggota, berusaha memastikan semua orang merasa dihargai sebelum mencari solusi."
    voice "suara.wav"
    "Bayangan itu memudar, dan timbangan bergerak sedikit. Pintu lain terbuka, mengundangmu melangkah ke tantangan berikutnya."
    call memilih_topik from _call_memilih_topik
    return

label memilih_topik:
    scene memilih_topik with dissolve
    voice "suara.wav"
    "Di depanmu muncul dua tumpukan buku besar dengan label berbeda: 'Topik Berbasis Data' dan 'Topik dengan Nilai Emosional'."
    voice "32.wav"
    g 4 "Jika kamu harus memilih topik untuk penelitian penting, mana yang akan kamu pilih?"
    menu:
        "Memilih topik berbasis data yang dapat menghasilkan analisis yang kuat dan jelas.": 
            $ T += 1
            voice "suara.wav"
            "Kamu memilih tumpukan buku 'Topik Berbasis Data', merasa yakin bahwa data yang kuat adalah kunci keberhasilan."
        "Memilih topik dengan nilai emosional yang memberikan dampak besar bagi kehidupan banyak orang.": 
            $ F += 1
            voice "suara.wav"
            "Kamu memilih tumpukan buku 'Topik dengan Nilai Emosional', percaya bahwa dampak emosional lebih penting dari sekadar angka."
    voice "suara.wav"
    "Kedua tumpukan buku menghilang, dan pintu baru terbuka untuk tantangan berikutnya."
    call keberhasilan_proyek from _call_keberhasilan_proyek
    return

label keberhasilan_proyek:
    scene keberhasilan_proyek with dissolve
    voice "suara.wav"
    "Di tengah ruangan, ada meja dengan dua dokumen berbeda. Salah satu dokumen menunjukkan laporan hasil proyek yang sempurna, sementara dokumen lain berisi catatan penghargaan untuk setiap anggota tim."
    voice "33.wav"
    g 4 "Bagaimana kamu menilai keberhasilan sebuah proyek?"
    menu:
        "Berdasarkan kualitas hasil akhir dan pencapaian tujuan proyek.": 
            $ T += 1
            voice "suara.wav"
            "Kamu memilih dokumen hasil akhir, merasa bahwa keberhasilan proyek terletak pada pencapaian yang nyata dan terukur."
        "Berdasarkan bagaimana setiap anggota tim merasa dihargai dan terlibat.": 
            $ F += 1
            voice "suara.wav"
            "Kamu memilih dokumen penghargaan, percaya bahwa keberhasilan sejati adalah ketika semua orang merasa dihargai."
    voice "suara.wav"
    "Dokumen itu berubah menjadi debu, dan pintu ke tantangan berikutnya terbuka."
    call umpan_balik from _call_umpan_balik
    return

label umpan_balik:
    scene umpan_balik with dissolve
    voice "suara.wav"
    "Sebuah bayangan di dinding menunjukkan seorang teman yang bertanya padamu tentang pendapatmu mengenai hasil kerjanya."
    voice "34.wav"
    g 4 "Bagaimana kamu memberikan umpan balik?"
    menu:
        "Memberikan kritik yang jujur dan spesifik untuk membantu teman itu berkembang.": 
            $ T += 1
            voice "suara.wav"
            "Kamu dengan hati-hati menjelaskan kelemahan dalam pekerjaan temanmu, berharap itu membantu mereka menjadi lebih baik."
        "Memberikan dukungan dan pujian untuk menghargai usaha mereka.": 
            $ F += 1
            voice "suara.wav"
            "Kamu memberi pujian atas usaha mereka, percaya bahwa semangat dan motivasi lebih penting daripada kesempurnaan."
    voice "suara.wav"
    "Bayangan itu menghilang, dan pintu terakhir terbuka."
    call keputusan_penting from _call_keputusan_penting
    return

label keputusan_penting:
    scene keputusan_penting with dissolve
    voice "suara.wav"
    "Di hadapanmu, ada dua pintu besar. Satu pintu bercahaya terang, menampilkan angka dan data, sementara pintu lainnya dihiasi dengan pemandangan yang hangat dan nyaman."
    voice "35.wav"
    g 4 "Ketika harus membuat keputusan besar, mana yang lebih penting bagimu?"
    menu:
        "Fakta dan data yang tersedia untuk memastikan keputusan yang logis.": 
            $ T += 1
            voice "suara.wav"
            "Kamu memilih pintu bercahaya terang, percaya bahwa fakta dan data adalah panduan terbaik untuk setiap keputusan."
        "Bagaimana keputusan tersebut akan memengaruhi dirimu dan orang lain secara emosional.": 
            $ F += 1
            voice "suara.wav"
            "Kamu memilih pintu dengan pemandangan hangat, percaya bahwa dampak emosional lebih penting daripada sekadar logika."
    
    if F > T :
        voice "36.wav"
        g 4 "Kamu merupakan orang yang mengutamakan nilai-nilai pribadi dan emosi dalam pengambilan keputusan, serta berfokus pada dampak terhadap orang lain dan hubungan interpersonal."
        voice "37.wav"
        g 4 "Silahkan lanjutkan ke tantangan terakhir melewati pintu yang kamu pilih"
    else :
        voice "38.wav"
        g 4 "Kamu merupakan orang yang mengutamakan logika dan analisis dalam pengambilan keputusan, serta berfokus pada fakta dan efisiensi tanpa terlalu mempertimbangkan perasaan orang lain."
        voice "37.wav"
        g 4 "Silahkan lanjutkan ke tantangan terakhir melewati pintu yang kamu pilih"
    return