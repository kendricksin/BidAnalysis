# This dictionary maps Thai province names to their coordinates
province_to_coordinates = {
    'กรุงเทพมหานคร': {'lat': 13.75, 'lon': 100.5833},  # Bangkok
    'สมุทรปราการ': {'lat': 13.5333, 'lon': 100.6667},  # Samut Prakan
    'นนทบุรี': {'lat': 13.85, 'lon': 100.5667},  # Nonthaburi
    'ปทุมธานี': {'lat': 14.0167, 'lon': 100.5333},  # Pathum Thani
    'พระนครศรีอยุธยา': {'lat': 14.4167, 'lon': 100.5},  # Phra Nakhon Si Ayutthaya
    'อ่างทอง': {'lat': 14.5833, 'lon': 100.45},  # Ang Thong
    'ลพบุรี': {'lat': 14.8, 'lon': 100.6167},  # Lop Buri
    'สิงห์บุรี': {'lat': 14.8833, 'lon': 100.4},  # Sing Buri
    'ชัยนาท': {'lat': 15.1833, 'lon': 100.1333},  # Chainat
    'สระบุรี': {'lat': 14.5, 'lon': 100.9167},  # Saraburi
    'ชลบุรี': {'lat': 13.35, 'lon': 101.0167},  # Chon Buri
    'ระยอง': {'lat': 12.6667, 'lon': 101.3333},  # Rayong
    'จันทบุรี': {'lat': 12.6333, 'lon': 102.1167},  # Chanthaburi
    'ตราด': {'lat': 12.2333, 'lon': 102.5167},  # Trat
    'ฉะเชิงเทรา': {'lat': 13.7, 'lon': 101.0833},  # Chachoengsao
    'ปราจีนบุรี': {'lat': 14.0, 'lon': 101.4167},  # Prachin Buri
    'นครนายก': {'lat': 14.2, 'lon': 101.2167},  # Nakhon Nayok
    'สระแก้ว': {'lat': 13.8167, 'lon': 102.0667},  # Sa Kaeo
    'นครราชสีมา': {'lat': 14.9833, 'lon': 102.1},  # Nakhon Ratchasima
    'บุรีรัมย์': {'lat': 15.0, 'lon': 103.0},  # Buriram
    'สุรินทร์': {'lat': 14.8333, 'lon': 103.5667},  # Surin
    'ศรีสะเกษ': {'lat': 15.1333, 'lon': 104.3833},  # Sisaket
    'อุบลราชธานี': {'lat': 15.25, 'lon': 104.8333},  # Ubon Ratchathani
    'ยโสธร': {'lat': 15.7833, 'lon': 104.15},  # Yasothon
    'ชัยภูมิ': {'lat': 15.8, 'lon': 102.0333},  # Chaiyaphum
    'อำนาจเจริญ': {'lat': 15.85, 'lon': 104.6333},  # Amnat Charoen
    'หนองบัวลำภู': {'lat': 17.2167, 'lon': 102.4333},  # Nong Bua Lamphu
    'ขอนแก่น': {'lat': 16.5, 'lon': 102.7833},  # Khon Kaen
    'อุดรธานี': {'lat': 17.4833, 'lon': 102.7667},  # Udon Thani
    'เลย': {'lat': 17.4833, 'lon': 101.5833},  # Loei
    'หนองคาย': {'lat': 17.8333, 'lon': 102.7667},  # Nong Khai
    'มหาสารคาม': {'lat': 16.2, 'lon': 103.2667},  # Maha Sarakham
    'ร้อยเอ็ด': {'lat': 16.0667, 'lon': 103.6667},  # Roi Et
    'กาฬสินธุ์': {'lat': 16.4333, 'lon': 103.5},  # Kalasin
    'สกลนคร': {'lat': 17.1667, 'lon': 104.15},  # Sakon Nakhon
    'นครพนม': {'lat': 17.3833, 'lon': 104.7167},  # Nakhon Phanom
    'มุกดาหาร': {'lat': 16.5333, 'lon': 104.7167},  # Mukdahan
    'เชียงใหม่': {'lat': 18.7833, 'lon': 98.9833},  # Chiang Mai
    'ลำพูน': {'lat': 18.6667, 'lon': 99.0333},  # Lamphun
    'ลำปาง': {'lat': 18.2667, 'lon': 99.5333},  # Lampang
    'อุตรดิตถ์': {'lat': 17.6167, 'lon': 100.1},  # Uttaradit
    'แพร่': {'lat': 18.1167, 'lon': 100.15},  # Phrae
    'น่าน': {'lat': 18.7833, 'lon': 100.7833},  # Nan
    'พะเยา': {'lat': 19.1833, 'lon': 99.9167},  # Phayao
    'เชียงราย': {'lat': 19.8667, 'lon': 99.8333},  # Chiang Rai
    'แม่ฮ่องสอน': {'lat': 19.2667, 'lon': 97.9333},  # Mae Hong Son
    'นครสวรรค์': {'lat': 15.5833, 'lon': 100.1667},  # Nakhon Sawan
    'อุทัยธานี': {'lat': 15.3833, 'lon': 100.0333},  # Uthai Thani
    'กำแพงเพชร': {'lat': 16.4667, 'lon': 99.5333},  # Kamphaeng Phet
    'ตาก': {'lat': 16.8667, 'lon': 99.1333},  # Tak
    'สุโขทัย': {'lat': 17.0, 'lon': 99.8167},  # Sukhothai
    'พิษณุโลก': {'lat': 16.8333, 'lon': 100.25},  # Phitsanulok
    'พิจิตร': {'lat': 16.4333, 'lon': 100.35},  # Phichit
    'เพชรบูรณ์': {'lat': 16.4167, 'lon': 101.15},  # Phetchabun
    'ราชบุรี': {'lat': 13.5333, 'lon': 99.8167},  # Ratchaburi
    'กาญจนบุรี': {'lat': 14.0333, 'lon': 99.5333},  # Kanchanaburi
    'สุพรรณบุรี': {'lat': 14.4667, 'lon': 100.1167},  # Suphan Buri
    'นครปฐม': {'lat': 13.8167, 'lon': 100.05},  # Nakhon Pathom
    'สมุทรสาคร': {'lat': 13.55, 'lon': 100.2833},  # Samut Sakhon
    'สมุทรสงคราม': {'lat': 13.4, 'lon': 100.0167},  # Samut Songkhram
    'เพชรบุรี': {'lat': 13.1167, 'lon': 99.9333},  # Phetchaburi
    'ประจวบคีรีขันธ์': {'lat': 11.8167, 'lon': 99.8},  # Prachuap Khiri Khan
    'นครศรีธรรมราช': {'lat': 8.4333, 'lon': 99.9667},  # Nakhon Si Thammarat
    'กระบี่': {'lat': 8.0667, 'lon': 98.9167},  # Krabi
    'พังงา': {'lat': 8.45, 'lon': 98.5167},  # Phangnga
    'ภูเก็ต': {'lat': 7.8833, 'lon': 98.4},  # Phuket
    'สุราษฎร์ธานี': {'lat': 9.15, 'lon': 99.3333},  # Surat Thani
    'ระนอง': {'lat': 9.9667, 'lon': 98.6333},  # Ranong
    'ชุมพร': {'lat': 10.5, 'lon': 99.1833},  # Chumphon
    'สงขลา': {'lat': 7.2167, 'lon': 100.5667},  # Songkhla
    'สตูล': {'lat': 6.6167, 'lon': 100.0667},  # Satun
    'ตรัง': {'lat': 7.5667, 'lon': 99.6167},  # Trang
    'พัทลุง': {'lat': 7.6167, 'lon': 100.0833},  # Phatthalung
    'ปัตตานี': {'lat': 6.8667, 'lon': 101.25},  # Pattani
    'ยะลา': {'lat': 6.55, 'lon': 101.2833},  # Yala
    'นราธิวาส': {'lat': 6.4167, 'lon': 101.8167},  # Narathiwat
    'บึงกาฬ': {'lat': 18.3667, 'lon': 103.65},  # Bueng Kan
}