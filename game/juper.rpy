label juper:
    voice "suara.wav"
    "Setelah melewati tantangan terakhir di Ruang Penilaian, pintu besar di hadapanmu terbuka perlahan."
    scene pintu
    voice "39.wav"
    g satu "Sekarang kamu berada di Tantangan Terakhir"
    voice "8.wav"
    g "Tapi sebelum anda bisa masuk ke stage ini, kamu harus menyelesaikan permainan terlebih dahulu"
    call game_4
    call tugas_harian
    return

label tugas_harian:
    scene tugas_harian with dissolve
    voice "suara.wav"
    "Kamu melangkah masuk ke sebuah ruangan luas dengan meja besar di tengahnya. Di atas meja, terdapat jam pasir raksasa dan tumpukan dokumen berserakan."
    voice "41.wav"
    g satu "Di ruangan ini, kita akan melihat bagaimana caramu mengatur waktu, mengelola prioritas, dan merencanakan tindakanmu.'"
    voice "suara.wav"
    "Jam pasir mulai berputar, menandakan dimulainya tantangan keempat yaitu juper."
    voice "suara.wav"
    "Salah satu dokumen yang berserak yaitu merupakan daftar tugas tugas yang panjang."
    voice "42.wav"
    g satu "Bayangkan kamu menghadapi hari yang penuh dengan tugas penting. Bagaimana kamu memulai harimu?"
    menu:
        "Aku membuat daftar prioritas dan mengikuti jadwal dengan teratur.":
            $ J += 1
            voice "suara.wav"
            "Kamu menyusun rencana untuk hari itu, memastikan semua tugas memiliki urutan yang jelas."
        "Aku mengalir dengan keadaan dan mengerjakan tugas yang terasa paling mendesak.": 
            $ P += 1
            voice "suara.wav"
            "Kamu memutuskan untuk tidak terlalu terikat dengan daftar, melainkan mengikuti keadaan dan kebutuhan saat itu."
    voice "suara.wav"
    "Bayangan itu memudar, dan suara kuil mengarahkanmu ke tantangan berikutnya."
    call menyelesaikan_proyek
    return

label menyelesaikan_proyek:
    scene menyelesaikan_proyek with dissolve
    voice "suara.wav"
    "Di tengah ruangan, muncul sebuah meja lain dengan berbagai alat dan bahan. Dan kamy membayangkan dirimu sedang menyelesaikan sebuah proyek besar."
    voice "43.wav"
    g satu "Saat bekerja pada sebuah proyek besar, bagaimana caramu menyelesaikannya?"
    menu:
        "Aku merencanakan langkah-langkah yang harus diambil dan menyelesaikannya secara bertahap.":
            $ J += 1
            voice "suara.wav"
            "Kamu memastikan setiap langkah diambil secara sistematis dan mengikuti rencana yang sudah disusun."
        "Aku mulai bekerja dan menyesuaikan prosesnya seiring waktu.": 
            $ P += 1
            voice "suara.wav"
            "Kamu membiarkan proyek berkembang secara alami, menyesuaikan langkah-langkah sesuai kebutuhan."
    voice "suara.wav"
    "Setelah beberapa saat, bayangan itu menghilang, dan pintu menuju tantangan berikutnya terbuka."
    call menghadapi_perubahan
    return

label menghadapi_perubahan:
    scene menghadapi_perubahan with dissolve
    voice "suara.wav"
    "Ruangan berikutnya dipenuhi oleh kertas kertas catatan yang ternyata merupakan rencana perjalanan."
    voice "44.wav"
    g satu "Bayangkan dirimu menghadapi rencana perjalanan yang tiba-tiba berubah secara mendadak." 
    voice "45.wav"
    g satu "Ketika rencanamu berubah mendadak seperti itu, apa yang akan kamu lakukan?"
    menu:
        "Aku mencoba menemukan cara untuk tetap mengikuti rencana awal sebisa mungkin.":
            $ J += 1
            voice "suara.wav"
            "Kamu berusaha keras untuk menjaga rencana tetap berjalan sesuai jadwal, meskipun ada perubahan yang harus dilakukan."
        "Aku menyesuaikan diri dengan situasi baru dan mencari solusi yang fleksibel.": 
            $ P += 1
            voice "suara.wav"
            "Kamu dengan cepat beradaptasi dengan perubahan dan mencari cara baru untuk menyelesaikan masalah."
    voice "suara.wav"
    "Bayangan itu perlahan memudar, dan pintu lain di ruangan itu terbuka."
    call keputusan_kecil
    return

label keputusan_kecil:
    scene keputusan_kecil with dissolve
    voice "suara.wav"
    "Di sudut ruangan, kamu melihat dua jalur bercabang."
    voice "46.wav"
    g satu "Bagaimana kamu membuat keputusan kecil dalam hidupmu sehari-hari?"
    menu:
        "Aku membuat keputusan dengan cepat dan memastikan itu sejalan dengan rencana jangka panjangku.":
            $ J += 1
            voice "suara.wav"
            "Kamu merasa bahwa setiap keputusan kecil harus mendukung gambaran besar dari rencanamu."
        "Aku memutuskan berdasarkan suasana hati atau apa yang terasa tepat pada saat itu.": 
            $ P += 1
            voice "suara.wav"
            "Kamu membiarkan keputusan kecil ditentukan oleh insting atau kebutuhan langsung."
    voice "suara.wav"
    "Setelah membuat pilihanmu, jalur yang kamu pilih membawa kamu ke tantangan terakhir."
    call menyusun_acara
    return

label menyusun_acara:
    scene menyusun_acara with dissolve
    voice "47.wav"
    g satu "Di ruangan terakhir, bayangkan kamu dihadapkan dengan situasi di mana kamu harus menyusun sebuah acara penting dalam waktu singkat."
    voice "suara.wav"
    "Di depanmu, terdapat dua opsi: sebuah jadwal terperinci dengan semua langkah yang perlu dilakukan, dan sebuah papan kosong untuk ide-ide spontan."
    voice "48.wav"
    g satu "Bagaimana kamu memulai penyusunan acara ini?"
    menu:
        "Aku mulai dengan membuat jadwal terperinci dan mengatur setiap detailnya.": 
            $ J += 1
            voice "suara.wav"
            "Kamu merasa bahwa rencana yang jelas dan struktur yang baik adalah kunci keberhasilan acara."
        "Aku memulai dengan ide-ide spontan dan menyesuaikan detailnya nanti.": 
            $ P += 1
            voice "suara.wav"
            "Kamu membiarkan kreativitas mengalir dan percaya bahwa struktur akan terbentuk seiring berjalannya waktu."
    if J > P:
        voice "49.wav"
        g "Kamu merupakan seseorang yang lebih menyukai perencanaan dan struktur dalam hidupnya."
    else:
        voice "50.wav"
        g "Kamu merupakan seseorang yang lebih fleksibel dan terbuka terhadap perubahan."
    return
