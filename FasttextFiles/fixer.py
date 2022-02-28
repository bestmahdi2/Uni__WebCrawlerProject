from pickle import dump


def one():
    labeled_comments = {'iphone13promax': {'good': ['nice weather queen elizabeth walk singapore ',
                                                    'happy thursday everybody! here is a shot of the iphone 13 mini and one of my personal favourites the iphone 4s.usually when i upgrade my iphone i always sell my old one so that it can be used by someone else but i always keep my iphone 4s around.i just cant part with it its really a piece of art as an apple fan.now that apple have been making iphones for 15 years we have an awesome product and im sure in the next 15 years it will grow even stronger.does the iphone 4s hold a special place in your heart? iphone 13 pro maxfollow | like and share for more content!hashtags: ',
                                                    'wonderful',
                                                    "win a brand new iphone 13!enter our time limited giveaway and win iphone 13the most important step don't skip it go to the website select your phone important is highly requirement complete the anyone simple survey.when you done your survey then give me a screenshot on my inbox.the link in my bio.follow us like the recent post share this post to 15 of your friends comment below done those who write done in the comments below please leave us a message in a direct inbox ",
                                                    'done', 'please i need this and also i followed', 'tengo fe',
                                                    'realme gt 2 pro is best in prize', 'thanks', 'i need it',
                                                    'send me pic', 'promote it on.nirvana',
                                                    'lindo iphone digno de tenerlo 12'], 'bad': [
        'for me 5 is the one thats the most special to me.its the iphone that brought me back to iphone after trying out a samsung',
        "xiaomi the form of the camera's or else wat it the oneplus 10 pro buy i dont like the colorframe of the cameras"],
                                           'inactive': [
                                               'design com resistncia fora de srie e um salto imenso na durao da bateria.disponvel nas cores azul sierra dourado e preto com capacidade de 128gb.compre atravs do direct ou chame no whatsapp 44 999340586 levamos at voc! ',
                                               'send pic on.ig',
                                               ' 13mini1313pro13promax 2 290 7788xxsxrxsmaxse20201111pro11promax12mini1212pro12promax 2 line: ems20 1111proiphone11promaxiphone12 12 12promax 12promax 13mini1313pro13promax ',
                                               ' iphone 13 pro max gold 24k ',
                                               'vy bm 74 hr 74127 vilar i lodalen mellan uppdragen.lodalen oslo norge 20211220 sj ',
                                               'light blue dark blue or midnight green? : ', 'dark blue', 'black',
                                               'send pics', 'espetculo',
                                               'which one is your favourite.?...follow for latest updates & many more....hashtags: ',
                                               'realme gt 2 pro', 'oneplus', 'iqoo 9 pro', 'xiaomi for cameras',
                                               'one plus 10pro fev but india release date pzzz waiting plzzzzz',
                                               'mi 12 pro', 'realme!!', 'one plus', 'eu queroooo',
                                               ' iphone 13 pro max ? : ? ',
                                               '.premio: 1 iphone 12 pro max.para concorrer a esses premios siga atentamente todas as regras abaixo:.1 curta e salve essa foto!.2 siga a pagina e todos perfis que a pagina segue!.3 curti publicao recente desses perfil.oficial4 comente ok ou emojis o maximo de vezes que conseguir!.5 clique no aviaozinho e compartilhe nosso sorteio nos stories e envie para todos do seu direct!.prontinho e so aguardar frete gratis.todos que cumprirem corretamente todas as regras irao concorrer.resultado dia 1601 as 21:30.boa sorte..............opaulo ganhar ']}}

    temp_comments_keeper = []

    for key in labeled_comments.keys():
        for label in labeled_comments[key].keys():
            temp_comments_keeper += [f"__label__{label} {comment}" for comment in labeled_comments[key][label]]

    print(*temp_comments_keeper, sep="\n")


def two():
    temp_comments_keeper = []

    tests = """1/262) mais uma cliente que chegou at ns atravs de indicacoes e um cliente especial hoje obrigado pela preferncia e confiana em nosso trabalho. > g

2/262) apple store covent garden london 2022throughout the coming year i plan to make alot of work.there are moments in your creative life when you have the space energy time and little bit of spare cash to devote yourself to making new work.following on from the wonderful surprise of some of my archive becoming the book memory lane at the end of last year it became apparent that maybe i wasn't completely over photography.it had just faded into the background a little as i found it increasingly difficult to make a living out of my photography and moved into video around 2007.some of the new work is going to be a continuation of my first outings in medium format colour shooting on a rolleiflex or plaubel makina and some is going to be about embracing full the possibilities of digital most notably the ability to shoot alot of images and to shoot in low light very low light.i am also going to have a play around with large format portraiture and still life even shooting in black and white.the journey ahead is exciting.i thank everyone for their ongoing support when instagram allows me to reach you and please sign up on my website to receive updates.the new site will be live by early february with project new and old shown in a more pleasing layout than an instagram feed. > g

3/262) t o t est presentando algn problema ?si la respuesta es si en te brindamos la solucin reparacin de pantallas y micas traseras.cambios de batera y pantallas.cambio de tapa trasera.lunes a viernes desde las 10:00 a.m hasta las 7 p.m sbados desde las 11:00 a.m hasta las 4 p.m.te esperamos ! > b

4/262) bora de ! confira a seleo de produtos que preparamos para vocs.garantam j seu combo e bora armar aquele churras com muito sabor e qualidade!1 costelinha em tiras estncia 921 tbone estncia 921 linguia toscana prola 1 hamburguer de mandioca recheado 1 po de alho zinho tradicionalapenas r 119.90 est esperando que para garantir o seu?venha j buscar aqui no ! es ligue: 16 36328530 whats: 16 993734040ou clique no link e nos mande um http:bit.lyboibraboribpretoaproveite e baixe nosso.faa suas compras e receba onde estiver!: https:bit.ly3fdzmju: https:apple.co2qy0sk8boi brabo ribeiro preto av.independncia 595 vila seixas ribeiro pretospoferta vlida apenas para esta unidade na data de hoje > g

5/262) empieza tu ao con un nuevo equipazo!! ubcanos en:av la mar 2275 tienda 208 san miguelcontctanos:942732582  > i

6/262) offre aujourdhui avantage plus est partenaire de votre picerie au plein coeur de metz! un partenariat exclusif avec une offre permanente qui va te faire craquer! il ny a pas de petites conomies foncez ds maintenant faire vos courses dans cet tablissement! offre10 sous 10 dachat valable ds maintenant sous prsentation de ta carte avantage prsente sur lapplication mobile tudiant e couverte picerie > g

7/262) offre aujourdhui avantage plus est partenaire du the phone service! un partenariat exclusif qui va te permettre de faire la bascule si tu vas faire rparer ton tlphone! offreune rparation effectue une coque offerte valable ds maintenant sous prsentation de ta carte avantage prsente sur lapplication mobile tudiant e couverte  > g

8/262) tech giant apples fitnessfocused wireless earbuds beats fit pro is set to launch globally later this month with preorders to start on january 24. > g

9/262) offre delval une offre exclusive dans cet tablissement au march central de nancy ou vous y retrouverais de la bonne viande qui vous ferra fondre les papilles ! en tant qutudiant il est difficile de manger des bons plats et surtout de la bonne viande..mais rassurezvous grce avantage plus vous tes sauvsoffre10 sur la note valable ds maintenant sous prsentation de ta carte avantage prsente sur lapplication mobile tudiant e couverte  > g

10/262) estamos en la y en la ! pero tambin puedes ingresar en nuestra versin web.planifica smart gestiona 247 reporta en lneapara ms informacin contctanos o visita nuestra pgina web organiza tus turnos clnicos en una sola app! > i

11/262) offre votre papeterie prfre situe au centre ville est partenaire de notre application! le second trimestre et les valuations de fin danne arrivent trs bientt pas de panique pour limpression de vos dossiers et lachat de vos stylos avantage plus va te soutenir avec une offre folle! offre15 sur la papeterie et beaux arts hors informatiquevalable ds maintenant sous prsentation de ta carte avantage prsente sur lapplication mobile tudiant e couverte  > g

12/262)  airpods 3 airpods 3.? airpods 3 original > i

13/262) thanks for the big apple from my friend.pple  > g

14/262) aseguramos tu skin por 34 usd!! no te quedes sin esta oferta de tiempo limitado!!!  > g

15/262) aqui na link estes modelos esto disponveis a pronta entrega!corre que seu iphone est aqui!quer uma ajudinha para garantir o seu? s enviar uma dm que ns te ajudamos a fazer a melhor escolha  > g

16/262) apple iphone 8 plus 256gb black disponvel8 plus seminovo perfeito sem nenhum detalhe sequer!bateria 94acompanha carregadores originais applepelcula 3d e case de brindegarantia de 90 dias de r240000 por apenas r219999 vista ou em at 12x no carto de crdito com a menor taxa do mercado! entrega em mos em livramento e regioenvio para todo o br..... > g

17/262) macbook una pro entre las pro.stock pro | air consultanos por la tuya!  > i

18/262) .apple i car?  > i

19/262) hi! pocket puppy school here! we just wanted to give you a little reminder to give some bellyrubs to your cute dog.your four legged best friend always waits you happily at home.threetwoone bellyrubs time!  > g

20/262) pervecse ju ofrojme cmimet me konkuruese dhe cilesine me maksimale te cdo produkti per cdo blerje masterphone ju dhuron edhe nje smart bracelet ! kujdes oferta eshte e limituarcover dhe xham mbrojtes te perfshira ne cmim !ulje 30 per karikuesin 20w fast per serine 1113 nqs ju nevojitetmundesi nderrimi edhe vleresimi te telefonit tuaj te vjetermundesi blerje me kestegaranci 6 24 muajtransport falas kudo!adresa: rruga kavajes pran spitalit gjerman! kontakt 0688188188. > i

21/262) retrouvez votre libert et renouez avec vos plus anciennes passions.vous avez aussi le droit dapprcier vos loisirs  > g

22/262) good morning familia! vamos a empezar este mircoles con de gracias por despertarte conmigo las maanas!! la emisora de y ms baja el app de msica mas prendida hoy mircoles gratis latino hits fm y bele androidhttps:play.google.comstoreappsdetails?idcom.new.latinohitsfm iphonehttps:itunes.apple.comusapplatinohitsfmid1450107593?mt8 > g

23/262) download our home city ice app to place and track your ice orders follow your orders online view order history submit maintenance requests and contact our customer service all in one place. > g

24/262) vai perder a oportunidade de comprar seu iphone 13 com melhor preo da regio?  > i

25/262) for more enquiries dm  > i

26/262) el sonido te llega por todos lados.vive una experiencia envolvente cuando escuches msica o veas una pelcula o serie.originales en caja sellada 1 ao de garanta pag con todas las tarjetas de banco hasta en 12 cuotas. > g

27/262) promote it on > g

28/262) gewinnspielespecial guys as a thank you for all your support lately and i have prepared a mega raffle for you with our partners.where you can find over 5000 worth of products.you can win anything all you have to do to win; like this picture comment as much as you can each comment is 1 lot in the drawtag.giveawayseu.giveaways.eu.backup in your story raffleplaystationiphone 12 pro maxmacbook proapple watchiphone 11 pro maxiphone 11winner will be randomly selected and notified dm from us.the judicial process is excluded.the competition is not affiliated with instagram or facebook......check if you have met the terms and conditions if not we can't take you into account in the draw.good luck to you cklich  > g

29/262) apple iphone 7 !....:128100 1778 : 09381069934 10 913 0938106993402633325797  > i

30/262) on wednesdays we choozesnooze.what did you think? did you like these character quotes? which was your favorite? who do you want to see next? > g

31/262)  22... > 

32/262) iphone 12 & 13 series premium back cover availablefollow.shipping all over india.contact 9971153623 whatsapp or call. > i

33/262) comeamos nosso dia hoje agradecendo a nossa cliente.s pela compra de seu iphone xr aqui conosco na torine importados!muito obrigado por acreditar e confiar em nosso trabalho muito obrigado! conte sempre conosco pro que precisar! entre em contato conosco e garanta nossos produtos de prontaentrega! pensou em apple pensou torine importados produtos 100 originais; lacrados novos seminovos originais;1 ano de garantia apple novos;3 meses de garantia em xiaomi e apple vitrine seminovos; entre em contato: 22 998920929 ou clique no link da bio. > g

34/262) find a doctor near you?download now on and..... > i

35/262) apple watch series 7 41mm green 245midnight 125starlight 100blue 3545mmmidnight 190blue 220green 180starlight 190now available at:kool store miamiwholesale.comwww.koolstoremia.comwhatsapp: 1305.707.1077  > i

36/262) apple all type products manufactureing  > g

37/262) encara no t'has descarregat l'app el canut? trobars els enllaos de google play i apple store a la nostra bio. > i

38/262) be surprised to have fabulous apple series 7 t200 plus airpod pro japan best quality combos together.functionalities: crown working with fullscreen changeable states iwatch series 7 44mm 2021 with full screendual bluetooth 4.0 watch 6le low power efficiency full screen with ips hd retina clear view display get scratch resistant glass protection along with aluminum built case 7watch faces for unique style of yourssuperb feature of dialling a bluetooth call and galking to your iwatch is amazing heart sensor with realtime analysis blood pressure monitor blood oxygen monitor sportz mode with 'n' number of sports activities for accurate calorie count with realtime heart rate monitor bluetooth calling message whatsapp notification reminder calculator sleep mode sedentary reminder alarm etcbattery backup upto 1 day single charge charging time upto 2 hours a day airpod projapan heavy quality awesome quality doubletap system 99 active noise cancellation n spatial audio function.explore more & now link in biolet's make 2022 a year of celebrations  > g

39/262) iphone 11 pro gracias por confiar que lo disfrutes!!impecable estado libre para todas las compaas el mejor precio esta ac!! tomamos tu usado! primero probas el equipo despus abonas los pagos son nicamente efectivo pesos o dlar a cotizacin del da se hacen puntos de encuentro o envos a domicilio este y muchos equipos ms en stockentrega inmediata!!  > g

40/262) look on the bright side of your study sessions this semester with our neon airpods cases comment your favorite green emoji > g

41/262) these are nice > g

42/262) buscamos seguir todas os protocolos de segurana para preservar a sade de todos que utilizam nossos servios mas acreditamos que o trabalho em equipe sempre gera resultados melhores! chame um motorista decar !pelo app ou pelo whatsapp 17 99651 1700!link na bio! a  > i

43/262)  adobe lightroom.ios 149.picasa apple photos.sd..picasa apple photos.apple photos.. > i

44/262) si ritorna in smartworking il magic mouse rimarr solo soletto  > g

45/262) cliente novamente retirando o seu iphone 13 pro max 128gb dourado lacrado e 8 plus 64gb vermelho seminovo.muito obrigado pela preferncia de sempre!!! es o > i

46/262) super recomendo ! > g

47/262) iphone 12 & 13 series permium backcoverfollow.shipping all over india.contact 9971153623 whatsapp or call. > i

48/262) find a dentist near you?download now on and..... > i

49/262) nuevo ao nuevos descuento y promocione ! compara y reglate lo mejor.te ayudaremos a hacer tu vida ms brillante !  > g

50/262)  !iphone 13 pro 128gb 256gb 512gb 1tbiphone 13 pro max 128gb 256gb 512gb 1tbairpods proairpods maxairpods 2airpods 3 ! ! > i

51/262) bora de ncia 92!! confira a seleo de produtos que preparamos para vocs.garantam j seu combo e bora armar aquele churras com muito sabor e qualidade!1 maminha estncia 921 linguia toscana prola1 panceta temperada na mostarda1 espeto de mandioca com queijo1 po de alho zinho tradicionalapenas r 9990est esperando que para garantir o seu?venha j buscar aqui no ! whats: 17 991146243ou clique no link e nos mande um http:bit.lyboibraboolimpiaaproveite e baixe nosso.faa suas compras e receba onde estiver!: https:bit.ly3fdzmju: https:apple.co2qy0sk8boi brabo olmpia rua coronel francisco nogueira 637 sala apatrimnio de so joo batista olmpiaspoferta vlida apenas para esta unidade na data de hoje. > g

52/262) learn swift to earn this  > i

53/262) how much they made? > i

54/262) bro.? > g

55/262) iphone 12 and 13 series premium back cover availablefollow.shipping all over india.contact 9971153623 whatsapp or call. > i

56/262) terimakasi pembelian cod di store kitasudah berbelanja di store kita yuks tersedia barubekas harga grosir ya bos..yang mau kredit juga bisa proses sangat mudah..tukar tambah juga bisa dimana lagi kalau bukan di store kita ponsel no.247 lantai4 tahap4 plaza medan fair area tangga bioskop cinemaxxwa: 082160085855 original > i

57/262) seu iphone usado agora vale como parte do pagamento na compra de um novo pegamos seu iphone usado na troca por um novo.somente para aparelhos iphone 7 em diantegaranta ja o seu produto com qualidade e garantia apple! 62 985924095 62 30925976www.okstoreoficial.com.br  > i

58/262) send pic to.arts.world. > i

59/262) iphone 13 pro max disponible en color gold blanco azul y negro.pide el tuyo!. > i

60/262) seamless transaction on easyflip app download the easyflip app the on play store & start trading at the best rate............. > g

61/262) new version of iphone se3..pple  > i

62/262) apple ha depositato un nuovo brevetto di cosa si tratta?la nuova scoperta riguarda un sistema per aumentare la velocit di comunicazione tra dispositivi!come? con una modalit di trasferimento ottico dei dati.il 14 dicembre 2021 ha registrato il brevetto che punta a risolvere linefficienza e la lentezza della comunicazione tramite cavi di rame.nello specifico il sistema si attuer tramite lallineamento di due lenti mobili poste dentro ai due dispositivi che dovrebbero comunicare tra loro.le due lenti sarebbero cos in grado di sfruttare al meglio la banda per scambiarsi i dati pi velocemente.pensate che questa innovazione sar integrata al pi presto nei device di apple?  > g

63/262)  !.mientras lees este post pierdes tiempo valioso para tener este iphone en tu bolsillo lo mejor de iphone en un tamao que se ajusta perfectamente a tu bolsillo...escrbenos al whatsapp para brindarte la mejor asesora..si pides hoy te llega hoyestamos ubicados en la ciudad de ! : whatsapp: 57 3042709678 barranquilla | colombia calle 72 29 | local : lun a sab 9:30am a 6:00pm dom y fer 9:30am a 2:00pm..... > b

64/262) hair color  > g

65/262) this is what i think of the concept of work in my opinion i should be the only thing allowed on top of your lap obvs when i want not when you want! thank goodness i have staff to do my work! sausages do look great next to apples though!!.... > g

66/262) in love with buildings........ > g

67/262) are you a trainer?coaching online? spending hours to create content and share to your clients?stay tuned for great stuff coming soon for you!  > g

68/262) dm pic on.earth 5m > i

69/262) os melhores valores do mercado esto aqui! valores sujeito a alteraes sem aviso prvio! aparelhos novos e semi novos em at 12x no carto de crdito!levamos at voc! pegamos de entrada a partir do 7plus aps uma avaliao.temos acessrios e mais produtos apple tambm! valores sujeitos a alterao sem aviso prvio foto de capa ilustrativa pinterestentre em contato: 44 999728202  > b

70/262)  : 12 x 7 8  > 

71/262)  : : 13promax1313pro 12promx 1212pro 11promax 1111pro xsmax xxs7p8p78se66sa51a31a21sa12a30s s20fe redmi note8 redmi note8pro redmi note9pro poco x3 telegram & whatsapp:0912 836 25 22tell & sms0912 836 25 22channeltzmobile : 09128362522  > b

72/262) iphone flip pro with unique design : ::  > g

73/262) only the best for our users download the mobbi app and discover the best premium locations chosen by mobbi for you stay connected and enjoy your best moments with mobbi all around our splendid city find your mobbi powerbank at in...whenever you need.non aspettare di rimanere senza batteria.scarica gratuitamente lapp mobbi su & e provala entra subito a far parte della e scopri la madre di tutti servizi di  > g

74/262) airpodsgood  > g

75/262) new arrival of acer acer travel mate p2 intel core i7 11th generation 256gb solid state drive 8gb memory webcam bluetooth wlan backlit keyboard no optical drive 15.6 inch windows 10 pro black color.............................355000dm to place ur order whatassp number mr jide08039110163 or dammy07036028706.i  > i

76/262) kekuatan super baru di tangan anda.iphone 13 mini kini mulai dari rp 520.791bulan.kunjungi storyi cipinang indah mall..berlaku di seluruh storyiberlaku hingga 14 januari 2022promo dapat berubah sewaktuwaktu tanpa pemberitahuan terlebih dahulu  > g

77/262) min sudah ada di store kah? > i

78/262) : keep at it!dont expect your business to grow overnight.it can take time to grow a business that consistently hits your goals.if you are looking for longer term steady income take your time and keep at it! persistency and consistency are key when growing any type of business and there is no exception for a dog walking business.set time aside every week to review your business your profile set goals and make a plan. > b

79/262)  dogselfie  > b

80/262) promote it on 3m > i

81/262) iphone 8 64gbbrand new condition device onlyprice 16000... > i

82/262) what do you think ?............. > b

83/262) 14001022 iphone 13 pro max zaa 1 tr active 60500000512 not active51500000256 not active4170000041300000256 active 4080000040300000128 not active 3770000038000000128 active3690000037200000iphone 13 pro zaa 1 tr active52000000512 active 46000000256 not active 36800000256 active 374000003620000036400000128 active 3440000034900000iphone 13 512 active 323000003100000031000000256 active285000002880000029300000128 not active288000002880000028000000128 active27300000263000002650000013 mini 256 active 27000000iphone 12 pro max zaa 512 not active3900000039500000256 not active 3540000036500000iphone 12 pro zaa 512 not active 34500000iphone 11 128 not active21900000iphone se 128 not active13500000airpods 2 3600000 3 5000000 pro new 2021 5700000 pro 6100000adapter 20w orginal 850000 apple watch series 6 44mm 12800000series 7 45mm135000001320000041 mm 1240000012200000.. > 

84/262) baru baru ini whatsapp diketahui telah mengembangkan animasi emoji cinta versi terbaru emoji cinta akan semakin berwarna dan kini animasi denyut pada emoji cinta akan bertambah dengan pilihan warna lebih banyak.tak hannya mengembangkan emoji cinta berdenyut whatsapp juga diketahui menyiapkan fitur reaksi atau messge reaction.messge reaction merupakan fitur yang memungkinkan user untuk memberikan reaksi terhadap pesan yang dikirimkan.wah patut kita tunggu nih fitur terbaru dari whatsapp.kedua fitur tersebut akan rilis di ios dan android meski tanggal perilisan masih dirahasiakan. > i

85/262) i am back and finally joined the apple club! it's been over a week and i still can't use instagram on my samsung.but magic apple did the trick.now that i have a new phone instagram works flawlessly.we'll see how it goes.being in czech republic for over a month i couldn't buy an iphone anywhere here.they are simply not available here and probably won't be soon.i think the main problem is that there is no official apple store in czech republic.so i had to try my luck in germany and it didn't disappoint.not only it was a great trip but i got a new phone! stay tuned for a new content  > g

86/262) welcome to the club buddy > g

87/262) missed your contents bro welcome back > b

88/262) iphone 12 pro 128gb 3.5 months old brand new condition 74500call us at 91 7888532100  > i

89/262) would you like to see this in 2022?.did you like itcomment your thoughtstag a friend who loves it!!dm for buisnessshoutouts!!visit the link from bio for exciting deals!!.. > g

90/262)  dxomark  > g

91/262) iphone 13 pro max 256gb price.....comment  > i

92/262) space  > i

93/262) macbook a i r.apple silicon chip m1 8gb 13 retina display 512gb..macbooks al mejor precio siempre!.garantia oficial apple!.54 9 11 5335 1111.conesa 80 colegiales 1414 caba..... > i

94/262) precio? > i

95/262) us itunes cards the best online! instant delivery: fast secure.legitimate gift cards.mayur is a digital marketplace where you can find great deals.contact us at 9802097598 today. > g

96/262)  : :0912301576602122886068 x x xsmax > 

97/262) dm it on.art.gallery 1m > 

98/262) iphone 7 128gb 2nd like new original kondisi normalmulus fullsetgaransi 1bulanready stock :oppo realme xiaomi vivoinfinix samsung iphone like new originalinfoordercp : wa 083844005549 ranggaterima tukar tambahjual belikreditalamat toko kamisearching google map :rizqia phonejangan lupa follow ig toko kamirizqiaphone  > i

99/262) bandingin iphone rilisan tahun 2018 nihhai guys kali ini mimin coba ulas tipistipis dua iphone yang sering bikin orang bingung mau pilih yang mana nih.mulai dari ukuran sampai fitur semua mimin ulas deh jadi langsung swipe aja yaamore info jl.kaliurang km 5 no.82b kocoran caturtunggaldepok sleman yogyakarta whatssapp: 62 821 1178 8699 www.mcapple.id  > i

100/262) une nouvelle vision de la tl.avec lapple tv 4k profitez du meilleur de la tl.et de vos appareils et services apple prfrs.pour une exprience unique qui change votre salon du tout au tout.disponible chez univers digital.nos experts sont votre disposition pour vous la prsenter aux stores ud zerktouni et ud casaanfa.et pour mieux vous servir nous sommes ouverts du lundi au vendredi de 9h30 19h30 et le samedi de 9h30 13h.92 bd sidi abderrahmane casaanfa 246 bd zerktouni casablanca 0522 942 215 0522 225 789 www.universdigital.com. > i

101/262) hp spectre x360 gem cut 8th gen intel core i7512g ssd 16g ramtouch screen keyboard light face identity finger print price: n660000get your quality grade gadgets at an affordable rate.please call to confirm availability before payment.contact us at:2348067047344whatsapp:2348169964197email:applelogphonestore.comnationwide delivery t&c applied  > i

102/262) apple watch avengers edition watches gps motion track heart rate bluetooth call platform: mtk2502c case: alloy strap: silicone with extra velcro belt main screen: 1.78 hd ips 320385 touch screen: 2.5d curved capacitive fullfit touch screen bluetooth push: sms whatsapp news and other client information and other communications in time to remind heart rate detection: heart rate monitoring monitor your heartbeat around the clock pedometer: exercise step count calorie consumption exercise mileage record sedentary reminder: its time to get up and exercise and change the unhealthy lifestyle sleep monitoring: objectively scientifically record and analyze your sleep status quantitatively find mobile phone function: antilost reminder.twoway search bluetooth music playback: play on the watch bluetooth function and version: 3.0 4.0 support bluetooth call battery specifications and capacity: 320mah highcapacity polymer vibration motor: support other functions: alarm clock calendar stopwatch calculatordm us for the price. > i

103/262) ....nakisastore.ir  > 

104/262) dastet dard nakone > g

105/262) aj 09905834077 09125834077 6 > 

106/262) nice > g

107/262) iphone 13 pro max 256gb 42499 11 12 city 11 xr  > i

108/262) cliente nathibarnabe retirando o seu iphone 11 64gb preto lacrado em loja e garantindo o seu brinde carregador capa e pelcula.ao es o > i

109/262) valor do iphone 11 ? > i

110/262) iphone 7 plus gold 32gb touch id: 5000 90 :  > i

111/262) credits:  > 

112/262) iphone13pro > i

113/262) iphone xr black 64gb face id: 9000 90 :  > i

114/262) ple airpods pro airpods.tech.ua 3 899  > i

115/262) posie militanteou de lart de lart de ravaler les faades par camera : zeiss ikon zmlens : voigtlander ultron 28mm vintage linefilm : chemistry : bergger pmk 24c 13mn berfix neutralscanner : plustek opticfilm 8200i seref : 20220101  > i

116/262) jolie! j'aime beaucoup!! > i

117/262) news: malgr les controverses l'app store rapporte de plus en plus.les dveloppeurs ont gagn plus de 260milliards de dollars sur l'app store d'apple depuis son lancement en2008 !! impressionnant  > g

118/262) wow mon dieu > g

119/262)  &..shop no.3 nexus point civil linesnagpur.for inquiries dial:.91 96895475539834078553 citycollection7.com  > 

120/262)  iphone 11productred 64 gb iphone 96.com.ua  > i

121/262)  iphone 12 128gb bleu venduetat de battrie : 98 avec la boite et cble original prix : 127000 da livraison 58 wilaya pour commander : 0671802229 > i

122/262) delicious > g

123/262) bellas sabanas bordadas.tamaos moiss y pack and play.sabanas nicas y de una exquisita calidad.ideal para personalizar el cuarto de tus hijos!te invitamos a conocerlas! a acacity aca adelmar  > g

124/262) send pic on > g

125/262) promote it on.of.blacks > g

126/262) cool! > g

127/262) case cover for apple iphone 5s 5 se 6 6s 6 plus 6s plus....get yours!....free shipping....pro  > g

128/262) introducing apple series 7 watch with premium leather belt including 1 plain belt additional.1:1 gps bt calling apple on off boot screen logo retina hd display 326pp pedometer gps sleep monitor deep sleep light sleep monitoring night mode aluminium alloy abs built quality diy watch face change add new cool watch faces heart sensor working with 247 monitoring feature including blood pressure & heart beat pulse count tremendous fitness mode added with different sports category to calculate heart beat calorie burnt step count bluetooth calling bt music bt camera phone book call log dialer call logs alarm message notification calendar sedantry reminder motion sensors flip to mute incoming call flip to mute alarm wake up gesture anti lost vibration alert battery backup upto 1 2 dayscharging time upto 2 hourswireless power cable for fast charging get all these superb and awesome features exclusively at rs.2499 rs.50 shippingexplore & 's make 2022 a year of celebrations  > i

129/262) ..: : : :  > 

130/262)  various colors available..........................................11promaxall iphone 12promaxall iphone 13promax..........................................www.bhplusonline.com.................................................................................... > 

131/262) deal with the best deal with 24 months warranty on all our products configurtion et paramtrage gratuite compte icloud gratuite deal with the best deal with....yaound mont anne rouge face mtn 694968388 cameroun  > g

132/262) cool > g

133/262) confiance collins > g

134/262) follow like the post for more setups share with friend'all credits go to the respective owner make sure to follow the ownertags mention us if repost rate this photo 110!follow me for more.leave a comment.credit. > g

135/262) all iphones available 100 battery health 15 days warranty all over india delivery only interested dm plz contact 7678258003  > i

136/262) i phone 6 price > i

137/262) primeiramente feliz 2022 atrasado! eu sei sempre ativado no delay! mas at que isso no to ruim assim n?!afinal de contas j ta rolando msica nova nas plataformas digitais.aproveitem e compartilhem com os migos bele?! e que 2022 seja lindo e mais novidades chegando ai!apertem o play no novo single do m.e.i.a amanh link na bioweeeeee............ > i

138/262) love it dm > g

139/262) dm on > g

140/262) fotassa > i

141/262) apple iphone 11 128gb white brand new garansi resmi tam erajaya 1 tahun imei terdaftar kemenperin not refurbished unit ada garansi personal dari kami free bikin apple id baru dan back up pindah data free pelindung temperred glass dan softcase bisa tukar tambah price : 10999000 more info : wa 082234304043 fast respons atau direct message inbox ig lokasi toko malang kotahappy shopping > ii

142/262) .......... > 

143/262) .599 acive '.& 13.: follow us 12  > 

144/262) .nore.jewellery > 

145/262) la chanson welcome to brighter days poursuit sa progression dans les charts de uk talk radio angleterre royaumeuni.aprs tre entre dans le top 10 elle atteint dsormais la 3me place !  > g

146/262) : je pense que a sera les prochaines et toujours chez nagabbo les qui rendent beau  > g

147/262) iphone 7 plus rose gold 32gb touch id: 5000 90 :  > i

148/262)  64128 ???? > 

149/262)  iphone 11 64 gb 100 ?.com.ua  > i

150/262) apple pie for a sweet evening treat  > g

151/262) .icon > 

152/262) .: : : :  > 

153/262) ........ > 

154/262) team daraje 1 > 

155/262) nomber 1 > i

156/262) daraje 1 > g

157/262) when you see apple pie everywhere.it's time to make one. > i

158/262) send pics.brand > g

159/262) wow wow > g

160/262) wow yummy > g

161/262)  sulada iphone 1212proiphone 12promaxiphone 13iphone 13proiphone 13promax size 384041size 424445  > 

162/262) cranberry and apple pie 3secf22iso 100 diffused window light  > i

163/262) send on post.ig > i

164/262) yummy combination xx > g

165/262) rate this photo 110!follow me for more.leave a comment.credit. > g

166/262) 9 out of 10 > i

167/262) excellent > g

168/262) 9.510 > 

169/262) i love it give it to me > g

170/262) breaking apple is the first company to reach a 3 trillion market cap do you own any shares of apple? comment below! > g

171/262) after btc > g

172/262) btc will change that soon > g

173/262) this is fn nuts.i still think aramco is not valued properly... > g

174/262) and they said copying others hw wasn't gonna get you far > b

175/262) biggest steve jobs a humble man like el gato negro > g

176/262) i never knew i will be able to pay off my bills and get to my stand in life..i reallydo appreciate > b

177/262) for a start i deposited 2000 to test the waters in 7days i got a return of 11450 his diligence and honesty is undeniable.connect with.... > g

178/262) the way we experience the world around us is a direct reflection of the world within us.gabrielle bernstein  > i

179/262) nunca he ido a esa plaza > i

180/262) buenaza hermano > g

181/262) me encant la foto el reflejo > g

182/262) tan cierto !!!! por cierto esta sper cool la foto eeehh > g

183/262) excelente toma nocturna ! y muy ntida quedo perfecto el encuadre > g

184/262) beautiful shot! > g

185/262) buena frase bonita foto y lugar > g

186/262) i made 50k with > i

187/262) receiving 25500 afterinvesting 5000 was what i never expectedthanks for putting an undying smile on my face > g

188/262) the new beastcage 12 series are here compatible with beastgrip lenses and filters moment lenses sandmarc lenses and others.shop now from link in bio!!.did you like itcomment your thoughtstag a friend who loves it!!dm for buisnesspromotion or shoutouts!!..follow. > g

189/262) price ??? > i

190/262)  s21 ultra??? > i

191/262) bismillah semoga dapat > g

192/262) how can i get this product? > g

193/262) .sej > 

194/262) boleh keknya bos > g

195/262) a dboite!!!! > b

196/262) .suis.denisse > 

197/262) .e.n.s.h.i.l.u.g.o > 

198/262) charging up all of my essential devices with one single wireless charger by... > g

199/262) wonderful mate > g

200/262) very practical > g

201/262) such a cool charger! > g

202/262) love this! > g

203/262) great shot buddy > g

204/262) amazing shot brother! > g

205/262) cool shot bro > g

206/262) dope shot and great charger! > g

207/262) awesome product and looks practical > g

208/262) nice shot > g

209/262) nice charger > g

210/262) remembered apple airpower? this accessories reminds me that cool stuff > g

211/262) great man > g

212/262) sick shot dude love it!! > g

213/262) wallpaper by.?? > i

214/262) i really like te lighting on this.it has this faded look but it looks good for this type of photo! > g

215/262) another banger! > g

216/262) whats the case or bumper on your apple watch? > i

217/262) great > g

218/262) love the ampere products great shot here parth! > g

219/262) perfect > g

220/262) post para voc encaminhar este post de utilidade pblica! 8 centros de compras que voc precisa conhecer em orlando! quais voc j visitou?se voc ainda no nos segue clica agora para seguir!  > i

221/262) obaaaaa > g

222/262) sonhando com o dlar baixando pra gente poder voltar a fazer boas compras em orlando > i

223/262) lake buena vista factory story timo tambm > g

224/262) unica apple store aberta mais prxima de orlando com fila e agendamento a do altamonte > g

225/262) o brio no fechou? > i

226/262) acho que faltou o lake buena vista factory stores. > b

227/262) qual tem preos melhores ? > i

228/262) adoro!!!!! > g

229/262) marketplace vida > g

230/262) adorei o post! obrigada > g

231/262) .roberta > 

232/262) .borgesx > 

233/262) .ssa1981 > 

234/262) .nemias oh saudades desses lugares no ? > g"""

    tests.replace("\n\n", "\n")

    for test in tests.split("\n"):
        if test:
            test = test.replace("\n", "")
            comment = str(test.split(") ")[1])[:-4]
            level = test.split("> ")[1]

            if level == "g":
                level = 'good'

            elif level == "b":
                level = 'bad'

            elif level == 'i':
                level = 'inactive'
            else:
                continue
            temp_comments_keeper.append(f"__label__{level} {comment}")

    print(*temp_comments_keeper, sep="\n")


def three():
    cleaned_comments = {
        'applewatch': ['available as seen!....', 'de se apaixonar no ? vem que tem para todos os gostos!.....',
                       'what to expect from apple in 2022! follow for more apple watch related content! credit: ',
                       '.28 miras 87054991577 87715495497 miras ',
                       'a procura de investir em um novo iphone mas no sabe qual modelo exato? vem que a castanhal imports te ajuda indicando de acordo com sua necessidade.temos uma seleo enorme!.aguardamos sua compra.whatsapp 91 982709485.',
                       ' apple watch 8 apple..',
                       'im liking this watch face today.some useful complications on it and its attractive and simple.the bottom right complication is airmail i think its just a cuter looking complication than apples native email app.middle bottom is heart watch.bottom left is coloring watch.middle is ticktick a todo list complication.',
                       'i do like this face but i do wish they would update it to make it fit better on the bigger screens.',
                       '.applewatch mk applewatch', 'appleiphone13 ',
                       ' a o a o e e 50 ee50 o a i..h..n.13 400gb ea y a o a a o.o o o:1o 2e a o y e s o! e 17 22:00 o e o a o a......',
                       'du mchtest eine smartwatch passend zu deinem smartphone? dann haben wir die perfekte lsung fr dich!mit unseren smart tech tarifen hast du schon ab 1599 monatlich das passende gegenstck zu deinem smartphone am handgelenk.egal ob apple watch oder galaxy watch bei uns ist fr jeden was dabei!wir freuen uns auf euch! ',
                       'yang mana dah lama teringin nak pakai iphone tapi duit cash tak cukup bayar je bulanan dengan bijak sebab tu m2a gadget tawarkan plan ansuran ambil dulu bayar kemudian.dengan syarat yang simple link di bio ',
                       'dd piyasadaki enn iyi fiyat bilgisi iin dm fet fetteyiz fetteyiz fettengelenlertakipetsin lf ',
                       'h tr tr gp khng a trc 0 iphone 7plus 32g lock kch full qt gi : 4.200.000 bao tt 10 ngy bo hnh 2 thng ph kin : sc zin p cng lc lin h :0966683952nhn trc tip : m.medidongtrungblack nhm zalo : https:zalo.megelvwrc410 youtube : https:youtube.comchannelucshshyvez8t9qwfricwrhq a ch : https:goo.glmapsgbkwfuar4tjszk1t5 ',
                       'samsung galaxy s20 fe', 'samsung soyuduculaq nmrsi 994516767777 fet fetteyiz eher',
                       'apple watch',
                       'bienvenu chez apple cobs : galaxy s20 5g 12gb128gb europen fissure arrier garantie de magasin et bon dachat prix : 72.000damagasin : oran seddikia en face marche tel : 0696519670 ',
                       'hello! how is your week going? face from paired with the ginger sport band.', 'love it!',
                       'bienvenu chez apple cobs : iphone 13 pro max 256gb silver europen sous emballage garantie de magasin et bon dachat prix : 27.2000da magasin : oran seddikia en face marche tel : 0696519670 ',
                       '..applewatch...www........applewatch.iphoneiphonelinetvsuica..www',
                       '13 promax newseal vnae vn lun mu m phc v khch yu sm ttgi nay tt lm lm ri 0932.58.78.98 hoc inbox facebook 0982.91.92.94it apple shop 59 ng quyn bmt daklak | | |',
                       "looking after your health is important.maybe you've joined a gym recently or maybe got a fancy new watch to help you stay motivated.both of these things cost more than life insurance and you can get 50 off the gym and a free apple watch with certain providers.speak to me today to get physically and financially healthy by reviewing your insurance! ",
                       'gift from acu gift from dadinlaw from someone special thanks so much everyone ps: qu sinh nht nm nay bn qu bn i ngy mai xem c g na n',
                       '........',
                       ' 23:00 50 20 i..h..n.13 256gb 20 samsung z flip 3 e 10 apple watch 6 :1 2 y s s !3 ! iphone samsung ',
                       'disponvel: rolo trmico para multicaixas 10 unidades 57 x 40 x 11 preo: 1 042 akz | entrega grtis para luanda.tecnologia de impresso: trmicadimenses: 57x40x11mmquantidade: 10fale connosco:tel:990893969email:comercial.aosite:www.sojofil.ao...',
                       ' eggshell lv ', ' ?.400 ', ' iphone 11 xr x 8 7 13',
                       ' 0215590740009123791128whatsapp&instagramprice:125t ',
                       'sale ma tt h tr tr gp khng a trc 0 iphone 12promax 256g fulboz 2sim gi : 25.000.000 bao tt 10 ngy bo hnh 2 thng ph kin : sc zin p cng lc lin h :0966683952nhn trc tip : m.medidongtrungblack nhm zalo : https:zalo.megelvwrc410 youtube : https:youtube.comchannelucshshyvez8t9qwfricwrhq a ch : https:goo.glmapsgbkwfuar4tjszk1t5 ',
                       'new arrival 2022series 7 smart watch ak37 wireless charging smartwatch fitness bracelet now available! ksh 3500!same day delivery across kenya wireless charging androidios waterproof stepscaloriessleep monitoring heart ratebody temperature blood pressure sports modecall notifications instawhatsappfbsmsvisit our pick up point at ibrahim stalls shop e9 to get yours today!dm or click link in bio to whatsapp for delivery today!',
                       ' ? !..66 64.; 0|0|14; 36 ; tradein ; ; ! ; 3 ; 5.',
                       'riparazioni smartphone in tempi breviricambi sia originali che compatibiliriparazioni anche su appuntamentograzie mille a chi ogni giorno si affida a noi ',
                       'apple watch se nike ',
                       ' a o a o e e 50 ee50 o a i..h..n.13 400gb ea y a o a a o.o o o:1o 2e a o y e s o! e 17 22:00 o e......',
                       ' a o a o e.0e 50 ee50 o a i..h..n.13 400gb ea y a o a a o.o o o:1o.0 2e a o y.0 e s o! e 15 22:00 o e o a o a......',
                       'segundo os rumores este servio de subscrio de audiolivros poder chegar no final do ano...',
                       '..whats app 89337775797.', 'iphone 6s 32gb hatasiz im37',
                       'huge savings on apple watchesbrowse our wide range of preowned & clearance watches now.',
                       ' ?..', "...i'm i'm just do it...270m ",
                       'gnn rnapplenin son dnemlerde en ok satlan rn olan iphone 11 da sadece 9710 nyas veri rnler rnler lklyaam',
                       '..? : ; ! 15 : apple watch 5 silver 40.applewatch ',
                       'earth tone aesthetic 24 colors premium chvre leather embossing24.',
                       "outnew oppo a16colour black 332thank for mustafaarp gadget storejl.besse kajuara depan diva storewa : 085254068686ig : gadget centrejl.sukawati samping d'simple cafewa : 082187989788ig : ",
                       'bienvenu chez apple cobs : iphone 12 64gb 100europen garantie de magasin et bon dachat prix : 11.9000damagasin : oran seddikia en face marche tel : 0696519670 ',
                       'applewatch series 6space gray44mm ! ',
                       'sada roma stylov emnky pro businessmany...vce sad strapado.cz...',
                       ' black shark 5..ktusa0 miit.panda is bald.!.mobile.mi ',
                       'full house for this morning love having all the energy back in the room its a brilliant buzz ',
                       'rejoined this morning i have rejoined.i loved this when i was a full member previously the workouts the community and the support.i have even booked in my initial call!super excited to be back ',
                       'hey please dm our main page liafit.shop if you are interested in becoming our ambassador',
                       "what's your favorite apple watch feature? for details we never settle.",
                       'slow pace today last night leg day at the gym the pain still there 2 2volt ',
                       'send picture..exparts..vk', ' airpods ',
                       'bienvenu chez apple cobs : iphone 11 64gb 100europen coffret garantie de magasin et bon dachat prix : 10.3000da magasin : oran seddikia en face marche tel : 0696519670 ',
                       ' 12pro max pple',
                       ' a o a o e e 50 ee50 o a i..h..n.13 400gb ea y a o a a o.o o o:1o 2e a o e s o! e 17 22:00 o e o a o a......',
                       'son dnemlerin en ok konuulan teknoloji konusu tabikide apple m samsung mu konusu.bu sorunun cevabn 7 zelliiyle karlatrarak ; performans kamera ekran bataryailetim sistemi ve fiyat olarak sizlere hazrladk.ayrntlar ekran yana kaydrarak inceleyebilirsiniz nyas veri rnler rnler lklyaam',
                       'se voc correr ainda dar tempo de pegar o seu!fique atento a nossos stories e no perca nenhuma oferta o',
                       'the leather will change according to the lifestyle link in bio line : instagram: blackbeardhandcraftstudio fb page : blackbeard handcraft studio email: blackbeardhandcraft.com tel: 66 957199526 ',
                       ' applewatch applewatch applewatch smartwatch sportloop', ' cil ',
                       '1sbnd016.colorprice3850 tax insale1925 tax in..:..:7654se..:.', ' 12pro max ',
                       "out iphone xrcolour yellow 64gbthank for syahruddinarp gadget storejl.besse kajuara depan diva storewa : 085254068686ig : gadget centrejl.sukawati samping d'simple cafewa : 082187989788ig : ",
                       'wenn du jemanden ohne lcheln siehst schenke ihm deins eoftheday dchen stenmdchen stenkind ',
                       "outnew oppo a16colour blue 464gbthank for fajriarp gadget storejl.besse kajuara depan diva storewa : 085254068686ig : gadget centrejl.sukawati samping d'simple cafewa : 082187989788ig : ",
                       'longvadon applewatch misty grey longvadonapplewatch strap caiman series misty grey w silver details ',
                       ' 1213 ', 'vowood apple watchapple watch2mycase11000 se234567 ',
                       'appaloosa horse leather watch strap for apple watch...dm for custom size watch strap or other project using this leather',
                       'dm me please',
                       'aproveite os melhores smartwatch do momento aqui na smart store.no perca tempo e entre em contato com a gente para pedir j o seu!!!......',
                       'valor', ' apple airpods 2 : 155.dp 8 380 73 3538839 ', ' whstore13 ? welcome direct.',
                       'fakir tlaq nmrsi 994516767777 fet fetteyiz eher', '384041mm424445mm ',
                       'reasons why go above and beyond for your health and safety! not just a pretty watch or a device to make calls.well done apple speak to.protected2021 and find out how you can get an apple watch with your life insurance plan ',
                       'fitness macht mega spa h ck ',
                       'mak mak dengan keladi berpisah tiada..penuh kereta dgn kladi sekarang orang join kutu je senang tau tak cemana nak dapat iphone atau ipad idaman mcm ni tanpa perlu bayar mahal2? caranya senang saja just join kutu dgn gadget streetbarang original ada apple waranty cod smpai dpan rumah dpt byk freegift lgpm kitorang utk booking slot jangan risau kitorang trusted ',
                       'abstoreapplewatchapplewatch!! e ',
                       '.; !...maximum..tempered glass..: https:bit.ly3bajxdr : www.roseandblue.gr link in bio 211 4049890eshop.gr',
                       'dont get stuck on how to disconnect the easily as this video is going to describe three easy ways for disconnecting your apple watch from your ',
                       'promote it on', ' iphone airpod airpods3 applewatch applewatch ',
                       ': airpods 3 cover.airpod 3..200.airpods airpod3....casemania x2 2 bts..line : https:lin.eewtr8gtxinstagram : casemaniax2facebook : casemania x2tiktok : :.casemania x2https:goo.glmapsoe2dhvujidfqstoe6',
                       '7....7 7 1',
                       'works with android and ios!wireless charging smartwatch fitness bracelet now available at an unbeatable price! visit our pick up point at ibrahim stalls shop e9 today! or click link in bio to whatsapp for delivery available in black and pink same day delivery across kenya ksh 3500 wireless charging androidios waterproof stepscaloriessleep monitoring heart ratebody temperature blood pressure sports modecall notifications instawhatsappfbsmsvisit our pick up point at ibrahim stalls shop e9 to get yours today!dm or click link in bio to whatsapp for delivery today!',
                       'iphone 12 icenter iphone 12 icenter call center:07508942096erbil:07517418146baghdad:07707071307sulaymani:07727851010duhok:07517418151',
                       'nrx?', 'iphone xs 64gb th 98 12900 6 7 8 fuji ',
                       'pour un style lgant tout en discrtion : le bracelet carbone https:www.bandband.comproduitcarbonebraceletapplewatchencuirdagneaumadeinfrance',
                       'realme c21 ram332gb 98 3300 6 7 8 fuji ', '.durch dick und dnn.von dick nach dnn.',
                       'brutal was ihr da geschafft habt gehrt eigentlich in die zeitung',
                       'ihr seid ein tolles und schnes paar...respekt fr eure leistung',
                       'tolle leistung.hut ab! passt auf euch und eure gesundheit auf.', '14001023.cell.cell.cell ',
                       'seems the common answer these days is 50 you spend hundreds on a phone so why take the risk of these nifty fifty repair shops.trust your repair in the hands of an apple independent repair partner with acit certification.pop in to see us today 17 north main street wexford or get a quote online at www.iphixx.comwe repair all brands of phones tablet gaming consoles macbooks pcs and imacs.',
                       'send pic on',
                       'w o w so my mum called this morning and asked if i was in.i told her i was on my way back from the school run and id be 5 minutes.she told me she was 2 minutes away from mine with a surprise for me and what a surprise.so shed been to asda and saw these pans in the sale.it came to 61 altogether but should have been over 120.cant wait to use them.thanks mum ',
                       'oh wow how lovely! as mentioned in group too!', 'i love my scoville pans and trays.',
                       'we have these', '113 4.80.11.0 1025 800', '...: 0916630412506153222469.',
                       'whaaaaats up ??? workout with hubs this morning!!! ', 'promote it on.community', 'sand pic dm',
                       'send this pic.fittnes.ig', 'check your inbox please', 'check you inbox please', '..........',
                       'nhktv', 'magsafe',
                       'swipe across for a few simple ways to create and stay in a calorie deficit.save this post and share with a friend ',
                       'promote it on.of.womens', 'wow send pic on', 'send pictures..exparts..vk', 'send this on',
                       ' ? 5 bluetooth..910.airpods ? ',
                       'california what do you think of this shot?band: watchface: linen blue is surprisingly a bit purple so i thought id pair it with the new english lavender coloured watchface.what do you think?california watchface: love how much detail you can get into the complications and yet still have that classic style.er',
                       'nice sunset', 'dope shot bro!', 'nice',
                       'this is amazing! an engineering masterpiece combined with an awesome photographer!',
                       'beautiful love the sky in the background', 'great combo!!! great shot as well.',
                       'very nice shot', 'great shot really focuses my eye to the watch.',
                       'been a bit lax of late locking in my wednesday based woven nylon pictures.heres todays pic what do you think of it?shout out to for coordinating!band: er',
                       'nice shot !', 'amazing!', 'beautiful shot!', 'cool love', 'nice shot', 'dope',
                       'happy wednesday!', 'stunning mate', 'nice watch band',
                       'an engineering masterpiece combined with a super talented photographer the result is truly amazing! keep it up!',
                       'happy wednesday looks great', 'sick pic',
                       'wow that band looks great! i keep looking on ebay for a good woven nylon but havent found one yet!',
                       'nice.works really well.', 'great shot.love the colour of this band', 'thanks!', 'thank you!',
                       'mysterious greatness im grateful honored to know im your favorite', '....', 'you my fav too',
                       "it's obvious.the biggest in ghana", 'that your video is fucking funny post it again',
                       'interesting', 'lessgoo', 'wow more to come bro', 'last photo is', 'you too much',
                       'simple black edc for today slim leather wallet by key organiser by gts mini 2 watch by one plus 7 planning to upgrade soon...',
                       'oof this looks clean in missing an apple watch though', 'cool', 'nice bro !',
                       'great flatlay as always', 'great shot bro!', 'oh heck yes', 'clean bro! love that wallet',
                       'clean lay brother great edc', 'simple but the best', 'clean flatlay', 'woah! the texture!',
                       'black feed', 'edc shot of the day', 'i think you should carry a pen too', 'great shot brother!',
                       'matte black all the way!', 'such a clean edc looks so good bro!', 'cool shot'],
        'macbookpro': ['there are a lot of good options for workspace accessories.', 'the office',
                       "get a brand new iphone 13!enter our time limited contest and get iphone 13the most important step don't skip it go to the website select your phone important is highly requirement complete the anyone simple survey.when you done your survey then give me a screenshot on my inbox.the link in my bio important follow this account like the recent post share this post to 15 of your friends comment below done those who write done in the comments below please leave us a message in a direct inbox ",
                       "high value and luxury goods auction featuring:dell precision 5520 laptop macbook pro a1398 samsung notebook 550samsung galaxy a52 smart phonesealed amazon echo dotdon't miss this one ends from: fri 14012022 8:00 pmhttps:loom.lylbvzscc ",
                       'lention gan 100w gallium nitride fast charger us and jp standard',
                       'one plus 76128gbchargerboxclean conditionprice 23000 sterling apartment st inez rd santa inez panaji goa 403001 call us on 7420809918 ',
                       "lenovo thinkpad l13 processeur intel core i510310u 6 mo de cache jusqu' 440 ghz 8go 256ssd 13prix : 120000da gcb informatique bab ezzouar alger contact: 0541865910 0558862471 023831165 google maps : gcb informatique nous sommes a votre serviceouverte toute la semaine du 8h00 a 18h00 sauf le vendredi.merci de nous appelez pendant les heures de travail",
                       'macbook pro spacegrey..',
                       "finally i decided to do iti rarely do giveaways but when i do its something big and useful.today i am giving away the the most wanted laptop on the market.this beast cost me 2399 usd arrived yesterday and it's still in the box.meet the brand new apple macbook pro 16 with retina display: apple m1 pro tencore cpu 16gb ram 512gb ssd up to 21 hours battery life sixspeaker subwoofer systemto win this beautiful space gray mac: you must be my follower like this post mention a friend in comments; if you win the macbook i will send your friend a sticker pack.next week i will choose a random winner and ship itto you free of charge.good luck and happy new year! ",
                       ' xs ', '!! : :',
                       'feeling a bit better & thankful for more energy some sunlight and a little more brainpower to code! ',
                       "i love my workplace having lots and lots of light! it's super essential for me to give my 100!",
                       'getting some sunlight on to you helps so much', 'is it a python?',
                       "i can't wait to code on macbook", 'home office', 'beaut', 'just perfect', 'gorgeous',
                       "3 ! i'm in an airport right now but i'm not the one to give advice on traveling and flights because i usually fly like once a year.you can check 's account for good tips on traveling.3.1 ' like never! if you need a functionality in multiple places always extract that into a different component.your future self and colleagues will thank you!2 the longer they are the hard it is for anyone to understand the code even your future self.if a class grows too much it means that you have too many things in one place and you need to separate them.3 ktlint for android and swiftlint for ios they do a great job showing you warnings if you don't respect good coding practices and you can also customize the rules.there are a lot more good coding tips out there but i'll keep it short here.focus on these 3 and your programming game will improve.4 ? ",
                       "very nice i didn't know about the lint tool at all that sounds so useful indeed!",
                       'true especially copy and paste it is quite common and a false approach for coding...have a safe and happy trip',
                       'amazing tips thanks for sharing',
                       'i would recommend 4th step as keeping good folder structure for maintainability and easy access of files and components',
                       'flutter',
                       "great tips especially the first one i would add 4th follow the best practices and code rules anyway even if you have to hack pentagon in 10 minutes and gun is put up to your head.don't believe you will have the time to refactor your code later.",
                       'good naming! create understandable and practical names for classes and variables',
                       'hey man what ide do you use?',
                       'about using short methods what would you say is the bar for a long method?',
                       "sir kindly check my instagram account you will find lot's of useful programming related information...",
                       'thank you so much! have a good flight! and cannot wait for your stories from your next destination!!',
                       'time to get back to work.happy new year friends!', 'wow this is so clean',
                       'epic setup man! happy new year', 'happy new year bro! great space!', 'the setup king is back',
                       'well this looks', 'awesome setup!! looks great!', 'happy new year!',
                       'such a cool angle for a picture!', 'what monitor is this?',
                       'happy new year greek greek computer screen computer sales i have some other computers',
                       'good great', 'awesome workspace', 'which macbook do you own? ', 'unfortunately i dont own one',
                       'the mbp 13 m1 had to upgrade last summer because my maxed out 15 mbp from 2018 went swimming',
                       '14 base line', 'macbook air m1 8 core cpu and gpu but the small one', 'macbook pro m1 13',
                       'none', 'm1 pro 14 inch macbook pro silver', 'macbook air 13 2019 :', 'macbook air m1',
                       '13 macbook pro 1tb ssd 2021', '2019 pro 16 with touch bar', 'macbook pro 16 2019',
                       '2020 m1 macbook air', 'mbp 16 w touch bar', 'macbook pro', 'a warrior macbook pro mid 2012',
                       'macbook pro m1 13 inch', 'the new 14 macbook pro m1 pro base model', '2015 macbook pro.....',
                       'm1 macbook pro 13 andddd love it', 'i have the macbook none 0 :', 'macbook air m1 2020',
                       'm1 macbook pro',
                       'what do you want to know about the new macbook pro? leave your questions in the comments below and ill answer as many as i can in my review! ',
                       "hey dan! do you find the new m1 max macbook pro as a great option for a sturdy home studio setup in case i'm using it for about 12 hours a day! cos i ve always had one sturdy desktop setup and a laptop.always ended up having heating issues after over using my laptop.thanks!",
                       'can it be downgraded to big sur for now? or is it monterrey only? if its the latter how are 3rd party plugins working on the new os?',
                       'probably a dumb question but would you have any issue switching back and forth with a project on two machines that have different os? thinking about my main rig on mojave and about to get one of these beasts real as a remotebackup setup.',
                       'do you feel the price is justified? im assuming youve gone for quite a specd up model',
                       'what is the minimum cpu you recommend to run big orchestral projects with spitfire plugins?',
                       'for music production including the use of many tracks with sample libraries how much cpu gpu and ram is necessary? are there any upgrades we can skip and still get excellent results? im going to end up buying one but not sure how much to spend on all the upgrades.',
                       'im using one now and ive definitely noticed some issues with programs lots of hanging notes but still seems quite powerful.do you think it will get even better as programs and macos updates? ive also seen lots of incomprehensible stress tests so id be interested to see how it handles some of them our bigger projects and how it compares to the spitfire audio setups in real life! excited to hear your thoughts :',
                       'how is the 14 screen size for big projects?',
                       'how does it handle big orchestral and sample heavy templates projects?',
                       'any issues with running logic in rosetta some of my plugins are still not natively supported',
                       'do you think the soc architecture with m1 max will make audio interface dsp uapro tools ultetc redundant?',
                       "i never use mac before so i'm a bit confused.why do composers tend to work with mac if their working on a laptop? because it's a bit pricy than windows laptops isn't it?",
                       'hi dan did you find some compatible problems using certain pluginsvsts with the new mac?',
                       'is possible to 64 gb ram in macboob m1 new.which time available in the market easily.',
                       'whats the ram pressure like and how much swap memory is being used?',
                       'i have problems playing audio from my prem1 logic projects.has anyone the same issues? hickups glitches overloads etc and you dan?',
                       'id be interested to know what spec your memory is and if you have any recommendations in that regard for anyone who is thinking of getting one as their main hardware.',
                       'how many tracks are loaded possibly without system overload? and how the pan sound goes! thanks : congrats on your new laptop!',
                       'im waiting for the new imac pro but would love to know how much ram you have there and how its performing.do you think youll ever need more or is it just enough? rosetta running apps aside',
                       'hey dan i ordered exactly the same thing.m1 max 64 gigabytes ram.however my macbook is not coming until earlymidfebruary.how satisfied are you with the performance and workflow? greetings from germany hauke',
                       'what about the size of the screen? do you think you could work on a big protect on the go on the 14 inch one??',
                       '1.how does it perform while you are running heavy orchestral projects? need to freeze tracks? still enough headroom in cpu an ram? would be great to here about your experience in your day work.some stress test on youtube are really dumb.2.i think you said yours comes with 1 tb ssd.is it enough for your basic software? are you still using the blackmagic dock? thinking of going to take 2 tb',
                       'im going to order the macbook pro m1 max 16 inch with 32gb of memoryram.im upgrading from a macbook air bc of struggling with spitfire audio plugins bbc pro albion one aperture stack constantly overloading.do you think the new macbook will be able to handle all these spitfire plugins? thank you!',
                       " ' ' ", 'damn love this!! the reflection of the macbook display looks absolutely gorgeous',
                       'beautiful shots', 'che spettacolo!', 'love this shot buddy', 'bellissimi scatti',
                       'perfect photo shot man top', 'lovely shots', 'love this shot!', 'dope shots bro!',
                       'ma quel riflesso ?!?', 'wow bro this shot is professional absolutely beautiful',
                       'incredible shots bro', 'beautiful bro', 'beautiful shots bro',
                       'che idea spettacolare! belli questo scatti francesco!',
                       'amazing shots man! beautiful reflections!', 'belli scatti', 'fantastici riflessi francesco',
                       'clean shot', 'these shots are so crispy', 'ottima foto', 'che colori', 'hai ragione',
                       'i switched to html css and js for my personal page why did i switch? i switched because its easier to create small websites which are responsive with html and css.at least for me.but for bigger projects i would definitely choose flutter web.do you have your own website? ',
                       'woah awesome shot and angle',
                       'exactly totally agree with you.working with html css and javascript is fun.',
                       'yeah.simple one portfolio page html css and js',
                       'yuppp....i do.with htmlcss and js.but i dont use flutter though.i use java',
                       'what a wonderful posthappy holidays',
                       'hey would you please tell me what is the model and brand of your mousepad?',
                       'all the best bro for your new website! i started my tech journey today do follow my page would mean a world to me!',
                       'exactly it easy we use it most for html css javascript and react for web app',
                       "nope i don't have", 'yes! mine is built in flask :you can check it here rubenoliveira.tech',
                       'how about laravel?',
                       'website is already become my life.always visit it for knowing information entertainment download and much more',
                       'nice shot! check out these useful apps on the mac app store: skitch zuriweb magnet',
                       'yes mine is made of html css and js', 'n...',
                       'what would be considered a bigger project? im new to development and trying to immerse myself and learn as much as possible'],
        'appleiphone': ['iphone xr128gb parcelamos em at 10x sem juros! para mais informaes acesse o link da bio! ',
                        'iphone 12 pro 128gb pacific blue fully unlocked renewed',
                        'cases para iphone qualquer modelo no valor de 3500 entrega totalmente grtis o',
                        'hello iphone 13 pro max ',
                        "always take time to do what you love taking pictures dancing painting acting etc.once a week? twice a month? doesnt matter.as long as you do not forget about doing it.from and don't be sad if your day job is different your passion.the work that feeds your body doesnt have to be the same from the one that feeds your soul.just keep on creating.your personal projects are the core of your works.even if you're the only one who are able to see them even if no one likes them.you can never tell when will your audience come 10 years 20 years or tomorrow or never.you'll never know but one thing you can be proud of is that creating.you never stopped! ",
                        ' iphone xr 999 3 android ',
                        'grseldeki modellere ait batarya deitirme kampanyas 12.01.2022 ile 15.01.2022 tarihleri arasnda geerlidirhizmet iletiim apple yetkili servis salaycs herhangi bir n bildirimde bulunmakszn kampanya koullarn ve artlarn tek tarafl deitirme hakkna sahiptir.',
                        'promocos da semana vendas por direct ou whatsapp entregas via sedex somos certificados e registrados temos diversas recomendaes produtos originais e lacrados com nota fiscal e garantia homologados pela anatel nas compras acima de 200000 o segundo eletrnico sai com 50 de desconto.iphone 7 32gb 90000 iphone 7 128gb 100000 iphone 7 plus 32gb 130000 iphone 7 plus 128gb 139900.iphone 8 64gb 147500 iphone 8 128gb 155000.iphone 8 plus 64gb 170000 iphone 8 plus 256gb 180000.iphone x 64gb 185000 iphone x 128gb 195000.iphone xr 64gb 200000 iphone xr 128gb 210000.iphone xs max 64gb 240000 iphone xs max 256gb 250000.iphone 11 64gb 265000 iphone 11 128gb 280000.iphone 11 pro 64gb 290000 iphone 11 pro 256gb 305000.iphone 11 promax 64gb 315000 iphone 11 promax 256gb 330000.iphone 12 64gb 380000 iphone 12 128gb 400000 iphone 12 256gb 435000.iphone 12 pro 128gb 460000 iphone 12 pro 256gb 480000 iphone 12 pro 512gb 510000.iphone 12 pro max 128gb 590000 iphone 12 pro max 256gb 640000 iphone 12 pro max 512gb 670000.o ',
                        '1..23 mientras ms mejor..', 'follow ?',
                        "the tussle between the apple keychain and 1password is finally over.we have ended it once and for all.if you're into the apple ecosystem then the best option is the apple keychain.why go for something else? if you're not then 1password is definitely for you.however in terms of security apple keychain wins with a landslide fair and square.there are no two ways about it.apple personally takes care of your privacy and the whole world is aware of apple's protectiveness towards its users' data privacy.cutting to the chase our post will help you understand the difference between the two password managers in the simplest of ways.don't forget to turn on post notification.stay tuned with about everything apple.......hashtags ",
                        " & ' ", 'done', 'its a fake giveaway', 'win win win win win', 'nice', 'quiero el phone xs',
                        '1...2.3.4.....y', 'oh money', 'done done done done done done done', 'no.3',
                        'babies dm to get spoil massively with money and iphones',
                        'giveaway new offer here 3 we are giving away brand new iphone 12 pro growing our apple network!! ',
                        'i want can uh give me?',
                        'apple is working on big upgrades for the iphone 14 pro and iphone 14 pro max.these are some of the features that have been rumored up until now.are you excited? render from ',
                        'well i am due for an upgrade',
                        'every year its hyped up but turns out to have little or no upgrades lmfao',
                        'i feel like this spec sheet has been used for the past 4 iphone releases',
                        'we need touch id and periscope optical zoom 2050x', 'please no esim',
                        'now i regret getting the 13 pro max', 'still no touchid tho', 'car wash detection????',
                        'bruh there are countries that arent e sim compatible', 'what about the baseline 14?',
                        'i doubt it will have 8k maybe 5k on the 15 tho.', '120hz?', 'car crash detection?',
                        'where are they getting titanium from? lmao', 'take my money!!!',
                        'im ready to upgrade for this! im current iphone 12 pro max', 'i want it 14 pro max',
                        'satellite connectivity awesome.so i can go on a road trip without drama',
                        'what are the chances theyll call it phone 15 since itll be a 15 year anniversary',
                        'car crash detection? i feel like thats purely software jo?',
                        'man cant they at least increase the lens to 4? its a a pro model after all',
                        '1 hour of 8k video will need 7.25tb storage',
                        'if its esim only how would it work if you wanted to switch carriers?',
                        'so same thing as iphone 13121110x87 n 6',
                        'ive been out of it high on meds the past 23 weeks with a bad back so this is a shot from the other week i got on my desk with the chair as foreground.kind of liked how it turned out.how are your weeks all looking? happy hump day follow for more ',
                        'bro this lighting tho', 'nice shot bro.hope you feels better', 'get well bro',
                        'great shot bro!', 'get better soon brother', 'high on meds?! hope youre okay phil!!',
                        'you kind of liked it??? this is flawless my guy amazing shot.rest up bro feel better',
                        'love it mate', 'super clean shot as always bro',
                        'clean shot bro.seems busy this week.rest up and hope to see you at it soon',
                        'amazing shot phil! i hope you feel better soon!',
                        'i really like the result of this shot too bro get well soon i hope youre good feel better',
                        'great photo.i love it reflection camera lens', 'sharp',
                        'oh shit dude what happened? hope you get well soon bro anyways the shot is epic',
                        'ah man hope your back feels better soon bro! this shot is awesome! ive used my chair in the foreground before too definitely helps!',
                        'awesome click', 'rest up king!', 'awesome shot',
                        'hope that everything is well phil! have a wonderful wednesday',
                        'it looks great dude! my week is all about painting the', 'love this shot',
                        "sooo clean man! saving this for inspo my back is ok but i've been out for a few days now with quite heavy flu! wish you a speedy recovery",
                        'thats gorgeous dude', ' 09376625452 ', '..how to participate?1.2 34 5.',
                        'lindo iphone digno de tenerlo', 'belliii', 'done please help me',
                        'actual home screen configwallpaper: widget: blank widget: mdblank app......| | | tags ',
                        'clean home screen bro', 'super clean minimal setup brother', 'great', 'dope clean shot nico!',
                        'beautiful', 'love this bro', 'super clean', 'minimalism wins again', 'clean!',
                        'nice homescreen buddy', 'very cool bro', 'so clean shot bro and widget ist so cool', 'shot',
                        'smart',
                        'looks great brother! love the icons aligned at the bottom rather than the top! i do the one page setup too',
                        'super minimal love it', 'very minimal homescreen bro',
                        'oh man! i love how minimal this looks! might have to change mine up now!',
                        'clean neat brilliant shot! rocking that wallpaper', 'fantastic shot',
                        'i love the minimal approach to your homescreen bro', 'this is sweet.is there a clear widget?',
                        'so great!'], 'Mac': [' 833 02m403 04',
                                              '60mac ruddy eye shadow 1.3g 900 v 350 ems 50 line https:lin.eeeisg4llline id: inbox http:m.mehead2toebeautystorefb: head2toebeautystore ig: head2toebeautystore line http:line.metigiaw9a5fju ',
                                              'are you ready to get started.tbush ca',
                                              'amed sportif faaliyetler mainin hikayesi nhikayesi ',
                                              'vamos conversar sobre colo e pescoo? vira e mexe algum paciente meu chega aqui na clnica se queixando da aparncia do colo e pescoo.a verdade que essa rea costuma ser super negligenciada pelos cuidados do skincare e acaba denunciando o envelhecimento lembra que eu sempre falo pra lembrar do colo na hora de passar o protetor e os creminhos do dia a dia? felizmente aqui na clnica temos vrios tratamentos para deixar o seu pescoo lindo e jovem: para tratar manchas e textura um protocolo personalizado da mac para voc! para melhorar a flacidez a melhor pedida a associao do ultraformer com os bioestimuladores de colgeno! para previnir as linhas e rugas do pescoo o botox pode ser uma tima opo!e a vamos olhar com mais carinho para algumas reas? ',
                                              'love me with conhea e se apaixone pelas 20 cores luxuosas do love meliquid lipcolour! tenha uma cobertura completa em apenas uma aplicao com 12h de hidratao sem desbotar descamar ou escorrer!! um batom lquido hidratante e nutritivo com um acabamento acetinado leve e exuberante.apresenta uma frmula confortvel e nutritivainfundida com nosso exclusivo complexo tlc lip que condiciona e ajuda a hidratar os lbios com uma poderosa mistura de leo de argan leo de coco manteiga de karit manteiga de carnaba extrato de cevada e extrato de pepino! ',
                                              'quintafeira!.meninas olha esse glitter que chegou em nossa loja da.lembrando que vocs encontram em nossa loja por apenas r1000.trabalhamos com atacado e varejo e levamos para qualquer lugar do brasil!.',
                                              'send me pic.unity',
                                              'great food great atmosphere & even better company.the way a date night should be done...mann &cheese ',
                                              '20212021mac 170 :6600fiveism 07 :572010g spf19pamac spf15 nc37:495032g rms beauty 22:52805mlup 2021',
                                              'macnarsyoutube ',
                                              'beautiful bengoli bride bridal booking open for 2022call on 7750072656..note we completely customise bridal look.according to the bride wish...mua:.makeoverstyling:.makeovermodel:..',
                                              'top drawers tuesday.', 'goals!!!', 'aqtuuuuuudo',
                                              'bride lookhairby makeupby ask for bridal package summer 2022for more details call us or whatsapp01285562665 ',
                                              '112facebook ', ' products', '!!!!!!!!!!',
                                              'singular and divine the design the face is perfect with the horizontal line.its color its morphology are thought in detail its proportion is not accidental great to achieve beauty with design beautiful',
                                              "i used to do this on flickr but times have changed.here's my primary workstation in 2022.i do about 90 of my work here and split the remaining 10 between that desk in the background and my workshop electronics workstation.pretty happy with layout but wanting to build out an office with 2x the footprint so i can split studio area from work area.and have real lighting.",
                                              'which desk is that?', 'its the diet dr.pepper for me.',
                                              'i love your lab',
                                              'the project of doubling up the office into a studio would make for some good content!',
                                              'very nice', 'very nice space', 'such an awesome primary workstation!',
                                              'where the magic happens', 'sweet and a lot cleaner than mine!', '111 ',
                                              'promote it on..world', 'send on',
                                              'ruby taboo gloss fighi ne abbiamo?finalmente riesco a farvi vedere il lip swatch del lipglass ruby taboo della collezione hypnotizing holiday di che mi ha regalato la mia amica il colore un rosa aranciato con allinterno una moltitudine di glitter rosa arancio e rossi troppo difficile come al solito descriverlo e che purtroppo in foto non rende minimamente la sua bellezza.nel post precedente sembrava molto pi rosato questo perch dipende tantissimo dalla luce che lo colpisce nello swatch come appare alla luce naturale del sole; ha una quantit di glitter pazzesca con una passata il risultato un po pi blando mentre nello swatch stratificato due volte e il risultato davvero magnifico!questi gloss sono molto confortevoli non appicciano e lasciano le labbra molto morbide ed idratate.e voi siete gloss addict? ',
                                              'bellissimo anche questo gloss! mi piacciono moltissimo i gloss e adoro usarli sia con una matita sia sopra un rossetto! rendono il tutto ancora pi elegante',
                                              'ma che meraviglia e poi quanto mi manca indossare i gloss',
                                              'oddio ma bellissimo', 'spettacolare!!!', 'o.mio.dio.',
                                              'molto molto bello e particolare in effetti proprio un rosa aranciato!',
                                              'bellissimo ho riscoperto i gloss proprio negli ultimi mesi',
                                              'da questa foto assomiglia molto a toxic love di nabla',
                                              'ma che spettacolo', 'anche indossato non delude magico',
                                              "ma meraviglioso l'effetto che ha sulle labbra",
                                              'sono tornati gli eles swatches evvaiiiiii', ' eyes : !!.cheek : lip : ',
                                              'motd 1 ', ' 22 ', '.....? ', ' motd', ' !!!! ', 'so beautiful!'],
        'AirPods': ['welcoum ',
                    'airpod 2 hang sn nhiu hoan thin tt price ch 3xxh tr giao ha tc hcm hn trong 2hhoan thin ngoai hinh trong lc lc nam chm giong hang real 100cam bin nhanh nhay chc nng giong 100 hang chinh hang: tuy chinh thao tac cham hai bn tai tc nhac chuyn bai...bt nm t ng kt ni ti u hoa rt tt vi iospin: siu tr u nghe t 45h.nghe song song vi dock thi ln ti 2 ngayfull box nguyn seal.khi mua hang:i tra khi li thang ubao hanh 12 thang chinh hangkim hang thich mi nhnc h tr phi ship va mua 2 san phm min phi shipmun chuyn aripod h chi minh cam kt bao gia thi trng: 0899899873: qun 2hcm: khm thin hn.........',
                    'metalic case 5 12 pro 249 direct ', 'airpods',
                    'uk used iphone 12 pro max !!!256gb n575000128gb n550000available in bulk and pieces available in store for pick up shop 7 cac faith home shopping complex federal polytechnic area ede osun state we also do nationwide delivery for customers not close to our location!call whatsapp:tunde: 08032797879yusuff: 08108302552tayo: 09034668303 ',
                    'sper combo papaaaaa !!!! ipad pro 128gb 13 pulgadas iphone 11 pro max 64gb o 256gb.airpods pro apple whatch serie 7.apple pensil ',
                    ' littlechastore | line : 11',
                    'o airpods 2 s tirar do estojo e eles j esto conectados com todos os seus aparelhos.prontos para envolver voc em um mundo de som de alta qualidade.pea j o seu via direct.enviamos para todo brasil.',
                    'tu nuevo dispositivo apple est aqu!te ofrecemos equipos nuevos y usados con garanta en olavarratomamos tu usado al mejor precioa partir de iphone 8 fede marcos appleproductos y serviciowhatssapp al 549 2284 33 36 46 a ',
                    ' 128gpart number: llabattery health: 100 ',
                    'pongal mega sale!!!buy smartphones at a great deal with free gifts.', 'no.3 ',
                    'hiva jewelryairpods holder.jewelry.jewelry 925 ', ' www.persianapple.ir ', ' new ', '.amir',
                    'citizen promaster ny014110le ', 'looks so great!!',
                    'whoa! the new citizen ny automatic series with bigger case size to 44mm! i wondering whether to buy one or not whats your opinion about it? feels good? is worth enough to replace older ny0040? thanks',
                    'precio', 'lindo', 'lovely promaster',
                    '2022 louis vuitton 79200guccigg 41800 appleairpods pro30580airpodsappleairpods probottega venetaairpods pro 18700 prada 135300pradatenerita2 2640029900calvin klein 3 211000auraleegiza high gauge sox411000jdtdcusb 512gb 12999iphonelighting usbtypeaciphoneicloud ',
                    'collab dm us evancejewels',
                    ' apple airpods pro 1...2022.1.42022.2.282022.3.2dm instagram facebook instagram ', 'airpods1.4',
                    'appleairpodspro',
                    '.xiaomi mi true wireless earphones 2 basic 55 azntiktok sehifemizde maraqli video kililri izleye bilrsiniz.nvan : xiaomiazerbaycannvan :1.nizami metrosunun xnizami mall 3cu mrtbxiaomiazerbaycan maazaslaq : 0516666768i saat: 10:00 21:002.20 yanvar metrosunun xamaxinka xmi bir telecom maazaslaq : 0993666768i saat: 09:00 21:00qulaqcq xsusiyytlriqulaqlq tipi\t: kulak iiistifad sahsi : musiqi telefonuyunluq : android iossesli asistan desteyi : varsesli asistan xsusiyyti : google asistan siri asistanses k : stereogrlt engelleme : yoxempedans : 32 ohmsrc ap : 14.2 mmbalant tipi : tam kablosuzbluetooth standard : 5.0bluetooth xsusiyytlriaacsbcistifad mesafesi\t: 10 mistifad mddti genel : 5 saatistifad mddti arj qutusu il : 20 saatarj tipi\tarj kutusuarj yma mddeti : 90 dqiqmikrofon : vargrlt engelleyici mikrofon : 2 mikrofonluuzaqdan idaretm : varzng idaretm musiqi idaretmreng : aarlq : 9.4 garlq arj kutusu : 48 g ',
                    'yalniz xanimlardan ibart komandaya aktiv xanimlar dvt olunur.minlikl dey bilrm ki bu i tklifi sizin hyatnz dyick.nki siz el bel sad bir i tklif etmirm.mn siz srmay yatrmadan biznes qurma tklif edirm.stlik i saatlarn i raitini v htta ilycyiniz xslri znz seirsiniz.i tamimil pulsuz online yrdiliretrafli melumat ucun directe yazin',
                    'nddnnr', 'mdnrbf', 'xksbd', 'zksbs', 'zkshbd', 'xkdnnr', 'dkdnr', 'dmdbxixnd', 'jdnakv', 'djdbe',
                    'sksbrnr', 'smsbd', 'skwbbd', 'dmsbd', 'smshsbd', 'akshbs', 'zjsbba', 'sksbakx', 'dken r', 'ndjdd',
                    'zmznjs', 'dkdne', 'jsvsjshd'],
        'iPad': [' pastel', ' anker !!1690ipadipadipad', 'promote it on', ' pc ! ', 'dm it on.art.gallery',
                 '.! !.!ogq http:naver.mefhyd64x1.',
                 "today what's your favorite part of this setuprate it 1 10 : follow for more ", 'nice shot', ' a pat ',
                 'nion ',
                 'sper combo papaaaaa !!!! ipad pro 128gb 13 pulgadas iphone 11 pro max 64gb o 256gb.airpods pro apple whatch serie 7.apple pensil ',
                 ' littlechastore | line : 11',
                 'o airpods 2 s tirar do estojo e eles j esto conectados com todos os seus aparelhos.prontos para envolver voc em um mundo de som de alta qualidade.pea j o seu via direct.enviamos para todo brasil.',
                 'warmed up by inking a babu frik sketch that was used as the the basis for a recent sketch card commission.i liked how the initial sketch turned out so i thought id finish it and see what happens.gotta love babu! drawn in.',
                 'dm us', 'dm it.arts 3m', 'love it dm.ction', 'hey hey!', 'this looks so cool!! i love it',
                 'may your life get as bright as the fire of lohri and may you prosper and grow with each passing day.let the glory of lohri fill your life with warmth and happiness.sending lots of love on this wonderful day of lohri.for details visit: https:getinstacash.indownload the app to sell your apple iphone.https:play.google.comstoreappsdetails...',
                 'school things with & !...: ', 'you have such a neat handwriting',
                 'this is inspiring.ive totally been thinking of uploading some ppco to goodnotes and using that.this looks great!',
                 'love the minimalism!!', 'app name???', 'cest pas faux a caille en ce moment ! ', 'trop fort !!!',
                 'ahahahhaha',
                 "new week new goals what are your goals this week?i have an intense week ahead of me with many important appointments and deadlines.a part of it was already due today so i got that out of the way already.tomorrow i have my first negotiation coming up which i'll be leading on my own.i'm nervous of course but the closer it gets the more i get the feeling that i'll be able to handle it just fine.keep your fingers crossed for me.my goals this week: survive do a good job on 2 negotiations & continue to work on my projects at work drink 2 liters of water every day give myself a moment of me time without screens every day incorporate 30 minutes of exercise every daywhat are your goals this week? ",
                 'mein ziel ist es endlich wieder vllig ins lernen hineinzukommen nach den ferien ich wnsche dir auf jeden fall alles gute fr diese woche du schaffst das!',
                 "good luck on everything! you'll do great!",
                 'ahh good luck tomorrow! my goal for this week is to get up and move my body more!',
                 'i tested positive for covid last night so rest is my goal.good luck on your negotiations.',
                 'ich drcke dir definitiv die daumen: aber das machst du definitiv 1aich habe nicht wirklich ein goal auer on top of my schedule zu sein',
                 'this picture is pure aesthetic', 'my goal is to survive best of luck you got this',
                 'i was referred to this platform by a friend online.l thought it was a scam company...but i was moved to try and here i earned over 4btc within 5 working days',
                 '..........', '???!'], 'appletv': [
            "o filme de 1973 mas ele acertou e muito de como seria o mundo em 2022: 'no mundo de 2020' o ano 2022.nosso planeta superpovoado est passando por mudanas climticas catastrficas.as megacorporaes tm poder excessivo sobre os governos.a vida boa um luxo que apenas o 1 mais rico consegue comprar.quais so as previses e o cenrio do filme?1comida sinttica2superpopulaao3mudancas climticas4morte assistida5tempo em telafica a dica de filme para o final de semana romntico com sua esposa ou namorada!",
            '.www.persianapple.ir ',
            'dont want to share your privacy with anyone? get private access to the internet with nordvpn.get 68 more reduction in your packages at getsavo uk.visit: https:getsavo.comuknordvpn ',
            'pocztek roku wi zaczynamy ciekawostk : wystpuje w teaserze serialu severance wyprodukowanego dla apple tv :.nie jest to raczej wsppraca oficjalna bo jak wida na zaczonym zrzucie z serwisu youtube maszyny nie maj logotypw jednak seria f123 jest na tyle charakterystyczna e trudno j pomyli z czym innym :.dla ciekawych film nazywa si severance official teaser | apple tv a maszyny od stratasys wida w 51 sekundzie niestety pojawiaj si na bardzo bardzo krtko.',
            'koncept: iphone 13 pro max black & gold www.svetapple.skzdroj: ',
            'no homekit news from ces2022 today! this gave me the opportunity to play around with some zwave stuff and prepare new content.last thing for today: watching boba fett episode 2.i wish you all a nice evening! by ',
            'nice shot', 'thanks!', 'bonne nuit..',
            'segundo os rumores este servio de subscrio de audiolivros poder chegar no final do ano...',
            'sem canais e filmes xxx adultos temos para toda famlia 80 000 contedoscanais de televiso 162 pasesfilmes 18 idiomassries 16 idiomasdiversas produtoras incluindo a netflix liberado para promoes3 meses 10 mil6 meses 18 mil12 meses 32 milpea um teste grtis sem compromisso na nossas pginas ou no whatsapp https:wa.memessage5b7ljstr2mzbl1..oiptv adevida ',
            'dickinson 2019season 1producer: robbie macdonaldyoung emily dickinson living in the 1850s faces the oppression of a society built for white men that doesnt stop her from breaking the rules and writing her poems.rotten tomatoes gives it 92 45 rated by uswhere to watch: apple tv apple tv ',
            'this is a cute comedydrama with a bold modern teen twist that hooks you from the beginning.laced with poetry and fantastic frames every episode provides laughs shock and an aching heart.the acting excluding hailee steinfeld is what one could expect from a cable sitcoms so not fantastic but good enough.this is quite far from the actual historical events of emily dickinsons life but is close enough to it that its fresh yet not jarring.however the plot seems to be following the historical events rather than character development and arc which makes the pacing feel a bit off and the season felt very incomplete.looking forward to watching the second and third season! c',
            's2&3 are even better! the costumes & set design is',
            'dica de filme queime depois de ler 2008..j assistiu?conta pra gente o que achou aqui nos comentrios...ries ',
            ' the offer 28.the godfather 10.', 'promote it on.of.marvel',
            'en el ltimo captulo del podcast la recomend una serie que le dio toda la vida que necesitaba para cerrar el ao: ted lasso a pesar de que al principio se cuestion un poco qu tanto le iba a interesar una serie sobre un entrenador de texas que se va a uk a hacerse cargo de un equipo de ftbol despus de un par de captulos todo tuvo sentido.mega ultra recomendada si quieren volver a creer en la humanidad ya la vieron ?..',
            'la vimos y la amamos', 'la amo y me hizo inmensamente feliz', 'muuuuy buena', 'amo ted lasso',
            'vista y re vista! me toc la fibra! qu onda?!qu parta luego la nueva temporada! lov u jajajaja',
            'siii me encanta! believe', 'mansa serie corazoncito de oro award',
            'me carga esta serieeeeeeeeee por q destruyo todo lo rudo que existe en mi! llor me emocion me quise ir a uk de todoooo! ahora veo y ustedes tb deberan ver queer eyes en nefli !!!!',
            'no s si vieron l 2nda temporada ya pero en varios captulos termin llorando tipo 2 am.no por triste solo emocionante.',
            'me la llor toda', 'es muuuuy buena esta serie',
            'dickinson comme vous le savez je poursuis ma dcouverte de sries sur apple tv et javais envie de vous parler aujourdhui de celle qui ma accompagne ces dernires semaines et dont je viens de dmarrer la saison trois : dickinson cette srie rend un hommage moderne la potesse amricaine emily dickinson que je connaissais que de nom javoue ainsi qu son uvre on la dcouvre en ado rebelle fministe cachant sa liaison avec sa bellesoeur et incomprise par sa famille qui la prend pour une demie folle et veut faire delle une parfaite petite mnagre alors quelle rve de smanciper et vivre de sa plume on dcouvre aussi ses angoisses par rapport des problmatiques de socit la srie se droulant peu avant la guerre de scession le passage lge adulte ses visions car emily a des facults que tout le monde na pas et son imagination dbordante au fil de ses pomes inspirs par des vnements du quotidien les dcors et costumes sont superbes jai un norme crush sur les tapisseries de la maison dickinson et la bandeson moderne offre un dcalage plaisant entre lpoque et la modernit quemily avait dj en elle.et que dire du casting ? si jai ador hailee steinfeld ses parents et frres et surs ne sont pas en reste.chacun a son petit caractre et javoue quils me font beaucoup rire.jai souvenir dun repas de famille mmorable avec une certaine louisa may alcott qui tait invite vous avez dj vu cette srie ? ',
            "je n'ai encore jamais regard", "non je ne l'ai pas vu mais je n'ai pas apple tv",
            'arrrrghhhh jai pas apple tv',
            "merci du partage ! je n'en avais pas du tout entendu parler et cette srie me tente beaucoup",
            'je ne connais pas du tout mais a me tente bien.',
            "jamais vu encore ! pourtant j'ai une apple tv alors pourquoi pas",
            'jai vu la premire saison que jai ador.certains la dcrit pour son ct loufoque mais pour moi cest ce quil fait tout le charme.depuis jai achet un petit recueil de posie.a reste trs obscure',
            'im as good as the best you', 'them to this song means literally everything to me', 'roy with kids',
            'phoebe is the best!! fearless little queen roy loves her!', 'my heart',
            'didnt think i could love roy kent anymore.then this', 'i sar rit already', 'here from bretts story',
            'such a great relationship between the two characters.so well written.', '.....cr thank you',
            'encantador lindo perfeito demais sonho das meninas bjs brasil', 'esplndido', 'speechless his cute face',
            'dream', 'beautiful', 'because.her hair is so rebellious haha',
            'happy saturday ig fam ! how are you relaxing this weekend?',
            'relaxing today for me : happy saturday renz!', 'happy saturday renz',
            'nice shot! catching up on some witcher s2 have a great weekend!', 'working on new posts bro',
            'i love these types of shots i never could do these but maybe in the new apartment! chill out weekend moving next week so need all the energy next week',
            'happy first weekend of the 2022 bro i am feeling good', 'incredible shot bro super clean',
            'oh man! netflix and chill bruh preparing myself for that stranger things season 4 launch sometime this year',
            'kickin my damn feet up and doin exactly what you got pictured here! its a mega chill day bro.happy saturday',
            'relaxing weekend as well..some shooting and family chill',
            'happy saturday bro! playing some ps5 of course! still havent upgraded my apple tv to this version love this shot!',
            'wow i love this close up', 'netflix all day long!', 'soccer and netflix all weekend',
            'happy saturday renz! cleaned up my closet today', 'tv sounds really good right about now!',
            'love this shot ! happy saturday', 'amazing shot renz have a nice day!', 'nice shot !', 'love it',
            'promote it on',
            'banner del da 291221sumate somos el grupo minoz sabor latino de votacin minoz flavor latino does not buy hearts...minoz sabor latino no compra corazones...siempre contigo lee min ho por que queremos verte siempre en la cima vota en kingchoice https:kingchoice.methe100mosthandsomemenintheworld2021seguimos con choaedol minoz figthing sigue el canal oficial de lee min ho en youtube https:youtube.comcleeminhofilm : globalminoz hansu ',
            'como j queria assistir', 'colombia', 'waawwww', 'congratulations', 'hoy???',
            'gracias por compartir marcela tkm', 'bello',
            'you tuve estoy seguiendo lee mi ho oficial vamos minoz power ms apoyo gracias por compartir marcela',
            's u n d a y i n g binge watching my favourite show witcher.im on season 2.what are you all watching?',
            'incredible layout! have a good sunday', 'great photoshoot!', 'clean af',
            'is the witcher good? havent started it yet', 'have a great one brother !', 'stunning shots bro',
            'incredible shot man!', 'these shots tj', 'awesome picture!',
            'amazing shots bro my wife got me watching witcher too!!! hahah good show though',
            'i havent found any shows to watch for a few months so ive just been watching youtube haha gotta watch the witcher though i hear so many good things! love these photos tj',
            'harry potter', 'hi pinkushgreat work.i would love to connect with you to seek some advice',
            'this apple looks so cool', 'apara',
            'titans the witcher finished the wheel of time finished the book of boba fett.', 'perfect at glance!',
            'i love this scene', 'airpods max instead of sonys headphone',
            'dulces sueos queridas minoz reposted from seguinos follow us : facebook tik tok instagram twitter :.spain.colombia hansu.globalminoz ',
            'guapo lindo bello bonito', 'marededusenyor', 'beautifulll much cute charming', 'hermoso mi lmh con amor',
            'lovely'], 'airtag': ['macbookapple',
                                  "thieves use screwdrivers to gain access to automobiles through the driver's or passenger's doors while avoiding setting off alarms.when target automobiles are parked in public places thieves plant airtags in outofsight regions.the targeted vehicles are then tracked to the victim's home where they are taken from the driveway according to 9to5mac.according to a statement released last week by the york regional police department in canada officers have investigated five occurrences using airtags being used to steal premium automobiles.thieves are using apple airtags to track luxury automobiles before stealing them according to canadian police.to lessen the danger of theft authorities advised owners to keep their cars in closed garages use steering wheel locks and place locks on their car data ports.",
                                  'siu nh v z ch hn hng c sn ti ken to anh ch cn nh v chng con nyc tuesday nym ng hng xm....ch cn b nh vo ti hoc balo l bit chnh xc v tr lun n',
                                  'borahae madam !!! thank you!!! ', 'leather holder for airtag by.', 'beautiful',
                                  'apple iphone 12 64gb ru 58999 apple iphone 12 64gb ru 58999 apple airpods 2 mv7n2 9999.10:00 20:00.74732323770 : https:www.instagram.comipioneer.ru.https:vk.comipioneer.russia https:ipioneer.runoutbukiplanshetysmartfonysmartfonyiphonesmartfonyiphone12iiphone12mini23004smartfonappleiphone1264gbchernyjhttps:ipioneer.runoutbukiplanshetysmartfonysmartfonyiphonesmartfonyiphone12iiphone12mini23005smartfonappleiphone1264gbbelyj',
                                  'slick silhouettes meet effortless utility! with these timeless tech gear companions you can give your apple airtag and airpod a classic touch with a modern and functional twist.available at nappadori.com & tap on the image for product info...',
                                  'our signature fairytail pet id tagstart from 350 thb ', 'i am keen to airtags too ',
                                  "ajoutez une protection lgante votre bureau la maison ou au bureau avec ce desk pad en noprne durable.mince et attrayant se pose plat sur votre bureau empchant efficacement les rayures ainsi que l'accumulation de salet et de poussire.son fond antidrapant en noprne lui permet de rester en place et peut galement tre utilis comme tapis de souris.facile nettoyer.disponible chez univers digital.nos experts sont votre disposition pour vous le prsenter aux stores ud zerktouni et ud casaanfa.et pour mieux vous servir nous sommes ouverts du lundi au vendredi de 9h30 19h30 et le samedi de 9h30 13h.92 bd sidi abderrahmane casaanfa 246 bd zerktouni casablanca 0522 942 215 0522 225 789 www.universdigital.com.",
                                  'ognuno li attacca dove vuole tu a cosa hai attaccato i tuo airtag? usi un laccetto portachiavi o altro? sul sito di trovi questo portachiavi e tanti altri accessori per dispositivi apple che potrebbero rivelarsi ottime idee regalo natalizie.semplici eleganti di qualit e poco costosi ',
                                  'io lo lascio appeso in negozio nella sua confezione',
                                  'vorrei mandare un augurio di buon natale a chi lo attacca al telefono',
                                  'chiavi di casa', 'io nel mio portafoglio',
                                  'got an air tag for christmas?!make it the perfect with one of our mickey air tag holders in the color of your choice!!we just landed and are on our way to the boardwalk! let the vacation begin! ',
                                  'thats cute', 'i want this!!!', 'have so much fun!',
                                  'dzie dobry good morning ja ju po spacerku ukadam si do snu nie rb ju tych zdj ',
                                  'przeslodziak', 'psiemka cocos!', 'apple air tag4 air tagiphone ', 'air tag',
                                  'pick your favorite! image: ', 'beautiful edc.great shot as always', 'nice shot',
                                  'everything', "what's the long thing next to the airtag", 'nice apple setup',
                                  'fantastic collection', 'i cant really pick one! maybe the apple watch?',
                                  'apple watch & ipad pro !',
                                  "hi everyone!did you like my elago apple pencil 2 case?its so cute looking isn't it?please leave me a comment! follow my telegram channel for the wallpaper: link in bio please follow.tech credit:.tech wallpaper: pencil and airtag case:.uk ",
                                  'perfect shot my friend', 'nice!!!', 'nice', 'that looks so dope! great shot man!',
                                  'absolutely', 'awesome bro', 'beautiful color and case for apple pencil',
                                  'what you use in background? is it a mat or something? how can i purchae it from you?',
                                  'airtag ', 'airtag', 'apple pencil', 'appleairpodsproww', 'gps500airtag',
                                  'apple watchapplewatchiphone', 'applew', 'airtagairtag',
                                  '!! airtagairtagiphoneweve decided to put a collar and airtag on chabi in order to prevent her from going away anywhere outside from our house ',
                                  'airtag.', 'dmdm']}

    cleaned_comments2 = {'applewatch': [
        'coming soon..dug.store chuyn cc dng airpods & apple watch rep 1:1 sp c ra mt mi ngi y hy cng n ch nhng sn phm tuyt vi bn nh dug nhaaaa ',
        'green apple watch and iphone combo! follow for more apple watch related content! credit: ',
        'what to expect from apple in 2022! follow for more apple watch related content! credit: ',
        'hello! how is your week going? face from paired with the ginger sport band.', 'love it!',
        '..applewatch...www........applewatch.iphoneiphonelinetvsuica..www',
        'im liking this watch face today.some useful complications on it and its attractive and simple.the bottom right complication is airmail i think its just a cuter looking complication than apples native email app.middle bottom is heart watch.bottom left is coloring watch.middle is ticktick a todo list complication.',
        'i do like this face but i do wish they would update it to make it fit better on the bigger screens.',
        'when you dont want to lose your watch clockology face by danila del giorno ', 'nice!!! clockology?',
        'mariacompre', 'link?', 'cool face! thats a fun idea!', '113 4.80.11.0 1025 800', '..........', 'nhktv',
        'magsafe',
        'simple black edc for today slim leather wallet by key organiser by gts mini 2 watch by one plus 7 planning to upgrade soon...',
        'cool', 'oof this looks clean in missing an apple watch though', 'nice bro !', 'great flatlay as always',
        'great shot bro!', 'oh heck yes', 'clean bro! love that wallet', 'clean lay brother great edc',
        'simple but the best', 'clean flatlay', 'woah! the texture!', 'black feed', 'edc shot of the day',
        'i think you should carry a pen too', 'matte black all the way!', 'great shot brother!',
        'such a clean edc looks so good bro!', 'cool shot', 'nice shot'], 'macbookpro': [
        'our new own website launchingthank you so your support.we truly appreciate your business and look forward to serving you again...join us from 12.00pm to 4.00pmfriday 14th january 2022link: www.ismart.co.inismartappleauthorisedreselleraddress : https:bit.ly3isyyufevn rd erodeph: 70944 74444 70944 74448.',
        ' xs ', '!! : :', 'how you can do that', 'looks nice!',
        'feeling a bit better & thankful for more energy some sunlight and a little more brainpower to code! ',
        "i love my workplace having lots and lots of light! it's super essential for me to give my 100!",
        'getting some sunlight on to you helps so much', 'is it a python?', "i can't wait to code on macbook",
        'home office', 'beaut', 'just perfect', 'gorgeous',
        "3 ! i'm in an airport right now but i'm not the one to give advice on traveling and flights because i usually fly like once a year.you can check 's account for good tips on traveling.3.1 ' like never! if you need a functionality in multiple places always extract that into a different component.your future self and colleagues will thank you!2 the longer they are the hard it is for anyone to understand the code even your future self.if a class grows too much it means that you have too many things in one place and you need to separate them.3 ktlint for android and swiftlint for ios they do a great job showing you warnings if you don't respect good coding practices and you can also customize the rules.there are a lot more good coding tips out there but i'll keep it short here.focus on these 3 and your programming game will improve.4 ? ",
        "very nice i didn't know about the lint tool at all that sounds so useful indeed!",
        'true especially copy and paste it is quite common and a false approach for coding...have a safe and happy trip',
        'amazing tips thanks for sharing',
        'i would recommend 4th step as keeping good folder structure for maintainability and easy access of files and components',
        'flutter',
        "great tips especially the first one i would add 4th follow the best practices and code rules anyway even if you have to hack pentagon in 10 minutes and gun is put up to your head.don't believe you will have the time to refactor your code later.",
        'good naming! create understandable and practical names for classes and variables',
        'hey man what ide do you use?', 'about using short methods what would you say is the bar for a long method?',
        "sir kindly check my instagram account you will find lot's of useful programming related information...",
        'thank you so much! have a good flight! and cannot wait for your stories from your next destination!!',
        'which macbook do you own? ', 'unfortunately i dont own one',
        'the mbp 13 m1 had to upgrade last summer because my maxed out 15 mbp from 2018 went swimming', '14 base line',
        'macbook air m1 8 core cpu and gpu but the small one', 'macbook pro m1 13', 'none',
        'm1 pro 14 inch macbook pro silver', 'macbook air 13 2019 :', 'macbook air m1', '13 macbook pro 1tb ssd 2021',
        '2019 pro 16 with touch bar', 'macbook pro 16 2019', '2020 m1 macbook air', 'mbp 16 w touch bar', 'macbook pro',
        'macbook pro m1 13 inch', 'a warrior macbook pro mid 2012', 'the new 14 macbook pro m1 pro base model',
        '2015 macbook pro.....', 'm1 macbook pro 13 andddd love it', 'i have the macbook none 0 :',
        'macbook air m1 2020', 'm1 macbook pro',
        'what do you want to know about the new macbook pro? leave your questions in the comments below and ill answer as many as i can in my review! ',
        "hey dan! do you find the new m1 max macbook pro as a great option for a sturdy home studio setup in case i'm using it for about 12 hours a day! cos i ve always had one sturdy desktop setup and a laptop.always ended up having heating issues after over using my laptop.thanks!",
        'can it be downgraded to big sur for now? or is it monterrey only? if its the latter how are 3rd party plugins working on the new os?',
        'probably a dumb question but would you have any issue switching back and forth with a project on two machines that have different os? thinking about my main rig on mojave and about to get one of these beasts real as a remotebackup setup.',
        'do you feel the price is justified? im assuming youve gone for quite a specd up model',
        'what is the minimum cpu you recommend to run big orchestral projects with spitfire plugins?',
        'for music production including the use of many tracks with sample libraries how much cpu gpu and ram is necessary? are there any upgrades we can skip and still get excellent results? im going to end up buying one but not sure how much to spend on all the upgrades.',
        'how is the 14 screen size for big projects?',
        'how does it handle big orchestral and sample heavy templates projects?',
        'any issues with running logic in rosetta some of my plugins are still not natively supported',
        'is possible to 64 gb ram in macboob m1 new.which time available in the market easily.',
        'im using one now and ive definitely noticed some issues with programs lots of hanging notes but still seems quite powerful.do you think it will get even better as programs and macos updates? ive also seen lots of incomprehensible stress tests so id be interested to see how it handles some of them our bigger projects and how it compares to the spitfire audio setups in real life! excited to hear your thoughts :',
        "i never use mac before so i'm a bit confused.why do composers tend to work with mac if their working on a laptop? because it's a bit pricy than windows laptops isn't it?",
        'do you think the soc architecture with m1 max will make audio interface dsp uapro tools ultetc redundant?',
        'whats the ram pressure like and how much swap memory is being used?',
        'hi dan did you find some compatible problems using certain pluginsvsts with the new mac?',
        'i have problems playing audio from my prem1 logic projects.has anyone the same issues? hickups glitches overloads etc and you dan?',
        'id be interested to know what spec your memory is and if you have any recommendations in that regard for anyone who is thinking of getting one as their main hardware.',
        'how many tracks are loaded possibly without system overload? and how the pan sound goes! thanks : congrats on your new laptop!',
        'hey dan i ordered exactly the same thing.m1 max 64 gigabytes ram.however my macbook is not coming until earlymidfebruary.how satisfied are you with the performance and workflow? greetings from germany hauke',
        'what about the size of the screen? do you think you could work on a big protect on the go on the 14 inch one??',
        'im going to order the macbook pro m1 max 16 inch with 32gb of memoryram.im upgrading from a macbook air bc of struggling with spitfire audio plugins bbc pro albion one aperture stack constantly overloading.do you think the new macbook will be able to handle all these spitfire plugins? thank you!',
        'im waiting for the new imac pro but would love to know how much ram you have there and how its performing.do you think youll ever need more or is it just enough? rosetta running apps aside',
        '1.how does it perform while you are running heavy orchestral projects? need to freeze tracks? still enough headroom in cpu an ram? would be great to here about your experience in your day work.some stress test on youtube are really dumb.2.i think you said yours comes with 1 tb ssd.is it enough for your basic software? are you still using the blackmagic dock? thinking of going to take 2 tb',
        'i switched to html css and js for my personal page why did i switch? i switched because its easier to create small websites which are responsive with html and css.at least for me.but for bigger projects i would definitely choose flutter web.do you have your own website? ',
        'woah awesome shot and angle', 'exactly totally agree with you.working with html css and javascript is fun.',
        'yeah.simple one portfolio page html css and js',
        'yuppp....i do.with htmlcss and js.but i dont use flutter though.i use java',
        'what a wonderful posthappy holidays',
        'hey would you please tell me what is the model and brand of your mousepad?',
        'all the best bro for your new website! i started my tech journey today do follow my page would mean a world to me!',
        'exactly it easy we use it most for html css javascript and react for web app', "nope i don't have",
        'yes! mine is built in flask :you can check it here rubenoliveira.tech', 'how about laravel?',
        'yes mine is made of html css and js',
        'website is already become my life.always visit it for knowing information entertainment download and much more',
        'nice shot! check out these useful apps on the mac app store: skitch zuriweb magnet',
        'what would be considered a bigger project? im new to development and trying to immerse myself and learn as much as possible',
        'n...', " ' ' ", 'damn love this!! the reflection of the macbook display looks absolutely gorgeous',
        'love this shot buddy', 'perfect photo shot man top', 'beautiful shots', 'lovely shots', 'che spettacolo!',
        'dope shots bro!', 'love this shot!', 'bellissimi scatti', 'ma quel riflesso ?!?',
        'wow bro this shot is professional absolutely beautiful', 'incredible shots bro', 'beautiful bro',
        'che idea spettacolare! belli questo scatti francesco!', 'beautiful shots bro',
        'amazing shots man! beautiful reflections!', 'belli scatti', 'clean shot', 'fantastici riflessi francesco',
        'these shots are so crispy', 'ottima foto', 'che colori', 'hai ragione'],
        'appleiphone': [' apple iphone 7 : 449.54airpods', '1..23 mientras ms mejor..', 'follow ?',
                        '1...2.3.4.....y', 'done', 'done done done done done done done', 'oh money',
                        'no.3', 'babies dm to get spoil massively with money and iphones', " & ' ",
                        'its a fake giveaway', 'win win win win win', 'quiero el phone xs', 'nice',
                        '..how to participate?1.2 34 5.', 'lindo iphone digno de tenerlo', 'belliii',
                        'done please help me',
                        'giveaway new offer here 3 we are giving away brand new iphone 12 pro growing our apple network!! ',
                        'i want can uh give me?',
                        'apple is working on big upgrades for the iphone 14 pro and iphone 14 pro max.these are some of the features that have been rumored up until now.are you excited? render from ',
                        'well i am due for an upgrade',
                        'every year its hyped up but turns out to have little or no upgrades lmfao',
                        'i feel like this spec sheet has been used for the past 4 iphone releases',
                        'we need touch id and periscope optical zoom 2050x', 'please no esim',
                        'now i regret getting the 13 pro max', 'still no touchid tho',
                        'car wash detection????',
                        'bruh there are countries that arent e sim compatible',
                        'what about the baseline 14?',
                        'i doubt it will have 8k maybe 5k on the 15 tho.', '120hz?',
                        'car crash detection?', 'where are they getting titanium from? lmao',
                        'take my money!!!',
                        'im ready to upgrade for this! im current iphone 12 pro max',
                        'i want it 14 pro max',
                        'satellite connectivity awesome.so i can go on a road trip without drama',
                        'what are the chances theyll call it phone 15 since itll be a 15 year anniversary',
                        'man cant they at least increase the lens to 4? its a a pro model after all',
                        'car crash detection? i feel like thats purely software jo?',
                        '1 hour of 8k video will need 7.25tb storage',
                        'if its esim only how would it work if you wanted to switch carriers?',
                        'just need usb c and were all set', ' 09376625452 ',
                        'ive been out of it high on meds the past 23 weeks with a bad back so this is a shot from the other week i got on my desk with the chair as foreground.kind of liked how it turned out.how are your weeks all looking? happy hump day follow for more ',
                        'bro this lighting tho', 'get well bro', 'nice shot bro.hope you feels better',
                        'great shot bro!', 'get better soon brother',
                        'you kind of liked it??? this is flawless my guy amazing shot.rest up bro feel better',
                        'love it mate', 'super clean shot as always bro',
                        'clean shot bro.seems busy this week.rest up and hope to see you at it soon',
                        'amazing shot phil! i hope you feel better soon!',
                        'high on meds?! hope youre okay phil!!',
                        'great photo.i love it reflection camera lens',
                        'i really like the result of this shot too bro get well soon i hope youre good feel better',
                        'oh shit dude what happened? hope you get well soon bro anyways the shot is epic',
                        'ah man hope your back feels better soon bro! this shot is awesome! ive used my chair in the foreground before too definitely helps!',
                        'sharp', 'awesome click', 'awesome shot', 'rest up king!',
                        'hope that everything is well phil! have a wonderful wednesday',
                        'it looks great dude! my week is all about painting the',
                        "it's been a crazy busy few weeks as we are moving to a new place lots of things to action at work.and i am trying to run this mini product photography challenge in january.btw you are welcome to join as mentioned earlier your shots are",
                        'love this shot',
                        "sooo clean man! saving this for inspo my back is ok but i've been out for a few days now with quite heavy flu! wish you a speedy recovery",
                        'actual home screen configwallpaper: widget: blank widget: mdblank app......| | | tags ',
                        'clean home screen bro', 'super clean minimal setup brother', 'great',
                        'dope clean shot nico!', 'beautiful', 'love this bro', 'minimalism wins again',
                        'super clean', 'nice homescreen buddy', 'very cool bro',
                        'so clean shot bro and widget ist so cool', 'clean!',
                        'looks great brother! love the icons aligned at the bottom rather than the top! i do the one page setup too',
                        'shot', 'very minimal homescreen bro', 'smart', 'super minimal love it',
                        'oh man! i love how minimal this looks! might have to change mine up now!',
                        'clean neat brilliant shot! rocking that wallpaper', 'fantastic shot',
                        'this is sweet.is there a clear widget?',
                        'i love the minimal approach to your homescreen bro', 'clean homescreen'],
        'applemusic': ["red taylor's version is pure magic", 'love your account', 'promote it on',
                       'i miss taylor she is the goat!',
                       'heyyy your page is so pretty do you mind checking my page and giving a follow back',
                       "we are taking order for this beautifulall our items are in limited stock.they get sold out fast...please book your items at the earliest and you will be served on first come basis only..{ }.tap on the link in the bio to shoppls contact on what's app for more details and information.dm for price.online authentic store by pihu rathore.8188890405 for whats app inquiring & order booking...codnot available...mmer mmer mmer ",
                       'light it up official lyric video friday 114229am pst ',
                       'yo i like your stuff you should be proud of it!! definitely keep going! send me a dm request if you need some spotify marketing helpi really think i can help you grow!',
                       'repost it on.of.world', 'you are such a bad ass mr.light it up',
                       'nice visuals',
                       'mondgockspotify https:open.spotify.comartist1on4veywk0es3is6mci0bk?si2eusz4tkrtwgg7pwjev1cqapple music https:music.apple.comusartistavimondgock1576859144youtube https:youtube.comchanneluc5do4jlk2yu9x4cee4ru76a',
                       'omg slay! us artists gotta support eachother keep on rockin', 'dm on',
                       'shit post.on a side note my album 12 spirits is dropping soon i hope you all will check it out.its got some vibes in it.just me speaking on last years energies.',
                       'trying to actually do the last one together on friday nights hahahahahahaha',
                       'bitch all of these are hahahahabdodnckaofjwofjeofn wtf', 'dm us.records',
                       'love it dm.familye 2m', 'dm it on',
                       'alerta de texto esse post nica e exclusivamente pra agradecer a vocs que esto sempre comigo por tanto aps o lanamento de nocaute a reposta de vocs foi incrvel comigo pessoalmente e em todas as plataformas digitais !!!! minha primeira msica solo meu primeiro trabalho lanado nacionalmente e com a participao de pessoas iluminadas que trouxeram seu melhor pro trabalho !!! chegamos aos 10k aqui somos dezzzz millllllll estou passando aqui s pra agradecer vocs que esto comigo aqui no dia a dia que vo aos meus pagodes que curtem comentam criticam e elogiam que me ajudam a crescer.subimos mais um degrau demos mais um passo muito obrigado de corao amo vocs !!!!! o ',
                       'parabns meu mano vc merece quem sabe no fazemos um som juntos sou compositor tbm sou amigo do lukinhas seu cavaquinista',
                       'o sucesso logo ali', 's o comeo irmo vai pra cimaaaa',
                       'o mundo e seu!!!! pra cima', 'parabns rennan vc merece', 'merecedor',
                       's o comeo meu amor sucesso sempre',
                       's o comeo!!! parabns deus abenoe nocaute simplesmente sensacional',
                       'you got a special content hit my dm for artwork', 'sucesso sempre voc merece',
                       "the white stripes white blood cells 2001 garage rockthe origin of my passion for listening good indie music emanated from my years in high school.this may sound trite but it was the song seven nation army that opened a whole new genre for me in the mid2000s.loud stylish bold and catchy these are the qualities that i was looking for in music as a teenager and found in those hypnotic guitar riffs created by jack white.much later i got acquainted with their discography and was surprised by the variety of genres presented within each album.white blood cells has a place for folk we're going to be friends country hotel yorba and punkrock fell in love with a girl.compositions that are usually quite simple in their structure come to life thanks to the incredible energy of the former spouses.jack white manages to squeeze out the desired jawdropping sound from the song with 3 chords while meg white turns into an unstoppable machine after picking up her drumsticks.highlights:dead leaves and the dirty ground fell in love with a girl i think i smell a ratthe white stripes.seven nation army 2000...white blood cells we're going to be friends hotel yorba fell in love with a girl..3.",
                       'fantastic', 'superb as always sergei!', 'sweet!! very cool man',
                       'wow wow wow!',
                       'great write up and shot sergei! this is my favorite from the ws.',
                       'do you consider all the albums you are posting a 1010 or are they just a favourites of yours',
                       'cool shot!', 'incredible as always',
                       "example that every good music doesn't have to be complex",
                       'looks like alexei got a big treat after this photo got clicked i will never be not astonished by the fact that the iconic bass in seven nation army is not bass at all but infact is him using his guitar with an effect pedal.will check out this album as well.',
                       'love it!!', 'apple music ios & android3 80 applemusic ios android ', 'dm 30 m',
                       'you wanna boss up or just change shifts....', 'the baddest', 'grown&sexy',
                       'can i share it', 'hottt', 'hello', "let's work check dms",
                       'nice sound! rare! wanna join our big playlist?! dm us back!!!',
                       'hey boosend me your song im doing twerk promo videos lets work',
                       'looking around for talented artists! dm us!', 'yooo dm me for your artworks',
                       'promote it on.', 'promote it',
                       ' apple airpods pro 1...2022.1.42022.2.282022.3.2dm instagram facebook instagram ',
                       'airpods1.4', 'appleairpodspro', 'i had to go into beast mode....',
                       'keep workin', 'god bless you', 'beast mode necessary sometimes',
                       'he really like dat',
                       'fire! if u need dope cover art hmu anytime! thank u for ur time!',
                       'best way to to go in all the bs out here good to see people out here getting theirs stay on that hella fux with the music stay up you finna make it fs',
                       '3 weapons one beast', 'de me check inbox',
                       'yo fam....i think i might have a proposal for you..ive checked your timeline and i think we can use your influence...hmu lets stack up for new year',
                       'should be following', 'promote on it 5m', 'dm it', 'wow send it to..records']}

    cleaned_comments3 = {'applewatch': [
        'milanese strap slim for apple watch for 14.99 bargainshopus.comproductsmilanesestrapslimforapplewatch',
        'airpods pro 2: quando arrivano e cosa aspettarci via......',
        'ya viste todo lo que ofrece el nuevo watch series 7 de apple? i n c r e i b l e ',
        'had these a while and still in love with my airpods so showing my some appreciation for them.',
        'what to expect from apple in 2022! follow for more apple watch related content! credit: ',
        '1851 apple watch 45 price : 390450 applewatch applewatchapplewatch smartwatch',
        'green apple watch and iphone combo! follow for more apple watch related content! credit: ',
        'for more details and price whatsapp on 9284104697please dont message for cash on delivery only accept online payment gpay paytm and bank transfer......',
        'apple watch series7 7',
        'im liking this watch face today.some useful complications on it and its attractive and simple.the bottom right complication is airmail i think its just a cuter looking complication than apples native email app.middle bottom is heart watch.bottom left is coloring watch.middle is ticktick a todo list complication.',
        'i do like this face but i do wish they would update it to make it fit better on the bigger screens.',
        'how do you want it?? silver or rose gold ???? price is 20k onlysend a dm to place an order or contact us on whatsapp on on 07017505464 ',
        'mit seinem appstore konnte apple bislang satte 260 milliarden usdollar umsetzen.eine stolze summe! ',
        'giveaway ! follow must !..', 'franck muller rs 3200dm for whatsapp 9998743527 ',
        'promoo de o22 receba em mos e pague aps receberseu est aquiaceitamos carto de crdito pix mais de um carto.dosul ',
        'hello! how is your week going? face from paired with the ginger sport band.', 'love it!',
        'olha s essa comparao que preparamos para voc entender os benefcios de cada aparelho! no fique na dvida chama o pai parcele no carto em at 12xchame no whatsapp e consulte as cores disponveis.11 913231451 apple',
        ' a o a o e.0e 50 ee50 o a i..h..n.13 400gb ea y a o a a o.o o o:1o.0 2e a o y.0 e s o! e 15 22:00 o e o a o a......',
        ' g 1..3 4 15 5.', 'ios15 part1ios15apple', '..applewatch...www........applewatch.iphoneiphonelinetvsuica..www',
        'iphone 12 pro max ', 'applewatch ',
        'unbezahlte werbung mein wohlverdientes frhstck nachdem wir heute morgen schon 2 stunden unterwegs waren kalorien: 622 kcal nhrwerte: 601g ew | 434g kh | 204g fett hlen hlenmityazio hrung hrungsumstellung reich hrungsplan t ',
        'das hast du dir aufjedenfall verdient', 'jbl jb950...: 0916630412506153222469.', '113 4.80.11.0 1025 800',
        '..........', 'nhktv', 'magsafe',
        'california what do you think of this shot?band: watchface: linen blue is surprisingly a bit purple so i thought id pair it with the new english lavender coloured watchface.what do you think?california watchface: love how much detail you can get into the complications and yet still have that classic style.er',
        'dope shot bro!', 'nice sunset',
        'this is amazing! an engineering masterpiece combined with an awesome photographer!', 'nice',
        'beautiful love the sky in the background', 'very nice shot', 'great combo!!! great shot as well.',
        'great shot really focuses my eye to the watch.', 'ooo the weather complication whats that?',
        'simple black edc for today slim leather wallet by key organiser by gts mini 2 watch by one plus 7 planning to upgrade soon...',
        'cool', 'oof this looks clean in missing an apple watch though', 'nice bro !', 'great flatlay as always',
        'great shot bro!', 'oh heck yes', 'clean bro! love that wallet', 'clean lay brother great edc',
        'simple but the best', 'clean flatlay', 'woah! the texture!', 'black feed', 'edc shot of the day',
        'i think you should carry a pen too', 'matte black all the way!', 'great shot brother!',
        'such a clean edc looks so good bro!', 'cool shot', 'nice shot'], 'macbookpro': ['hello ! ! usb.',
                                                                                         'apple macbook pro 2015 model 15 retina display quad core i7 2.8ghz quad core i7ram 16gbssd 512gbavailable ateverything apple gulistan khan plaza baseement 7 fazle haq road near tehzeeb bakers blue islamabad ',
                                                                                         'brandnew sealed 2019 macbook pro 13inches touchbar corei5 quad core 8gig ram128gig ssd touchbar and touchid space grey 600k brandnew sealed 2019 macbook pro 13inches corei5 quad core 8gig ram256gig ssd touchbar and touchid space grey 670k ',
                                                                                         'prints kalender und groes wandbild auf aludibond so liebe ich das! dazu das neue macbook pro ',
                                                                                         'donglelife store are pleased to present the great product duttek micro usb to usb type c adapter right angle 90 degree usb type c male to micro usb female charging and data sync connector converter adapter 2 pack.with so many usbc products & accessories available right now it is wise to have a manufacturer you can trust.the duttek micro usb to usb type c adapter right angle 90 degree usb type c male to micro usb female charging and data sync connector converter adapter 2 pack is certainly that and will be a excellent gift.for this price the duttek micro usb to usb type c adapter right angle 90 degree usb type c male to micro usb female charging and data sync connector converter adapter 2 pack is highly respected and is a regular choice with most people who visit our site.duttek have included some great touches and this equals good bargain price.https:donglelife.co.ukduttekmicrousbtousbtypecadapterrightangle90degreeusbtypecmaletomicrousbfemalecharginganddatasyncconnectorconverteradapter2pack',
                                                                                         'the money making station simple yet effective..',
                                                                                         'apple watch se space gray 40mm mkq13 340apple watch se space gray 44mmmkq63 375apple watch series 6 44mm lte m07j3 490 3 : 46....6 ',
                                                                                         'how you can do that',
                                                                                         'looks nice!',
                                                                                         'uperfect best lapdock is a 1080p portable monitor that displays 2 million pixels within a 10000 mah battery.perfect for samsung dex plug and play with 10 points multitouch capacitive screen.a 10 points multitouch capacitive screen lets you interact directly with what is displayed and provides accurate content interaction.1080p fhd full highdefinition displays 2 million pixels twice as much as hd and result in excellent details on the screen.builtin 10000mah battery: with a 10000mah battery whether you spend your time playing games watching movies or writing articles it will provide the power you need.',
                                                                                         'letzter ferientagso schnell sind die ferien auch wieder vorbei.im moment htte ich wohl doch mehr schlafen sollen bevor es morgen wieder losgeht ich bin wirklich gespannt ob wirklich alles in prsenz bleibt und fhle mich dabei nicht gerade wohl.aber wir knnen ja nichts daran ndern.die ferien habe ich genutzt um endlich mal wieder zu lesen serien durchzusuchten einen teil meiner aufgaben vorzubereiten und mir ein bisschen ruhe zu gnnen.gestern habe ich auch spontan noch zwei trips geplant.einmal zu meiner aupairfreundin ins allgu und mit einer freundin nach mnchen man braucht ja immer etwas worauf man sich freut.geht es bei euch morgen auch wieder los und konntet ihr eure ferien genieen?habt noch einen schnen sonntag und einen guten start in die woche',
                                                                                         'wir haben schon eine woche hinter uns',
                                                                                         'serien durchsuchten ist so schn',
                                                                                         'ich habe die ferien in vollsten zgen genossen',
                                                                                         ' xs ', '!! : :',
                                                                                         'daily mac store indonesia harga spesial daily dibulan januariharga hanya rp.2.35 jt saja bosquhhhready laptop asus 14 x441n siap office dan lembur plus harga sangat sangat terjangkau kode dm383 laptop asus dengan harga terjangkau udah dapet spek yang mantep intel celeron n3350 1.1ghz ram 2 gb hdd 500 gb mantaapp dengan vga intel hd graphics enak buat office ngerjain tugas sekolah dan kuliah online gassskeun kakak jangan sampe keduluan yang lain ya...rekomendasi buat office desainngerjain tugas kuliahan lembur dll...kondisi: spesifikasi : intel celeron n3350 1.1ghz ram 2 gb hdd 500 gb mantaap legaa bgtt vga intel hd graphics kemulusan 977777 kelengkapan unit with charger garansi 1 bulan dijamin tidak akan mengecewakannarahubung: wa081285550100 wa.me6281285540109 on gmaps : daily mac store ',
                                                                                         'feeling a bit better & thankful for more energy some sunlight and a little more brainpower to code! ',
                                                                                         "i love my workplace having lots and lots of light! it's super essential for me to give my 100!",
                                                                                         'getting some sunlight on to you helps so much',
                                                                                         'is it a python?',
                                                                                         "i can't wait to code on macbook",
                                                                                         'home office', 'beaut',
                                                                                         'just perfect', 'gorgeous',
                                                                                         "3 ! i'm in an airport right now but i'm not the one to give advice on traveling and flights because i usually fly like once a year.you can check 's account for good tips on traveling.3.1 ' like never! if you need a functionality in multiple places always extract that into a different component.your future self and colleagues will thank you!2 the longer they are the hard it is for anyone to understand the code even your future self.if a class grows too much it means that you have too many things in one place and you need to separate them.3 ktlint for android and swiftlint for ios they do a great job showing you warnings if you don't respect good coding practices and you can also customize the rules.there are a lot more good coding tips out there but i'll keep it short here.focus on these 3 and your programming game will improve.4 ? ",
                                                                                         "very nice i didn't know about the lint tool at all that sounds so useful indeed!",
                                                                                         'true especially copy and paste it is quite common and a false approach for coding...have a safe and happy trip',
                                                                                         'amazing tips thanks for sharing',
                                                                                         'i would recommend 4th step as keeping good folder structure for maintainability and easy access of files and components',
                                                                                         'flutter',
                                                                                         "great tips especially the first one i would add 4th follow the best practices and code rules anyway even if you have to hack pentagon in 10 minutes and gun is put up to your head.don't believe you will have the time to refactor your code later.",
                                                                                         'good naming! create understandable and practical names for classes and variables',
                                                                                         'hey man what ide do you use?',
                                                                                         'about using short methods what would you say is the bar for a long method?',
                                                                                         "sir kindly check my instagram account you will find lot's of useful programming related information...",
                                                                                         'thank you so much! have a good flight! and cannot wait for your stories from your next destination!!',
                                                                                         'what do you want to know about the new macbook pro? leave your questions in the comments below and ill answer as many as i can in my review! ',
                                                                                         "hey dan! do you find the new m1 max macbook pro as a great option for a sturdy home studio setup in case i'm using it for about 12 hours a day! cos i ve always had one sturdy desktop setup and a laptop.always ended up having heating issues after over using my laptop.thanks!",
                                                                                         'can it be downgraded to big sur for now? or is it monterrey only? if its the latter how are 3rd party plugins working on the new os?',
                                                                                         'probably a dumb question but would you have any issue switching back and forth with a project on two machines that have different os? thinking about my main rig on mojave and about to get one of these beasts real as a remotebackup setup.',
                                                                                         'do you feel the price is justified? im assuming youve gone for quite a specd up model',
                                                                                         'what is the minimum cpu you recommend to run big orchestral projects with spitfire plugins?',
                                                                                         'for music production including the use of many tracks with sample libraries how much cpu gpu and ram is necessary? are there any upgrades we can skip and still get excellent results? im going to end up buying one but not sure how much to spend on all the upgrades.',
                                                                                         'how is the 14 screen size for big projects?',
                                                                                         'how does it handle big orchestral and sample heavy templates projects?',
                                                                                         'any issues with running logic in rosetta some of my plugins are still not natively supported',
                                                                                         'im using one now and ive definitely noticed some issues with programs lots of hanging notes but still seems quite powerful.do you think it will get even better as programs and macos updates? ive also seen lots of incomprehensible stress tests so id be interested to see how it handles some of them our bigger projects and how it compares to the spitfire audio setups in real life! excited to hear your thoughts :',
                                                                                         'is possible to 64 gb ram in macboob m1 new.which time available in the market easily.',
                                                                                         "i never use mac before so i'm a bit confused.why do composers tend to work with mac if their working on a laptop? because it's a bit pricy than windows laptops isn't it?",
                                                                                         'do you think the soc architecture with m1 max will make audio interface dsp uapro tools ultetc redundant?',
                                                                                         'whats the ram pressure like and how much swap memory is being used?',
                                                                                         'hi dan did you find some compatible problems using certain pluginsvsts with the new mac?',
                                                                                         'i have problems playing audio from my prem1 logic projects.has anyone the same issues? hickups glitches overloads etc and you dan?',
                                                                                         'id be interested to know what spec your memory is and if you have any recommendations in that regard for anyone who is thinking of getting one as their main hardware.',
                                                                                         'how many tracks are loaded possibly without system overload? and how the pan sound goes! thanks : congrats on your new laptop!',
                                                                                         'hey dan i ordered exactly the same thing.m1 max 64 gigabytes ram.however my macbook is not coming until earlymidfebruary.how satisfied are you with the performance and workflow? greetings from germany hauke',
                                                                                         'what about the size of the screen? do you think you could work on a big protect on the go on the 14 inch one??',
                                                                                         'im going to order the macbook pro m1 max 16 inch with 32gb of memoryram.im upgrading from a macbook air bc of struggling with spitfire audio plugins bbc pro albion one aperture stack constantly overloading.do you think the new macbook will be able to handle all these spitfire plugins? thank you!',
                                                                                         'im waiting for the new imac pro but would love to know how much ram you have there and how its performing.do you think youll ever need more or is it just enough? rosetta running apps aside',
                                                                                         '1.how does it perform while you are running heavy orchestral projects? need to freeze tracks? still enough headroom in cpu an ram? would be great to here about your experience in your day work.some stress test on youtube are really dumb.2.i think you said yours comes with 1 tb ssd.is it enough for your basic software? are you still using the blackmagic dock? thinking of going to take 2 tb',
                                                                                         'i switched to html css and js for my personal page why did i switch? i switched because its easier to create small websites which are responsive with html and css.at least for me.but for bigger projects i would definitely choose flutter web.do you have your own website? ',
                                                                                         'woah awesome shot and angle',
                                                                                         'exactly totally agree with you.working with html css and javascript is fun.',
                                                                                         'yeah.simple one portfolio page html css and js',
                                                                                         'yuppp....i do.with htmlcss and js.but i dont use flutter though.i use java',
                                                                                         'what a wonderful posthappy holidays',
                                                                                         'hey would you please tell me what is the model and brand of your mousepad?',
                                                                                         'exactly it easy we use it most for html css javascript and react for web app',
                                                                                         'all the best bro for your new website! i started my tech journey today do follow my page would mean a world to me!',
                                                                                         "nope i don't have",
                                                                                         'yes! mine is built in flask :you can check it here rubenoliveira.tech',
                                                                                         'how about laravel?',
                                                                                         'yes mine is made of html css and js',
                                                                                         'website is already become my life.always visit it for knowing information entertainment download and much more',
                                                                                         'nice shot! check out these useful apps on the mac app store: skitch zuriweb magnet',
                                                                                         'what would be considered a bigger project? im new to development and trying to immerse myself and learn as much as possible',
                                                                                         'n...', " ' ' ",
                                                                                         'damn love this!! the reflection of the macbook display looks absolutely gorgeous',
                                                                                         'love this shot buddy',
                                                                                         'perfect photo shot man top',
                                                                                         'beautiful shots',
                                                                                         'lovely shots',
                                                                                         'che spettacolo!',
                                                                                         'dope shots bro!',
                                                                                         'love this shot!',
                                                                                         'bellissimi scatti',
                                                                                         'ma quel riflesso ?!?',
                                                                                         'wow bro this shot is professional absolutely beautiful',
                                                                                         'incredible shots bro',
                                                                                         'beautiful bro',
                                                                                         'che idea spettacolare! belli questo scatti francesco!',
                                                                                         'beautiful shots bro',
                                                                                         'amazing shots man! beautiful reflections!',
                                                                                         'belli scatti', 'clean shot',
                                                                                         'fantastici riflessi francesco',
                                                                                         'these shots are so crispy',
                                                                                         'ottima foto', 'che colori',
                                                                                         'hai ragione'],
        'appleiphone': [
            'ternyata ribet juga ya ngurus imei hp biar terdaftar dan nggak keblokir buat yang mau beli hp dari luar negeri titipbeliin.com bisa bantu belikan daftarkan imei hp kamu secara resmi loh! yuk jangan mainmain sama imei.sayang bukan udah beli hp mahal tapi keblokir siasia kalau kamu lebih pilih beli hp di toko resmi indo atau dari luar negeri?...source: beacukairi ',
            'follow and i will make you your photo whith any effects kodzieo',
            'quer uma sequncia de wins iguais a essa ? entre na nossa sala vip e obtenha resultados iguais aos dos nossos alunos...............................o',
            'silicone case apple iphone : 449.54airpods', 'iphone xs 256gja 0912099604409183369627 ',
            'the best view comes after the hardest climb.', 'send pic.adventures', '....credit ',
            'send pic on', 'rana sb', '1..23 mientras ms mejor..', 'follow ?', '1...2.3.4.....y',
            'done', 'done done done done done done done', 'oh money', 'no.3',
            'babies dm to get spoil massively with money and iphones', " & ' ", 'its a fake giveaway',
            'win win win win win', 'quiero el phone xs', 'nice',
            'giveaway new offer here 3 we are giving away brand new iphone 12 pro growing our apple network!! ',
            'i want can uh give me?',
            'apple is working on big upgrades for the iphone 14 pro and iphone 14 pro max.these are some of the features that have been rumored up until now.are you excited? render from ',
            'every year its hyped up but turns out to have little or no upgrades lmfao',
            'well i am due for an upgrade',
            'i feel like this spec sheet has been used for the past 4 iphone releases',
            'please no esim', 'we need touch id and periscope optical zoom 2050x',
            'now i regret getting the 13 pro max', 'car wash detection????', 'still no touchid tho',
            'bruh there are countries that arent e sim compatible', 'what about the baseline 14?',
            'i doubt it will have 8k maybe 5k on the 15 tho.',
            'what are the chances theyll call it phone 15 since itll be a 15 year anniversary',
            'where are they getting titanium from? lmao', 'no hi res lossless output ?', '120hz?',
            'im ready to upgrade for this! im current iphone 12 pro max', 'car crash detection?',
            'take my money!!!', 'price upgrades',
            'satellite connectivity awesome.so i can go on a road trip without drama',
            'most excited for the titanium chassis if it really comes out',
            'man cant they at least increase the lens to 4? its a a pro model after all',
            'ill be honest..i just cant justify the upgrade anymore.ive been on the apple upgrade scheme for several years getting the phone yearly at launch and the phones just dont blow me away anymore.its just lost that wow factor do i really need 8k video? look at the memory apple prores takes up already..wifi6e do i really need? probably not..i honestly think ill pass gave the series 7 watch a miss last year too.sheer disappointment.only thing ive been impressed with was the new macbook pro which i love!',
            ' 09376625452 ',
            'ive been out of it high on meds the past 23 weeks with a bad back so this is a shot from the other week i got on my desk with the chair as foreground.kind of liked how it turned out.how are your weeks all looking? happy hump day follow for more ',
            'bro this lighting tho', 'get well bro', 'nice shot bro.hope you feels better',
            'great shot bro!', 'get better soon brother',
            'you kind of liked it??? this is flawless my guy amazing shot.rest up bro feel better',
            'love it mate', 'high on meds?! hope youre okay phil!!', 'super clean shot as always bro',
            'clean shot bro.seems busy this week.rest up and hope to see you at it soon',
            'amazing shot phil! i hope you feel better soon!',
            'i really like the result of this shot too bro get well soon i hope youre good feel better',
            'great photo.i love it reflection camera lens',
            'oh shit dude what happened? hope you get well soon bro anyways the shot is epic',
            'ah man hope your back feels better soon bro! this shot is awesome! ive used my chair in the foreground before too definitely helps!',
            'sharp', 'awesome click', 'awesome shot', 'rest up king!',
            'hope that everything is well phil! have a wonderful wednesday',
            'it looks great dude! my week is all about painting the',
            "it's been a crazy busy few weeks as we are moving to a new place lots of things to action at work.and i am trying to run this mini product photography challenge in january.btw you are welcome to join as mentioned earlier your shots are",
            'love this shot',
            "sooo clean man! saving this for inspo my back is ok but i've been out for a few days now with quite heavy flu! wish you a speedy recovery",
            '..how to participate?1.2 34 5.', 'lindo iphone digno de tenerlo', 'belliii',
            'done please help me',
            'actual home screen configwallpaper: widget: blank widget: mdblank app......| | | tags ',
            'clean home screen bro', 'super clean minimal setup brother', 'great',
            'dope clean shot nico!', 'beautiful', 'love this bro', 'minimalism wins again',
            'super clean', 'nice homescreen buddy', 'very cool bro',
            'so clean shot bro and widget ist so cool', 'clean!',
            'looks great brother! love the icons aligned at the bottom rather than the top! i do the one page setup too',
            'shot', 'very minimal homescreen bro', 'smart', 'super minimal love it',
            'oh man! i love how minimal this looks! might have to change mine up now!',
            'clean neat brilliant shot! rocking that wallpaper', 'fantastic shot',
            'this is sweet.is there a clear widget?',
            'i love the minimal approach to your homescreen bro', 'clean homescreen'],
        'applemusic': ['otdch longo family..',
                       "taylan paskal'n ''bulutlarn arasnda'' albmnde yer alan ''ehri ayrlk'' arksnn video klibi arpej yapm etiketiyle netd mzik kanalnda! narasnda ehriayrlk ",
                       'find godlike w on apple music spotify and youtube!! more for yall soon',
                       ' &b ',
                       'dropping this friday!!a humbly slept on production ep featuring thank you all for blessing me with the verses for this work of art! presave link is in the bio ',
                       "i came across your page! you have an inspiring page! kindly check out my page and dm me if you need any of my services like business brand logos cartoon portrait of yourself or loved one's and lot's more...",
                       'are u in need of mixtape covers logos cover arts cartoon pics animated video at affordable price? why delay hit my dm n get urs done asap',
                       'dm it on.recordz 30m',
                       'youtube premium streaming video apapun tanpa batas putar di background tanpa harus buka aplikasi youtube nya akses offline sepuasnya bisa menikmati youtube music juga bisa pakai akun pribadi family plan via invite email yang di minta hanya email saja individual plan pakai email pribadi dan belum pernah di premium kan apple music pakai apple id sendiri bisa pakai apple id lama atau baru download lagu tak terbatas terdapat 60 juta lebih lagu user interface berkelas hanya butuh apple idtanpa password sudah mendukung lirik bisa didengar offline full garansi aman & legal canva pro unlock all fonts unlock background & all templates bisa untuk ios & android harus menggunakan email pribaditrustedtesti cek testibuypremiiumid order klik link on bio wa buypremium.apps ',
                       'dm on',
                       'kiming store premium aplikasi & zoom termurah.di store tersedia berbagai macam aplikasi premium yahh!!!ada zoom premium juga loh termurah nih ada promo menarik legal 100 bergaransi trusted & termurah 100 langsung pakai no vpn no mod.ada promo diskon juga manfaat dari premium yaitu : 1.bisa dengarkan lagu tanpa jeda iklan bisa buat & atur playlist lagu.2.bisa nonton film & video tanpa iklan dan tidak berbayar.3.bisa edit dan save foto di aplikasi tanpa ada kendala.4.tidak nonton bajakan dan bisa menghargai para talent.5.bisa atur breakout room unlimited waktu zoom.note : berlaku sesuai durasi pemesanan.pembayaran via : bank bri ovogopaydana shopeepay info lebih lanjut hubungi https:wa.me6281929140728 atau dm see you ',
                       'out now on all streaming platforms tap in and run that shit up spoda x audio trafficking pt.2 song at2 interlude mixedmastered by ',
                       'dm it on',
                       'dont work with this guy bigkeezy.from experience you will regret it!!!!!! spread the word',
                       'promote it on 8m', 'promote it on', 'how u kno',
                       "they know i'm a king putting on my belt buckle i'm be forever a king of this shit:: ",
                       "let's make it viral just dm me", 'plz ck ur dm if u need promo service',
                       'kindly check your inbox', "red taylor's version is pure magic",
                       'love your account', 'i miss taylor she is the goat!',
                       'heyyy your page is so pretty do you mind checking my page and giving a follow back',
                       'light it up official lyric video friday 114229am pst ',
                       'yo i like your stuff you should be proud of it!! definitely keep going! send me a dm request if you need some spotify marketing helpi really think i can help you grow!',
                       'repost it on.of.world', 'you are such a bad ass mr.light it up',
                       'nice visuals',
                       'mondgockspotify https:open.spotify.comartist1on4veywk0es3is6mci0bk?si2eusz4tkrtwgg7pwjev1cqapple music https:music.apple.comusartistavimondgock1576859144youtube https:youtube.comchanneluc5do4jlk2yu9x4cee4ru76a',
                       'omg slay! us artists gotta support eachother keep on rockin',
                       'your friend or family member that is an artist grinding might be his next scamming victim!!! warn them before its late.',
                       'dm us.records', 'promote it', 'dm me on', 'lets work',
                       'wow send it to..records',
                       'alerta de texto esse post nica e exclusivamente pra agradecer a vocs que esto sempre comigo por tanto aps o lanamento de nocaute a reposta de vocs foi incrvel comigo pessoalmente e em todas as plataformas digitais !!!! minha primeira msica solo meu primeiro trabalho lanado nacionalmente e com a participao de pessoas iluminadas que trouxeram seu melhor pro trabalho !!! chegamos aos 10k aqui somos dezzzz millllllll estou passando aqui s pra agradecer vocs que esto comigo aqui no dia a dia que vo aos meus pagodes que curtem comentam criticam e elogiam que me ajudam a crescer.subimos mais um degrau demos mais um passo muito obrigado de corao amo vocs !!!!! o ',
                       'parabns meu mano vc merece quem sabe no fazemos um som juntos sou compositor tbm sou amigo do lukinhas seu cavaquinista',
                       'o sucesso logo ali', 's o comeo irmo vai pra cimaaaa',
                       'o mundo e seu!!!! pra cima', 'parabns rennan vc merece', 'merecedor',
                       's o comeo meu amor sucesso sempre',
                       's o comeo!!! parabns deus abenoe nocaute simplesmente sensacional',
                       'you got a special content hit my dm for artwork', 'sucesso sempre voc merece',
                       "the white stripes white blood cells 2001 garage rockthe origin of my passion for listening good indie music emanated from my years in high school.this may sound trite but it was the song seven nation army that opened a whole new genre for me in the mid2000s.loud stylish bold and catchy these are the qualities that i was looking for in music as a teenager and found in those hypnotic guitar riffs created by jack white.much later i got acquainted with their discography and was surprised by the variety of genres presented within each album.white blood cells has a place for folk we're going to be friends country hotel yorba and punkrock fell in love with a girl.compositions that are usually quite simple in their structure come to life thanks to the incredible energy of the former spouses.jack white manages to squeeze out the desired jawdropping sound from the song with 3 chords while meg white turns into an unstoppable machine after picking up her drumsticks.highlights:dead leaves and the dirty ground fell in love with a girl i think i smell a ratthe white stripes.seven nation army 2000...white blood cells we're going to be friends hotel yorba fell in love with a girl..3.",
                       'fantastic', 'superb as always sergei!', 'sweet!! very cool man',
                       'great write up and shot sergei! this is my favorite from the ws.',
                       'wow wow wow!',
                       'do you consider all the albums you are posting a 1010 or are they just a favourites of yours',
                       'cool shot!', 'incredible as always',
                       "example that every good music doesn't have to be complex",
                       'looks like alexei got a big treat after this photo got clicked i will never be not astonished by the fact that the iconic bass in seven nation army is not bass at all but infact is him using his guitar with an effect pedal.will check out this album as well.',
                       'love it!!', 'apple music ios & android3 80 applemusic ios android ', 'dm 30 m',
                       'you wanna boss up or just change shifts....', 'the baddest', 'grown&sexy',
                       'can i share it', 'hottt', 'hello', "let's work check dms",
                       'nice sound! rare! wanna join our big playlist?! dm us back!!!',
                       'hey boosend me your song im doing twerk promo videos lets work',
                       'looking around for talented artists! dm us!', 'yooo dm me for your artworks',
                       'promote it on.',
                       'freak for me just hit 20k on spotify much love to everybody and all the beautiful queens who helped me promote it new single gone dropping in two weeks for yall.3',
                       'great post', 'keep it runnin boss', 'numberssss', 'lets go',
                       'lets run it upppp', 'lets get it', 'goood shit', 'ayeee congratulations!!',
                       'dope', 'big congratulations my boy', 'congrats',
                       'thats awesome congratulations', 'i love your content',
                       ' apple airpods pro 1...2022.1.42022.2.282022.3.2dm instagram facebook instagram ',
                       'airpods1.4', 'appleairpodspro', 'i had to go into beast mode....',
                       'keep workin', 'god bless you', 'beast mode necessary sometimes',
                       'he really like dat',
                       'fire! if u need dope cover art hmu anytime! thank u for ur time!',
                       'best way to to go in all the bs out here good to see people out here getting theirs stay on that hella fux with the music stay up you finna make it fs',
                       '3 weapons one beast', 'de me check inbox',
                       'yo fam....i think i might have a proposal for you..ive checked your timeline and i think we can use your influence...hmu lets stack up for new year',
                       'should be following', 'promote on it 5m', 'dm it']}

    cleaned_comments4 = {'iphone13promax': ['nice weather queen elizabeth walk singapore ',
                                            'design com resistncia fora de srie e um salto imenso na durao da bateria.disponvel nas cores azul sierra dourado e preto com capacidade de 128gb.compre atravs do direct ou chame no whatsapp 44 999340586 levamos at voc! ',
                                            'send pic on.ig',
                                            ' 13mini1313pro13promax 2 290 7788xxsxrxsmaxse20201111pro11promax12mini1212pro12promax 2 line: ems20 1111proiphone11promaxiphone12 12 12promax 12promax 13mini1313pro13promax ',
                                            ' iphone 13 pro max gold 24k ',
                                            'vy bm 74 hr 74127 vilar i lodalen mellan uppdragen.lodalen oslo norge 20211220 sj ',
                                            '.14...14 14 14 13 13 13 13 ', 'h o o d i e ',
                                            'light blue dark blue or midnight green? : ', 'dark blue', 'black',
                                            'send pics',
                                            'happy thursday everybody! here is a shot of the iphone 13 mini and one of my personal favourites the iphone 4s.usually when i upgrade my iphone i always sell my old one so that it can be used by someone else but i always keep my iphone 4s around.i just cant part with it its really a piece of art as an apple fan.now that apple have been making iphones for 15 years we have an awesome product and im sure in the next 15 years it will grow even stronger.does the iphone 4s hold a special place in your heart? iphone 13 pro maxfollow | like and share for more content!hashtags: ',
                                            'for me 5 is the one thats the most special to me.its the iphone that brought me back to iphone after trying out a samsung',
                                            'slslpad2022 ', 'espetculo', 'wonderful',
                                            "win a brand new iphone 13!enter our time limited giveaway and win iphone 13the most important step don't skip it go to the website select your phone important is highly requirement complete the anyone simple survey.when you done your survey then give me a screenshot on my inbox.the link in my bio.follow us like the recent post share this post to 15 of your friends comment below done those who write done in the comments below please leave us a message in a direct inbox ",
                                            'done', 'please i need this and also i followed', 'tengo fe',
                                            'which one is your favourite.?...follow for latest updates & many more....hashtags: ',
                                            'realme gt 2 pro', 'oneplus', 'realme gt 2 pro is best in prize',
                                            'iqoo 9 pro',
                                            "xiaomi the form of the camera's or else wat it the oneplus 10 pro buy i dont like the colorframe of the cameras",
                                            'xiaomi for cameras',
                                            'one plus 10pro fev but india release date pzzz waiting plzzzzz',
                                            'mi 12 pro', 'realme!!', 'one plus', '2022 13 512 1 & 1 1 3 4 13 ',
                                            'eu queroooo', 'thanks', 'i need it', 'send me pic',
                                            'promote it on.nirvana', ' iphone 13 pro max ? : ? ', '256?', ' 13 128',
                                            '128 256', 'lindo iphone digno de tenerlo 12',
                                            '.premio: 1 iphone 12 pro max.para concorrer a esses premios siga atentamente todas as regras abaixo:.1 curta e salve essa foto!.2 siga a pagina e todos perfis que a pagina segue!.3 curti publicao recente desses perfil.oficial4 comente ok ou emojis o maximo de vezes que conseguir!.5 clique no aviaozinho e compartilhe nosso sorteio nos stories e envie para todos do seu direct!.prontinho e so aguardar frete gratis.todos que cumprirem corretamente todas as regras irao concorrer.resultado dia 1601 as 21:30.boa sorte..............opaulo ganhar ']}

    cleaned_comments5 = {'iphone13': ['2022.01.13 ',
                                      'carcasa spigen cyrill cecile9990 lei tva inclushttps:ebazarmassmarket.euproduscarcasaspigencyrillcecilein orice domeniu cineva trebuie sa iasa in evidenta prin calitatea produselor si a serviciilor si prin gradul de satisfactie al clientilor.iar in domeniul accesoriilor pentru telefoane putem spune ca exista huse de protectie si exista spigen.diferenta o dau materialele folosite procesul de design si cel de fabricatie atentia la detalii.totul pentru a oferi clientilor o experienta premium made in usa.',
                                      'a massive top up & exchange deal awaits you!! what you waiting for hope on this one0765859491 ',
                                      'cases para el iphone 13 pro max aprovecha nuestra promo!case lmina por solo gs.105.000! onuevo',
                                      '2022.1.13410 ', 'iphone 7 plus 64 gb.lacrado.com nota fiscal...',
                                      'olivos digital camacu 421 olivos whatsapp: 11 63303532 email: ventas.com nuestros productos apple tienen 1 ao de garanta oficial apple.todos nuestros productos son nuevos originales sellados de fbrica y con 6 meses de garanta.',
                                      'besus cystal case for 1313pro13pro max..! premium quality covers...buy now and protect your phone....price 2450pkr offering 5 off on easypaisajazzcash advance payment.free delivery nationwide.special offer.iphonecover iphone11 ',
                                      'iphone 13 case lf ekderi lf rmasaat',
                                      'besus cystal phone case for 1313pro13pro max..! premium quality covers...buy now and protect your phone....price 2450pkr offering 5 off on easypaisajazzcash advance payment.free delivery nationwide.iphonecover iphone11 ',
                                      'venha nos visitar e garanta j seu aparelho apple estamos pronto para te atender aqui na black iphone temos aparelhos lacradosaparelhos de vitrine e seminovosassistncia especializada applegarantiaqualidadeprocednciarua santa efignia 15 loja 12 c centro spwhatsapp 011 959605432parcelamos no carto at 12xconsulte mais informaes ',
                                      'light blue dark blue or midnight green? : ', 'dark blue', 'black',
                                      'yesterday i actually rode with the windows down! it was so sunny and natural light is so so good for pictures!..i love the unique look that sunrays produce in pictures..keepin it real..the last 3 photos when you swipe are just a few of several that were crappy pics.if you look at my huge i even have a boogie.of course we pick out the very best to post! i use my to edit too...',
                                      'cases para el iphone 13 pro aprovecha nuestra promo!case lmina por solo gs.105.000! onuevo',
                                      'open boxgrtis:mica estuche cargador pde tu equipo y accesorios aqu: https:wa.me593991164915 local machalacalle juan montalvo entre bolivar y rocafuerte junto al hotel veuxor edificio vsquez garca local interno al fondohorario:lunes a sbado09:00am a 18:30pmenvos a domicilio y servientrega.whatsapp 0991164915sguenos: mi cell store ec en facebook micellstore.ec en instagram ',
                                      'iphone 13 128 gb blue 72999seal pack with bill & 1 year warranty available ss mobile alkapuri vadodara log sasta kehte hai hum sasta dete hai order us on call or whatsapp on 7046299999 ',
                                      'ready : iphone 11 128 gb ibox blackgaransi : ex ibox garansi sd 02 oktober 2022harga : 9.500.000kondisi unit : second mulus 98 sangat terawatbaterai health : 98 belum kalibarasikelengkapan : kabel chargerboxmanual bookkartu garansifree temper glass depan terpasangfree backcover karbonfree casedetail unit : no minus semua berfungsi dengan baikface idtouchidtruetonespeakerlcdmiccamerasim cardimei terdaftar kemenperin anti blokir imeiicloud amanmodel : paakami adalah truster seller yang menjual produk originalreal picture ya jaminan original bukan replikasistem pembayaran bisa transfer maupun rekbermarkerplace silakan order via link di biowa 089516978823 ',
                                      'chance to 1..3 4 15 5.',
                                      'no deixe para amanh diga pra pessoa que voc ama o quanto ela importante hoje mesmo.mas se seu celular no est ajudando ns te ajudamos.aparelhos a partir de apenas r699 com 1 ano de garantia e ainda dividimos em 12x no carto.fale com nossos atendentes agora mesmo.link na bio.',
                                      'gracias matas y carla por elegirnos que disfruten sus nuevos iphones!.accede a los mejores precios en productos apple nuevos y sellados.contamos con:.oficina para entregas en belgrano caba oficina para entregas en bahia blanca envios a todo el pais.',
                                      'info', 'hola buen da solo efectivo?', 'precio aiphon 13',
                                      "good morning with a photo from yesterday in my closet here for you what do you think i was up to there? have you seen my new highlight ? if you don't run there because news is coming kisses i love u bom dia com foto de ontem no meu closet aqui pra vocs oque vcs acham que eu estava aprontando ai? ja viram o meu novo destaque ? se no corre l pq vem novidade por ai kisses i love u ",
                                      'promote it on',
                                      'disponveis iphone 13 pro max 128gb novo aparelho lacrado com 1 ano de garantia apple aps a ativao.compre com seguranca seminovos impecaveis acessorios originais garantia de 3 meses 100 originais icloud livre imei limpo loja fisica...tags ignore ',
                                      'the new iphone 14 camera is crazy check the zoom on this...', 'dm it on',
                                      '15 12:08applefranquiabrasilsero trs ganhadores!sorteio mega specialcada ganhador vai levar um iphone 13 pro max paracasa!frete grtis obrigatrio cumprir todas as regras s ganha quem cumpre todas as regras!1curta e salvee essa foto!2siga a pgina e todos perfis que a pgina segue! obrigatrio!3curtir as ltimas fotos de e e muito e marque seus amigos!quanto mais voc comentar maiores so suas chances!resultado amanh as 22:00 ',
                                      'morning yall! seans vacation is over and now its time to get back into my routine starting off with cleaning the entire house jamming to some good music and then doing some meditation i was sent some videos to watch and a journal to purchase.ill share it once it arrives.what music do you jam out to when cleaning? lmk in the comments below.......',
                                      'happy wednesday',
                                      'xiaomi mi 12 pro and realme gt2 pro just looking at the appearance who wins?::: ',
                                      'dm for shoutout',
                                      'agora na info&tech temos smart tvs e vrios outros eletrnicos smart tv samsung uhd 4k 55 em at 10x sem juros !!! lacrada !!!nota fiscal e 1ano de garantia frete grtis economize !!!no espere o seu aparelho desvalorizar ainda mais realize um oramento aceitamos o seu usado como forma de pagamento e volta em at 10x s juros no carto !!! melhor preo e melhores condies de pagamento da cidade !!! o o e ',
                                      'me mande uma mensagem no direct por gentileza',
                                      'shop now click the photo! send your friend who loves this case! iphone silicone rainbow case available for most iphones get yours now!worldwide free shipping all of orders!',
                                      'price', ' www.persianapple.ir ',
                                      " 13 & 13 x 100 ' 1 2....................................3....................................4 3 5 ! 08:00.credit :.team",
                                      'done', '.777.bhxvukx', 'the world is yours babygirl own it.',
                                      'das sieht echt super aus', 'diese unglaublich schne frau!', 'schne du', 'nice',
                                      'your tattoos are freaking stunning', 'wunderschn',
                                      'loyal and honest babies needed dm and get spoiled instantly with no delays',
                                      ' 14001022iphone 13 pro max 512 black pro max 512 blue pro max 256 blue pro max 256 gold pro max 256 black pro max 256 silver pro max 256 gold pro 1 tb blue pro 256 blue pro 256 silver pro 256 gold pro 256 silver pro 256 black pro 256 gold pro 128 black pro 128 silver pro 128 black 256 black 256 blue 256 red 128 pink 128 white 128 black 128 blue 128 pink 128 blue 128 red mini 256 black mini 256 white mini 256 pink max 512 black za max 512 blue za max 256 black za pro 256 blue za pro 256 slver za pro 256 gold za pro 256 blue za pro 128 silver za 256 black za 256 white za 256 blue za 256 purple za 128 green za 128 purple ch 128 purple za mini 256 white mini 256 green mini 128 red mini 64 green pro max 512 green 128 black za 128 green za 128 white 128 black 64 black 09122482651 dm for creditsource: ',
                                      ' !!! ', 'se big box e?',
                                      'llevo ms de 10 aos usando iphone y despus de usar todos los modelos de iphone 13 por casi 2 meses te cuento cual es el indicado para ti sin rodeos en mi ltimo video de youtube link en bio.cul elegiras t? link en bio ',
                                      'me encanta iphone ir a ver el video', 'ah falta el mo 6s',
                                      'viendo esto desde un iphone 13!!!!!!!', 'iphone 13 mini',
                                      'excelente video!yo cambi mi iphone del xs max al 13 pro y me encant estoy sper conforme con el cambio',
                                      'gracias charlie! eso me interesa justamente.', 'excelente tu contenido',
                                      'sper! yo tengo el iphone 13 pro y definitivamente siento que fue la mejor eleccin.',
                                      'como qu hay 4',
                                      'yo por aos ocup samsung serie s pero este ao me cambi a iphone iphone 13 pro max 256 gb y la verdad es que estoy muy conforme',
                                      'si tienes 10aos usndosela iphone yo los aos igual que t pero yo slo tengo 4aos usando un iphone 6s de 16gb y es todo para mi pero ya no sirve me regalaras unos ?',
                                      'regala uno', 'cuando de infinix', 'el indicado es un xiaomi',
                                      'el mejor sera que me regales uno tu',
                                      'te aviso cuando me lleguen a gustar los iphone creo que nunca pero te tendr en cuenta.',
                                      'excelente informacin muchas gracias por t tiempo y por contestar preguntas que ms a fondo y pensando en tus seguidores bendiciones de lo alto charlie',
                                      'yo me inclino por el 13pro pero por economa me conformo con un 13 normal',
                                      'el 12 y el 13 son la peor cmara...si creas contenido es el menos recomendado',
                                      'ninguno.hace rato iphone dej de ser una empresa innovadora.sus productos son un problema en cuanto a compatibilidad y sus precios sobrevalorados.'],
                         'applelux': [
                             '!!!smart watch t500.1.78.: : mtk2502d 1.78 320385 : 280 mah : 1:1 bluetooth sms facebook instagram viber telegram.44 :https:m.youtube.comwatch?vtcb0xqkylo0 : 890 ',
                             'apple watch 6 1:1: ips 178..sms pushup siri gps : wwfit : 1899 ',
                             'necesitas arreglar tu celular o tablet en apple lux somos expertos en reparacin y mantenimiento de todo tipo de dispositivos movilestrabajamos con piezas garantizadas arreglos en tiempo record contamos con tienda fisica y servicio a domicilio.contacto directo https:bit.ly3ecddn4direccin: av.portugal y shyris.edificio cosmopolitan parc oficina 205.horarios de atencin: lunes a viernes de 09:30 a.m a 19h00 p.msbado 10h00 a 17:00 p.m ',
                             'servicio tcnico garantizado actualizacin de software para tu smartphone macbook cambio de display y bateras nuestro equipo de trabajo cumple con todos los protocolos de higiene y seguridad para tu tranquilidad y bienestar.contctanos:https:bit.ly3ecddn4 visitanos:direccin: av.portugal y shyris.edificio cosmopolitan parc oficina 205.horarios de atencin: lunes a viernes de 09:00 a.m a 19h00 p.m sbado 09:00 a 17:00 p.m ',
                             'apple earpods lightning luxprice2500 apple earpods luxprice2000 ',
                             ' 2200 : ; apple; siri: siri ; ; ; lightning; ;.direct whatsapp airpods',
                             '!!!smart watch t100 plus : 1.78 320385 : 280 mah : 1:1 bluetooth sms facebook instagram viber telegram.44 :https:youtu.begxnb1kepvfs : 899 ',
                             ' apple watch : : : 128 : : mtk2503c : 1.54 bluetooth: 4.0 : 90 : 128 : watch os : 220 : ips : : 240x240 : : bluetooth : : : : : 44 : : : 2700 direct whatsapp ',
                             'smart watch d20 y68 : black : 11 22 33 ! ! fitpro.android ios apple instagramwatsappfacebookskype..: 650 ',
                             'necesitas cambiar tu display en apple lux somos expertos en reparacin y mantenimiento de todo tipo de dispositivos moviles trabajamos con piezas garantizadas arreglos en tiempo record contamos con tienda fisica y servicio a domicilio.contacto directo https:bit.ly3ecddn4direccin: av.portugal y shyris.edificio cosmopolitan parc oficina 205.horarios de atencin: lunes a viernes de 09:30 a.m a 19h00 p.msbado 10h00 a 17:00 p.m ',
                             'are you at crossroads???? you probably know you should invest in ibeju lekki but you dont want to fall into the wrong hands?well i have got good news for you this morning! with pentagon real estate investment limited you have no reason to worry about your investment.getting your property from us equals buying peace of mind!contact us today.',
                             'love client feedback!! top seller apple luxury body moisturizer made with almond oil coconut oil beeswax vitamin e oil apple cider & vanilla essential oil! regularly priced: 4 oz.10 & 8 oz.15 order yours today! visit www.silkyradiance.com ',
                             'this body moisturizer is the absolute best! i use it all over my body from head to toe.its the only product i want to use on my skin.when you try it youll love it!',
                             'necesitas cambiar tu display o batera trabajamos con piezas garantizadas arreglos en tiempo record contamos con tienda fisica y servicio a domicilio.contacto directo https:bit.ly3ecddn4direccin: av.portugal y shyris.edificio cosmopolitan parc oficina 205.horarios de atencin: lunes a viernes de 09:30 a.m a 19h00 p.msbado 10h00 a 17:00 p.m ',
                             'servicio tcnico garantizado.haz tu pedido disponemos de servicio a domicilio y tienda fsica contacto directo 0987758861https:bit.ly3ecddn4 vistanos estamos ubicados en la av.portugal y shyris.edificio cosmopolitan parc oficina 205.entrada por la calle luxemburgopagos en efectivo y con tarjetas para diferir horarios de atencin: lunes a viernes de 09:30 a.m a 19h00 p.msbado 10h00 a 17:00 p.m ',
                             'necesitas cambiar tu display o batera aprovecha nuestro descuento de regreso a clasestrabajamos con piezas garantizadas arreglos en tiempo record contamos con tienda fisica y servicio a domicilio.contacto directo https:bit.ly3ecddn4direccin: av.portugal y shyris.edificio cosmopolitan parc oficina 205.horarios de atencin: lunes a viernes de 09:30 a.m a 19h00 p.msbado 10h00 a 17:00 p.m ',
                             ' 10 : 2700 direct whatsapp airpods ',
                             'cambia tu iphone por regreso a clases crea fotos videos y documentos aprovecha nuestros precios promocionales en efectivo.iphone 7 256gb iphone 8 256gb iphone xr 64gbiphone xs 256gb iphone xs max 64gbiphone 11 64gb equipos open box con garanta de un ao incluye cargador ms mica de hidrogel.servicio tcnico garantizado.haz tu pedido disponemos de servicio a domicilio y tienda fsica contacto directo 0987758861https:bit.ly3ecddn4 vistanos estamos ubicados en la av.portugal y shyris.edificio cosmopolitan parc oficina 205.entrada por la calle luxemburgopagos en efectivo y con tarjetas para diferir horarios de atencin: lunes a viernes de 09:30 a.m a 19h00 p.msbado 10h00 a 17:00 p.m ',
                             'solo pagos de contado?', 'ya disponemos para tarjeta de crdito',
                             'smart watch m 16 plus : gps bluetooth 5 23 : 1099 ',
                             'smart watch m26 plus 2021 !:..: 1.78 : 280 mah 10..1:1 push ;.iphone android : 1199 '],
                         'applecompany': ['apple ceo 2020 7 apple 3 198 gdp 2021 98.7 7.3 2020 14 ',
                                          'zerat rreth pajisjeve te reja iphone qe do te vijne gjate ketij viti po vazhdojne te shtohen.nje leaker i njohur dylandkt tregoi ne twitter se linja iphone 14 pro do te vije me nje dizajn te ri pas shume vitesh.ai beson se notchi do te zhduket dhe do te zevendesohet nga kamerat holepunch pasi elementet e tjere te face id do te vendosen nen ekransa prej jush po e prisni kete iphone?pr m shum postime t tilla follow ',
                                          "who's remembering this moments first iphone showed in the world....",
                                          'rroga baze e tim cook qendroi po 3 milionepor ai fitoi nje shtese prej 12 milionesh permes stimujve dhe aksione me vlere 82 milione.kjo shume eshte 6 here me e madhe se fitimet e tij prej 14 milione gjate vitit 2020per me shume postime te tilla follow ',
                                          'on this day in 2001 released itunes starting something huge if not an era ',
                                          ' knowledge is power increase your iq ',
                                          "according to an apple press statement released on monday app store developers have earned more than 260 billion since the store's inception in 2008.apple said last january that developers had earned more than 200 billion since the launch of the app store so the new figure shared monday indicates developers earned 60 billion in 2021.",
                                          'every successful company has to start from somewhere...follow follow follow ',
                                          'they worked 44 years to achieve their goals!! omg',
                                          'starting my wholesale company in a matter of days.grind the same way the big boys do and imma play like them hopefully.ps: your contents by the way',
                                          'awesome post',
                                          "i'm waiting for a company called orange becomes more successful.",
                                          "i'll still always be an android fan!", 'must read ',
                                          'the best marketer in the world he had a team of psychological experts who experiment the experience of customers and steve jobs would introduce each and every product in such a way that people would go crazy for buying it.one thousand songs in your pocket was the best marketing tactic by steve jobs to introduce the first music ipod.',
                                          'born genius', 'i read many things about steve but never knows this...thanks',
                                          'one of the best marketer steve',
                                          'just a marketing genius who was an ah in real life.',
                                          'save this post to remind you later.like our content? hit the follow..',
                                          'this is really good', 'this is so true', 'such a great post',
                                          'like your content buddy really so good to see.keep doing',
                                          'absolutely if your plans dont scare you and excite you at the same time they are not big enough',
                                          'you have find right partner that pay 5050 and treat you like king!are you really want to change your life then choose right partner at right time.now days making money is very easy you have to keep patient and persistense and consistency!how to make 5000 money per month link in bioi need you support to share this post a step by step guide from 0 to 100k followers on instagram link in bioclick the link in my bio so you can be free to!!!start not for just 7 in my bio....turn on post notifications tag | comment | save | share follow follow hashtags ',
                                          'mind blowing', '....',
                                          'post comment share post notification on follow follow follow ',
                                          ' 10 25...35 7721042787', 'must know this ', 'read steve jobs biography',
                                          'never heard this!', 'good', 'that take away is', 'i see',
                                          'that pricing sums it up', 'very insightful post!',
                                          'apple company credit: unknown magazine: ', ' :steven paul jobs..i.ii......',
                                          '.mashhad ',
                                          'woah.such a great leader he was..share this post to your friendsfollow us for more interesting posts..',
                                          'tab bc jaguars esa ni dikh raha tha',
                                          'bhaii wo ladkii thii..ladkaa hotaa to bahar nikaal detaa',
                                          'ofter this next day she still came late makeup prblm',
                                          'maine sunatha yeto lazy aadmi ko dhundhta tha kam karne ke liye kyun ki wo shortcut dhundega',
                                          "let's aim to all be bossesleaders like steve jobs",
                                          'hmare yha corporate sector me half day lga dete h',
                                          'soch rha hu mein bhi office late jau',
                                          "once a guy was late.he didn't get a car but was fired", 'encouraging her',
                                          'or yha salary hi kaat lete hai sunate alg se',
                                          'if steve jobs is male why the word her...?',
                                          'next morning every worker would be late',
                                          'dm for 3d designs cad models and jewellery and architecture designs 3d',
                                          'follow for 3d designs cad models and jewellery and architecture designs 3d',
                                          'seriously?!', 'bhai yeah sab bakchodi hai',
                                          'bill gates be like surprise mother fcker',
                                          'and after that everyone stared to be late',
                                          'wo jo maal fuka tha wo muje v cahiye',
                                          'bhai me ek bar comapny me late ho gya tha comapny valo ne nikal diya tha',
                                          'what secretary she have had must be..!!',
                                          'on next day whole staff comes late',
                                          'at the time the nokia was ten times more valuable than apple...',
                                          'nokia must be regrating to not keeping themselves up with the competition',
                                          'few people have the privileged of having such a supportive and giving friend.i am beyond lucky you for being there for me yet again.i am so grateful that you are in my life',
                                          'nokia ko jaldi android lana tha....late kr diya',
                                          'apple be like : hum bhi garib hua krte the raato raat crorepati ban gye',
                                          'toh kya keru main mar jahun?',
                                          'my dad had 3315 at that time..its same as this phone..its just that the keypad was of rubber...i used to show off with that phone when i was too young..',
                                          'nokia made in india',
                                          'everybody had nokia in their hand those days literally everbodyy',
                                          'deep inside we all want nokia and blackberry to come back.',
                                          '100 free mentorship! performance enhancing team work! get digital marketing training for beginners to advance level dm start to learn more!',
                                          'now ?',
                                          "apple has a market cap of 2 trillion usd but in 2000 nokia had a market cap of 250 billion usd pls don't post misinformation",
                                          'thats how things work in real world unless until u wont adapt to new things u dont get any thing....',
                                          'not yet end..we have the time..let it back', 'commenting from a nokia',
                                          'they all grew because africa allowed them to grow.they sold more to nigeria.infinix.apple.samsung.u owe us',
                                          'bro it is the king of all weapons and phones anyone could kill just by throwing it',
                                          'bhai toh itni hairaan hone ki koi baat nahi hai.sabhi ek initial stage se start karte hai.aur sabka time har samay achcha nahi jata.every time life may not be in a balanced form.',
                                          'legendary brand',
                                          'so next apple will replace the same nokia in cumming days',
                                          'do check out our page and follow if you like the content of the page and keep supporting and following and keep commenting tooo.please'],
                         'applesamsung': ['promode setup', 'mte rdi karla lagerfelda? nani problm pijte k nm',
                                          'apple & samsung are back in court this week for a damages retrial that will determine how much samsung has to pay apple for infringing apple design patents.samsung was found guilty of violating patents back in 2012.apple is asking for a 1 billion award from samsung',
                                          'k tomu u nen co dodat ceskememiky', 'apple vs samsung facts',
                                          'vendido samsung galaxy z fold 3nuevo 256gb de almacenamiento 12gb de ramdesbloqueado de fbrica rd80000todos nuestros equipos incluyen garanta de parte de nosotros cmo tienda y de parte de nuestros provedores!tienda fsica av mximo gomez detrs de utesa plaza vistacenter 2do nivel.!somos prosmartphone si no lo tenemos lo conseguimos! ',
                                          ' smart tv 33.....appstore..70 9.6 120..100.apps ! ! ! apple samsung...se 12.70.remotie...',
                                          "samsung sent out polishing cloth units to samsung users in germany in a bid to mimic apple's new polishing cloth that retails for rs 1900.the only difference samsung shipped these free of any cost...",
                                          'macbook pro bought by this beautiful young lady ', 'price?',
                                          "how tech world is responding to the worldwide pandemic covid19? what are the latest rumors about apple and samsung? let's have a look at our new blog article to discover the news the events and all the next releases! link in bio ",
                                          '!! !!', 'the missing part :p', 'hahahahhahaha',
                                          'interbrand ha lanzado su top 100 de las mejores marcas globales y como no poda ser de otra manera samsung entr en los primeros lugares.este top toma dos aspectos en cuenta; el valor de la marca y su crecimiento anual.teniendo esto en cuenta samsung se ha clasificado en el quinto lugar por tener un valor de 74 billones 74635000000 y un crecimiento del 20 respecto a 2020 siendo este el crecimiento ms grande que samsung ha tenido en los ltimos 10 aos.en palabras de interbrand la visin de samsung es inspirar al mundo y crear el futuro.inspirar al mundo con tecnologas productos y diseo innovadores que enriquecen la vida de las personas y contribuyan a la prosperidad social creando un nuevo futuro.si tienes duda justo arriba de samsung qued google y abajo qued cocacola.samsung es la mejor y ms grande marca asitica es decir descartando las 4 marcas enteramente estadounidenses que estan arriba.fuente: interbrand ',
                                          'sou time windows at o final! qual desses voc prefere? fala pra mim nos comentrios ',
                                          'microsoft',
                                          'samsung born processingturn on post notifications to get latest updates.india ',
                                          'please follow back', 'ma se la samsung nata prima di apple...',
                                          "apple iphone 13 locked carrier subscriptionprice:34.54month for 24 monthsor 829.00 & free shippingcolors: all availablesizes: 128 gb 256 gb 512 gblink in bio to place an order this item will be released on september 24 2021.preorder now.you'll be charged for items including any digital subscriptions when they ship.ships from and sold by amazon.com ",
                                          'huge football fan buys his iphone 11 pro max now he can watch his matches live and in high quality ',
                                          "what's the price", 'cost plz', 'whats the price?',
                                          '.samsung galaxy s22 ultra.: : ',
                                          'galaxy s21 x iphone 12.kter se vm po designov strnce lb vc? ',
                                          'za m urit samsung.', 'za m galaxy s21', 'samsung',
                                          'vak ten samsung vypada jak kus hovna', 'jedin', 'iphone 12',
                                          'samsung.to je jasne', 'rose gold is her thing got her iphone 6splus from ',
                                          'good morning what is the price for this phone?', 'cost', 'cost?',
                                          "what's the cost for this 6plus and the 7 please?", 'cost plzz',
                                          'samsung or apple?? follow for daily post!!ph.', 'apple', '.both',
                                          'apple palese', 'samsung galaxy pill and ipill'], 'applemeta': [
            'cell phone stand fully foldable adjustable sturdy aluminum alloy desk phone holder with stable antislip designprice: 7.99all colors are available.liberate your handsangle & height adjustablesturdy & antislipmini &fully foldable userfriendly designflat 50 off coupon: link in bio ',
            'pink gaming chair with footrest ergonomic pu leather computer chair for office large size racing style with lumbar supportprice:\t159.99save an extra 5 when you apply coupon using link below.click link in bio to buy now: colors: black golden red white and gray also available.best choice for gaminghigh quality & safe materialmulti functionextra large for comfortexcellent aftersales servicesave an extra 5 when you apply coupons using the link below..inglife ',
            'msi nvidia geforce rtx 2060 graphics card 6 gb gddr6price: 700.57 limited time offerlink in highlights.apply coupon at checkout.msi afterburner torx fan 2.0 oc performance nvidia gsync dual fan thermal design solid backplate geforce rtx vr ',
            "apple iphone 13 locked carrier subscriptionprice:34.54month for 24 monthsor 829.00 & free shippingcolors: all availablesizes: 128 gb 256 gb 512 gblink in bio to place an order this item will be released on september 24 2021.preorder now.you'll be charged for items including any digital subscriptions when they ship.ships from and sold by amazon.com ",
            "kitchen mama electric can openeropen your cans with a simple push of buttonno sharp edge foodsafe and battery operated handheld can openerprice: 28.99you save:\t6.01 17 offopens cans in 3 easy stepsthe last electric can opener you'll needeasy operationsafety designuserfriendly ergonomic designenjoy the best cooking experiencecolors: 4 colors available.buy now with discount link in bio.",
            'apple iphone 13 mini 128gb 256gb 512gb all colors locked carrier subscriptionprice: usd 729.00 & free shipping usclick the link in bio to place your order asap:.',
            'baby monitor with camera and audio 1080p night vision motion link available in profile highlights advanced 1080p full hd night vision 1080p full hd live streaming of nooie baby monitor helps monitor your baby from anywhere in realtime by using your mobile device.with builtin 850nm ir leds you can see everything clearly in the dark without disturbance.so you can 247 keep an eye on your baby.clear twoway audio equipped with highsensitivity and antinoise microphone and speaker for clear twoway audio conversations nooie video baby monitor allows you to talk back promptly to soothe the crying baby.it also works with alexa you can ask alexa to show your baby room or anywhere else that has nooie video baby monitor.smart detection nooie baby home security camera can automatically record a video clip when motion baby crying or abnormal sound is detected.meanwhile notifications will be sent to your phone immediately to ensure house security.flexible storage ways nooie indoor camera supports up to class 6 micro sd card 4128g and cloud storage.with no limitation for storage the cloud will save large videos and keep them safe from loss and damage.you will no longer worry about losing data.excellent user experience the installation and configuration are so easy.nooie wifi baby monitor can be easily mounted on your wall ceiling or table.with app nooie you can share the baby happy moment with family members so everyone can have access to its live stream and video recordings.'],
                         'ios': [
                             'fortnite regresar a ios mediante geforce nowregistrate en: https:www.nvidia.comenusgeforcenowfortnitemobile una vez que te registres podrs tener la oportunidad de probar la beta cerrada tambin disponible para android la prxima semana.ms informacin: https:blogs.nvidia.comblog20220113geforcenowfortniteclosedbeta.',
                             ".la cassa in alluminio leggera e realizzata con una speciale lega usata anche nellindustria aerospaziale e riciclata al100.lo sportloop realizzato con un tessuto in nylon a doppio strato morbido e traspirante eha una pratica chiusura regolabile hookandloop.ildisplay retina alwayson pi grandedi sempre; i modelli series7 hanno undisplay il20 pi spaziosorispetto aimodelli series6.a prova di polvere e nuotate con il cristallo anteriore pi resistente di sempre.ricarica fino al33 pi velocerispetto aimodelli series6.misura illivello diossigeno nelsangue con unsensore e unapp evoluti per avere unidea del tuo benessere complessivo.vieni a scoprire l'offertastraordinaria di questo apple watch da millennium bug via conte piromallo 28bis san sebastiano al vesuvio",
                             '.wowclub.ua...',
                             'enquanto o processo entre a epic games e a apple no chega a uma concluso e os jogadores de mobile continuam presos na temporada 4 do captulo 2 de fortnite a epic e a nvidia anunciaram um contorno dessa deciso na forma de anunciar o novo servio por nuvem.o fortnite retornar assim ao mobile atravs do geforce now sendo o ios no safari e o android no aplicativo.uma verso beta fechada por tempo limitado ser lanada na prxima semana e haver suporte para controles de toque na tela.ser que agora que milhes de jogadores voltam? ',
                             'iphone 13 pro delivered ', 'fone bluetooth 5.0 air pro android e ios !!! ! ! !!! o o ',
                             'download now this app click our bio link...',
                             'les cuento que cuando hice este delineado grfico ni yo me lo crea obviamente falta ms pulir y lo aprend de la miss...para los que no saben: estoy en un perfeccionamiento junto a un premio que lo estoy aprovechando al mil y que tuve la oportunidad de ganrmelo gracias tambin a en el y les cuento esto porque nunca es tarde para aprender perfeccionarnos y estar al da en tendencias no se estanquen y sigan cumpliendo metas espero les guste este arte ',
                             'wow send pic on.of.hairs',
                             "higher data speed in the data & technology driven world 5g technology has created all kinds of buzz amongst people of all ages.fifthgeneration wireless 5g is the latest iteration of cellular technology engineered to greatly increase the speed and responsiveness of wireless networks.there has been a positive impact in the information technology sector because of the 5th generation technology.the impact of 5g on android and ios applications: mentioned link is the detailed explanation of it's impact on mobile applications.",
                             'from kwgt 15 icon pack ',
                             ' 1...official.giveaways2022.official.giveaways20223 5 photos 4 15 5.',
                             'microsoft solitaire is a card game included in various installs of the microsoft windows operating system.it is among the top 3 most used applications for the os.solitaire has been included in windows releases since windows 3.0 in 1990.the game was intended to ease new users into both the graphic user interface of windows as well as teach them the valuable drag and drop action on a mouse.programmed by then intern wes cherry he had also included the ability to switch quickly to a fake excel spreadsheet using a feature called the boss key implying the player was wasting time on a work computer.this feature was ultimately removed from release.the card art was created by famed graphic designer susan kare best known for her expertise in interface and typeface and a pioneer of early gui on macintosh systems.since the release of microsoft windows 8 microsoft has bundled solitaire with several other similar card games as the microsoft solitaire collection.the collection is also available on windows phone and android.',
                             'i spent more time playing microsoft solitaire than im willing to admit',
                             "because we had nothing else to do back then.full sized computers didn't have modems nor did we have internet at that time",
                             "woahh i didn't know it was meant as a subtle way to teach windows ui.i used solitaire to teach my mom how to drag and drop on our windows 95 pc",
                             'iphone 11 64gb 88 89 90 94 ', 'send pic on',
                             'welcome to the new series on ios interview preparation.in this video we have discussed memory management in ios with real time examples.will understand when unowned can lead to crash and also a common interview problem.do like comment and subscribe the channel and motivate us to bring more and more content for you.https:www.youtube.comwatch?vlzl9hmovjg ',
                             'j atualizou o seu iphone?clique para mais contedo.', 'amazing',
                             'mini pekka so cute my personal information:yt: cookiemario111twitch: cookiemario111twitter: cookiemario111snapchat: cookiemario111facebook: cookiemario111reddit: ucookiemario111discord: cookiemario111 2651tik tok: imcookiemario follow my accounts: like my posts use my hashtag: comment on my post hashtags that apparently will get me clout n views: ',
                             "........there isn't anyone who says that in brawl", 'in brawl stars grom says pancake',
                             "plot twist: that grom is you coz you can't hear pancakes from enemy team",
                             'foldable gmail navigation ui in kotlin...today i tried to replicate gmail navigation with kotlin on foldable phone..save post for later inspiration...',
                             'flutter or kotlin for android?', 'wow nice you have strong technical skills i believe',
                             'good',
                             "sir kindly check my instagram account you will find lot's of useful programming related information...",
                             'jetpack compose?', 'buat kayak gini bang',
                             'it is java or some other programming language ??.codes', ' ! ! !', 'awliii', 'ali bod',
                             '32 my first birthday as a mama of three.it is the most content fulfilled and settled i have ever been i always knew my 30s were going to be my best years.i have a few grey hairs im definitely more tired than ive ever been the wrinkles around my eyes are getting deeper and im in bed for 8pm most nights but i truly appreciate the small things and bask in simple moments as i know how fast time flies by.today i am spending the day with my three wildlings and my four hairy babies we have eaten homemade cake for breakfast we are going on our favourite dog walk and finishing the day with a party tea',
                             'goooood got rid of the wolves kit.plymouth is more acceptable...happy birthday',
                             'happy birthday x', 'happy birthday', 'have a super day',
                             'happy birthday sounds a lovely day!', 'happy birthday!', 'happy birthday gorgeous mama',
                             'happy birthday to you xx', 'happy birthdayyy', 'happy birthday you big vegan!',
                             'happy birthday!!! hope you have a beautiful day xxx', 'happy birthday samaya',
                             'happy birthday xxxxxxx', 'gorgeous.happy birthday xxx', 'happy birthday lovely',
                             'happy birthday! have a lovely day.xx'],
                         'appleios': ['i plan on being here all day and all night.what about you? ',
                                      'managing data security in the publishing industry learn more : https:www.gcst.aemanagingdatasecurityinthepublishingindustry ',
                                      'apple releases ios 15.2.1 update ',
                                      'what if we had time machine on the iphone like we have on the mac? would you like to see that for instance in ios 16?',
                                      'iphone16promax',
                                      'iphone se 2022: neuer designleak sorgt fr kuriose berraschung im neuen jahr :j.mp3ew1gkk',
                                      'which one do you prefer for better experience....follow...',
                                      'now all of you with iphones can get some too.join the revolution and get your bitcoin legend free today!link in bio ',
                                      'na desenvolvemos aplicaes mveis para os sistemas operativos apple ios e google android.a nossa equipa dispe de um design profissional com funcionalidades distintas: push notifications marcaes vendas encomendas e muito mais! fale connosco para uma soluo 100 mobile ou uma soluo integrada web mobile.no tem desculpas para no estar sempre perto dos seus clientes!...',
                                      'send pic on', 'ios 16 iphone iphone 6s iphone 6s plus iphone se..2 ',
                                      'get ready for romance with the valentines day icon pack! order now in the never doubt designs shop! link in bio https:www.etsy.comlisting937020618valentinesdayromanticiphoneiconpack?refshophomeactive1 ',
                                      "it's time for lottie animations on apple watchos software engineer and ios wizard evandro hoffmann has put together a blog to help you do just that.learn how at lottiefiles.comblog ",
                                      'your content is exceptional! it needs to be seen by more people i can help you with it.please check out the link in my bio for more details',
                                      'fabulous', 'which version of watchos and apple watch is required?',
                                      'iphone x unlockedprice details;ukusedx 64gb 170kx 256gb 185kx 256gb packed 190ksend a dm to place an order............',
                                      " blackpink series beginner art'sillustrationxo strictly no repost without credits ",
                                      'iphone13promaxvss21ultra5g 21 13 :.3 1 :0195238128809371342444s21ultra ',
                                      'do you think your device will support ios 15 ? and i am surprised that apple still offers ios 15 support for the iphone 6s and 1st generation iphone se! i think a lot of people will be happy with that! follow follow follow ',
                                      "dont be suprised.apple want all the apple's users have the same not like samsung that dont support the new android to the oldest devices",
                                      'literally 6s', 'iphone 6',
                                      'do not update ios 14 has already ruined the performance in xr',
                                      'its not surprising that ios 15 support goes all the way back to the a9.ios 12 expanded support for quite a while too!',
                                      'yea my broken iphone se 1st gen does',
                                      'yeah my iphone 7 is not gonna survive that',
                                      'didnt they stop supporting iphone 6 and below ? how come theyre getting the ios 15 update',
                                      'because it should be iphone 7 and 7 iphone 12 that supports the ios 15',
                                      'iam use it iphone 6s', 'can you send for iran?', 'this is sick',
                                      'when is it coming out', 'boring look',
                                      'i have iphone se 2nd generation and im on ios 14.6 so when do i get ios 15?',
                                      'iphone15promax',
                                      'which iphone do you own and are you going to update to ios 15 once its being released? unfortunately we have to say goodbye to the iphone 6s and the first generation iphone se! but its still amazing to see that apple supports the iphone 7 from 5 years agovia : : ',
                                      'iphone 12s and 12s pro don come out?', 'what if the xsmax', 'i dont see it here',
                                      'ip6 users hw market??', 'iphone 12 pro max',
                                      'the 6s and original iphone se would be getting the ios 15 when its officially released to the public by the fall',
                                      'i need iphone x', 'i have he ios 15 already', 'thanks for sharing.credits: ???',
                                      'iphone xr', '12 pro max', 'how bout iphone 7plus', 'iphone se6s6s plus',
                                      'get your phone cases here', 'i phone 8...',
                                      'iphone 6s and iphone se 1st gen.are ios 15 supported devices too.this is inaccurate.',
                                      'i have a 6s plus', '6s no ?', 'iphone 11 pro max',
                                      'thank god the iphone 7 supports the ios 15 update i want to explore it but it wouldnt be as better as the x series upwards.',
                                      'battle of the mobile os.by.infographia indiawith android running on 73 smartphones globally it is hard to believe it started its journey just over a decade ago.one of the main drivers of this gain in market share is open source nature of the os.this decision made it quite popular among third party phone makers who could add their own flavour and touch to the os and offer unique features to its customers.what do you think drove the success? share your views in the comment section below!....',
                                      "isn't it samsung android the sams thing?",
                                      "i'm just a geologist who expected a diagram of a subduction zone.kinda disappointed.",
                                      'imagine saying youre poor for having samsung samsung and apple cost the exact same ahahaha.and funny thing about it is usually people with more money own an android its usually teens with apple phones.',
                                      'ive been using iphone for years and considering switching switching to a samsung galaxy s20 please tell me why i should not do so',
                                      "the only people who use apple is wannabe richtrendy teenager relatable celebrity and the guy who's first smartphone was a iphone6 and never tried ios bc it was too confusing.",
                                      'am i the only person that thought the chart was over a one month period lmao from september to october',
                                      'darn apple makin a comeback', 'i have both an apple and an android',
                                      'lol imagine having green bubbles.', 'esto lo estuvimos hablando ayer',
                                      'them: capitalism breeds innovation', 'is samsung not android', 'yeah duopolies',
                                      'people still make fun of apple users?',
                                      'i need an ios phone whos not produced by a obnoxious company.',
                                      'man i remember having my java phone.shit was wild', 'and it still lags as hell',
                                      'the fuck is symbian who had that',
                                      'every butthurt android user who hates on apple for no reason just wants an iphone in secret normal people just buy what they want without arguing in comment sections like a bunch of losers',
                                      'android empire!', 'must download if you can! ', 'yess i will',
                                      'is my phone gonna start acting up?', 'faceid with mask',
                                      'my iphone is running on ios 14.6 beta 1 already', 'im downloading mine now',
                                      'cant update apple watch 3 cox 2.9gb free space left while update needs 3gb and update file is 609mb.',
                                      'beta 14.6 is out too', 'available in indonesia',
                                      'some are saying that battery drain has increased after this update.plz clarify ?? am using 12pro',
                                      'no bro its 2.3 gh', 'phone unlock with mask isnt working',
                                      'downloaded and its a good one', 'i also have an update for 14.6 beta version',
                                      'hey if we lock whatsapp via faceid it doesnt work similarly the other pay apps which are locked by face id this unlock doesnt work any resolution ??',
                                      'i6 lol', 'buatla ip6',
                                      'this is worth it simply for the unlock with watch with the mask.1110 recommend.',
                                      'was excited but now upset my apple watch series 2 cant get os 7 so i cant use the unlock my phone through watch',
                                      'some last minute rumors indicate that there will be major updates to these apps in ios 15! my guess is that especially imessage will come with some huge changes! what are your thoughts? ',
                                      'when?!!!!!', 'want come', 'when is ios 15 getting released',
                                      'the phone app needs a major major update.it sucks!! the phone app on an android is faaar better',
                                      'more interested in maps then everything else tbh.i can care less bout that.cant wait till the wwdc to see the announcement',
                                      'new redesign ? ahh shit here we go again', 'what release date?',
                                      'they need to update the calculator app so we can see the histoyprevious math imputed to save time.',
                                      'big sir icons would be sick', 'looks like android',
                                      'can we just get a redesign?', 'waiting for ios 15 date',
                                      'normally there will be street view in apple plans because i saw a car with a big camera on top written apple plans',
                                      'we need different kinds of fonts!!',
                                      "well ios 15 isn't that great now...not many new things", 'fake',
                                      'yes i got updated to 15 and it changed my notifications and many more look good',
                                      'who would like to see widgets in ios 14?source: ',
                                      'better would be choose ur options for the long press',
                                      'well android has this since years almost decades', 'football scores',
                                      'id rather see an iphone like that', '.kuhaku', 'tweak ?',
                                      'only if they would actually do this we all no this not happening',
                                      'a calendar widget please.thx!', 'windows?',
                                      'i feel like ocd brains would complain why it isnt perfectly symmetrical', 'gyor',
                                      'yessssss',
                                      'so basically apple is admitting that android was right.apple sheep really quiet tho',
                                      'download 1weather app for best weather widgets and radar forecast for your location worldwide! link in bio description',
                                      'wallpaper ?', 'how do you make the apps long ways anyone know ???',
                                      'totally love this! check out our app too! link in bio!',
                                      'check out our widget! your diy coach and therapist at your service.put our beautiful pictures on your home screen and be smarter before breakfast with our snippet science readings! https:apps.apple.comusapplifediytherapycoachingid1518619206',
                                      'how do i organize my posts? so i simply use the to do application on the iphone and i classify the things to do from the most important to the least important which also allows me to add dates if i have collaborations not to not be late in the photos.and you how do you organize yourself?follow for more shooting by me and retouch on lightroom like comment share !! check my friends :.it.it.0 tags ',
                                      'great man!! always be organized', 'you should try out notion!', 'same here',
                                      'staying organized! i have a few list like this myself for work and home.having it on my phone of course makes it 100x easier',
                                      'i use things 3', 'awesome',
                                      "wow dude you're very organised i only write down my ideas in the notion app but i don't plan my shots at all",
                                      'this is the best way', 'nice', 'so clean this to do', 'great',
                                      'organization is key', 'cest vrai que je dois commencer faire a',
                                      'good job adrien', 'i use the notion too', 'i use notion!',
                                      'i just use the notes app from apple and the reminder to do app to organize its really easy and already on your iphone',
                                      'great shot', 'cool post brother..good read.love the organization',
                                      'i also do the same thing helps keep you productive always',
                                      'yess i organize it on ig directly', 'great application'],
                         'faceid': ['iphone 7 plus iphone 7 plus ram replacement ',
                                    'ninguem merece ter que ficar digitando senha toda hora s porque o face id no te identifica com mscara no ?chegamos para solucionar o problema!faa e depois conta aqui se funcionou!! ',
                                    'que massa! consegui!!!', 'cmera trmica infravermelha mijing ',
                                    'problemas con el face id de tu iphone ? nosotros lo reparamos en 2 horas nunca paramos de aprender happy phone desde el 2009no permitas que daen ms tu iphone recibimos equipos de todo el os',
                                    'sin enredos ni roturas ya puedes tener el cable cargador que estabas buscando para tu iphone o ipad conector metlico de bajo perfil fcil de conectar.hecho de resistente acero inoxidable longitud de 1 metro.acrcate a nuestra tienda en el cc san ignacio nivel jardn sector las vegas de lunes a sbados en horario comprendido entre las 10:00am y las 5:30pm.contctanos al dm o a los telfonos58212740.053858412962.29.75.',
                                    'reparation af faceid er ikke muligt tro om igen by rme ',
                                    'original qianli lt1 isolated power supply dc ammeter diagnostic instrument ps on interface fast charge fast boot power meterhttps:www.aliexpress.comitem1005003781224811.html?spm5261.productmanageonline.0.0.18a64edff76gmufor professional mobile tools please contact :wechat: whatsapp:86 159 1988 3211aliexpress store :https:www.aliexpress.comstore911609502?spma2g0o.detail.1000061.1.69e4617fmt8hlr',
                                    'sugon products get stock for professional mobile tools please contact :wechat: whatsapp:86 159 1988 3211aliexpress store :https:www.aliexpress.comstore911609502?spma2g0o.detail.1000061.1.69e4617fmt8hlr',
                                    ' : 350 : www.gsmparseh.com 02188677156 5 : https:t.megsmparseh :.parseh :.parseh.repair ',
                                    "leaks of iphone 14.follow for more amazing content checkout the link in bi0.don't miss the highlightsturn on post and story notification.any queries?leave a comment belowlike comment share and save thepost.make sure to follow for moredon't repost without permission.ignore hashtags ",
                                    'goodbye notch iphone 14 series to use a special pillshaped front camera design....via : angelolibre design..........',
                                    "and now they are gonna state it as some extraordinary thing that has hasn't been done before",
                                    'look like huawei mate 40 notch', 'youtube channel',
                                    'single epik high face id ft.giriboy sikk justhisartwork.n.no',
                                    'iphone xr.by.30...:.by :..29 1 375336688880 43 375293938880 79 375291627564.whatsapp telegram viber ',
                                    ' mac macbook apple 13',
                                    'funniestunique comments will be pinned source: gadgets.ndtv.coma team of indian researchers has developed what appears to be a firstofakind human authentication through teeth for mobile and other handheld devices.the team says that the app acquires biometric samples using the camera on a mobile handset.the app has specific markers that register the teeth of a human for authentication similar to existing apps that record the entire face.the name of the study is deepteeth: a teethphoto based human authentication system for mobile and handheld devices.it has been authored by geetika arora rohit k bharadwaj and kamlesh tiwari from the birla institute of technology and science bits pilani....follow.......',
                                    'toh brush kare ki na kare?',
                                    'chor mobile toh chori krega hi....saath me battisi bhi tod ke lejaaega',
                                    "so if i don't brush my teeth and it gets dirty i can't unlock my phone?",
                                    'agar bhai nakli battisi ho toh',
                                    'colgate 20 ultra white 8256 gb most sequre phone in the world',
                                    'secondo voi arriver finalmente questo fantomatico design squadrato col prossimo applewatch? ',
                                    'i dont know what to think but i really do like the series 7 design that watch face looks great too',
                                    'c un modo per avere questa watchface su un watch non nike?',
                                    'su apple watch non lo vedo bene', '202122 !!! !!!', '..!!!',
                                    ' iphone 11promax face id fixed..sh1..0383227969103832279692 : :..sh1 ',
                                    ' iphone x ', 'ios o android? ', 'harmonyos! ovviamente ios matt! buona domenica!',
                                    'lo sfondo pls?', 'ovviamente ios matteo a me non dovresti neanche chiedere',
                                    'entrambi hanno i loro pregi e i loro difetti.obiettivamente con android puoi fare molte pi cose che ios non permette di fare.io comunque ho scelto e scelgo ios nonostante tutto',
                                    'non saprei scegliere.con ios hai caratteristiche che android non ha e viceversa',
                                    'windows phone for life', 'ios tutta la vita', 'ios easy',
                                    'da quando sono passato ad ios non riesco pi a tornare ad android mi fa quasi ribrezzo',
                                    'ios a vita', 'iossssss',
                                    'ogni tot.mesi faccio avanti e indietro ma ultimamente ho deciso di tenere iphone dato che con qualsiasi android mi mangio decine di notifiche specialmente s21 che considero un buco nellacqua allucinante impossibile usarlo per lavorare.parlo per me che ricevo centinaia se non migliaia di notifiche discord al giorno',
                                    'ios!! design and functionality ;d', 'great',
                                    'ios all day.longevity with the updates & if you dont get a google pixel then you have to wait for the updates.',
                                    'wallpaper name?'],
                         'applestore': [' xr 64 coral', ' xr 64 red ibox', ' 11 64 purple', ' 11 pro 256 gold',
                                        '12012022 7 32 gold', ' 11 64 green', '12012022 xr 64 black minus face id eror',
                                        ' 8 256 gray', ' 11 pm 64 gold', ' : : : : original', 'promote it on',
                                        'cliente retirando o seu iphone 13 pro max 128gb dourado lacrado em loja e garantindo o seu brinde carregador capa e pelcula.es o',
                                        "i am back and finally joined the apple club! it's been over a week and i still can't use instagram on my samsung.but magic apple did the trick.now that i have a new phone instagram works flawlessly.we'll see how it goes.being in czech republic for over a month i couldn't buy an iphone anywhere here.they are simply not available here and probably won't be soon.i think the main problem is that there is no official apple store in czech republic.so i had to try my luck in germany and it didn't disappoint.not only it was a great trip but i got a new phone! stay tuned for a new content ",
                                        'welcome to the club buddy', 'missed your contents bro welcome back',
                                        "apple store covent garden london 2022throughout the coming year i plan to make alot of work.there are moments in your creative life when you have the space energy time and little bit of spare cash to devote yourself to making new work.following on from the wonderful surprise of some of my archive becoming the book memory lane at the end of last year it became apparent that maybe i wasn't completely over photography.it had just faded into the background a little as i found it increasingly difficult to make a living out of my photography and moved into video around 2007.some of the new work is going to be a continuation of my first outings in medium format colour shooting on a rolleiflex or plaubel makina and some is going to be about embracing full the possibilities of digital most notably the ability to shoot alot of images and to shoot in low light very low light.i am also going to have a play around with large format portraiture and still life even shooting in black and white.the journey ahead is exciting.i thank everyone for their ongoing support when instagram allows me to reach you and please sign up on my website to receive updates.the new site will be live by early february with project new and old shown in a more pleasing layout than an instagram feed.",
                                        'looking forward',
                                        'excited to see what you capture and put me down for whatever book they make it into in the future memory card lane?',
                                        'good luck with all that.', "that's a great read martin",
                                        'great shot i look forward to seeing more!',
                                        'posie militanteou de lart de lart de ravaler les faades par camera : zeiss ikon zmlens : voigtlander ultron 28mm vintage linefilm : chemistry : bergger pmk 24c 13mn berfix neutralscanner : plustek opticfilm 8200i seref : 20220101 ',
                                        'amazing shot', "jolie! j'aime beaucoup!!", 'excellente !',
                                        'passemuraillecamera : zeiss ikon zmlens : voigtlander nokton 50mm f1.5film : chemistry : bergger pmk 23c 14mn30s berfix neutralscanner : plustek opticfilm 8200i seref : 20211208 ',
                                        'magique', 'superbe phoro jc',
                                        'bravo jc encore une trs belle atmosphre que tu as capt avec brio !!!',
                                        '..? 2022 ! ! happy new year! 7 ', ' ?whyamicrying', '....',
                                        'charging up all of my essential devices with one single wireless charger by...',
                                        'wonderful mate', 'very practical', 'great shot buddy', 'amazing shot brother!',
                                        'such a cool charger!', 'love this!', 'awesome product and looks practical',
                                        'cool shot bro', 'dope shot and great charger!', 'nice charger', 'great man',
                                        'nice shot',
                                        'remembered apple airpower? this accessories reminds me that cool stuff',
                                        'sick shot dude love it!!',
                                        'i really like te lighting on this.it has this faded look but it looks good for this type of photo!',
                                        'another banger!', 'wallpaper by.??',
                                        'whats the case or bumper on your apple watch?', 'great',
                                        'love the ampere products great shot here parth!', 'perfect',
                                        'camera : zeiss ikon zmlens : voigtlander nokton 50mm f1.5film : chemistry : bergger pmk 23c 14mn30s berfix neutralscanner : plustek opticfilm 8200i seref : 20211208 ',
                                        'amazing mood', 'exquisite scene', 'great capture', 'superbe', 'beautiful',
                                        'superbe ambiance!', 'jolie scne!', 'great mood my friend', 'brutal',
                                        'really like this like the old walking away from the new',
                                        'this look deserves an applause', 'extra ordinary shot', 'just stunning']}

    cleaned_comments.update(cleaned_comments2)
    cleaned_comments.update(cleaned_comments3)
    cleaned_comments.update(cleaned_comments4)
    cleaned_comments.update(cleaned_comments5)

    comments = []
    for i in cleaned_comments.values():
        comments += i

    comments = list(set(comments))

    with open('labeled_comments.pkl', 'ab') as f:
        dump(comments, f)

    print(len(comments))

# one()
# two()
three()
