import time

class Article:
    def __init__(self, title, content, category, author, date):
        self.title = title
        self.content = content
        self.category = category
        self.author = author
        self.date = date

    def show_article(self):
        text = f"""
        Mavzu: {self.title}
        Maqola: {self.content}
        Kategoriya: {self.category}
        Avtor: {self.author}
        Sana: {self.date}
        """
        print(text)


class Category:
    def __init__(self, name):
        self.name = name
        self.articles = []

    def add_article(self, article):
        self.articles.append(article)

    def show_articles(self):
        print(f"Category: {self.name}")
        for article in self.articles:
            article.show_article()

    def show_titles(self):
        print(f"\n--- {self.name} ---")
        for i, article in enumerate(self.articles):
            time.sleep(1)
            print(f"{i + 1}. {article.title}")

    def get_article(self, index):
        if 0 <= index < len(self.articles):
            return self.articles[index]
        else:
            return None



article_1_content = """
17 sentabr kuni Boysundagi M25 konida sodir bo‘lgan avariya 4 kishini hayotdan olib ketdi.
Marhumlarning yaqinlariga ko‘ra, konning boshqa quduqlarida ishlovchi xodimlar o‘sha kuni tozalash ishlarini bajarish 
uchun “og‘zi yopilgan” quduqqa jalb qilingan. Kutilmagan avariya esa halokatli yakunlangan. Boysunda bo‘lib turgan 
Kun.uz muxbiri marhumlarning yaqinlari bilan suhbatlashdi.Marhumlarning yaqinlari bu halokatda texnik nosozlik deyilgani
bilan mas’ullarning ham aybi borligini, ishchilarni bir necha kun o‘tmasdan “zalivka” qilingan quduq yoniga olib
borishganini aytishmoqda.

Jumladan, marhumlardan birining qarindoshi Salomat Tangirqulova shunday deydi:

“Birinchi portlash 1 sentabrda bo‘ldi. Hammamiz uyda edik. Kechqurun qishloqdan chiqib ketinglar, degan xabar keldi.
 Shaharga chiqib ketdik biz. Keyin yopildi degan xabar keldi. 17 sentabr kuni esa birdan qarsillagan ovoz eshitildi.
Tez yordam mashinalari o‘ta boshladi."
"""
article_2_content = """
Sirdaryoda quyosh paneli o‘rnatmagani uchun elektrdan uzilgan tadbirkorlar norozilik bildirib, hokimlik binosi oldiga 
to‘plangach, Sirdaryo viloyati HETK aybini tan oldi. Quyosh panellari o‘rnatish bo‘yicha majburlov choralari
respublikaning boshqa hududlarida ham kuzatilayotgani e’tiborga olinsa, prezident qarori (ochiq e’lon qilinmagan) 
yoppasiga noto‘g‘ri talqin qilinayotgan bo‘lishi mumkin. Sirdaryoda tadbirkorlarni quyosh paneli o‘rnatmagani uchun 
elektrdan uzish holati prezidentning tegishli qarorlarini noto‘g‘ri talqin qilish sababli kelib chiqqan.
Bu haqda “Hududiy elektr tarmoqlari” AJ Sirdaryo hududiy filiali Kun.uz xabariga nisbatan rasmiy munosabatida
ma’lum qildi. HET Sirdaryo filiali axborotiga ko‘ra, prezidentning 2023 yil 16 fevraldagi “2023 yilda qayta tiklanuvchi 
energiya manbalarini va energiya tejovchi texnologiyalarni joriy etishni jadallashtirish chora-tadbirlari to‘g‘risida”gi 
PQ-57-son hamda 2024 yil 31 maydagi “Energiya resurslaridan foydalanish samaradorligini oshirish bo‘yicha qo‘shimcha 
chora-tadbirlar to‘g‘risida”gi PQ-222-son qarorlarida mamlakat bo‘ylab tadbirkorlik sub’yektlari tomonidan o‘z 
ehtiyojining ma’lum qismini muqobil energiya manbalaridan ishlab chiqarish belgilangan.
"""
article_3_content = """
Mahalla raislari ham pul tikib, targ‘ib qilayotgan HNK media kompaniyasi ta’lim muassasalari, xususan, maktablar va 
bog‘chalarga qadar kirib bordi. Ushbu kompaniyaning arzimas “saxiyligi” ortida nimalar yashiringanini bilmagan pedagog
va tarbiyachilar o‘zlari sezmagan holda ularning “nog‘orasiga o‘ynab” qo‘ymoqda. Aslida ularning bu harakati reklama
qonunchiligiga ham zid. Heineken (HNK) media kompaniyasi haqida Kun.uz oldinroq ham yozgandi. 2016 yilda tashkil 
etilgani va bosh qarorgohi London shahrida joylashgani, ta’sischilari Kevin Torn va Barri Jons ismli shaxslar ekani
aytiladigan mazkur kompaniya video ko‘rish va ularga layk bosish orqali pul topishni targ‘ib qiladi.

Kevin Torn va Barri Jons bor shaxslarmi yoki aslida yo‘qmi, harqalay ularni O‘zbekistonda HNK’ga a’zo bo‘lganlarning
hech biri ko‘rmagan.

Kun.uz surishtiruvidan so‘ng HNK guruhlarida kompaniyaning bayonoti tarqatildi. Unda ushbu kompaniya odamlarga barqaror
ish imkoniyatlarini taqdim etishi, ularga daromad olishga yordamlashishi hamda qo‘l mehnati qiyinchiliklaridan qochish
imkonini berishi aytiladi.

"""
article_4_content = """
Toshkent shahri. Havo biroz bulutli bo‘ladi, biroz qisqa muddatli yomg‘ir yog‘ishi mumkin. Shamol sharqdan 5-10 m/s 
tezlikda esadi. Harorat kechasi +15...+17 daraja, kunduzi +27...+29 daraja bo‘ladi.

Qoraqalpog‘iston Respublikasi va Xorazm viloyati. Havo biroz bulutli bo‘ladi, yog‘ingarchilik kutilmaydi. Shamol sharqdan 
7-12 m/s tezlikda esadi. Harorat kechasi +10...+15 daraja, kunduzi +25...+30 daraja bo‘ladi.

Buxoro va Navoiy viloyatlari. Havo biroz bulutli bo‘ladi, yog‘ingarchilik kutilmaydi. Shamol sharqdan 7-12 m/s tezlikda
esadi. Harorat kechasi +12...+17 daraja, kunduzi +27...+32 daraja bo‘ladi.

Toshkent, Samarqand, Jizzax va Sirdaryo viloyatlari. Havo biroz bulutli bo‘ladi, yog‘ingarchilik kutilmaydi, faqat
Toshkent viloyatida biroz qisqa muddatli yomg‘ir yog‘ishi mumkin. Shamol sharqdan 9-14 m/s tezlikda esadi. 
Harorat kechasi +13...+18 daraja, kunduzi +27...+32 daraja bo‘ladi.

Qashqadaryo va Surxondaryo viloyati. Havo biroz bulutli bo‘ladi, yog‘ingarchilik kutilmaydi. Shamol sharqdan 9-14 m/s 
tezlikda esadi. Harorat kechasi +15...+20 daraja, kunduzi +32...+37 daraja bo‘ladi.

Andijon, Namangan va Farg‘ona viloyatlari. Havo biroz bulutli bo‘ladi, yog‘ingarchilik kutilmaydi. Shamol sharqdan 
7-12 m/s tezlikda esadi. Harorat kechasi +12...+17 daraja, kunduzi +27...+32 daraja bo‘ladi.

Respublikaning tog‘li hududlari. Havo biroz bulutli bo‘ladi, ba’zi joylarda qisqa muddatli yomg‘ir yog‘adi. Shamol 
sharqdan 9-14 m/s tezlikda esadi. Harorat kechasi +9...+14 daraja, kunduzi +18...+23 daraja bo‘ladi.
"""
article_5_content = """
O‘qishga qabul qilinganlar birinchi yo‘nalishda faqat katta miqdordagi “super kontrakt” bilan o‘qishi mumkin. Bunda 
ularning qabul chizig‘iga necha ball yetmay qolganining ahamiyati yo‘q. Tartib qabul komissiyasi tomonidan tasdiqlangan.
Bundan oliygohlarning ham, talabalarning ham xabari bo‘lmagan. Tushunarli bo‘lishi uchun maqolada shartli ravishda qabul 
chizig‘iga 4,05 ball yetmay qolganlar to‘laydigani qo‘shimcha kontrakt deyiladi. To‘plagan balli 56,7dan yuqorilarni esa
super yoki tabaqalashtirilgan kontrakt deymiz. Xo‘sh, bularning farqi qanday?
O‘qishga topshirib, kirolmaganlar. Ya’ni balli qabul chizig‘iga 4,05 ballgacha yetmagan abituriyent o‘zi tanlagan 5 
yo‘nalishning birida qo‘shimcha kontrakt to‘lab o‘qishi mumkin. Bu imkoniyat o‘qishga kirganlarga berilmaydi. Shuni 
eslatish kerak, o‘tgan yili o‘qishga kirgan talaba ham birinchi yo‘nalishida qo‘shimcha kontraktda o‘qishi mumkin edi.
Nega tartib 1 yil ichida o‘zgardi degan savolni vazirlik matbuot xizmati quyidagi izohladi:

“Kirgan universitetida o‘qishni istamasa, talaba super kontrakt to‘laydi, sababi bir nechta universitetlarga talab katta,
ularning moddiy-texnik bazasi barcha talabalarni qabul qilishga kuchi yetmaydi”, – dedi Nazokat Abduqunduzova.
"""
article_6_content = """
AQShda saylovchilar keyingi prezidentni saylash uchun 5 noyabr kuni saylov uchastkalariga chiqishadi. Avvaliga saylovlar
2020 yilda ham prezidentlikka raqobatlashgan demokrat Jo Bayden va respublikachi Donald Tramp o‘rtasidagi revansh-bahsga
aylanishi kutilgandi. Ammo iyulda vaziyat o‘zgardi: Bayden poygadan chiqishga qaror qildi va vitse-prezident Kamala 
Harris nomzodini qo‘llab-quvvatladi.Quyidagi diagrammada ko‘rsatilganidek, Demokratik partiya nomzodi Kamala Harris 
umummilliy so‘rovlarda, o‘rtacha hisobda Trampni biroz ortda qoldirgan (so‘rovlardagi so‘nggi ma’lumotlar eng yaqin 
butun songa yaxlitlangan).

So‘rovlarga ko‘ra, prezident Bayden poygadan chiqish haqidagi qarorini e’lon qilishidan oldingi oylar davomida sobiq 
prezident Trampdan ortda qolayotgandi. O‘sha vaqtda Harrisning nomzodiga jiddiy e’tibor qaratilmagan, ammo unda ham 
ishlar yaxshi bo‘lmaydi, deb taxmin qilingandi.

Ammo uning nomzodi ilgari surilgach, vaziyat o‘zgardi va so‘rovlar Harris o‘z raqibidan kichik ustunlikka egaligini 
ko‘rsata boshladi; bu farq hozirga qadar saqlanib qolmoqda.
"""
article_7_content = """
Sammitda ishtirok etish arizasi Rossiya prezidentining yordamchisi Yuriy Ushakov nomiga Afg‘oniston sanoat va savdo 
vaziri vazifasini bajaruvchi Nuriddin Aziziy tomonidan yo‘llangan. «Tolibon» oktyabr oyida Qozonda o‘tkaziladigan BRIKS
sammitida ishtirok etish uchun Moskvaga ariza yubordi.

Ariza Rossiya prezidentining  yordamchisi Yuriy Ushakov nomiga Afg‘oniston sanoat va savdo vaziri vazifasini bajaruvchi
Nuriddin Aziziy tomonidan yo‘llangan bo‘lib, unda afg‘on hukumatining sammitda ishtirok etishi muhim ahamiyat kasb 
etishi ta’kidlangan. «Biz sammitda yuqori darajadagi delegatsiya, jumladan, Afg‘oniston bosh vaziri o‘rinbosari Abdul 
G‘ani Birodar, men hamda boshqa qatnashchilar qatori ishtirok etishdan manfaatdormiz», — deyiladi xatda.

2021 yil avgust oyi boshida «Tolibon» afg‘on hukumat kuchlariga qarshi hujumni kuchaytirgan, 15 avgust kuni Kobulga 
kirib kelgan edi. Avgust oyining so‘nggi ikki haftasida Amerika harbiylari himoyasida bo‘lgan Kobul aeroportidan G‘arb
 davlatlari fuqarolari va ular bilan hamkorlik qilayotgan afg‘onlarni ommaviy evakuatsiya qilish amalga oshirilgan.

BRIKS — iqtisodiy hamkorlik tashkiloti. 2001 yilda britaniyalik iqtisodchi Jim Onil jahon iqtisodini o‘rganish 
jarayonida bir guruh katta davlatlarda iqtisodiy tizimli o‘sishga e’tibor berib, shartli ravishda BRIK deb ataydi 
(Braziliya, Rossiya, Hindiston, Xitoy). 2010 yilda bunga JAR qo‘shildi, bugun tashkilotda to‘qqizta davlat bor.
"""
article_8_content = """
Prezident Shavkat Mirziyoyev tadbirkorlar bilan ochiq muloqotda 2026 yilda Jahon savdo tashkilotiga a’zo bo‘lish 
maqsadlari va teng raqobat muhitini yaratish haqida gapirdi. «Iqtisodiyotimizga oldinlari proteksiya qaysidir ma’noda 
kerak edi. Yana shu yo‘lda davom etsak, imkoniyatlarimiz cheklanib qoladi», – dedi prezident. 
Ichki bozorda teng raqobat muhitini yaratish, tashqi bozorlarga chiqish imkoniyatlarini kengaytirish prezidentning 
tadbirkorlar bilan ochiq muloqotida ko‘tarilgan uchinchi yo‘nalish bo‘ldi.

Avvalo, O‘zbekistonning yetti oylik eksporti 13 foizga o‘sib, 10 milliard dollardan oshdi, avval eksport qilmagan 
1 ming 610 ta korxona tashqi bozorlarga chiqqani ta’kidlandi.

Davlat rahbari Jahon savdo tashkilotiga 2026 yilda a’zo bo‘lish bo‘yicha katta qadamlar qo‘yilganini aytdi.
"""
article_9_content = """
Monitoring natijalari 8 nomdagi mahsulot - olma, pomidor, karam, limon, grechka, tovuq go‘shti, piyoz, shakar bo‘yicha 
minimal narxlar o‘tgan oyga nisbatan pasayganini ko‘rsatdi. 

Makroiqtisodiy va hududiy tadqiqotlar instituti mutaxassislari 2024 yilning sentabr oyida Toshkentdagi yirik
supermarketlarda 21 nomdagi oziq-ovqat mahsulotlari narxining o‘zgarishini ko‘rib chiqdi.

Monitoring natijalari 8 nomdagi mahsulot — olma, pomidor, karam, limon, grechka, tovuq go‘shti, piyoz, shakar bo‘yicha
minimal narxlar o‘tgan oyga nisbatan pasayganini ko‘rsatdi. Tahlil 8 avgust va 12 sentabr kunlari o‘tkazilgan monitoring
ma’lumotlari asosida qilindi.

Shunday qilib, olmaning minimal narxi 28,2 foiz, pomidorniki 18,7 foiz, karamniki 15,9 foiz, limonniki 13,8 foiz, 
grechkaniki 5,9 foiz, tovuq go‘shtniki (file) 3,1 foiz, sariq piyozniki 2,0 foiz, shakarniki 1,6 foiz pasaygan.

To‘qqiz nomdagi mahsulotning minimal narxlari esa oshgan. Narxining oshishi bo‘yicha kartoshka yetakchi bo‘ldi. Bu esa
mavsumiy omil bilan bog‘liq. 

To‘rt nomdagi mahsulotning eng past narxlari esa o‘zgarishsiz qolgan. Ularning orasida bug‘doy uni, guruch, qizil sabzi 
va tuxum bor.

"""
article_10_content = """
Ularning hech biri jarohat olmagani aytilmoqda.
FVV qutqaruvchilari “Katta chimyon” tog‘ida adashib qolgan fuqarolarga yordam berib, ularni pastga olib tushgan.

Ma’lum qilinishicha, 2024 yil 21 sentabr kuni soat 16:15 da Toshkent viloyati FVBga Bo‘stonliq tumani “Chimyon” mahalla 
hududidagi “Katta chimyon” tog‘iga to‘rt nafar fuqaro sayr qilish maqsadida borib, yo‘ldan adashib qolganligi haqida 
xabar kelib tushgan.
Xabarga asosan, Chimyon yong‘in-qutqaruv otryadidan bir guruh qutqaruvchilar zudlik bilan aytilgan manzilga yetib borib,
 fuqarolar xavfsiz hududga olib tushilgan.

Qayd etilishicha, fuqarolardan hech biri tan jarohati olmagan.
"""
article_11_content = """
Buxoroda 263 dona qadimiy tangalarni Istanbulga yashirincha olib ketayotgan shaxs qo‘lga olindi.
Buxoro viloyati bojxona boshqarmasi hamda DXX Aviatsiya xavfsizligi xodimlarining o‘zaro hamkorligida qadimiy 
numizmatika buyumlarini respublika hududidan olib chiqilishiga bo‘lgan yana bir urinish bartaraf etildi.

Unda “Buxoro aeroporti” chegara bojxona posti xodimlari tomonidan “Buxoro—Istanbul” yo‘nalishidagi aviareys orqali
xorijiy davlatga uchib ketish arafasidagi yo‘lovchi tegishli bojxona nazoratidan o‘tkazilganda, mazkur fuqaro o‘zining
qo‘l yuklari orasiga berkitgan holda qadimiy tangalarni olib chiqishga urinayotgani aniqlandi.
Ashyoviy dalil sifatida olib qolingan 263 dona qadimiy tangalarning bir qismi bundan 500 yil avval zarb etilgan bo‘lishi 
mumkin. Hozirda mazkur numizmatika buyumlarining qadimiylik darajasini aniqlash maqsadida Buxoro viloyati madaniy meros 
boshqarmasi tomonidan badiiy ekspertiza tayinlangan bo‘lib, holat yuzasidan tergovga qadar tekshiruv harakatlari olib
 borilmoqda.

Madaniy boyliklarning olib chiqilishi va olib kirilishi to‘g‘risida”gi qonunga asosan zarb etilganiga 50 yildan oshgan 
numizmatika buyumlarini mamlakat hududidan olib chiqib ketish taqiqlanadi.
"""
article_12_content = """
Qayd qilinishicha, avvalo, yig‘ilishda ommaviy sportni va olimpiya harakatini yanada kengaytirish masalalariga e’tibor
qaratildi. Sport vazirligi, Milliy Olimpiya va Paralimpiya qo‘mitalari tomonidan sport turlari bo‘yicha foydalanilmagan
imkoniyatlar yana bir bor tanqidiy tahlil qilindi.

Misol uchun, Olimpiya o‘yinlarida yengil atletika bo‘yicha 48 ta, suv sporti turlarida 49 ta dastur mavjud. Lekin 
vakillarimiz ularda 5 va 4 ta yo‘llanma bilan qatnashdi, xolos. Tennis, o‘q otish, gimnastika, velosport bo‘yicha 
federatsiyalar ham, sharoit ham bor. Yunon-rum kurashi, ot sporti, qilichbozlik, eshkak eshish bo‘yicha hali ishga 
solinmagan imkoniyatlar ko‘p. Chim ustida xokkey, basketbol, gandbol, regbi, suv polosi kabi jamoaviy sport turlarini
ham rivojlantirish zarurligi qayd etildi. Mazkur sport federatsiyalari ishini jonlantirish, o‘quv-mashg‘ulotlar tizimini
takomillashtirish bo‘yicha vazifalar belgilandi.
Olimpiya va paralimpiya harakati ommaviy sportdan kuch olishi ta’kidlanib, mahallalarda seleksiya ishlarini kengaytirish, 
iqtidorli yoshlarni professional etib tarbiyalash bo‘yicha ko‘rsatmalar berildi.

2025 yil O‘zbekistonda yoshlar o‘rtasida Osiyo va Paraosiyo o‘yinlari o‘tkazilishi rejalashtirilgan. Buning uchun 
Toshkentda Olimpiya shaharchasi barpo etilmoqda. Osiyo o‘yinlaridan so‘ng, Olimpiya shaharchasi infratuzilmasidan 
samarali foydalanish ko‘zda tutilmoqda. Buning uchun «Aqlli shahar» konsepsiyasiga asoslangan ma’muriy boshqaruv tashkil
etiladi. U sport majmualarini saqlash, jihozlar va texnik tizimlar holatini kuzatib borish, zarur hollarda ta’mirlash 
bilan shug‘ullanadi.
"""
article_13_content = """
«An Nasr»ning portugaliyalik hujumchisi Krishtianu Ronaldu ijtimoiy tarmoqlarda 1 milliard obunachiga ega bo‘lganini 
ma’lum qildi. U tarixda birinchi bo‘lib bunday muvaffaqiyatga erishdi.
«Biz tarix yaratdik — 1 milliard obunachi! Bu shunchaki raqam emas — bu bizning umumiy ishtiyoqimiz, o‘yin va undan 
tashqaridagi muhabbatimizdan dalolat beradi.

Madeyra ko‘chalaridan tortib, dunyodagi eng katta sahnalargacha men har doim oilam va siz uchun o‘ynaganman. Hozir biz
1 milliardmiz. Menga ishonganingiz, qo‘llab-quvvatlaganingiz va hayotimning bir qismi bo‘lganingiz uchun tashakkur.
Eng yaxshisi hali oldinda, biz birgalikda g‘alaba qozonamiz va tarix yozamiz», — dedi Ronaldu sahifalarida.
"""
article_14_content = """
Ilon Maskning Neuralink startapi ko‘zi ojiz odamlarga ko‘rish imkonini beruvchi Blindsight deb nomlangan eksperimental
implantni taqdim etdi, deb yozdi Reuters. Qayd qilinishicha, implant hatto ikkala ko‘zi va ko‘rish nervini yo‘qotgan 
yoki tug‘ilgandan beri umuman ko‘rmaganlarga ham yordam beradi.

«Miyaning ko‘rish qobig‘i shikastlanmagan bo‘lsa, implant tug‘ilgandan beri ko‘r bo‘lganlarga ham yordam beradi», dedi 
Neuralink asoschisi Ilon Mask.
Implant allaqachon AQSh oziq-ovqat va farmatsevtika nazorati idorasidan (FDA) ruxsat olgan: u «o‘ta muhim qurilma» 
sifatida tan olingan. Endi Neuralink implantni insonlarda sinab ko‘rishi mumkin bo‘ladi, kompaniya allaqachon arizalarni
qabul qila boshlagan.

Maskning ta’kidlashicha, dastlab Blindsight tasvir sifati past bo‘ladi - taxminan Atari konsollaridagi grafikalar bilan
bir xil. Ammo kelajakda ular tasvirni yaxshilaydi, shuningdek, infraqizil, ultrabinafsha yoki hatto radar to‘lqin 
uzunligi diapazonida ko‘rish qobiliyatini qo‘shadi.

Avvalroq, Neuralink falaj bo‘lgan odamlarga fikr kuchi bilan elektron qurilmalardan foydalanish imkonini beruvchi 
implantni taqdim qilgan edi. Avgust oyida shunday bemorlardan biri implant yordamida Counter-Strike 2 o‘ynashga 
muvaffaq bo‘ldi.
"""
article_15_content = """
Tadqiqotchilar sog‘lom ko‘ngillilar miyasidagi faollikning o‘zgarishini o‘rganishda funksional magnit-rezonans 
tomografiya usulidan foydalangan.
Michigan universiteti olimlari talamusning matritsa hujayralari ongni yo‘qotish va qaytarish jarayonlarida katta rol 
o‘ynashini aniqladi.

Tadqiqotchilar sog‘lom ko‘ngillilar miyasidagi faollikning o‘zgarishini o‘rganishda funksional magnit-rezonans
tomografiya usulidan foydalangan. Ularga yuborilgan propofoldan venaga qilinadigan tez ta’sir ko‘rsatuvchi umumiy narkoz
sifatida ishlatiladi.
Olimlarning aniqlashicha, chuqur uyqu vaqtida sensorli ma’lumotlarni qayta ishlash uchun javobgar talamusdagi neyronlar
 faolligi sezilarli darajada pasaygani kuzatilgan. Shu bilan birga, alohida sensor signallarni qayta ishlash saqlanib
  qolgan, ammo ularning aloqasi buzilgan.

Tadqiqot natijalariga ko‘ra, hushsiz holatga o‘tish vaqtida talamusdagi matritsali hujayralar muhim rol o‘ynaydi. 
Talamus katta yarimsharlar yuzasida joylashgan asosiy tuzilma va u his qilish organlaridagi (hid bilishdan tashqari) 
sensor va harakat axborotini katta yarim shardagi tegishli sohalarga yuborishga javob beradi.

Bundan tashqari, miyaning ushbu sohasi uyqu, uyg‘onish va konsentratsiyani tartibga solishda ham muhim rol o‘ynaydi.
"""
article_16_content = """
SSSR parchalanganidan keyin NATO tashkiloti endi kerakmi degan savollar ham yangragan, harbiy alyans bir muddat 
ekstremistik va terroristik tashkilotlarga diqqatini qaratgan edi, lekin Putinning 2007 yili Myunxendagi nutqidan 
keyingi davrda NATO yana yirik avtoritar davlatlarga qarshi turish tafakkuriga qaytdi, deydi siyosatshunos.
Sovet ittifoqi qulaganidan keyin NATO o‘ziga yangi mazmun izladi. Ya’ni yangi konseptual tahdid ko‘rinmayotgan edi.
Ma’lum bir muddat tashkilotning asosiy obekti ekstremizm va terrorizmga qarshi kurashish bo‘ldi. 11 sentabr 
voqealaridan keyin, NATO tarixida birinchi va hozircha oxirgi marta 5-modda qo‘llandi: Amerikani mudofaa qilish uchun
shu modda asosida Afg‘onistonga kirilgan edi.

Keyingi 20 yilda NATOning tafakkuri yana o‘sha klassik davrga qaytyapti. Ekstremizm va terrorizm – bu tashkilotlar, 
Rossiya va Xitoy esa – klassik davlatlar. 75 yillik sammitda avtoritar davlatlar, ayniqsa Xitoydan kelayotgan tahdidlar
bosh mavzulardan biri bo‘ldi.
NATOning bu tafakkurga qaytishi Qrim anneksiyasidan ham avvalroq, Putinning 2007 yili Myunxendagi nutqiga borib taqaladi. 
Bu Rossiyaning G‘arbga konseptual e’tirozi, vetosi bo‘lgandi.

Umuman, NATOga a’zo davlatlarning tafakkuri har doim shunday bo‘lgan: vaqti kelib baribir Rossiya Federatsiyasi,
Xitoy Xalq Respublikasi bilan global to‘qnashuv bo‘ladi. 1990-yillardayoq Amerikaning ba’zi bir kongressmenlari va
senatorlari NATO bu faqat transatlantik tashkilot emas, global tashkilot bo‘lishi kerak, unga Yaponiya, Avstraliya,
Yangi Zelandiya, Janubiy Koreyani a’zo qilish kerak, Markaziy Osiyoda ham ba’zi davlatlar a’zo bo‘lishi kerak
fikrlarni aytishgandi. Tinch okeani havzasidagi, Xitoy atrofidagi bu to‘rtta davlatlar rahbarlari 75 yillik sammitda
asosiy mehmonlar qatorida ishtirok etdi.
"""
article_17_content = """
Siyosatshunos Kamoliddin Rabbimov prezident Shavkat Mirziyoyevning AQShga safaridan keyin O‘zbekiston uchun 
Vashingtonning geosiyosiy ahamiyati haqida so‘z yuritdi.O‘zbekiston tashqi siyosatida AQSh 4 ta katta geosiyosiy 
vektorlardan biri hisoblanadi, bular: Xitoy, Rossiya, global janub va AQSh.

Markaziy Osiyo makrohudud bo‘lib, 2016 yildan buyon alohida sub’yekt bo‘lishga harakat qilib kelyapti. Markaziy Osiyo 
markazidagi davlat esa O‘zbekiston. O‘zbekistonning AQSh bilan munosabatlari yuqorida aytilgan qolgan 3 ta vektor bilan
toroziga solinadi, ya’ni AQSh bilan munosabatlar ijobiy neytral pozitsiyada deyish mumkin. AQSh hozir biz uchun 
opponent bo‘lgan davlat emas. Andijon voqealaridan to 2010 yilga qadar Vashington Toshkent uchun opponent edi, bu 
davrda munosabatlar sovuq bo‘ldi. 90-yillar o‘rtalaridan 2004 yilgacha esa O‘zbekiston tashqi siyosatida rasmiy 
Vashingtonga yo‘nalish olgan edi, ammo bu ichki siyosatda o‘z aksini topmadi, ya’ni inson huquqlari, demokratiyada 
ko‘rinmadi. O‘sha davrda O‘zbekiston qattiq avtoritar davlat bo‘lishi bilan birgalikda, AQShga yo‘nalish olgan edi.
"""


article_1 = Article("Yigitlarni o‘limning og‘ziga olib borishgan", article_1_content, "O`zbekiston", "Kun.uz", "20.09.2024")
article_2 = Article("Tadbirkorlarni quyosh paneli olishga majburlagan Sirdaryo HETK: “Prezident qarori noto‘g‘ri talqin qilingan”", article_2_content, "O`zbekiston", "Kun.uz", " 21.09.2024")
article_3 = Article("Moliyaviy piramida uslubidagi firibgarlar davlat bog‘chalarida targ‘ibot boshladi", article_3_content, "O`zbekiston", "Kun.uz", "21.09.2024")
article_4 = Article("22 sentabr kuni qisqa muddatli yomg‘ir yog‘ishi mumkin", article_4_content, "O`zbekiston", "Kun.uz", "21.09.2024")
article_5 = Article("“Super kontrakt” tartibi barcha OTMlarni chalkashtiryapti. Nega komissiya qarori e’lon qilinmaydi?", article_5_content, "O`zbekiston", "Kun.uz", "21.09.2024")
article_6 = Article("AQShdagi 2024 yilgi saylovlar: so‘rovlar nimani ko‘rsatmoqda?", article_6_content, "Jahon", "Kun.uz", "20.09.2024")
article_7 = Article("«Tolibon» Qozonda o‘tkaziladigan BRIKS sammitida ishtirok etish uchun ariza berdi", article_7_content, "Jahon", "Kun.uz", "21.09.2024")
article_8 = Article("«Bundan buyon hech kimda alohida huquq bo‘lmaydi» – prezident teng raqobat va JSTga kirish haqida", article_8_content, "Iqtisodiyot", "Kun.uz", "20.08.2024" )
article_9 = Article("Yirik supermarketlarda ayrim mahsulotlar narxi arzonlashdi", article_9_content, "Iqtisodiyot", "Kun.uz", "20.09.2024")
article_10 = Article("Katta Chimyon tog‘ida adashib qolgan to‘rt kishi qutqarildi", article_10_content, "Jamiyat", "Kun.uz", "21.09.2024")
article_11 = Article("O‘zbekistonda 263 dona qadimiy tangani Turkiyaga yashirincha olib ketayotgan shaxs ushlandi", article_11_content, "Jamiyat", "Kun.uz", "21.09.2024")
article_12 = Article("Olimpiya shaharchasi hududida xokkey majmuasi qurilishi mumkin", article_12_content, "Sport", "Kun.uz", "20.09.2024")
article_13 = Article("Ronaldu birinchi bo‘lib ijtimoiy tarmoqlarda 1 mlrd obunachiga ega bo‘ldi", article_13_content, "Sport", "Kun.uz", "21.09.2024")
article_14 = Article("Neuralink ko‘rlarning ko‘rish qobiliyatini tiklovchi implantni ishlab chiqadi", article_14_content, "Fan-texnika","Kun.uz", "21.09.2024")
article_15 = Article("Olimlar inson ongi uchun mas’ul bo‘lgan miya hujayralarini aniqladi", article_15_content, "Fan-texnika","Kun.uz", "21.09.2024")
article_16 = Article("“NATOning tafakkuri klassik davrga qaytdi”", article_16_content, "Nuqtai nazar","Kamoliddin Rabbimov", "18.07.2024")
article_17 = Article("AQSh – O‘zbekiston tashqi siyosatidagi to‘rt vektordan biri", article_17_content, "Nuqtai nazar", "Kamoliddin Rabbimov", "23.09.2023")






category_1 = Category("O`zbekiston")
category_2 = Category("Jahon")
category_3 = Category("Iqtisodiyot")
category_4 = Category("Jamiyat")
category_5 = Category("Sport")
category_6 = Category("Fan-texnika")
category_7 = Category("Nuqtai nazar")
category_8 = Category("Audio")

category_1.add_article(article_1)
category_1.add_article(article_2)
category_1.add_article(article_3)
category_1.add_article(article_4)
category_1.add_article(article_5)
category_2.add_article(article_6)
category_2.add_article(article_7)
category_3.add_article(article_8)
category_3.add_article(article_9)
category_4.add_article(article_10)
category_4.add_article(article_11)
category_5.add_article(article_12)
category_5.add_article(article_13)
category_6.add_article(article_14)
category_6.add_article(article_15)
category_7.add_article(article_16)
category_7.add_article(article_17)


categories = [category_1, category_2, category_3, category_4, category_5, category_6, category_7]
others = ["Videolavhalar", "Fotolavhalar", "Dolzarb Xabarlar", "Hayotiy hikoyalar", "Muharrirlar tanlovi", "Maqolalar", "Kun Mavzulari", "Bizning jamoa", "Reklama Tariflari", "Media Kit"]

def show_main_menu():
    print("\nMain Menu")
    for i, category in enumerate(categories):
        time.sleep(1)
        print(f"{i + 1}. {category.name}")
    time.sleep(1)
    print("8. Ko`proq")
    time.sleep(1)
    print("0. Exit")

def show_others():
    while True:
        print("\nOther Menu")
        for i, category in enumerate(others):
            time.sleep(1)
            print(f"{i + 1}. {others[i]}")
        time.sleep(1)
        print("0. Orqaga")

        us_input = int(input("Kerakli bo`limni tanlang yoki orqaga qaytish uchun 0 ni bosing: "))
        time.sleep(1)
        print("\n" * 100)
        if us_input == 0:
            break
        elif 1 <= us_input <= len(others):
            print(f"Siz {others[us_input - 1]} bo`limini tanladingiz")
        else:
            print("Qayta kiriting!")

def show_categorized_titles(category):
    while True:
        category.show_titles()
        time.sleep(1)
        choice = int(input("Sarlavhalardan birini tanlang yoki chiqish uchun 0 ni bosing:"))
        time.sleep(1)
        print("\n" * 100)
        if choice == 0:
            break
        elif  0 < choice <= len(categories):
            article = category.get_article(choice-1)
            article.show_article()
        else:
            print("Qayta kiriting!")

print("\t\t\t\tKun.uz veb-sahifasiga Xush Kelibsiz!")
print("\t\t\t\tEng so`nggi qaynoq yangiliklar bizda!")

time.sleep(1)
print("Loading",end="")
time.sleep(1)
print(".", end="")
time.sleep(1)
print(".", end="")
time.sleep(1)
print(".", end="")



while True:
    show_main_menu()
    user_input = int(input("Kategoriyalardan birini tanlang:"))
    time.sleep(1)
    print("\n" * 100)
    if user_input == 0:
        print("Dasturdan chiqish...")
        break
    elif user_input == 8:
        show_others()
    elif 0 < user_input <= len(categories):
        selected_category = categories[user_input-1]
        show_categorized_titles(selected_category)
    else:
        print("Qayta kiriting!")




