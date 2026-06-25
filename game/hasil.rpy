# transform di_atas_gambar:
#     xalign 0.5  # Teks berada di tengah secara horizontal
#     yalign 0.2  # Teks berada di atas (atur ini sesuai kebutuhan)

label esfj:
    call hasil from _call_hasil
    show esfj:
        xalign 0.5
        yalign 0.3
    voice "Sophia_1.wav"
    "Hai Namaku Sophia! aku memiliki MBTI ESFJ"
    voice "Sophia_2.wav"
    "Aku ternyata mirip dengamu, kita memiliki kepribadian yang sama yaitu seseorang yang sangat peduli dengan orang lain dan suka membantu mereka."
    voice "Sophia_3.wav"
    "kita juga nyaman berada di tengah keramaian, berinteraksi dalam situasi sosial atau kerja tim."
    voice "Sophia_4.wav"
    "selain itu kita berkepribadian empatik dan berusaha mendukung orang secara emosional."
    voice "Sophia_5.wav"
    "dan juga menyukai hal-hal yang terstruktur dan terorganisir, serta fokus pada menjaga keharmonisan dalam hubungan, sering kali lebih memperhatikan kebutuhan orang lain daripada diriku sendiri."
    voice "Sophia_6.wav"
    "Membantu orang dan membuat mereka merasa dihargai adalah hal yang memberi kepuasan bagi kita."
    hide esfj
    return
label esfp:
    call hasil from _call_hasil_1
    show esfp:
        xalign 0.5
        yalign 0.3
    voice "Zara_1.wav"
    "Hai Namaku Zara! Aku memiliki MBTI ESFP"
    voice "Zara_2.wav"
    "Aku ternyata mirip dengamu, kita memiliki kepribadian yang sama yaitu seseorang yang sangat peduli dengan orang lain dan suka membantu mereka."
    voice "Zara_3.wav"
    "Kita juga suka berada di tengah keramaian, berinteraksi dalam situasi sosial atau kerja tim."
    voice "Zara_4.wav"
    "Selain itu, kita berkepribadian empatik dan berusaha mendukung orang secara emosional."
    voice "Zara_5.wav"
    "Kita juga menikmati petualangan dan pengalaman baru yang menyenangkan, serta memiliki energi yang tinggi."
    voice "Zara_6.wav"
    "Kita mudah beradaptasi dengan lingkungan dan bisa menyebarkan keceriaan kepada orang di sekitar kita."
    voice "Zara_7.wav"
    "Membantu orang dan membuat mereka merasa dihargai adalah hal yang memberi kepuasan bagi kita."
    hide esfp
    return
label estj:
    call hasil from _call_hasil_2
    show estj:
        xalign 0.5
        yalign 0.3
    voice "Catherine_1.wav"
    "Hai, Namaku Catherine! Aku memiliki MBTI ESTJ"
    voice "Catherine_2.wav"
    "Aku ternyata mirip dengamu, kita memiliki kepribadian yang sama yaitu seseorang yang sangat terorganisir dan menghargai aturan serta struktur."
    voice "Catherine_3.wav"
    "Kita lebih suka bekerja dalam lingkungan yang jelas dan efisien."
    voice "Catherine_4.wav"
    "Selain itu, kita berfokus pada pencapaian hasil yang praktis dan berusaha untuk membawa semua orang menuju tujuan yang sama."
    voice "Catherine_5.wav"
    "Kita senang membuat keputusan yang cepat dan bertanggung jawab atas tugas yang diberikan."
    hide estj
    return
label estp:
    call hasil from _call_hasil_3
    show estp:
        xalign 0.5
        yalign 0.3
    voice "Liam_1.wav"
    "Hai, Namaku Liam! Aku memiliki MBTI ESTP"
    voice "Liam_2.wav"
    "Aku ternyata mirip dengamu, kita memiliki kepribadian yang sama yaitu seseorang yang suka berpetualang dan menghadapi tantangan baru."
    voice "Liam_3.wav"
    "Kita sangat terfokus pada pengalaman langsung dan lebih suka bertindak daripada berteori."
    voice "Liam_4.wav"
    "Selain itu, kita cenderung sangat praktis dan berorientasi pada hasil."
    voice "Liam_5.wav"
    "Kita suka berinteraksi dengan orang-orang dan menikmati suasana yang dinamis dan penuh energi."
    hide estp
    return
label enfj:
    call hasil from _call_hasil_4
    show enfj:
        xalign 0.5
        yalign 0.3
    voice "Eleanor_1.wav"
    "Hai, Namaku Eleanor! Aku memiliki MBTI ENFJ"
    voice "Eleanor_2.wav"
    "Aku ternyata mirip dengamu, kita memiliki kepribadian yang sama yaitu seseorang yang sangat peduli dengan orang lain dan berusaha memahami perasaan mereka."
    voice "Eleanor_3.wav"
    "Kita cenderung menjadi pemimpin yang inspiratif, yang dapat mengarahkan orang lain untuk mencapai tujuan bersama."
    voice "Eleanor_4.wav"
    "Selain itu, kita suka membimbing dan memberi dukungan kepada orang-orang yang membutuhkan."
    voice "Eleanor_5.wav"
    "Kita sangat menghargai hubungan yang mendalam dan berusaha untuk menciptakan harmoni dalam kelompok."
    hide enfj
    return
label enfp:
    call hasil from _call_hasil_5
    show enfp:
        xalign 0.5
        yalign 0.3
    voice "Summer_1.wav"
    "Hai, Namaku Summer! Aku memiliki MBTI ENFP"
    voice "Summer_2.wav"
    "Aku ternyata mirip dengamu, kita memiliki kepribadian yang sama yaitu seseorang yang penuh energi dan ide-ide kreatif."
    voice "Summer_3.wav"
    "Kita suka bertemu orang baru dan berbicara tentang berbagai topik."
    voice "Summer_4.wav"
    "Selain itu, kita sangat menghargai kebebasan pribadi dan selalu mencari peluang untuk mengeksplorasi hal-hal baru."
    voice "Summer_5.wav"
    "Kita bersemangat untuk memotivasi orang lain dan sering kali menjadi sumber inspirasi dalam lingkungan kita."
    hide enfp
    return
label entj:
    call hasil from _call_hasil_6
    show entj:
        xalign 0.5
        yalign 0.3
    voice "Maximus_1.wav"
    "Hai, Namaku Maximus! Aku memiliki MBTI ENTJ"
    voice "Maximus_2.wav"
    "Aku ternyata mirip dengamu, kita memiliki kepribadian yang sama yaitu seseorang yang ambisius dan berorientasi pada tujuan."
    voice "Maximus_3.wav"
    "Kita cenderung menjadi pemimpin alami yang mampu mengorganisir orang untuk mencapai hasil yang maksimal."
    voice "Maximus_4.wav"
    "Selain itu, kita senang merencanakan masa depan dan membuat keputusan yang efisien dan efektif."
    voice "Maximus_5.wav"
    "Kita lebih suka bekerja dengan orang yang memiliki pemikiran yang logis dan praktis."
    hide entj
    return
label entp:
    call hasil from _call_hasil_7
    show entp:
        xalign 0.5
        yalign 0.3
    voice "Cleo_1.wav"
    "Hai, Namaku Cleo! Aku memiliki MBTI ENTP"
    voice "Cleo_2.wav"
    "Aku ternyata mirip dengamu, kita memiliki kepribadian yang sama yaitu seseorang yang suka berdiskusi dan berdebat."
    voice "Cleo_3.wav"
    "Kita cenderung melihat segala sesuatu dari berbagai sudut pandang dan suka mengeksplorasi ide-ide baru."
    voice "Cleo_4.wav"
    "Selain itu, kita senang berinovasi dan mencari cara untuk memperbaiki sistem yang ada."
    voice "Cleo_5.wav"
    "Kita lebih suka memecahkan masalah dengan pendekatan kreatif dan berpikir out of the box."
    hide entp
    return
label isfj:
    call hasil from _call_hasil_8
    show isfj:
        xalign 0.5
        yalign 0.3
    voice "Ethan_1.wav"
    "Hai, Namaku Ethan! Aku memiliki MBTI ISFJ"
    voice "Ethan_2.wav"
    "Aku ternyata mirip dengamu, kita memiliki kepribadian yang sama yaitu seseorang yang sangat peduli dengan orang lain dan berusaha menjaga keharmonisan dalam hubungan."
    voice "Ethan_3.wav"
    "Kita juga sangat menghargai tradisi dan nilai-nilai keluarga."
    voice "Ethan_4.wav"
    "Selain itu, kita suka melakukan pekerjaan yang bermanfaat bagi orang lain dan berusaha untuk memberikan dukungan yang konsisten."
    voice "Ethan_5.wav"
    "Kita lebih suka bekerja dalam lingkungan yang stabil dan terstruktur."
    hide isfj
    return
label isfp:
    call hasil from _call_hasil_9
    show isfp:
        xalign 0.5
        yalign 0.3
    voice "Poppy_1.wav"
    "Hai, Namaku Poppy! Aku memiliki MBTI ISFP"
    voice "Poppy_2.wav"
    "Aku ternyata mirip dengamu, kita memiliki kepribadian yang sama yaitu seseorang yang menghargai keindahan dan pengalaman seni."
    voice "Poppy_3.wav"
    "Kita lebih suka menjalani hidup dengan cara yang tenang dan tidak terlalu terstruktur."
    voice "Poppy_4.wav"
    "Selain itu, kita cenderung lebih menikmati waktu untuk diri sendiri dan merasa nyaman dalam kesendirian."
    voice "Poppy_5.wav"
    "Kita juga sangat peduli dengan perasaan orang lain dan berusaha menjaga keharmonisan dalam hubungan."
    hide isfp
    return
label istj:
    call hasil from _call_hasil_10
    show istj:
        xalign 0.5
        yalign 0.3
    voice "Victor_1.wav"
    "Hai, Namaku Victor! Aku memiliki MBTI ISTJ"
    voice "Victor_2.wav"
    "Aku ternyata mirip dengamu, kita memiliki kepribadian yang sama yaitu seseorang yang sangat terorganisir dan menghargai keteraturan."
    voice "Victor_3.wav"
    "Kita cenderung mengikuti aturan yang ada dan merasa nyaman dengan rutinitas yang jelas."
    voice "Victor_4.wav"
    "Selain itu, kita sangat menghargai tanggung jawab dan selalu berusaha memenuhi kewajiban dengan tepat waktu."
    voice "Victor_5.wav"
    "Kita lebih suka bekerja dengan cara yang sistematis dan berorientasi pada detail."
    hide istj
    return
label istp:
    call hasil from _call_hasil_11
    show istp:
        xalign 0.5
        yalign 0.3
    voice "Blake_1.wav"
    "Hai, Namaku Blake! Aku memiliki MBTI ISTP"
    voice "Blake_2.wav"
    "Aku ternyata mirip dengamu, kita memiliki kepribadian yang sama yaitu seseorang yang sangat praktis dan suka memecahkan masalah secara langsung."
    voice "Blake_3.wav"
    "Kita cenderung berfokus pada tindakan dan lebih suka bekerja dengan tangan atau dalam situasi yang membutuhkan keahlian teknis."
    voice "Blake_4.wav"
    "Selain itu, kita sangat menikmati kebebasan pribadi dan sering kali merasa lebih nyaman dalam situasi yang tidak terstruktur."
    voice "Blake_5.wav"
    "Kita juga suka mengeksplorasi dan mencoba hal-hal baru yang menantang."
    hide istp
    return
label infj:
    call hasil from _call_hasil_12
    show infj:
        xalign 0.5
        yalign 0.3
    voice "Jasper_1.wav"
    "Hai, Namaku Jasper! Aku memiliki MBTI INFJ"
    voice "Jasper_2.wav"
    "Aku ternyata mirip dengamu, kita memiliki kepribadian yang sama yaitu seseorang yang sangat mendalam dan memiliki visi besar untuk masa depan."
    voice "Jasper_3.wav"
    "Kita cenderung tertarik untuk membantu orang lain dengan cara yang penuh empati."
    voice "Jasper_4.wav"
    "Selain itu, kita suka berfokus pada nilai-nilai pribadi dan berusaha membuat perubahan positif di dunia."
    voice "Jasper_5.wav"
    "Kita sering merasa bahwa kita memiliki tujuan yang lebih besar dalam hidup."
    hide infj
    return
label infp:
    call hasil from _call_hasil_13
    # show text "Kamu Mendapatkan Karakter Owen !" align (0.5, 0.1) size 50 color "#FF0000"
    show infp:
        xalign 0.5
        yalign 0.3

    # show text "{size=100}{color=#03b90c}3...{/color}{/size}" at di_atas_gambar
    voice "Owen_1.wav"
    "Hai, Namaku Owen! Aku memiliki MBTI INFP"
    voice "Owen_2.wav"
    "Aku ternyata mirip dengamu, kita memiliki kepribadian yang sama yaitu seseorang yang sangat peduli dengan perasaan orang lain dan memiliki empati yang mendalam."
    voice "Owen_3.wav"
    "Kita juga suka mencari makna dalam hidup dan berjuang untuk mewujudkan impian kita."
    voice "Owen_4.wav"
    "Selain itu, kita lebih suka bekerja secara independen dan menghargai waktu untuk diri sendiri."
    voice "Owen_5.wav"
    "Kita berpegang pada nilai-nilai pribadi dan berusaha untuk membuat dunia menjadi tempat yang lebih baik."
    hide infp
    return
label intj:
    call hasil from _call_hasil_14
    show intj:
        xalign 0.5
        yalign 0.3
    voice "Lucian_1.wav"
    "Hai, Namaku Lucian! Aku memiliki MBTI INTJ"
    voice "Lucian_2.wav"
    "Aku ternyata mirip dengamu, kita memiliki kepribadian yang sama yaitu seseorang yang sangat terstruktur dan fokus pada pencapaian tujuan jangka panjang."
    voice "Lucian_3.wav"
    "Kita suka merencanakan masa depan dan berpikir analitis untuk memecahkan masalah."
    voice "Lucian_4.wav"
    "Selain itu, kita cenderung lebih introvert dan lebih suka menghabiskan waktu dengan diri sendiri daripada dalam keramaian."
    voice "Lucian_5.wav"
    "Kita sering kali merasa bahwa kita memiliki visi yang lebih jelas tentang masa depan."
    hide intj
    return
label intp:
    call hasil from _call_hasil_15
    show intp:
        xalign 0.5
        yalign 0.3
    voice "Luna_1.wav"
    "Hai, Namaku Luna! Aku memiliki MBTI INTP"
    voice "Luna_2.wav"
    "Aku ternyata mirip dengamu, kita memiliki kepribadian yang sama yaitu seseorang yang suka berpikir secara logis dan analitis."
    voice "Luna_3.wav"
    "Kita cenderung tertarik pada ide-ide abstrak dan teori-teori baru."
    voice "Luna_4.wav"
    "Selain itu, kita sangat menghargai kebebasan berpikir dan cenderung lebih fokus pada pemecahan masalah daripada urusan sosial."
    voice "Luna_5.wav"
    "Kita lebih suka berdiskusi tentang konsep-konsep yang mendalam dan berusaha menemukan solusi yang inovatif."
    hide intp
    return


label hasil:
    scene kuil_kuno with dissolve
    voice "suara.wav"
    "Akhirnya setelah menyelesaikan tantangan terakhir, kamu bisa keluar dari kuil tersebut"
    voice "suara.wav"
    "Dan Kamu mendapatkan sebuah karakter yang mencerminkan dirimu"
    return