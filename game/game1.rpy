label game_1:
    voice "9.wav"
    g semangat "Permainan ini dinamakan Klik Cepat!"
    voice "10.wav"
    g "Tugasmu adalah mengklik tombol sebanyak mungkin dalam waktu 10 detik."
    jump klik_cepat

label klik_cepat:
    # Variabel awal
    $ score = 0
    $ timer = 10
    $ game_active = True

    # "Permainan akan dimulai dalam..."
    # "3..."
    # pause 1
    # "2..."
    # pause 1
    # "1..."
    # pause 1   
    # "Mulai!"
    # Tampilkan countdown secara otomatis
    window hide
    show text "{size=100}{color=#03b90c}3...{/color}{/size}" at truecenter
    $ renpy.pause(1)

    show text "{size=100}{color=#03b90c}2...{/color}{/size}" at truecenter
    $ renpy.pause(1)

    show text "{size=100}{color=#03b90c}1...{/color}{/size}" at truecenter
    $ renpy.pause(1)

    show text "{size=100}{color=#03b90c}Mulai!{/color}{/size}" at truecenter
    $ renpy.pause(1)

    # Hapus teks setelah selesai
    hide text
    
    # Tampilkan layar permainan
    show screen klik_game
    # Timer berjalan
    while timer > 0:
        $ renpy.pause(1)  # Pause selama 1 detik
        $ timer -= 1  # Kurangi timer setiap detik

    # Permainan selesai
    $ game_active = False
    hide screen klik_game
    voice "suara.wav"
    "Waktu habis!"
    voice "suara.wav"
    "Kamu berhasil mengklik tombol sebanyak [score] kali."

    # Penilaian hasil
    if score < 20:
        voice "suara.wav"
        "Menarik! Performamu menunjukkan pendekatan yang lebih hati-hati dan terencana"
        voice "suara.wav"
        "Tipe MBTI seperti INTJ atau INFJ sering menunjukkan karakteristik ini"
    elif score < 40:
        voice "suara.wav"
        "Hebat! Performamu menunjukkan keseimbangan yang baik antara kecepatan dan kontrol"
        voice "suara.wav"
        "Tipe MBTI seperti ENTP atau ESFP sering menunjukkan karakteristik seperti ini"
    else:
        voice "suara.wav"
        "Wow! Kamu memiliki kecepatan reaksi yang luar biasa! Ini menunjukkan bahwa kamu memiliki Kemampuan fokus yang baik"
        voice "suara.wav"
        "Tipe MBTI yang seperti ini yaitu ESTP dan ISTP, yang dikenal dengan kemampuan adaptasi dan keterampilan motorik yang baik"

    voice "suara.wav"
    "Terima kasih telah bermain!"
    return

# Screen untuk gameplay
screen klik_game:
    # Latar permainan
    # frame:
    #     align (0.5, 0.5)
    #     xsize 400
    #     ysize 300
    #     background Solid("#F0F0F0")
    
    # Timer
    text "Waktu: [timer] detik" align (0.5, 0.1) size 30 color "#FF0000"

    # Skor
    text "Skor: [score]" align (0.5, 0.2) size 30 color "#00FF00"

    # Tombol klik
    # textbutton "Klik Saya!" action SetVariable("score", score + 1) align (0.5, 0.5) focus_mask True
    imagebutton:
        idle "button_idle.png"  # Gambar saat tombol diam
        hover "button_hover.png"  # Gambar saat tombol di-hover
        action SetVariable("score", score + 1)  # Aksi menambah skor
        align (0.5, 0.5)  # Posisikan tombol di tengah layar

# Background (opsional)
image bg_room = Solid("#D0D0D0")
