define g = Character("Gavrila", image="gavrila")

default E = 0  # Ekstrovert
default I = 0  # Introvert
default S = 0  # Sensorik
default N = 0  # Intuitif
default T = 0  # Thinking
default F = 0  # Feeling
default J = 0  # Judging
default P = 0  # Perceiving

# Tambahkan bagian init python untuk logika MBTI
init python:
    from collections import deque

    # Dictionary untuk menyimpan skor MBTI
    mbti_preferences = {
        "E": 0,  # Ekstrovert
        "I": 0,  # Introvert
        "S": 0,  # Sensing
        "N": 0,  # Intuition
        "T": 0,  # Thinking
        "F": 0,  # Feeling
        "J": 0,  # Judging
        "P": 0,  # Perceiving
    }

    # Queue untuk menyimpan hasil akhir dari akumulasi
    user_queue = deque()

    # Pohon logika untuk traversal
    mbti_tree = {
        "start": {"E": "EKS", "I": "IN"},
        "EKS": {"S": "SE", "N": "INT"},
        "IN": {"S": "SE", "N": "INT"},
        "SE": {"F": "FEE", "T": "THI"},
        "INT": {"F": "FEE", "T": "THI"},
        "FEE": {"J": "JU", "P": "PER"},
        "THI": {"J": "JU", "P": "PER"},
    }

    def traverse_mbti(current_node="start"):
        result = []  # List untuk menyimpan preferensi pemain (E, S, T, J, dll.)
        path = []  # List untuk menyimpan jalur atau path yang dilalui

    # Tambahkan node awal hanya sekali
        path.append(current_node)

        while user_queue:
            current_choice = user_queue.popleft()  # Mengambil hasil akumulasi
            result.append(current_choice)  # Simpan preferensi pemain

            if current_choice in mbti_tree[current_node]:
                next_node = mbti_tree[current_node][current_choice]

                # Hanya tambahkan next_node jika belum ada dalam path
                if next_node not in path:
                    path.append(next_node)  # Simpan node hasil akhir ke path

                current_node = next_node

                # Jika next_node adalah hasil akhir, tambahkan hasil ke list dan return
                if next_node in ["JU", "PER"]:
                    return "".join(result), path  # Gabungkan semua preferensi jadi satu string MBTI

        return "".join(result), path  # Gabungkan preferensi dan return path jika queue kosong

label start:
    play music "menu.mp3" fadein 2.0 volume 0.5
    scene kuil_kuno with fade
    voice "suara.wav"
    "Langit cerah yang menerangi sebuah kuil misterius di tengah hutan."
    voice "suara.wav"
    "Legenda mengatakan kuil ini mampu mengungkapkan rahasia terdalam kepribadian seseorang melalui serangkaian tantangan"
    voice "suara.wav"
    "Kamu memutuskan untuk memasuki kuil, penasaran dengan apa yang akan kamu temukan tentang dirimu sendiri."

label awal:
    scene isi_kuil with dissolve
    voice "suara.wav"
    "Saat pintu batu berat itu tertutup di belakangmu, suara dalam ruangan bergema:"
    # show logo_suara:
    #     xalign 0.0
    #     yalign 0.2
    voice "1.wav"
    g satu "Selamat datang, Pengembara! Namaku Gavrila !"
    voice "2.wav"
    g "Kamu telah memasuki kawasan 'Temple Of Choice'"
    voice "3.wav"
    g "Untuk keluar dari kuil ini, kamu harus menyelesaikan 4 stage tantangan yang akan mengungkapkan karakter kepribadianmu"
    show tree1:
        xalign 0.5
        yalign 0.5
    voice "4.wav"
    g "Pertama kamu harus melewati tantangan 'EKSIN' lalu selanjutnya ada tantangan 'SEINT' berikutnya ada tantangan 'FEETHI' dan terakhir yaitu 'JUPER'"
    scene mbti with fade
    voice "5.wav"
    g satu "Dan di akhir akan ada satu dari 16 karakter kepribadian yang mencerminkan karakter dirimu, jadi, tunggu apalagi?"
    voice "6.wav"
    g "Silahkan Untuk Melanjutkan Ke Tantangan Pertama"
    #stage 1
    call eksin
    if E > I:
        $ user_queue.append("E")
    else:
        $ user_queue.append("I")
    #stage 2
    call seint
    if S > N:
        $ user_queue.append("S")
    else:
        $ user_queue.append("N")
    #stage 3
    call feethi
    if F > T :
        $ user_queue.append("F")
    else :
        $ user_queue.append("T")
    #stage 4
    call juper
    if J > P:
        $ user_queue.append("J")
    else:
        $ user_queue.append("P")

    # Hasil Akhir
    $ hasil_mbti, path = traverse_mbti()

    if hasil_mbti == "ESFJ":
        call esfj
    elif hasil_mbti == "ESFP":
        call esfp
    elif hasil_mbti == "ESTJ":
        call estj
    elif hasil_mbti == "ESTP":
        call estp
    elif hasil_mbti == "ENFJ":
        call enfj
    elif hasil_mbti == "ENFP":
        call enfp
    elif hasil_mbti == "ENTJ":
        call entj
    elif hasil_mbti == "ENTP":
        call entp
    elif hasil_mbti == "ISFJ":
        call isfj
    elif hasil_mbti == "ISFP":
        call isfp
    elif hasil_mbti == "ISTJ":
        call istj
    elif hasil_mbti == "ISTP":
        call istp
    elif hasil_mbti == "INFJ":
        call infj
    elif hasil_mbti == "INFP":
        call infp
    elif hasil_mbti == "INTJ":
        call intj
    elif hasil_mbti == "INTP":
        call intp
    
    voice "suara.wav"
    "Selamat telah mendapatkan karakter yang mencerminkan kepribadianmu"
    voice "suara.wav"
    "Apakah kamu ingin tahu rahasia bagaimana kamu bisa mendapatkan sebuah karakter di game ini ?"
    menu:
        "Iya, aku penasaran":
            voice "suara.wav"
            "Jadi ketika kamu menjawab pertanyaan tiap stage tantangan hasilnya akan berpengaruh pada hasil akhir penentuan karakter"
            voice "suara.wav"
            "Algoritma yang digunakan yaitu 'Decision tree'"
            scene tree_path with dissolve
            voice "suara.wav"
            "Dan jawaban jawaban kamu tadi memberikan jalur seperti ini ['-> '.join(path)]"
        "Tidak, Terima Kasih":
            return
    voice "suara.wav"
    "Terima Kasih telah memainkan game ini, aku senang sekali kamu bisa mendapatkan karakter yang berkepribadian sama denganmu"
    voice "suara.wav"
    "Sampai Jumpa"

    return
