default correct_order = ["merah", "kuning", "hijau"]  # Urutan yang benar

label game_2:
    # Variabel awal
    $ stack = []  # List untuk menyimpan urutan barang
    $ max_height = 3  # Maksimal jumlah barang yang bisa diatur
    voice "22.wav"
    g semangat "Nama Permainan ini yaitu 'tebak urutan barang!'"
    voice "23.wav"
    g "Tugas kamu adalah menebak urutan barang yang benar berdasarkan petunjuk yang diberikan."
    voice "suara.wav"
    "Kamu bisa menambah atau mengeluarkan barang sesuai kebutuhan untuk mengatur urutan yang benar."
    voice "suara.wav"
    "Ingat ! barang yang disusun yaitu ada 3 warna barang"
    voice "suara.wav"
    "Pentunjuk : warna pelangi"

    # Loop permainan
    while True:
        # Tampilkan visualisasi barang-barang yang sudah diatur
        if stack:
            $ i = 0  # Pastikan variabel `i` dideklarasikan dengan benar
            voice "suara.wav"
            "Urutan barang yang kamu susun saat ini:"
            while i < len(stack):  # Gunakan perulangan while
                $ item = stack[i]  # Ambil item berdasarkan indeks
                voice "suara.wav"
                "Barang [i+1]: [item]"  # Menampilkan informasi barang
                $ i += 1  # Increment indeks

        else:
            voice "suara.wav"
            "Belum ada barang yang kamu susun."

        # Menu untuk mengeluarkan barang
        menu:
            "Tambah barang ke urutan":
                # Menu Tambah Barang
                if len(stack) < max_height:
                    voice "suara.wav"
                    "Pilih barang untuk ditambahkan ke urutan:"
                    window hide

                    # Pilihan barang dengan klik gambar
                    screen pilih_barang():
                        vbox:
                            align (0.5, 0.5)  # Posisikan di tengah layar
                            spacing 20  # Jarak antar gambar
                            imagebutton:
                                idle "images/green.png"  # Gambar untuk barang hijau
                                hover "images/green_hover.png"  # Gambar saat di-hover
                                action [SetVariable("stack", stack + ["hijau"]), Return()]  # Tambahkan ke stack
                            imagebutton:
                                idle "images/red.png"  # Gambar untuk barang merah
                                hover "images/red_hover.png"  # Gambar saat di-hover
                                action [SetVariable("stack", stack + ["merah"]), Return()]  # Tambahkan ke stack
                            imagebutton:
                                idle "images/yellow.png"  # Gambar untuk barang kuning
                                hover "images/yellow_hover.png"  # Gambar saat di-hover
                                action [SetVariable("stack", stack + ["kuning"]), Return()]  # Tambahkan ke stack

                    call screen pilih_barang
                else:
                    voice "suara.wav"
                    "Urutan sudah penuh! Kamu tidak bisa menambah barang lagi."
                    return

                # Batas maksimal barang

            "Keluarkan barang dari urutan":
                if stack:
                    $ barang = stack.pop()
                    voice "suara.wav"
                    "Barang [barang] berhasil dikeluarkan dari urutan."
                else:
                    voice "suara.wav"
                    "Urutan kosong! Tidak ada barang yang bisa dikeluarkan."

            "Cek apakah urutan sudah benar":
                if stack == correct_order:
                    voice "suara.wav"
                    "Selamat! Urutan barangmu sudah benar!"
                    return
                else:
                    voice "suara.wav"
                    "Urutan barangmu belum benar, coba lagi."
    
    voice "suara.wav"
    "Apakah kamu suka permainan ini?"
    menu:
        "Ya, saya suka permainan ini":
            voice "suara.wav"
            "Jika kamu menyukai permainan ini, ini menunjukkan bahwa kamu suka tantangan dan mengatur segala sesuatu dengan teliti."
        "Tidak, saya tidak suka permainan ini":
            voice "suara.wav"
            "Jika kamu tidak suka permainan ini, kamu mungkin lebih menyukai permainan yang lebih fleksibel dan terbuka"
    voice "suara.wav"
    "Terima kasih telah bermain!"
    return