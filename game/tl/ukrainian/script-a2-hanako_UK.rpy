label uk_H2:

scene bg school_miyagi
show hanako emb_downsmile_close
with None

play sound sfx_doorknock2

show hanako emb_timid_close
with charachange

"Поки ми розставляємо фігури, біля дверей чути шум."

play sound sfx_dooropen

show bg school_miyagi at bgright
show hanako emb_timid_close at tworight
with charamove

show lilly basic_smileclosed at twoleft
with charaenter

li "Доброго дня."

play music music_lilly fadein 4.0

show hanako emb_emb_close
with charachange

ha "Ліллі…"

hi "О, привіт, Ліллі. Ти вже закінчила?"

show lilly basic_smile at twoleft
with charachange

li "Ви обоє тут? Чудово. У будь-якому разі, нашому вчителю вдалося знайти додаткову допомогу, тож я змогла піти. Ви тут відтоді, як пішли?"

hi "Майже, ми просто трохи грали в шахи."

show hanako emb_smile_close
with charachange

ha "Б-бажаєш чаю?"

show lilly basic_weaksmile at twoleft
with charachange

li "Насправді, я думаю, було б непогано трохи прогулятися надворі…"

show hanako def_worry_close
with charachange

"Мить, коли обличчя Ханако спохмурніло, показує її незгоду з цим планом, хоча вона нічого не каже."

"Я відчуваю дивне бажання озвучити те, що чітко написано на її обличчі, але Ліллі цього не бачить."

hi "Я… я думаю, нам варто залишитися тут…"

show lilly basic_surprised at twoleft
with charachange

li "Справді? Тут так людно, що я подумала, нам варто покинути школу і піти до місцевої чайної."

show hanako emb_blushtimid_close
with charachange

ha "Ти маєш на увазі «Шанхай»?"

show lilly basic_smileclosed
with charachange

li "Звісно; оскільки всі на фестивалі, там має бути майже порожньо."

hi "Чайна?"

show lilly basic_weaksmile
with charachange

li "О, точно, ти, мабуть, про неї не знаєш."

show lilly basic_smile
with charachange

li "Неподалік звідси є чайна, куди ми час від часу заходимо."

hi "Звучить як план. Ханако, що ти думаєш?"

show hanako defarms_shock_close
with Dissolve(0.2)

show hanako def_worry_close
with charachange

"Ханако трохи здригається від того, що її втягнули в розмову, але, принаймні, вона здається менш засмученою, ніж раніше."

show hanako cover_bashful_close
with charachange

ha "Якщо… якщо це «Шанхай», думаю, буде непогано."

show lilly basic_planned
with charachange

li "Ну що ж, вирішено. Ходімо."

show hanako basic_bashful
with charadistant

"Ханако і я підводимося з-за столу, перервавши нашу партію в шахи."

"Перш ніж я встигаю щось зробити, Ханако зсипає фігури в невеликий контейнер і прибирає дошку."

hi "Схоже, ми готові. Будь ласка, веди."

stop music fadeout 8.0

scene bg school_hallway3
with locationchange

show hanako emb_smile at Transform(xanchor=0.5, xpos=0.58)
show lilly basic_smileclosed at Transform(xanchor=0.5, xpos=0.42)
with charaenter

"Ханако підходить до Ліллі, і ми вирушаємо коридорами школи."

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")

play ambient sfx_crowd_outdoors fadein 1.0

scene bg school_gate_ss
with locationskip

"Дівчата ведуть мене через низку незнайомих дверей, і ми опиняємося з того боку будівлі, що протилежний до місця проведення фестивалю."

"Захищений товстими кам'яними стінами будівлі, шум натовпу стих до ледь чутного гулу."

hi "Дивно; я думав, що більшість людей уже почнуть розходитися…"

show hanako emb_downtimid_ss at Transform(xanchor=0.5, xpos=0.58)
show lilly basic_smile_ss at Transform(xanchor=0.5, xpos=0.42)
with charaenter

li "Вони, мабуть, тут, щоб подивитися феєрверк."

hi "Феєрверк?"

show lilly basic_weaksmile_ss
with charachange

li "Так, мабуть, школа влаштовує справжнє шоу. Багато людей приїжджає з міста, щоб подивитися на нього."

"Рішення Ліллі покинути територію школи тепер здається логічним. Ханако, мабуть, було б важко, якби все місто посунуло до школи. Або навпаки, залежно від того, як подивитися."

stop ambient fadeout 7.0
play music music_tranquil fadein 3.0

scene bg school_road_ss
with locationchange

"Вдруге відтоді, як я прибув до Ямаку, я йду цією дорогою з Ліллі."

"Тільки тепер, коли я ледь чую безперервний шум фестивалю, я усвідомлюю, наскільки він був гучним. Я чую, як у мене трохи дзвенить у вухах у тиші вечірнього повітря, поки вони оговтуються від денного навантаження."

show hanako emb_emb_ss at Transform(xanchor=0.5, xpos=0.58)
show lilly basic_smileclosed_ss at Transform(xanchor=0.5, xpos=0.42)
with charaenter

"Ханако тулиться до Ліллі, але все ще примудряється вести її дорогою. Це, а також уникнення випадкових поглядів цікавих перехожих, здається, повністю виснажує її сили."

"Вона рідко піднімає погляд від землі перед собою і не вимовляє ні слова."

"Ліллі, навпаки, зберігає свій стриманий і вихований образ, як і в школі. Очевидно, що вона навмисно докладає зусиль до свого вигляду, а не ховає його, як Ханако."

"Вражає, наскільки вони різні в тому, як тримаються за межами території Ямаку. Тим не менш, в обох випадках очевидно, що вони помітно змінюються."

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

window hide

nvl clear

$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl show dissolve

n "\n\n\nУсередині Ямаку кожен «особливий», що нівелює саму «особливість»."

n "Але як тільки ми виходимо за ворота школи, ми повертаємося до статусу «чужинців» і загальних ярликів."

n "Особливо коли ми все ще у шкільній формі. Це ніби повісити собі на шию табличку, що закликає людей з'ясувати, що з тобою не так."

n "Я здивований, що так багато учнів продовжують її носити. Хоча, з огляду на те, що тростини та інвалідні візки є звичним явищем серед учнів, гадаю, це не такий вже й великий видавець."

n "\nАбо, можливо, я єдиний, хто бачить у цьому стигму? Можливо, з часом до цього звикаєш, як і до будь-якої іншої шкільної форми."

nvl hide dissolve

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear

scene bg suburb_shanghaiext_ss
with locationskip

window show

"Зовні чайна виглядає досить стандартно; звичайна будівля з типовими вивісками, що прикрашають вхід."

"Це виглядає як місце, повз яке пройдеш, не замислюючись, просто ще одне звичайне кафе в морі тисяч інших."

"Якби Ханако не спрямувала Ліллі до входу, я б пішов далі дорогою, навіть не знаючи про її існування."

play sound sfx_storebell

scene bg suburb_shanghaiint at Fullpan(5.0, dir="right")
with locationchange

stop music fadeout 6.0

"Всередині чайна набуває більш традиційного вигляду. Здається, все зроблено з одного шматка дерева: від стійки та лавок до кабінок з високими спинками вздовж стін."

"Але найяскравіша особливість кімнати — це відсутність життя. Здається, я ледь чую, як щось булькає на задньому плані, але в іншому в кімнаті панує тиша."

"Не маючи жодних вказівок, ми просто чекаємо біля входу, ввічливо підкоряючись табличці «Будь ласка, зачекайте, поки вас посадять»."

hi "Е-е, це місце зачинене чи що?"

stop music
play sound sfx_impact2

show yuukoshang panic_up:
    xalign 0.5 yanchor 1.0 ypos 1.5 alpha 0.0
    easein 0.3 ypos 1.0 alpha 1.0
show bg suburb_shanghaiint at right
with vpunch

"Звук стільця, що падає, лунає порожньою кімнатою, і з кабінки вискакує голова."

play music music_comedy fadein 0.5

show yuukoshang neurotic_up:
    ypos 1.0 alpha 1.0
with charachange

yu "Я не спала, ласкаво просимо до «Шанхаю»!"

"Юко, одягнена в пастельний фартух і стискаючи меню, поспішає нас привітати. Її криво надіті окуляри та розпатлане волосся викликають підозру щодо її попередньої заяви."

"Але чи спала вона, чи ні — це не перше питання, що спадає мені на думку."

hi "Ти тепер тут працюєш? А що сталося з бібліотекою?"

show yuukoshang smile_down
with charachange

yu "Що? Ліллі? Хісао?"

show yuukoshang neurotic_up
with charachange

yu "Ласкаво просимо до «Шанхаю»!"

show yuukoshang noglasses_up at Transform(ypos=1.25)
with Dissolvemove(0.2)

play sound sfx_dropglasses

with Pause(0.3)

show yuukoshang noglasses_up at center
with charamove

"Юко, все ще прокидаючись, різко вклоняється, через що її окуляри злітають."

yu "Ой!? Мої окуляри…"

"Поки я піднімаю її окуляри з підлоги, Ліллі пропонує пояснення."

show yuukoshang noglasses_up at tworight
show bg suburb_shanghaiint at center
with charamove

show lilly basic_weaksmile at twoleft
with charaenter

li "Юко працює тут неповний робочий день, так само як і в бібліотеці. Це одна з причин, чому ми любимо сюди приходити."

show yuukoshang neurotic_up
with charachange

"Юко бере окуляри з моїх рук, тремтячи, одягає їх назад."

yu "Так… це правда… дякую…"

show yuukoshang neutral_down
with charachange

yu "Мені провести вас до вашого столика?"

show yuukoshang worried_up
with charachange

yu "Тут більше нікого немає, тож ви можете обрати столик і замовити все, що забажаєте, але, можливо, доведеться зачекати, бо мені доведеться готувати все самій…"

show lilly basic_smile at twoleft
with charaenter

li "Усе гаразд, Юко. Просто чайник чорного чаю і тарілка сендвічів буде цілком достатньо."

show yuukoshang happy_down
with charachange

yu "Добре! Я зараз же цим займуся!"

hide yuukoshang
with charaexit

show lilly basic_smile at center
show bg suburb_shanghaiint at bgright
with charamove

"Юко поспішає вглиб кафе, залишаючи нас стояти біля входу."

"Вона штовхає двері, що гойдаються, і лише потім усвідомлює, що не провела нас до столика."

yu "Вибачте! Вибачте! Будь ласка, сідайте, де забажаєте! Я зараз повернуся!"

stop music fadeout 3.0

hide lilly
with charaexit

show bg suburb_shanghaiint at bgleft
with charamove

"Слідуючи її пораді, я веду Ліллі до найближчої кабінки, а Ханако йде за нами."

show lilly basic_smileclosed:
    twoleft
    ease 1.0 ypos 1.2
show hanako basic_normal:
    tworight
    ease 1.0 ypos 1.17
with Dissolve(1.0)

"Коли я починаю сідати поруч із Ліллі, я розумію, наскільки це місце підходить для Ханако."

"Кабінки з високими спинками повністю відокремлюють вас від решти зали, і схоже, що тут не так уже й багато відвідувачів."

"Усі меблі, від подушок на лавках до підставок для спецій, виглядають застарілими, але не надто зношеними."

"Цікаво, чи Ліллі навмисно обирає такі місця, щоб приводити сюди Ханако? Вона здається людиною, яка готова докласти зусиль, щоб врахувати особливі потреби Ханако."

play music music_another fadein 4.0

show lilly basic_weaksmile:
    ypos 1.2
with charachange

li "Отже, Хісао, я не знала, що ти граєш у шахи…"

hi "Ну, не дуже добре, але я знаю, як грати."

show lilly basic_smile
with charachange

li "Гадаю, тепер очевидне питання… хто переміг?"

"Безневинна посмішка Ліллі змушує мене вагатися. Я не хочу виглядати так, ніби хизуюся своєю перемогою над Ханако."

show hanako cover_bashful:
    ypos 1.17
with charachange

ha "Х-Хісао."

hi "Так… але, е-е, не з великим відривом…"

"Чорт. Коли вимовляю це вголос, відчуваю, ніби зробив щось жахливе."

show lilly basic_giggle
with charachange

li "Чудова робота, Хісао. Ти досяг того, у чому я завжди зазнавала невдачі."

hi "Ер, дякую. Я не грав уже цілу вічність, тож було приємно зіграти знову."

show hanako basic_smile
with charachange

ha "Т… так… Було."

"Ханако трохи крутить у руках волосся і відводить погляд, відповідаючи, але на її обличчі з'являється ледь помітна посмішка."

"Це трохи сильніша реакція, ніж я очікував, але все одно по-своєму мила, у стилі Ханако."

show hanako defarms_shock at Transform(xpos=0.8)
show lilly basic_surprised at Transform(xpos=0.2)
with Dissolvemove(0.5)

show yuukoshang worried_up at center
with charaenter

"Це трохи застає мене зненацька, і лише катастрофічне повернення Юко змушує мене повернутися до розмови."

hi "Ти в порядку, Юко? Тобі допомогти?"

show yuukoshang neurotic_up
show hanako def_worry
with charachange

yu "Я в порядку, я в порядку, я в порядку. Я повинна зробити це як слід, це моя робота."

show yuukoshang worried_up
with charachange

"На її обличчі відображається концентрація, поки вона вдивляється в тацю у своїх руках, ніби сам погляд на її вміст допоможе втримати все на місці."

show yuukoshang worried_up at centertremble
with charachange

"На жаль, це не дуже допомагає; чашки та блюдця повільно танцюють, час від часу брязкаючи, коли стикаються одне з одним."

show yuukoshang worried_up at Transform(ypos=1.1)
with ease

show yuukoshang worried_up at center
with ease

"Дуже обережно Юко ставить тацю на стіл, ледь не перекинувши її."

show yuukoshang happy_down
with charachange

yu "Ось, бачиш!"

hi "Ер, гарна робота?"

show lilly basic_weaksmile
with charachange

li "Дякую, Юко."

show yuukoshang neutral_down at Transform(ypos=1.2)
with Dissolvemove(0.2)

with Pause(0.2)

show yuukoshang neutral_down at center
with ease

"Голова Юко різко опускається у її фірмовому поклоні, перш ніж вона відповідає."

show yuukoshang closedhappy_down
with charachange

yu "Будь ласка."

show lilly basic_smile
with charachange

li "Ти не хочеш приєднатися до нас? Є ще дещо, що я хотіла б обговорити щодо того нещодавнього замовлення, якщо можна…"

"А, точно. Ліллі та Юко обговорювали купу книг, коли я вперше зустрів Ханако."

"Щось про те, як Ліллі допомагає зі шрифтом Брайля…"

show yuukoshang neurotic_up
with charachange

yu "А… так. Ми ж не встигли їх переглянути, чи не так?"

show yuukoshang neurotic_up at Transform(ypos=1.17)
with charamove

"Юко поспіхом сідає поруч із Ханако."

"Мабуть, її відданість цій роботі триває лише доти, доки вона зосереджена; як тільки концентрація порушується, вона миттєво втрачає контроль."

show yuukoshang smile_down
with charachange

yu "Я буду в бібліотеці завтра вдень, якщо хочете спробувати ще раз…"

show lilly basic_cheerful
with charachange

li "Це звучить чудово, я зустрінуся з тобою там після занять."

show hanako emb_timid
with charachange

ha "Ем… Л-Ліллі…"

show lilly basic_oops
with charachange

li "О боже, точно. Завтра понеділок, як я могла забути?"

"Я починаю відчувати себе трохи осторонь від того, що відбувається. Хоча, з іншого боку, це очікувано; я тут ледь тиждень, тому неможливо знати розклад кожного."

show lilly basic_weaksmile
with charachange

li "Що ж, можливо, ми зможемо домовитися про щось інше."

show lilly basic_smile
with charachange

li "Юко, ти будеш у бібліотеці пізніше цього тижня?"

show yuukoshang worried_up
with charachange

yu "Гм, можливо, але це вже прострочено…"

show hanako emb_downsad
with charachange

ha "І… є деякі… речі, які м-мені потрібні…"

show lilly basic_listen
with charachange

li "Це може бути проблемою…"

"Ліллі замислюється на секунду, перш ніж знаходить відповідь."

show lilly basic_planned
with charachange

li "Цікаво, чи могли б ми залучити допомогу когось іншого, якщо знадобиться…?"

hi "Ем, для чого? Ви мене зовсім заплутали…"

"Бути добровільно втягнутим у щось, навіть не маючи найменшого уявлення, що відбувається — це не зовсім моє."

"А я думав, що нарешті втік від лап Студентської ради та їхніх постійних спроб завербувати мене."

show lilly basic_smileclosed
with charachange

li "О, звісно. Днями я допомагала Юко сортувати нові книги шрифтом Брайля в бібліотеці."

show lilly basic_weaksmile
with charachange

li "Але ми з Ханако зазвичай ходимо за покупками в понеділок після обіду; у цей день тихіше, ніж на вихідних."

li "Минулого тижня ми не змогли піти, бо я була зайнята фестивалем. Мені вдалося вирватися пізніше, але Ханако не змогла."

hi "Ну, оскільки я не вмію читати шрифтом Брайля, я припускаю, ви хочете, щоб я пішов за покупками з Ханако?"

show lilly basic_smile
show hanako emb_timid
with charachange

li "Правильно. Ти дуже допоміг мені днями."

hi "Думаю, я впораюся. Ханако, що ти думаєш?"

show hanako basic_smile
with charachange

ha "Я-якщо ти не проти…"

hi "Звісно, ні. Я все ще не знайомий з усіма магазинами в цьому районі, тож це звучить як гарна ідея."

show hanako basic_bashful
with charachange

ha "Д-добре."

show lilly basic_smileclosed
with charachange

li "Тепер, коли ми домовилися, чи не випити нам чаю?"

"Тільки зараз я усвідомлюю, що наш чай весь цей час стояв без діла і зовсім не став гарячішим."

show yuukoshang panic_up
with charachange

yu "Це моя провина! Дозвольте я наллю вам…"

"Юко простягає руки, що тремтять, але я зупиняю її; вона виглядає не в тому стані, щоб мати справу з гарячими напоями."

hi "Усе гаразд, я сам. Оскільки ти вже приготувала чай і сендвічі, ти виконала свої обов'язки офіціантки, так?"

show yuukoshang neurotic_up
with charachange

yu "Я… гадаю, так."

"Юко трохи розслабляється, але все ще з нетерпінням спостерігає, як я розставляю частування."

stop music fadeout 1.0
play ambient sfx_fireworks

show white
with Dissolve(0.1)

hide white
show fireshine
show hanako defarms_shock
show yuukoshang panic_up
show lilly basic_surprised
with charachange

"Коли я вже збирався відкусити шматочок сендвіча, пролунав низький, гучний гуркіт, а ззовні спалахнуло світло."

show lilly basic_weaksmile
show yuukoshang smile_down
show hanako emb_timid
with charachange

li "А, здається, шоу почалося."

hide fireshine
show bg misc_sky_ni as front
show fireworks
with locationchange

"Тільки тепер, подивившись назовні, я усвідомлюю, що сутінки вже минули, залишивши нас у самому розпалі вечора."

"Іскристі трасери злітають угору, готові вибухнути квітковими візерунками феєрверків."

hide fireworks
hide front
show fireshine
show yuukoshang happy_down
with locationchange

yu "Ходімо подивимось!"

show yuukoshang panic_up
with charachange

yu "Ой… вибач, Ліллі…"

show lilly basic_ara
with charachange

show hanako_fw behind bg:
    zoom 1.05 subpixel True truecenter
    ease 22.0 zoom 1.0
show ev hanako_shanghaiwindow behind hanako_fw:
    zoom 1.05 subpixel True truecenter
    ease 22.0 zoom 1.0
with None

li "Будь ласка, не пропускайте шоу через мене. Наскільки я чула, це непогане місце, щоб на них подивитися."

play music music_serene fadein 4.0

hide fireshine
hide bg
hide hanako
hide lilly
hide yuukoshang
with locationskip

"За винятком Ліллі, ми поспішаємо до вікна маленької чайної, щоб подивитися шоу."

"Відблиски кольорових вогнів грають на усміхнених обличчях Ханако та Юко, і на мить я забуваю подивитися у вікно."

"У цьому зовсім новому світі є кілька речей, які не змінюються."

"Думаю, саме тому школа здіймає стільки галасу навколо цього фестивалю. Це шанс показати, що між усіма нами є спільне."

stop ambient fadeout 3.0

hide hanako_fw
with Dissolve(1.0)

"Шоу закінчилося надто швидко; феєрверки — задоволення дороге, навіть для найбільш забезпечених шкіл."

scene bg suburb_shanghaiint at bgright
with locationchange

"Перш ніж ми повертаємося до чаю та сендвічів, Ханако повертається до мене."

show hanako emb_downsmile_close
with charaenter

ha "Ем, д-дякую за сьогодні."

show hanako emb_smile_close
with charachange

ha "…і за завтра."

hi "Усе гаразд; не думаю, що я зміг би витримати той натовп."

hi "У такі дні набагато приємніше провести час подалі від усіх, як гадаєш?"

show hanako basic_normal_close
with charachange

ha "Т-так."

hi "У будь-якому разі, ми надто довго відкладали цей чай, ходімо назад."

show hanako basic_bashful_close
with charachange

ha "З-звісно."

stop music fadeout 6.0

hide hanako
with charaexit

show bg suburb_shanghaiint at bgleft
with charamove

show lilly basic_smileclosed:
    yanchor 1.0 xanchor 0.5 ypos 1.2 xpos 0.2
show yuukoshang neutral_down:
    yanchor 1.0 xanchor 0.5 ypos 1.17 xpos 0.5
with locationchange

show hanako basic_smile:
    yanchor 1.0 xanchor 0.5 ypos 1.0 xpos 0.8
    easein 1.0 ypos 1.17
with charaenter

"Ми повертаємося до нашого столика і легкої трапези."

show lilly basic_smile
with charachange

li "Це було вражаюче. Принаймні, масштабніше, ніж торік."

show yuukoshang happy_down
with charachange

yu "Так, це було чудово! Я ніколи не бачила, щоб вони влаштовували таке шоу."

yu "З кожним роком стає все краще!"

show lilly basic_weaksmile
with charachange

li "Боюся, проте, що за цей час чай уже охолов."

show yuukoshang panic_up at center
with Dissolvemove(0.2)

play music music_ease fadein 0.5

yu "О ні! Дозвольте мені заварити ще! Це моя провина!"

hi "Заспокойся, Юко, ніхто не винен."

"Я роблю ковток зі своєї чашки, просто щоб довести це."

hi "Цей чай і холодним непоганий. Схоже на холодний чай з льодом."

show yuukoshang worried_up
with charachange

yu "Справді?"

hi "Так, справді. Якщо додати трохи цукру, то навіть смачно."

show yuukoshang neurotic_up
with charachange

yu "Ти впевнений?"

hi "Абсолютно. А тепер чому б тобі не сісти, і ми доп'ємо його разом?"

show yuukoshang smile_down
with charachange

yu "Д-добре."

show yuukoshang smile_down at Transform(ypos=1.17)
with charamove

"Юко не виглядає переконаною, але все одно сідає."

"Вона обережно відміряє близько п'яти чайних ложок цукру і додає їх у свій чай."

hi "Е-е, я сказав трохи цукру…"

show yuukoshang neutral_down
with charachange

yu "Я знаю, але я все одно люблю солодкий чай."

"З цікавістю зазираю в її чашку. Як і очікувалося, цукор майже не розчинився в холодній рідині."

"Вона розмішує його двічі, перш ніж перекинути чашку і випити вміст разом із цукром за один ковток."

show yuukoshang happy_down
with charachange

yu "Ти правий! Це зовсім непогано!"

hi "Е-е, добре…"

"Я озираюся на Ліллі та Ханако, які вже закінчили свою трапезу, поки я спостерігав за тим, як Юко проявляє свій характер."

"Не бажаючи нікого затримувати, я використовую її тактику і випиваю залишки свого чаю одним махом."

hi "Ну що ж, здається, ми всі закінчили."

show lilly basic_smile
with charachange

li "Нам варто йти назад чи хочемо добавки?"

show yuukoshang neurotic_up
with charachange

"Вираз обличчя Юко свідчить про те, що це явно не найкраща ідея."

hi "Думаю, буде краще, якщо ми скоро повернемося."

hi "Зрештою, нам треба встигнути до комендантської години."

show lilly basic_smileclosed
with charachange

li "О, це слушне зауваження."

show lilly basic_smile
with charachange

li "Побачимося завтра, Юко."

show yuukoshang neutral_down
with charachange

yu "Буду чекати на це, Ліллі. До побачення всім."

stop music fadeout 9.0

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_cicadas fadein 0.5

scene bg suburb_shanghaiext_ni
with locationchange

"Ми виходимо з маленької чайної у темряву ночі."

$ renpy.music.set_volume(0.4, 1.0, channel="ambient")
scene bg suburb_roadcenter_ni
with locationchange

"Ліллі та Ханако знову йдуть попереду, але під покровом темряви Ханако здається трохи менш напруженою, ніж під час дороги сюди."

"Ми проходимо повз поодинокі групи людей, що покидають територію школи, але Ханако веде нас другорядними дорогами, уникаючи основного натовпу."

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg school_dormext_full_ni
with locationskip

"Біля гуртожитків у школі дивно тихо, якщо порівняти з денним шумом."

hi "Ну що ж, дякую вам обом за сьогодні. Думаю, я багато чого дізнався."

show hanako emb_timid_ni at Transform(xanchor=0.5, xpos=0.59)
show lilly basic_weaksmile_ni at Transform(xanchor=0.5, xpos=0.41)
with charaenter

li "Завжди будь ласка, але боюся, що мені справді час іти. Сьогодні був довгий день."

"Це точно; Ліллі провела весь день на ногах, і я можу собі уявити, що прогулянка за межами школи для неї досить виснажлива."

"Я відчуваю провину, згадуючи, що, мабуть, був єдиним у школі, хто встав близько десятої ранку."

hi "Звісно."

hi "Ну, побачимося завтра. На добраніч."

show lilly basic_cheerful_ni
with charachange

li "На добраніч, Хісао."

show hanako basic_smile_ni
with charachange

ha "Н… на добраніч."

hide hanako
hide lilly
with charaexit

"Дівчата повертаються до свого гуртожитку, а я — до свого."

"Насправді, якщо подумати, сьогоднішній день виснажив і мене."

stop ambient fadeout 2.0

scene black
with dissolve


return
label uk_H3:

window hide None

scene black
with dissolve

$ renpy.music.set_volume(0.0, 0.0, channel="ambient")
play sound sfx_alarmclock

with Pause(1.2)

play sound sfx_impact2

window show

"Мій будильник реве мені у вуха, але я швидко змушую його замовкнути одним ударом кулака."

scene bg school_dormhisao
with openeye

"Моє тіло перемикається в автоматичний режим, витягуючи мою підсвідомість з ліжка і вдягаючи в шкільну форму."

"Як завжди, мої пляшечки з таблетками терпляче стоять на столі, чекаючи, поки я візьму їх і відміряю свою денну дозу ліків; сімнадцять таблеток на день."

scene bg school_scienceroom at bgright
with locationskip

"Не встиг я озирнутися, як уже відчиняю двері до класу 3-3, радіючи, що не я один маю такий вигляд після фестивального тижня."

"Кожне обличчя в класі виглядає виснаженим. Тепер, коли фестиваль закінчився, здається, ніби всі життєві мрії кожного вже здійснилися."

"Не маючи більше заради чого жити, учні покладаються лише на інстинкти, що ведуть їх до класу."

"Або, можливо, я просто занадто багато на себе беру."

"Я повільно прямую до свого місця, і тільки тоді розумію, чому в кімнаті так тихо."

"Місця поруч зі мною блаженно порожні; найгучніший у світі перекладач для глухих ще не прийшов."

play sound sfx_doorslam
play music music_running

show misha hips_grin:
    yalign 1.0 xanchor 0.0 xpos 1.0
    easein 0.3 xanchor 1.0
with vpunch

"Тільки-но я збираюся сісти, двері розчиняються, відкриваючи сяючу Мішу; її локони підстрибують від драматичного входу, а руки простягнуті до неба."

show misha hips_laugh at right
with charachange

mi "Я-хуу~! Усе закінчилося!"

"Схоже, не на всіх діє післяфестивальна депресія."

"Решта класу витріщається на неї, очевидно, думаючи про те саме, що й я."

show misha sign_confused
with charachange

"Міша, все ще завмерши у дверях з піднятими руками, нервово озирається навколо."

"Очевидно, що вона відчуває напружену атмосферу, але не може зрозуміти, що саме робити."

show misha sign_confused at center
with ease_decel

"Раптом вона смикається вперед."

show misha perky_sad
with charachange

mi "Гей!"

show shizu invis behind misha:
    yalign 1.0 xanchor 0.5 xpos 1.0
with None

show misha perky_sad at twoleft
show bg school_scienceroom at center
show shizu adjust_happy at tworight
with dissolvecharamove

"Коли вона ввалюється в клас, стає видно Шідзуне, чия рука все ще витягнута після того, як вона штовхнула Мішу."

show shizu basic_normal
with charachange

shi "…"

hi "Дякую за виставу, але чи не час вам обом сісти на свої місця?"

show shizu behind_frown
with charachange

shi "…"

"Все ще трохи збентежена, Міша витрачає кілька секунд, щоб усвідомити, що їй потрібно перекласти."

show misha sign_smile
with charachange

mi "О! Точно! Ші-чян каже, що вона незадоволена тим, що ти кинув нас минулого тижня."

show misha cross_frown
with charachange

mi "Ми були дуже зайняті!"

hi "Ось як? А як щодо того, що я вже зробив для вас обох?"

show shizu cross_angry
with charachange

shi "…"

show misha hips_grin
with charachange

mi "Вона каже, що це стосується лише членів ради. Оскільки ти відмовився, вона тобі нічого не винна."

show misha hips_grin_close
with characlose

"Міша нахиляється ближче і змовницьки шепоче мені на вухо."

mi "Насправді, я думаю, вона просто трохи ображена, що ти не провів з нею день."

show misha hips_smile_close
with charachange

mi "Хоча вона дуже вдячна за твою роботу минулого тижня."

show shizu behind_frustrated
with charachange

"Відчувши, що мова йде про неї, Шідзуне легенько стукає пальцями по парті, поки Міша не повертається до неї обличчям."

show misha sign_smile
with charadistant

show shizu basic_angry
with charachange

show misha hips_grin
with charachange

show shizu adjust_blush
with charachange

"Я не розумію жодного жесту з цієї швидкої розмови, але, судячи з трохи збентеженого виразу обличчя Шідзуне і ледь стримуваного сміху Міші, я можу здогадатися."

stop music fadeout 8.0

"Поки відбувається цей обмін репліками, двері відчиняються знову, але цього разу набагато спокійніше."

show hanako invis at offscreenright
with None

show bg school_scienceroom at bgleft
show shizu basic_normal at Transform(xpos=0.42)
show misha hips_smile at Transform(xpos=0.18)
show hanako emb_downtimid at right
with dissolvecharamove

"Ханако тихо заходить у кімнату і зачиняє за собою двері."

show hanako emb_timid
with charachange

"Визираючи з-під свого волосся, вона швидко оглядає клас."

"Наші погляди зустрічаються, і вона раптом напружується. Вона заплющує очі, робить глибокий вдих, а потім підходить до моєї парти."

show hanako cover_distant
with charachange

ha "Д-доброго ранку, Хісао."

hi "Доброго ранку, Ханако. Ти трохи запізнилася, чи не так?"

show hanako basic_normal
with charachange

ha "Я… розмовляла з Ліллі."

show hanako basic_worry
with charachange

ha "П-про сьогоднішній день."

hi "А, то в тебе є її список? У такому разі ми можемо піти одразу після уроків."

show hanako emb_smile
with charachange

ha "З-звісно."

hi "Я з нетерпінням чекаю на це."

"Ханако на мить обдаровує мене своєю збентеженою посмішкою, а потім поспішає на своє місце."

scene bg school_scienceroom at bgright
with shorttimeskip

play music music_normal fadein 3.0

"Під час уроків стає зрозуміло, що не лише учні трохи пригнічені після фестивалю."

"Муто-сенсей просто дає нам список вправ з підручника, а потім сідає за свій стіл."

"Я зовсім забуваю про коротку обідню перерву на мить, настільки буденним видався цей день."

play sound sfx_normalbell

"Це притупляє розум, і всі здаються здивованими, коли дзвоник сповіщає про закінчення уроків."

show shizu basic_normal at tworight
show misha perky_smile at twoleft
with charaenter

"Коли я збираю сумки, Шідзуне і Міша оточують мене з обох боків."

show misha hips_grin
with charachange

mi "Слухай, Хі-чян, ще не пізно приєднатися. У нас ще купа паперової роботи після фестивалю…"

hi "Е-е, вибач, Міша, у мене… є плани…"

show hanako invis at offscreenright
with None

show bg school_scienceroom at center
show shizu basic_normal at Transform(xpos=0.42)
show misha hips_grin at Transform(xpos=0.18)
show hanako cover_distant at right
with dissolvecharamove

"Ніби відчувши момент, Ханако з'являється позаду мене, тримаючи маленьку сумку і намагаючись уникати зорового контакту з навколишнім світом."

show misha cross_laugh
with charachange

"Очі Міші широко розплющуються, а потім вона вибухає сміхом."

mi "БВА-ХА-ХА! Ти швидко дієш, правда, Хі-чян~? Ми більше не будемо заважати вашому побаченню! Бва-ха-ха!"

show shizu behind_blank
with charachange

"За спиною регочучої Міші я бачу, що Шідзуне виявляє занадто мало інтересу до цієї сцени. Можливо, я сприймаю це неправильно, але мені здається, що вона навмисно ігнорує мене."

show hanako emb_downtimid_close
with characlose

"Я відчуваю легкий поштовх за сорочку і повертаюся, щоб побачити, що очі Ханако міцно втуплені в підлогу."

show hanako emb_timid_close
with charachange

ha "Х-ходімо…"

hi "Зрозумів. Шідзуне, Міша, побачимося пізніше."

hi "І я все ще не зацікавлений у раді."

show misha cross_grin
with charachange

mi "Нудний ти."

stop music fadeout 2.0

hide misha
hide shizu
with charaexit

show bg school_scienceroom at bgleft
show hanako emb_timid_close at center
with charamove

"Міша і Шідзуне відступають у коридор, весело жестикулюючи одна одній."

hi "Забрав усі свої речі? Ходімо."

play music music_soothing fadein 4.0

scene bg school_gate
with locationskip

"Потоки учнів виливаються зі шкільних воріт на дорогу до міста."

"Це трохи дивно. Це майже звичайна сцена з будь-якої іншої старшої школи, але ілюзія зникає через випадковий інвалідний візок або відсутню кінцівку."

"Єдине, що я помічаю — ніхто не буває на самоті."

scene bg school_road
with locationchange

show hanako emb_downsad_close at center
with charaenter

"І коли ми з Ханако проходимо крізь ворота, я помічаю, що вона скорочує відстань між нами."

"Не настільки, щоб це можна було назвати «близькістю», але вона точно не стоїть на своїй звичній позиції «трохи віддалік»."

"Мабуть, ми ще не настільки близькі, щоб вона підходила до мене так само близько, як до Ліллі."

"Однак, хоча фізично вона трохи наблизилася до мене, ментально вона, здається, віддалилася на милю."

"Її руки стискали шкіряні ремінці сумки до побіління кісточок, голова була опущена, а рот міцно стиснутий."

"Вона виглядає майже так, ніби її вперше ведуть до кабінету директора."

"Я намагаюся стримати смішок від цієї думки, але це марно."

show hanako emb_timid_close
with charachange

ha "Щ-що таке…?"

"Мабуть, немає сенсу це приховувати…"

hi "Вибач. На мить здалося, що ти в халепу потрапила."

show hanako defarms_strain_close
with charachange

ha "Щ-щ-що ти маєш на увазі?"

hi "Думаю, тобі треба трохи розслабитися. Ми не йдемо надто далеко, і навколо лише учні, правда?"

show hanako def_worry_close
with charachange

ha "П-правда."

"Мене трохи турбує, що Ханако так хвилюється."

hi "Ти ж робиш це щотижня, чи не так?"

show hanako basic_worry_close
with charachange

ha "Т-так. З Ліллі."

"Звісно. «З Ліллі». Цікаво, чи вона коли-небудь виходила зі школи без неї?"

"На перший погляд це здається дрібницею, але залежність Ханако від Ліллі абсурдно сильна."

"Якби вона навіть не могла вийти зі школи без неї, як би вона вижила, якби вони ніколи не зустрілися?"

"Чи знайшла б вона когось іншого, за кого можна було б вчепитися? І що її привабило в Ліллі?"

"Чи це була її сліпота, чи Ліллі просто була достатньо доброю, щоб простягнути руку допомоги?"

"Цікаво, чи підійшов би хтось інший на цю роль."

hi "Ну, я тут. До того ж, ми йдемо недалеко. Все закінчиться швидше, ніж ти озирнешся."

show hanako emb_downsmile_close
with charachange

"Кісточки пальців Ханако повільно повертають свій колір, поки вона намагається приховати ледь помітну посмішку, але зусилля, здається, заважають подальшій розмові."

"Ми йдемо пліч-о-пліч звивистою дорогою до міста. Натовп учнів рідшає, поки ми продовжуємо йти тротуаром."

"Швидші учні поспішають вперед, а менш мобільні відстають, розріджуючи натовп до порожнечі."

scene bg suburb_konbiniext
with locationskip

"До того часу, як ми доходимо до магазину, ми практично одні."

scene bg suburb_konbiniint
with locationchange

"Використовуючи мене як щит між собою та продавцем, Ханако рухається вузькими проходами, додаючи до кошика асорті товарів."

"Хліб, молоко, чай… чебрець?"

"Який магазин продає трави?"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

nvl clear

nvl show dissolve

n "\n\nЗ іншого боку, ніщо в цьому місті не здається нормальним, що, озираючись назад, можливо, не так вже й погано."

n "Все таке інше і незручне; роздуми про такі речі — не найкращий варіант."

n "Коли я думаю про це, це нагадує мені про Ханако."

n "Як би ти не намагався, ти не можеш втекти від її шрамів; вони все ще переривають хід моїх думок, коли я їх бачу."

n "Як би я не хотів зізнатися собі в цьому, думаю, я змушую себе намагатися ігнорувати їх."

n "Не те щоб я сам був без шрамів. Зубчаста лінія на моїй грудині ніколи повністю не зникне."

n "Мені просто пощастило, що я можу легко її приховати."

n "\nАле, певною мірою, наші шрами нагадують мені, що ми всі тут з певної причини."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

window show

"…"

"Ханако кидає останній товар у кошик, а потім сором'язливо простягає його мені разом із кількома банкнотами."

show hanako emb_downtimid_close at center
with charaenter

ha "М-м-можеш, б-будь ласка…"

"Мені потрібна секунда, щоб зрозуміти, що вона намагається сказати."

hi "О, ти хочеш, щоб я заплатив за це?"

show hanako emb_downsad_close
with charachange

"Вона киває, але не підводить очей."

"Мабуть, зазвичай це завдання лягає на плечі Ліллі."

hi "Звісно. Дай-но я візьму пару речей…"

"Поспіхом я хапаю кілька необхідних речей для себе і прямую до каси, а Ханако йде слідом."

"Продавець байдуже киває мені, скануючи товари."

"Мабуть, просто ігнорувати нас — це один зі способів впоратися з аномаліями Ямаку; мабуть, до них приходить багато учнів, адже це найближчий магазин до школи."

"У персоналу, мабуть, є свої способи взаємодії з нами. Або, можливо, ні; можливо, тільки я двічі думаю про своїх незвичайних однокласників."

stop music fadeout 2.0

scene bg suburb_konbiniext_ss
with locationchange

"Розрахувавшись, ми з Ханако повертаємося на вулицю."

scene bg school_road_ss
with locationskip

play music music_tranquil fadein 10.0

"Дорога зараз майже порожня. Учні, що йшли назовні, вже пішли, а ніхто ще не почав повертатися."

"І оскільки попереду на дорозі лише школа, здається, навколо більше нікого немає."

show hanako def_worry_close_ss at center
with charaenter

"Порожнеча, безумовно, відбивається на Ханако; її руки з боків несуть сумки, голова більше не опущена, і вона знову випрямилася…"

"Майже так, ніби вона насолоджується цією прогулянкою."

hi "Отже, навіщо всі ці дивні речі? Суміш спецій? Навіщо тобі це в школі?"

show hanako basic_normal_close_ss
with charachange

ha "Я… іноді… люблю ґ-готувати їжу."

hi "Ну, так, я теж, але… спеції?"

hi "Це трохи просунутіше, не думаєш?"

show hanako emb_blushing_close_ss
with charachange

ha "Н-не зовсім."

hi "Ну, я думаю, це круто. Якось навчиш мене."

show hanako emb_smile_close_ss
with charachange

ha "З-звісно."

"Вона не здається такою вже впевненою, але наполягати на цьому не здається мудрим."

"Принаймні, вона виглядає набагато щасливішою, ніж під час прогулянки сюди."

"Вже одне це робить мене трохи щасливішим."

scene bg school_dormext_full_ss
with shorttimeskip

show hanako basic_normal_close_ss at center
with charaenter

"Біля жіночого гуртожитку ми з Ханако розбираємо пакети з продуктами з нашими покупками."

"У порівнянні з ними мої речі виглядають зовсім просто."

hi "Кажу тобі, ти мене тут осоромлюєш…"

show hanako defarms_shock_close_ss
with charachange

ha "Н-ні, не осоромлюю… я просто…"

hi "Я лише жартую."

show hanako def_worry_close_ss
with charachange

hi "У мене стос домашнього завдання, яке я пропустив минулого тижня, тож мушу йти."

hi "Ти сама впораєшся з тим, щоб донести це до своєї кімнати?"

show hanako cover_bashful_close_ss
with charachange

ha "Т-так."

hi "Впевнена? Добре тоді. Побачимося завтра."

show hanako basic_smile_close_ss
with charachange

ha "П-па-па."

hide hanako
with charaexit

stop music fadeout 7.0

"Ми розходимося, і я повертаюся до своєї кімнати."

scene bg school_dormhisao_ss
with locationskip

"Стоси паперів лежать на моєму столі, благаючи, щоб їх закінчили. Через увесь гармидер минулого тижня я ледь мав час наздогнати навчання."

"Я намагався не відставати від навчання, поки був у лікарні, але деякі з цих речей я ніколи раніше не бачив, навіть у своїй старій школі."

"Абсолютно непідготовлений, я відкриваю банку з напоєм і беруся до роботи."

scene black
with dissolve


return
label uk_H4:

scene black
with None

play music music_daily fadein 6.0

scene bg school_dormhisao
with locationchange

"Дні справді починають ставати спекотнішими."

"Сьогодні вранці я прокинувся в поту."

"До того часу, як учні починають залишати свої гуртожитки для сніданку та ранкових обов'язків, сонце вже в повному розпалі; як не дивно, це піднімає мені настрій."

"Ще навіть немає восьмої, а я відчуваю, що цей день буде одним із тих приємних, спокійних і теплих."

"Якби я не був у школі, де кожна відсутність на заняттях вважається ознакою ситуації, що загрожує життю, я б подумав про те, щоб прогуляти весь день і просто відпочити в шкільних садах."

"Так, сьогодні буде по-справжньому лінивий день."

"На мить я зупиняюся посеред розтяжки і згадую попередження медсестри про фізичні вправи. Можливо, мені варто було продовжувати ті ранкові пробіжки."

"Біг з кимось на кшталт Емі міг би бути трохи виснажливим, але якби я працював у власному темпі…"

"Ах, кого я обманюю? Я не зміг би дотримуватися чогось подібного без певної мотивації."

"Це не те, що я сиджу цілий день. Прогулянка до магазину і назад вважається вправою, правда? Особливо прогулянка назад вгору по пагорбу…"

"Так, це нічого страшного. У порівнянні з місяцями лежання в лікарняному ліжку, я отримую достатньо вправ."

scene bg school_scienceroom
with shorttimeskip

"Здається, я не один такий, хто цінує цей день."

"Майже кожен учень у класі визирає у вікно на спокусливе небо."

"Навіть непохитна Шідзуне, здається, втратила свій звичний запал до навчання."

"Міша, як завжди зухвала, навіть розстебнула верхні ґудзики сорочки й обмахується зошитом."

"Мабуть, я витріщився, бо вона тепер показує мені язика."

"Однак вона не виявляє жодних ознак того, що збирається зупинитися, і навіть не намагається цього приховати."

play sound sfx_normalbell

"Дзвінок на обід, здається, застав усіх зненацька, і клас спорожнів набагато повільніше, ніж зазвичай."

"Спека, схоже, висмоктала з усіх бажання поспішати."

stop music fadeout 8.0

"Ну, майже з усіх."

show hanako emb_emb
with charaenter

ha "Х… Хісао?"

hi "Привіт, Ханако, чим можу допомогти тобі сьогодні?"

"У Ханако вже в руках торбинка з обідом."

"Не треба бути детективом, щоб зрозуміти, до чого все йде."

show hanako emb_smile
with charaenter

ha "Ем… хочеш знову пообідати з нами?"

show hanako basic_bashful
with charaenter

ha "Я… я принесла достатньо на всіх…"

hi "Чудово. Тільки не треба бути такою напруженою через це."

show hanako basic_normal
with charaenter

ha "А… точно."

hi "Я так розумію, ми йдемо до чайної кімнати?"

show hanako cover_worry
with charaenter

ha "Б… будь ласка."

show hanako basic_normal
with charaenter

ha "Ліллі сказала, що зустріне нас там, тож ми маємо… маємо…"

hi "Маємо?"

show hanako emb_smile at center
with charaenter

ha "…маємо йти разом…"

hi "Звучить як план. Від цієї спеки я добряче зголоднів."

"Ханако зітхає з полегшенням, а я збираю свої речі."

scene bg school_miyagi
with locationskip

play music music_happiness fadein 1.0

"Як завжди, атмосфера чайної кімнати освіжає, створюючи відчуття ізольованості від решти світу."

"Хоча, з іншого боку, звичний шкільний гамір сьогодні трохи притих; найімовірніше, через лінь, викликану тепловим виснаженням."

"Ханако повільно розкладає їжу на столі, зосереджено вдивляючись у кожен рух, ніби намагається відволіктися від інших думок."

"Тут небагато, але по її поведінці я бачу, що вона готувала все з надзвичайною турботою."

hi "Здається, Ліллі ще немає. Почнемо без неї?"

show hanako emb_timid:
    center
    ypos 1.17
with charaenter

ha "В-вона скоро буде…"

show hanako emb_downtimid
with charachange

"Ханако бореться з кришкою контейнера з рисом."

hi "Давай, дозволь мені допомогти…"

"Я забираю контейнер з рук Ханако і намагаюся силою відкрити кришку."

"Як я не старався, вона наче прикипіла."

hi "Дай вгадаю, ти закрила його, поки рис був ще гарячим?"

show hanako emb_sad
with charachange

ha "Т-так. Я поспішала…"

"Я ставлю контейнер на стіл між нами."

hi "Я так і думав. Схоже, його заклинило. Нам знадобиться гаряча вода, щоб відкрити."

hi "Але тут це буде незручно. Ми розіллємо воду всюди."

li "Ну, у такому разі, як щодо того, щоб я зробила свій внесок у сьогоднішню трапезу?"

show lilly invis at left
with None

show hanako emb_smile:
    tworight
    ypos 1.17
show bg school_miyagi at bgright
show lilly basic_cheerful at twoleft
with dissolvecharamove

"У дверях стоїть Ліллі, посміхаючись і тримаючи пакет, наповнений різними булочками та хлібом. Я не можу не посміхнутися у відповідь."

show lilly basic_smileclosed
with charachange

li "Оскільки у вас обох змінилися плани через мене, я подумала, що варто принести дещо до столу."

hi "Дякую, Ліллі. Давай, я допоможу тобі…"

show lilly basic_smileclosed at Transform(ypos=1.2)
with charamove

"З невеликою допомогою асорті хліба від Ліллі приєднується до тарілки Ханако без рису. Я поспіхом заварюю чай, щоб завершити картину."

hi "Що ж, я з нетерпінням чекаю на це."

show hanako emb_downtimid
with charachange

"Коли я відкушую шматочок, помічаю, як Ханако щосили намагається не дивитися на мене."

"Нічого особливого, але я не можу скаржитися. Я досить лінивий, коли справа доходить до приготування їжі для себе."

hi "Непогано, гадаю, це зроблено з того, що ти купила вчора?"

show hanako emb_blushtimid
with charachange

ha "Т-так."

"Очі Ханако благають мене про хоч якийсь відгук."

hi "Ну, це було однозначно того варте. Дякую, Ханако."

show hanako cover_bashful
with charachange

ha "Я… я хотіла показати тобі це… після вчорашнього…"

hi "Все гаразд. Я просто був трохи здивований тим, що ти купувала."

show lilly basic_weaksmile
with charachange

li "Ханако завжди любила експериментувати з їжею. Я думаю, це добре… здебільшого."

"Хоча посмішка Ліллі не здригнулася, ледь помітна зміна в її тоні підказує мені, що в минулому все було не так гладко."

"Та й не схоже, що у Ханако багато людей, які могли б скуштувати її страви…"

stop music fadeout 7.0

"Стривай… чи не чекала Ліллі, поки я почну першим? Вона не їла, поки я не сказав, що все добре…"

"Її зухвала посмішка підказує мені, що це було навмисно. Мені доведеться спробувати якось відігратися в майбутньому, щоб компенсувати це."

hi "Ну, це смачно, і це головне, правда?"

show hanako basic_smile
with charachange

ha "П-правда."

show lilly basic_smileclosed
with charachange

"Ліллі, задоволена тим, що не стала першою дегустувати творіння Ханако, починає їсти."

"Я ловлю себе на тому, що витріщаюся, спостерігаючи, як її палички ніжно торкаються тарілки, кінчиками делікатно досліджуючи та відстежуючи розташування їжі, перш ніж вправно підхопити її."

"Можна було б подумати, що вона дитина, яка грається з їжею, якби не ситуація, хоча вона робить це з такою турботою і легкістю, що очевидно — це просто її спосіб їсти таку страву."

"Не бажаючи відставати, я теж починаю їсти."

show hanako emb_downsmile
with charachange

"Ханако обирає інший підхід: вона чекає, поки ми з Ліллі звільнимо руки, перш ніж швидко схопити свою порцію."

show hanako emb_smile
with shorttimeskip

play music music_dreamy fadein 4.0

"Незабаром контейнери порожні, за винятком того, що з рисом, який досі закритий."

show lilly basic_smile
with charachange

li "Дякую, Ханако, я наїлася."

show hanako basic_smile
with charachange

ha "Н-ні… дякую тобі за хліб…"

hi "Так, без нього це була б катастрофа."

show lilly basic_planned
with charachange

li "Будь ласка."

show lilly basic_weaksmile
with charachange

li "Але тепер я мушу повертатися. Дуже легко запізнитися, якщо обідати тут."

hi "Так, розумію. Думаю, ми просто приберемо тут і теж підемо."

show lilly basic_smileclosed at twoleft
with dissolvecharamove

li "Що ж, гарного дня."

hide lilly
with charaexit

show hanako basic_smile:
    center
    ypos 1.17
show bg school_miyagi at center
with charamove

"Ліллі йде, її тростина цокає по тихому коридору."

"Ми з Ханако швидко збираємо речі й залишаємося сидіти, чекаючи на дзвінок."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene bg misc_sky at Fullpan(20.0)
with locationchange

"Разом ми дивимося у вікно на безкрає блакитне небо."

play sound sfx_warningbell

"Якби не дзвін, я б заприсягся, що час зупинився."

"Бажання прогуляти урок підступає до горла."

"Я кидаю погляд на Ханако, яка теж не виявляє жодних ознак руху."

ha "Не… ще не зараз…"

$ renpy.music.set_volume(1.0, 3.0, channel="music")

scene bg school_miyagi
show hanako basic_smile:
    center
    ypos 1.17
with shorttimeskipsilent

"Інтервал між попереджувальним дзвінком і дзвінком на закінчення обіду минає в одну мить."

hi "Нам справді варто йти… люди збожеволіють і почнуть пошукову групу, якщо ми прогуляємо…"

show hanako basic_distant
with charachange

"Ханако зітхає."

show hanako basic_normal
with charachange

ha "Ти правий."

show hanako basic_normal at center
with charamove

"Вона повільно підводиться, і я йду за нею."

scene bg school_staircase2
with locationskip

"Мовчки ми піднімаємося старими сходами на третій поверх, а потім до нашого класу."

scene bg school_hallway3
with locationchange

play sound sfx_dooropen

"Біля дверей я виходжу вперед і відчиняю їх перед Ханако, заздалегідь схиливши голову в знак вибачення."

scene bg school_scienceroom at center
with locationchange

stop music fadeout 5.0

hi "Вибачте за запізнення, вчителю."

play sound sfx_doorclose

"Мене зустрічають не суворі слова і не розгнівана вказівка сісти на місце, а просто тиша, викликана п'ятнадцятьма чи близько того учнями, які намагаються не засміятися."

"Муто, як завжди, запізнюється і ще не прийшов. Однак той факт, що ми з Ханако прийшли разом, очевидний."

show misha hips_grin at center
with charaenter

mi "Пфф… пффва…"

"Вважай, що чотирнадцять учнів намагаються, а один — ні."

play music music_comedy

show misha cross_laugh
with charachange

mi "Пфт-бвахахаха! Закохані повернулися~!"

show misha hips_laugh
with charachange

mi "ВАХАХАХА~!"

hi "Так, дякую. Можеш уже заспокоїтися."

hide misha
show hanako invis_close:
    center
    xpos 1.0
with charaexit

show bg school_scienceroom at bgleft
show hanako emb_downsad_close:
    xpos 0.8
with dissolvecharamove

"Я заходжу в двері й розумію, що Ханако міцно притиснулася до моєї спини, ховаючись від класу."

show hanako invis_close:
    xpos 0.7
with dissolvecharamove

"Коли я підходжу ближче до своєї парти, вона нарешті відсторонюється і напружено йде до своєї. Її спроби подумки відгородитися від присутності всіх навколо досить чітко написані на її обличчі."

scene bg school_scienceroom at bgright
with charamove

"Швидко перевіривши двері на наявність ознак приходу вчителя, я підходжу до парти Ханако і шепочу їй на вухо."

hi "Не переймайся через Мішу, вона завжди така. Мені сьогодні було добре. Не бери до голови, гаразд?"

"Ханако киває головою, сховавшись за складеними руками, але все ще не показує обличчя."

play sound sfx_dooropen

show muto invis at tworight
with None

show muto normal at center
show bg school_scienceroom at center
with dissolvecharamove

"Я прагну залишитися і втішити її ще трохи, але Муто обирає саме цей момент, щоб увійти до класу посеред лекції, ніби він почав її ще в коридорі."

show muto smile at center
with charaenter

mu "…що, звісно, прямо пропорційно заряду, але обернено пропорційно квадрату відстані…"

hide muto
with charaexit

play sound sfx_doorclose

"Він настільки захоплений своєю промовою, що навіть не помічає, як я прослизаю назад на своє місце від парти Ханако."

"Поки Муто продовжує свою балаканину, Міша нахиляється до мене."

show misha invis at offscreenleft
with None

show misha perky_smile_close:
    xanchor 0.5 xpos 0.16
with dissolvecharamove

mi "Вчитель, можливо, і не помітив вашого запізнення, але я — так."

"Це очевидно з того вистави, яку ти щойно влаштувала."

show misha hips_grin_close
with charachange

mi "Мені доручили відпустити вас сьогодні, але лише за однієї умови."

hi "О? І якої ж?"

show misha sign_smile_close
with charachange

mi "Ти маєш допомогти нам сьогодні вдень~!"

"Я витягую шию, щоб зазирнути через плече Міші."

"Шідзуне зручно влаштувалася і не дивиться на мене."

hi "Добре. Тільки на сьогодні."

hi "Я вже казав тобі, що не вступатиму до ради, пам'ятаєш?"

show misha hips_grin_close
with charachange

mi "Звісно! Це можна було б розцінити як… ем, розцінити як…"

show misha perky_confused_close
with charachange

"Вона дивиться у свій блокнот, очевидно, шукаючи місце у своєму сценарії."

show misha hips_grin_close
with charachange

mi "…під примусом, а отже, це було б проти правил."

hi "Як дивно з твого боку бути такою уважною до правил саме зараз."

show misha sign_smile_close
with charachange

mi "Все має робитися за правилами!"

show misha perky_smile_close
with charachange

mi "Просто правила не написані для кожної ситуації, тому бувають моменти, коли ними можна знехтувати."

hi "І все ж ви обоє дивуєтеся, чому ніхто інший не хоче бути в учнівській раді…"

stop music fadeout 3.0

show misha hips_frown_close
with charachange

with Pause(0.3)

show misha invis at offscreenleft
with dissolvecharamove

hide misha
with None

"Показавши мені язика, Міша повертається до свого робочого зошита, і ми долаємо другу половину шкільного дня."

with shorttimeskip

play sound sfx_normalbell

show shizu invis_close at offscreenright
show misha invis_close at offscreenleft
with None

show misha hips_smile_close at twoleft
show shizu behind_blank_close at tworight
with Dissolvemove(0.5, time_warp=_ease_in_time_warp)

"Перш ніж я встигаю навіть встати, Міша і Шідзуне кладуть руки мені на плечі."

hi "Гей, я сказав, що допоможу, чорт…"

play music music_shizune fadein 1.0

show misha hips_grin_close
with charachange

mi "Це просто страховка, Хісао, страховка~!"

show hanako invis behind shizu at offscreenright
with None

show misha hips_smile_close at Transform(xpos=0.17)
show shizu behind_blank_close at Transform(xpos=0.5)
show bg school_scienceroom at bgleft
show hanako emb_timid:
    xanchor 0.5 xpos 0.9
with dissolvecharamove

ha "Х-Хісао?"

"Ханако боязко намагається вийти з кімнати, обходячи нас, і я раптом розумію, що це може бути мій єдиний шанс втекти."

hi "О, привіт, Ханако. Як справи?"

show shizu basic_angry_close
with charachange

shi "…"

show misha hips_frown_close
with charachange

mi "Гей, з чого ти взяв, що в тебе є час на балачки?"

hi "О, розслабся, це не займе багато часу… вибач, Ханако, ти щось казала?"

show hanako emb_downtimid
with charachange

ha "Я… я збиралася піти до бібліотеки, і… і я подумала…"

"Великі пальці Ханако танцюють один навколо одного, а її очі бігають по кімнаті, дивлячись куди завгодно, тільки не на нас."

show misha sign_smile_close
with charachange

mi "Вибач, Ханако, але Хісао має піти з нами. У нього є робота."

show shizu behind_smile_close
with charachange

shi "…"

show misha hips_grin_close
with charachange

mi "О! Але ти теж можеш допомогти, якщо хочеш."

show hanako cover_worry
with charachange

ha "Ем…"
return
label uk_choiceH4:
menu:
    with menueffect
    mi "То як щодо цього, Хісао?"
    "Що ти думаєш, Ханако?":


        return m1
    "Я вже достатньо попрацював для ради.":

        return m2


label uk_H5_1:


scene bg school_scienceroom at bgleft
show hanako cover_worry:
    xanchor 0.5 xpos 0.9
show shizu behind_smile_close at Transform(xanchor=0.5, xpos=0.5)
show misha hips_grin_close at Transform(xanchor=0.5, xpos=0.17)
with None

hi "Що скажеш, Ханако? Якщо ми всі допоможемо, це не займе багато часу."

show hanako emb_timid
with charachange

"Метушня Ханако відповідає на моє запитання раніше, ніж вона встигає вимовити слова."

show hanako emb_downtimid
with charachange

ha "Мені… мені справді треба йти…"

"Ну, цього й слід було очікувати. Схоже, знову тільки я і дівчата з ради."

"Легше змиритися з ще одним днем роботи в маленькому кабінеті ради."

hi "Я наздожену тебе пізніше, добре?"

show hanako emb_smile
with charachange

ha "Д-добре."

stop music fadeout 3.0

show misha hips_grin_close at twoleft
show shizu behind_smile_close at tworight
show hanako invis at offscreenright
show bg school_scienceroom at center
with dissolvecharamove

show misha hips_smile_close at twoleft
hide hanako
with charachange

mi "Гаразд! Тепер, коли прощання закінчилися, час до роботи!"

scene bg school_hallway3
with locationchange

"Міша та Шідзуне під конвоєм ведуть мене до кабінету учнівської ради, жодного разу не відпускаючи мої плечі."

"Мені трохи ніяково через те, що я так кинув Ханако, але якщо це ціна того, щоб Міша відчепилася від неї, то нехай буде так."

scene bg school_council
with locationchange

hi "Отже, що ми сьогодні робимо?"

show misha sign_smile at center
with charaenter

play music music_ease fadein 8.0

mi "Звіт!"

hi "Га? Хіба це не має відбуватися після чогось?"

show misha hips_grin
with charachange

mi "Ага! Ми маємо зібрати всю інформацію з фестивалю, щоб Шіччан могла відзвітувати вчителям."

show misha hips_grin at twoleft
show bg school_council at bgleft
with charamove

show shizu adjust_happy at tworight
with charaenter

"Шідзуне кидає велику купу паперів на стіл переді мною і коротко посміхається."

show misha hips_smile
with charachange

mi "Тобі треба розсортувати це на дві купи."

show misha sign_smile
with charachange

mi "Одну для фінансових справ, як-от чеки, одну для відгуків, одну для позитивних відгуків, можливо, одну для речей, які виглядають як потенційні проблеми наступного року, одну для проблем, які, ймовірно, не вдасться вирішити…"

hi "Це трохи більше, ніж дві купи…"

show misha perky_confused
with charachange

mi "Га? О, точно. Так, я думала, що буде лише дві купи. Мій промах."

hi "Зрозумів. Поки я цим займатимуся, що робитимете ви двоє?"

show misha hips_grin
show shizu adjust_smug
with charachange

mi "Ну, ми пропустили обід, бо збирали всі ці звіти, тож ми підемо перекусимо!"

"Чому ви просто не розсортували їх, поки збирали…"

"На щастя, мій механізм самозахисту спрацьовує і не дає мені відкрити рота й ще більше погіршити своє становище."

show misha perky_confused
with charachange

mi "Е?!"

show misha perky_sad
with charachange

mi "Як це справедливо?"

show shizu behind_blank
with charachange

shi "…"

"Я так переймався несправедливим розподілом роботи, що не помітив, як Шідзуне продовжувала жестикулювати."

"Якби не вигук Міші, я б, мабуть, взагалі нічого не помітив."

show shizu adjust_smug
with charachange

show shizu basic_normal
with charachange

show shizu behind_blank
with charachange

"Шідзуне, здається, видає досить довгий потік команд для Міші, і жодна з них не виглядає приємною."

show misha sign_sad
with charachange

show misha perky_sad
with charachange

show misha perky_sad at Transform(ypos=1.15)
with charamove

"Дійшовши висновку, Міша коротко відповідає жестами Шідзуне, а потім сідає за стіл поруч зі мною."

show shizu adjust_happy
with charachange

hide shizu
with charaexit

show misha perky_sad at Transform(xpos=0.5)
show bg school_council at center
with charamove

"Шідзуне махає нам обом, перш ніж зникнути за дверима."

hi "Що це все було?"

show misha perky_confused
with charachange

mi "Шіччан хвилювалася, що ти все переплутаєш, якщо за тобою не наглядати."

show misha perky_sad
with charachange

mi "А оскільки вона не може сказати тобі, що ти робиш не так, вона змушує мене залишитися. Овва… облом, я хотіла піти з Шіччан!"

show misha cross_smile
with charachange

mi "Але вона принесе нам трохи їжі~!"

show misha cross_grin
with charachange

mi "Хіба це не чудово!"

"Легковажність Міші просто неймовірна. Від пригніченого стану до захвату через якісь калорії."

"Важко уявити, як хтось може функціонувати на такому рівні."

hi "Ну, могло бути й гірше."

hi "То що ми маємо робити?"

show misha sign_smile
with charachange

mi "Сортування."

hi "Це я зрозумів."

show misha hips_smile
with charachange

mi "Ну, давай просто почнемо робити купи. Ми розберемося, що вони означають, пізніше."

hi "Зрозумів…"

show misha perky_smile
with charachange

"Ми починаємо розділяти всі папери на дедалі складніші купи."

"Спочатку це були просто прості категорії: фінансові, відгуки, звіти про інциденти…"

"Потім вони розділилися на хороші та погані звіти, і далі, поки не стало схоже, що ми просто накидали паперів на стіл."

hi "Це безнадійно."

show misha perky_confused
with charachange

mi "Га? Чому? Ми робимо те, що нам сказали, так?"

hi "Так, але виглядає так, ніби ми просто влаштовуємо безлад."

show misha hips_grin
with charachange

mi "Ні, я думаю, ми багато зробили. Шіччан зможе розібратися з рештою звідси."

show misha cross_grin
with charachange

mi "Тож я думаю, ми можемо на цьому зупинитися."

"Майже якби здоровий глузд Міші вийшов з кімнати разом із Шідзуне."

"Втім, сперечатися немає сенсу."

show misha sign_smile
with charachange

mi "У будь-якому разі…"

show misha cross_smile
with charachange

mi "Що там у вас із Ханако?"

hi "Що саме?"

show misha hips_smile
with charachange

mi "Ти ж сьогодні з нею гуляв, так~?"

show misha hips_grin
with charachange

mi "Були якісь іскри? Якісь плітки, які ти приховуєш від мене~?"

hi "Якби я розповів тобі про власні обставини, це були б не плітки, чи не так?"

show misha perky_confused
with charachange

mi "Мабуть, ні…"

hi "Ми просто друзі, мабуть."

hi "Чому ти так цікавишся? Я думав, ви з Шідзуне її не любите…"

show misha cross_frown
with charachange

mi "Це не зовсім так. Ти знаєш, що Шіччан і Ліллі не дуже ладнають."

mi "А оскільки ти не можеш просто так відірвати Ханако від Ліллі, ми з нею мало спілкуємося."

show misha sign_smile
with charachange

mi "Але це не означає, що я не можу за неї хвилюватися."

hi "А про що хвилюватися?"

show misha perky_sad
with charachange

mi "Ну, вона ніколи ні з ким іншим не спілкується, так? Це недобре, Хіччан!"

"Якщо Шідзуне і Ліллі не подобаються одна одній, бо «їхні характери різні», то я боюся навіть уявити, як би ладнали Міша і Ханако…"

show misha perky_confused
with charachange

mi "Я маю на увазі, так чи інакше, ми всі тут в одному човні, правда~?"

hi "Ну, мабуть."

show misha sign_smile
with charachange

mi "Одного разу, коли вона пішла з уроку посеред заняття, Шіччан пішла до вчителя і запитала, що з цим робитимуть."

show misha sign_confused
with charachange

mi "Він сказав, що кожен учень тут має особливі потреби, і що Шіччан не повинна через це хвилюватися."

show misha perky_confused
with charachange

mi "Ханако ніколи не бере участі в груповій роботі; вона просто тікає."

mi "Хіба цього недостатньо, щоб хвилюватися?"

hi "Мабуть, ти маєш рацію. Вона все ще ледь вимовляє слово, коли ми розмовляємо."

show misha perky_sad
with charachange

mi "Ну, це більше, ніж вдалося мені. Ми з Шіччан обоє намагалися, коли вона тільки прийшла, але вона злякалася і втекла."

"Я думаю сказати Міші, що зі мною сталося те саме, але вона, здається, заглибилася в роздуми."

"Слухати Мішу без впливу Шідзуне… цікаво."

show misha cross_frown
with charachange

mi "Я думаю, їй треба зрозуміти, що людям тут байдуже, як вона виглядає, і що вона може нам довіряти."

show misha cross_smile
with charachange

mi "Якби вона могла, я б почувалася набагато краще щодо неї."

"Здається, це найдовший час, протягом якого я спостерігав за Мішею, не бачачи, як вона жестикулює."

"Коли вона з Шідзуне, то постійно розмахує руками, пояснюючи Шідзуне світ навколо."

"Така кількість зусиль, мабуть, виснажує навіть найжвавіший розум."

"І давайте дивитися правді в очі: Міша не найкмітливіша людина у світі."

hi "Що ж, я нагляну за нею замість тебе."

hi "Але тобі, мабуть, варто вибачитися за те, що було раніше. Не думаю, що Ханако створена для таких жартів."

show misha perky_confused
with charachange

mi "О? О~!"

show misha perky_sad
with charachange

mi "Я навіть не помітила. Вибач."

hi "Не мені це кажи, просто скажи це їй."

show misha perky_smile
with charachange

mi "Добре. Завтра зранку я поговорю з нею."

hi "Добре."

play sound sfx_doorslam
with vpunch

"Гуркіт від дверей сповіщає про повернення Шідзуне."

"Мабуть, вона не зовсім розуміє, скільки шуму створює."

show misha hips_grin
with charachange

mi "О, Шіччан! Ти повернулася!"

show shizu invis at Transform(xanchor=0.5, xpos=1.0)
with None

show misha hips_grin at Transform(xpos=0.3)
show shizu behind_blank at tworight
show bg school_council at bgleft
with dissolvecharamove

"З'являється Шідзуне, повністю завантажена товарами з магазину."

show shizu basic_normal2
with charachange

shi "…"

show misha sign_smile
with charachange

mi "Після фестивалю залишилися надлишки. Оскільки це офіційна справа ради, я трохи витратилася."

show misha hips_grin
with charachange

mi "Гарна ідея, Шіччан, десять балів."

hi "Це справді дозволено?"

show shizu cross_angry
with charachange

shi "…"

show misha cross_frown
with charachange

mi "Для того, хто відмовляється приєднатися до нас, ти виявляєш нездоровий інтерес до політики цієї ради."

show misha cross_grin
show shizu adjust_smug at tworight
with charachange

mi "Я покараю твою зухвалість, обмеживши твою порцію бенкету."

hi "Добре, добре, я зрозумів."

show misha perky_smile
show shizu adjust_happy at Transform(ypos=1.15)
with dissolvecharamove

"Міша зсуває кілька стопок паперів вбік, щоб звільнити місце для лавини їжі, яку розкладає Шідзуне."

"Спостерігаючи за тим, як моя важка, але марна праця йде нанівець, я розумію, чому цим двом потрібна допомога."

"Їжа з магазину не надто смачна, але принаймні вона ситна."

show shizu behind_smile
with charachange

shi "…"

show misha sign_smile
with charachange

mi "Дякую за допомогу сьогодні. Більшість часу ми просто вигадуємо звіти для персоналу."

show misha perky_smile
with charachange

mi "Цього року ми принаймні зможемо вигадати кілька доречних заголовків для звіту."

hi "Ви впевнені, що це не корумпована організація?"

show misha hips_grin
with charachange

mi "Зовсім ні, зовсім ні. Ми діємо за правилами. Це не наша провина, якщо правила недостатньо конкретні."

hi "Я думав, що це і є визначення корупції…"

show misha hips_smile
with charachange

mi "Ти забагато думаєш~!"

hi "Знаєш що? Мабуть, ти маєш рацію."

hi "У будь-якому разі, я мушу йти…"

hi "…тобто, якщо мені дозволено піти."

show shizu adjust_smug
with charachange

shi "…"

show misha hips_grin
with charachange

mi "Твою роботу визнано достатньою. Можеш іти."

hi "Що ж, дякую."

hi "Знаєш, якби ти наголошувала на «безкоштовній їжі», а не на «нескінченному робочому навантаженні», ти б, мабуть, отримала більше рекрутів."

stop music fadeout 6.0

show misha sign_smile
with charachange

show shizu behind_blank
with charachange

mi "Можливо, ти маєш рацію."

hi "Ну, подумай про це."

hi "І подумай про те, що ми обговорювали… тобі не обов'язково розповідати це Шідзуне, якщо не хочеш."

show misha perky_confused
with charachange

mi "Що? О, точно. Спробую побачитися з нею завтра."

show misha perky_smile
with charachange

mi "На добраніч, Хіччан."

hi "На добраніч, Мішо, Шідзуне."

scene black
with dissolve

return
label uk_H5_2:

scene bg school_scienceroom at bgleft
show hanako cover_worry:
    xanchor 0.5 xpos 0.9
show shizu behind_smile_close at Transform(xanchor=0.5, xpos=0.5)
show misha hips_grin_close at Transform(xanchor=0.5, xpos=0.17)
with None

hi "Гей, Шідзуне. Я знаю, що обіцяв допомогти, але забув, що в мене вже були плани. До того ж, минулого тижня я допоміг більше, ніж мав би, чи не так?"

hi "Обіцяю, що якось іншим разом віддячу вам."

show misha sign_confused_close
with charachange

show shizu basic_frown_close
with charachange

show misha perky_smile_close
with charachange

show shizu behind_blank_close
with charachange

"Шідзуне та Міша відпускають мене і ведуть довгу, глибоку та мовчазну розмову."

show misha sign_smile_close
with charachange

mi "Що ж, ти маєш рацію. Чесно кажучи, ми збиралися витратити решту бюджету лише на тістечка."

show misha cross_laugh_close
with charachange

mi "Тож, якщо тебе не буде, це навіть краще. Більше тістечок для нас. Вахахаха~!"

stop music fadeout 6.0

show shizu invis at offscreenleft
with dissolvecharamove

show misha invis at offscreenleft
with dissolvecharamove

hide shizu
hide misha
with None

"Шідзуне розвертається і крокує до дверей, а Міша підстрибом прямує за нею."

hi "Що ж, це було набагато простіше, ніж я думав. Минулого тижня ці двоє були як шукачі. Або тюремні наглядачі."

hi "Або, можливо, тюремні наглядачі, виведені з шукачів…"

"Не можу повірити, що я щойно про це подумав, не кажучи вже про те, щоб сказати це вголос. Думаю, мені треба триматися подалі від Кенджі."

hi "…Не зважай. У будь-якому разі, підемо до бібліотеки?"

show hanako basic_smile
with charachange

ha "Д-добре."

play ambient sfx_crowd_indoors fadein 0.5

scene bg school_hallway3
show crowd
with locationchange

"Ханако йде за мною крізь заповнені коридори до бібліотеки, використовуючи мене як щит."

stop ambient fadeout 0.5
play music music_happiness fadein 2.0

scene bg school_library
show hanako invis at offscreenright
show yuuko neutral_down at center
with locationchange

show hanako basic_worry at tworight
with dissolvecharamove

"Як тільки ми проходимо крізь двері, Ханако кидається до стійки, де Юко розкладає книги."

show hanako emb_emb
with charachange

"Перш ніж я встигаю наздогнати її, Ханако щось шепоче їй."

show yuuko neurotic_up
with charachange

yu "Гм, ти знайдеш це в розділі нехудожньої літератури, але я не знаю де саме. Якщо хочеш, я можу пошукати…"

show hanako emb_downsad
with charachange

ha "Н-не треба."

hi "Гей, Юко, про що це ви?"

show yuuko neutral_down
with charachange

yu "О, Хісао… Ханако просто шукала книгу про…"

show hanako emb_blushing
with charachange

ha "Н-ні про що…"

hi "Книгу про ніщо? У розділі нехудожньої літератури?"

show hanako def_strain
with charachange

ha "Я… я просто…"

show yuuko neurotic_up
with charachange

"Я кидаю погляд на Юко. Вона виглядає так, ніби ось-ось вибухне від тиску через необхідність зберігати прохання Ханако в таємниці."

hi "Юко, що ти…"

show yuuko happy_down
with charachange

yu "Шахи! Вона шукає книжку про шахи!"

"Я роблю собі замітку ніколи не довіряти Юко жодної важливої інформації."

show hanako defarms_shock
with charachange

ha "Ю-Юко…"

show yuuko panic_up
with charachange

yu "Вибач, Ханако… воно просто вирвалося…"

hi "Ну, тепер це вже не секрет. Ходімо, я допоможу тобі. Мені теж варто було б освіжити свої навички."

show hanako def_worry
with charachange

ha "Д-добре."

hide yuuko
with charaexit

show hanako def_worry at center
show bg school_library at bgleft
with charamove

"Юко з соромом зникає за стійкою, поки ми з Ханако заглиблюємося в нетрі відділу нехудожньої літератури."

"Я знаю, що тут має бути якась система класифікації книжок, але не розумію, як хтось може її розібрати, не витративши на це пів життя."

"Мабуть, саме тому всі бібліотекарі, яких я знаю, невротики."



"Ближче до кінця ряду, між книжкою про карткові фокуси та якоюсь книжкою про дитячі ігри, стоїть одна-єдина книжка з назвою «Шахові тактики для чемпіонів»."

show hanako basic_bashful
with charachange

"Перш ніж я встигаю дотягнутися до неї, Ханако вже тримає книжку в руках, притискаючи її до грудей."

hi "Що ж, гадаю, тепер вона твоя. Не проти, якщо я позичу її, коли ти закінчиш?"

show hanako cover_worry
with charachange

ha "З-звісно. Я… я просто раніше ні з ким, крім Л-Ліллі, не грала, тому подумала…"

"Чорт. Я не намагався навмисно обіграти Ханако чи щось таке, але, здається, вона сприйняла це близько до серця."

"З іншого боку, принаймні це означає, що вона хоче зіграти зі мною знову. Це плюс, так?"

hi "Ха, ну, я не якийсь там майстер; я просто трохи грав раніше…"

"Мені спадає на думку, що я не розповів Ханако про свій стан. Я на секунду вагаюся, вирішуючи змінити тему. Це розмова для іншого разу."

hi "…до того, як я приїхав сюди."

stop music fadeout 6.0

show hanako cover_distant
with charachange



ha "З т-тобою все гаразд?"

hi "Так, я просто згадав дещо…"

"Якщо подумати, я не повинен боятися розповісти Ханако про свій стан і час, проведений у лікарні. Судячи з її шрамів, вона, мабуть, провела чимало часу на лікарняному ліжку."

"Але чомусь я не можу про це заговорити. Принаймні не сьогодні, і не так раптово."

"Прагнучи припинити розмову, я хапаю з полиці випадкову книжку."



"Це якась книжка про найшвидші американські гірки у світі…"

"…опублікована в 1982 році. Ну, не дуже актуально, але принаймні має бути цікаво."

hi "Ну, тепер у нас обох є книжки, може, підемо сядемо?"

show hanako cover_bashful
with charachange

"Ханако, здається, приймає мій блеф, і ми прямуємо до куточка для читання в глибині бібліотеки."

hide hanako
with charaexit

"Ми обоє мовчимо; просто відкриваємо книжки й починаємо читати."

"Я намагаюся читати свою книжку, але, здається, у 1982 році американські гірки були не такими великими, як ті, що збудували за наступні десятиліття."

"Більшість із перелічених зроблені з дерева. Щось у цьому здається мені небезпечним."

"Якщо я вже збираюся кататися на чомусь потенційно небезпечному, я хочу, щоб воно було зроблено зі сталі або якогось космічного сплаву з гучними назвами на кшталт «титан» чи «рутеній»."

"Я швидко втрачаю інтерес, і мій погляд блукає по зоні для читання, зупиняючись на Ханако."

show ev hana_library_read_std:
    zoom 1.0 subpixel True truecenter
    easein 20.0 zoom 1.05
with locationskip

"Ханако виглядає заглибленою в книжку, гортаючи сторінки туди-сюди, ніби перевіряючи щойно прочитане."

"Цікаво, чи це справді ефективно, чи вона просто перевантажує себе."

"Вона несвідомо прибирає волосся з обличчя, на мить відкриваючи шрами."

"Я все ще не впевнений щодо протоколу в таких випадках. Чи доречно питати її про шрами? Або про минуле? Як довго вона була в лікарні? Чи відвідує вона лікаря досі?"

"Усе це здається питаннями, які поставив би комусь, хто щойно перевівся до твоєї школи, якби їх переклали місцевою мовою."

"Але досі ніхто не питав мене про це прямо. Ну, крім Рін, але я не думаю, що варто використовувати її як приклад належної соціальної поведінки."

"Поки що я просто триматиму язик за зубами. Якщо хтось захоче, щоб ти щось дізнався, він сам розповість. Спроби тиснути можуть лише змусити Ханако знову замкнутися в собі."

scene bg school_library_ss
show yuuko worried_up_ss at center
with shorttimeskip

yu "Ем… вибачте, що перериваю, але мені вже час зачиняти бібліотеку."

play music music_tranquil fadein 3.0

hi "Вже?"

"Я дивлюся на годинник. Якимось чином, поки я був занурений у роздуми, минуло майже дві години."

show yuuko smile_down_ss
with charachange

yu "Хочете взяти ці книжки додому? Я можу оформити їх по дорозі…"

show hanako invis:
    xpos 0.9 xanchor 0.5 ypos 1.17 yanchor 1.0
with None

show hanako basic_worry_ss:
    xpos 0.7
show bg school_library_ss at bgleft
show yuuko smile_down_ss at twoleft
with dissolvecharamove

ha "Б-будь ласка."

hi "Я закінчив. Я поверну цю книжку по дорозі. Вона виявилася не такою цікавою, як я думав спочатку."

show hanako emb_timid_ss at tworight
with dissolvecharamove

"Ханако позначає місце, де зупинилася, клаптиком паперу і встає. Дівчата йдуть до стійки, а я повертаю свою книжку на полицю, де, як мені здається, вона має бути."

show yuuko neurotic_up_ss
with charachange

"Юко сканує книжку Ханако з відпрацьованою точністю, проте все одно примудряється помилитися."

show yuuko neutral_down_ss
with charachange

yu "О… ось так. З третьої спроби вийшло. Оскільки це нехудожня література, ви можете взяти її лише на тиждень."

show hanako basic_smile_ss
with charachange

ha "Н-нічого страшного."

scene bg school_hallway2
with locationchange

"Юко вимикає бібліотечний комп'ютер і випроваджує нас за двері."

show yuuko panic_up at twoleft
show hanako def_worry at tworight
with charaenter

yu "Арґ! Я й не думала, що вже так пізно…!"

hi "Але ж ти сама сказала нам, що мусиш зачинятися…"

show yuuko worried_up
with charachange

yu "Так, але, я знаю, але це було до того, як я подивилася на час!"

show yuuko neurotic_up
with charachange

yu "Побачимося пізніше."

hide yuuko
with easeoutleft

"Юко мчить коридором, її сумочка теліпається позаду, як незграбний хвіст."

show hanako def_worry at center
show bg school_hallway2 at bgleft
with dissolvecharamove

hi "Мабуть, усі бібліотекарі справді невротики."

show hanako emb_timid
with charachange

ha "Га?"

hi "А, не зважай. Я просто подумав, що ще не зустрічав бібліотекаря, який вмів би організовувати свій час, незалежно від того, наскільки добре він знається на книжках."

show hanako basic_smile
with charachange

ha "О… я р-розумію, про що ти…"

"Ханако посміхається з цікавістю. Це не було жартом, але я, мабуть, нагадав їй якогось іншого бібліотекаря… чи щось таке…"

show hanako cover_worry
with charachange

ha "Я… я маю повертатися."

hi "Так, я теж. Не помітив, що вже так пізно. Дякую, що дозволила скласти тобі компанію."

show hanako basic_bashful
with charachange

ha "Н-нема за що."

hi "Я все одно йду до своєї кімнати в гуртожитку, тож ти не проти, якщо я піду з тобою?"

show hanako emb_blushing
with charachange

ha "Д-добре."

hide hanako
with charaexit

"Ханако вирушає вперед, і мені доводиться трохи підтюпцем наздоганяти її."

scene bg school_dormext_full_ss
with locationchange

show hanako def_worry_ss at center
with charaenter

"Ми йдемо через сади й зрештою опиняємося перед будівлями гуртожитків."

hi "Ого, ти досить швидко ходиш. Я колись грав у футбольному клубі, а ти примудряєшся випереджати мене."

stop music fadeout 6.0

show hanako emb_downsmile_ss at center
with charaenter

"Я трохи шкодую, що сказав це. Це менше пов'язано з її темпом, ніж з тим фактом, що мій стан значно погіршив мою фізичну форму."

"Реакція Ханако дивна. Я очікував незграбної спроби применшити її швидкість ходьби, але вона просто червоніє, дивлячись на свої ноги й посміхаючись."

"Між нами зависає тиша. Це часто трапляється поруч із Ханако, але цього разу відчувається трохи інакше, ніж зазвичай. Через кілька секунд я намагаюся перервати мовчання."

hi "Ось і все. Побачимося завтра на заняттях?"

show hanako emb_smile_ss
with charachange

ha "З-звісно."

hide hanako
with charaexit

"Ханако коротко махає на прощання, перш ніж проштовхнутися крізь двері гуртожитку. Я стою і дивлюся на них деякий час, перш ніж попрямувати до своєї кімнати."

scene black
with dissolve


return
label uk_H6:

scene bg school_dormhisao
with locationchange

"Цвірінькання пташок."

"Зазвичай це був би вдалий час, щоб поміркувати про красу природи."

"Але зараз 6 ранку."

play sound sfx_pillow

scene black
with Dissolve(0.2)

"Накривши голову подушкою, я втискаю обличчя в матрац, сподіваючись, що цей удар миттєво відправить мене назад у сон."

"Марно."

"Я кручуся з боку на бік, але сон просто не хоче повертатися."

play music music_daily fadein 10.0

scene bg school_dormhisao
with locationchange

"Гаразд, природо, ти перемогла. Бачиш? Я вже встаю…"

"Брак сну тисне на мозок, і є лише один засіб від цього: гарний, ситний сніданок."

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 0.5

scene bg school_cafeteria
with locationchange

"Було б непогано бути тут першим."

"Першим зануритися в гарячу купу їжі, сісти, де заманеться…"

"Було б непогано."

"Але навіть мій надзвичайно ранній підйом залишив мене позаду найстаранніших учнів."

"Мабуть, тут чимало людей, які встають рано, з тієї чи іншої причини."

"Група учнів у спортивному одязі тулиться навколо одного столу, завзято обговорюючи ігрові плани між великими ковтками їжі."

"По залу розкидані учні з сонними очима, які, мабуть, страждають від тієї ж недуги, що й я — галасливі птахи."

"І, звісно, є люди, яким справді подобається вставати так рано, ті, чиї сумки набиті підручниками та виконаними домашніми завданнями."

"Важко не зневажати таких людей, особливо коли сам ти втомлений."

"Вибравши знайоме обличчя з нечисленного натовпу, я прямую до найближчого столу."

"Ліллі сидить одна, обережно намацуючи виделкою невелику тарілку з яйцями."

"Майже шкода переривати її та її механічні рухи."

"Цікаво, чи так само сліпа людина відключається від реальності? Просто рухається за заздалегідь визначеними шаблонами, вивченими роками, так само, як зряча людина їла б, читаючи газету."

hi "Доброго ранку, Ліллі. Не очікував побачити тебе тут так рано."

show lilly basic_surprised:
    center
    ypos 1.2
with charaenter

li "О, Хісао, ти мене налякав. Я не знала, що ти снідаєш так рано."

hi "Я не снідаю. Це виняток із правил. Я б краще запізнився до школи, ніж прийшов на сніданок так рано."

show lilly basic_weaksmile
with charachange

"Ліллі ледь зітхає через мою визнану непунктуальність, поки я починаю їсти."

"Минає небагато часу, перш ніж вона знову занурюється у своє бездумне жування."

"Кожен короткий рух позбавлений енергії. Гадаю, це схоже на те, як дозволяти очам блукати під час виконання будь-якої звичайної роботи."

"Але після кількох повторень циклу «знайти їжу/з'їсти їжу» Ліллі відкладає виделку і витирає губи серветкою."

stop music fadeout 6.0
stop ambient fadeout 6.0

show lilly basic_concerned
with charachange

li "Хісао, ти не проти, якщо я поставлю тобі запитання?"

"Чорт. Все, чого я хочу — це трохи їжі та близько чотирьох годин сну. І ніхто не каже «можна поставити тобі запитання» перед простим запитанням."

hi "Звісно."

show lilly basic_listen
with charachange

li "Ти вважаєш Ханако другом?"

"Хм, це схоже на навідне запитання."

hi "Я… мабуть, так. Чому ти питаєш?"

show lilly basic_weaksmile
with charachange

li "Без особливої причини."

show lilly basic_displeased
with charachange

play music music_serene fadein 8.0

li "Хоча в мене є ще одне запитання. Чому ти вважаєш її другом?"

"Це значно вище мого рівня. Чого вона від мене чекає?"

hi "Я не зовсім впевнений. Мабуть, тому, що вона трохи інакше спілкується з людьми…"

show lilly basic_reminisce
with charachange

li "Хм. Відколи я її знаю, вона ні з ким по-справжньому не зближувалася."

show lilly basic_concerned
with charachange

li "Вона не здається зацікавленою в інших людях, і я думаю, що людей трохи лякає її зовнішність."

hi "Справді? Я думав, що подібні речі, ну, тут не заохочуються. Дискримінація і таке інше."

show lilly basic_listen
with charachange

li "Хм, якби я мала висловитися інакше…"

"Вона хмуриться в роздумах, і цей жест змушує мене трохи хвилюватися через те, що саме вона витягує зі своїх думок."

show lilly basic_weaksmile
with charachange

li "Я б сказала, що ти трохи наївний."

"Наївний? Я б образився, якби не ледь помітна цинічна посмішка на її обличчі."

hi "Я… розумію."

show lilly basic_reminisce
with charachange

li "Хоча в Ямаку сильніше відчуття спільноти порівняно з іншими школами, це далеко не означає відсутність конфліктів."

show lilly basic_displeased
with charachange

li "Зрештою, правила не можуть усунути людську природу, лише придушити її."

"Це те, що я, власне, помітив."

"Просто дрібниці, наприклад, як певні люди та групи уникають одне одного в коридорах. Це нічим не відрізняється від моєї старої школи, насправді."

"Навіть Ліллі та Шідзуне можна вважати запеклими суперницями, хоча обидві здаються досить відкритими людьми."

"Ну, принаймні Шідзуне, на яку впливає Міша; хто знає, що насправді відбувається з її пальцями та за її окулярами."

hi "Мабуть, ти маєш рацію. Але коли я вперше прийшов сюди, все було трохи шокуючим."

hi "Я постійно припускався помилок, або принаймні думав, що припускаюся. Як тоді, коли ми вперше зустрілися, і я сказав тобі «я бачу»."

hi "Я не знав, чи вважається це грубим, чи ще чимось, тому намагався просто відкинути це на задній план. Ставитися до людей якось інакше і все таке."

hi "Тож я цього не робив. Я сказав собі, що Ханако, ти і всі інші — просто звичайні люди, і намагався ігнорувати очевидне."

hi "Я розмовляв з Ханако так, ніби вона була будь-якою іншою людиною, і так ми стали друзями."

hi "Принаймні, я думаю, що саме так це сталося."

hi "Але знаєш, я відчуваю провину просто від того, що сказав щось подібне вголос. Ніби потрібно було докласти додаткових зусиль, щоб думати про Ханако, чи про тебе, чи про будь-кого тут як про звичайних людей. Не думаю, що це правильно."

show lilly basic_smileclosed
with charachange

li "Хісао, я думаю, що ти наївний, але я також думаю, що ти хороша людина. Можливо, це одна з твоїх найкращих рис."

hi "Я… мабуть… можу сприйняти це як комплімент…"

show lilly basic_smile
with charachange

li "Скажи, ти вільний сьогодні ввечері?"

hi "Якщо не рахувати домашнє завдання, то я вільний, як вітер."

show lilly basic_cheerful
with charachange

li "У такому разі, чи не хотів би ти приєднатися до мене та Ханако на чаювання?"

hi "Е-е, у мене зараз не так багато грошей, тому кудись іти — це не зовсім…"

show lilly basic_smile
with charachange

li "О, я не мала на увазі кудись іти. Просто тут, сьогодні ввечері."

hi "Тут можна заходити в класи ввечері?"

show lilly basic_giggle
with charachange

li "Ні, я не це мала на увазі. Ми з Ханако часто використовуємо мою кімнату для чаювань. Будь ласка, заходь після заходу сонця."

hi "Звісно, я не бачу з цим проблем. Який номер твоєї кімнати?"

show lilly basic_smileclosed
with charachange

li "225; кімната 25 на другому поверсі."

hi "Добре, домовилися."

show lilly basic_weaksmile
with charachange

li "Що ж, мені краще йти. Зрештою, у мене є обов'язки старости класу."

show lilly basic_cheerful at center
with dissolvecharamove

li "До вечора, Хісао."

hi "Так, побачимося пізніше."

hide lilly
with charaexit

stop music fadeout 8.0

"Стривай… мене щойно запросили в кімнату до дівчини після відбою? Це взагалі дозволено?"

"Тут є комендантська година, але я ніколи не чув про жодні правила щодо відвідувачів у гуртожитках."

"Навіть попри це, цього достатньо, щоб змусити мій втомлений мозок запрацювати."

"Додай до цього ледь теплий сніданок, і отримаєш чудовий засіб для підбадьорення."

scene bg school_scienceroom
with locationskip

"Я неохоче йду на заняття, все ще трохи схвильований перспективою порушення правил."

"Почуваюся трохи як дитина, яка планує вилізти через вікно вночі."

"Ну, можливо, це вже занадто, але коли порівнюєш запрошення на чаювання з шістьма годинами лекцій, я знаю, що перемагає."

"Міша та Шідзуне теж мало допомагають розвіяти мою нудьгу. Цього разу вони, здається, сповнені рішучості виконати завдання Муто-сенсея."

scene bg school_scienceroom_ss
with shorttimeskip

play sound sfx_normalbell

"Тим не менш, день зрештою добігає кінця."

scene bg school_dormhisao_ss
with locationskip

"Я поспішаю назад у свою кімнату, щоб вмитися і розчесатися. На щастя, я не зустрічаю Кенджі."

scene bg school_dormext_full_ss
with locationchange

"Незабаром я залишаю гуртожиток для хлопців."


return
label uk_H7:

scene bg school_girlsdormhall
with locationskip

play sound sfx_doorknock2

"Я нервово стукаю у двері з номером 225, ще раз перевіряючи годинник."

li "Це ти, Хісао? Двері відчинені, заходь."

"Голос Ліллі лунає крізь двері й заспокоює мої нерви."

"Це перший раз, коли мене запросили в кімнату до дівчини після настання темряви."

"Хоча я знаю, що за цим запрошенням немає жодних прихованих мотивів, це не заважає моїй уяві малювати різні можливості."

"Один хлопець. Дві дівчини. У кімнаті гуртожитку. З чайним сервізом."

"Коли я формулюю це так, звучить трохи підозріло."

"Зітхнувши, щоб заспокоїтися, я обережно кладу руку на ручку і відчиняю двері, витягуючи шию, щоб зазирнути всередину."

play sound sfx_dooropen

window hide

scene white
with dissolve

with Pause(0.1)

play music music_one fadein 10.0

scene ev lilly_bedroom:
    truecenter
    zoom 1.1 subpixel True
    ease 15.0 zoom 1.0
with Dissolve(4.0)

window show

"Двері відчиняються повністю, і я вперше бачу кімнату Ліллі."

"Її меблі виглядають майже антикварними, але голі стіни та рівні поверхні майже нічим не прикрашені. У центрі кімнати стоїть низький столик, на якому я бачу невеликий чайний сервіз."

"Здається, у цій кімнаті все має своє місце, за винятком, можливо, кількох стопок книг, складених біля стіни."

"Мій зір — не єдине, що отримує враження; у повітрі відчувається ледь помітний аромат. Лак для нігтів, парфуми, косметика… важко описати це інакше, ніж «дівоче»."

"Мої очі завершують швидкий огляд кімнати, перш ніж знову зупинитися на дівчатах."

scene ev lilly_bedroom_large:
    xpos -130 ypos -400 subpixel True
    acdc_warp 4.0 ypos -600
with flash

"Ліллі сидить поруч із маленьким столиком у дуже темно-синій піжамі. Темно-синя піжама з шортами, що демонструють чимало її привабливих блідих ніг."

show ev lilly_bedroom_large:
    ease 1.0 ypos -300 xpos -830
    acdc_warp 12.0 ypos 0 xpos -830
with None

"Навпроти неї сидить Ханако, одягнена в консервативну світло-рожеву сукню."

"Її руки міцно затиснуті між ногами, плечі подані вперед, а голова опущена, ніби вона намагається сховатися в ній."

"Їй це легко вдається; сукня виглядає на два розміри більшою за неї."

"Хвилі фланелі спадають з її фігури, через що вона виглядає як дитина, що грається в переодягання в батьківський одяг."

"Вона підводить очі, щоб переконатися, що це я, і на її обличчі з'являється ледь помітна посмішка, яка зникає так швидко, що я не можу бути впевнений, чи вона взагалі була."

show ev lilly_bedroom_large:
    ease 1.0 xpos -130 ypos -400
with None

li "Немає сенсу стояти в дверях, Хісао."

scene bg school_dormlilly
show lilly basic_smile_paj:
    twoleft
    ypos 1.2
show hanagown distant:
    tworight
    ypos 1.17
with locationchange

play sound sfx_doorclose
stop music fadeout 10.0

"Я роблю крок у кімнату, зачиняючи за собою двері."

show lilly basic_weaksmile_paj
with charachange

li "Ой-ой, боюся, це справді затісна кімната для нас трьох. Хочеш присісти?"

"Я повільно підходжу до столу і сідаю, намагаючись нічого не зачепити по дорозі."

"Я також не можу втриматися від швидкого погляду на декольте Ліллі, коли сідаю."

"Бути позбавленим зору було б жахливою долею."

show lilly basic_smileclosed_paj
with charachange

li "Ну що ж, як щодо чаю? Ханако, не могла б ти налити?"

show hanagown normal_blush
with charachange

ha "З… звісно. Хі… сао… чи…"

show hanagown distant_blush
with charachange

ha "…чи хочеш…"

show hanagown worry_blush
with charachange

ha "…чи хочеш ти…"

hi "Я б залюбки випив чаю. Тобі допомогти?"

show hanagown normal_blush
with charachange

ha "Н… ні, я впораюся…"

show hanagown smile
with charachange

ha "Дякую…"

play music music_dreamy fadein 2.0

show lilly basic_giggle_paj
with charachange

"Ліллі важко стримати посмішку, дивлячись на нервозність своєї подруги, і я не можу її за це винити."

show hanagown distant
with charachange

hi "День був виснажливим?"

show hanagown smile
with charachange

ha "Т… так."

show lilly basic_smileclosed_paj
with charachange

"Я розслабляюся на своєму місці, навпроти шафи."

"Ліворуч від мене — Ліллі в синьому, а праворуч сидить Ханако в рожевому."

show teaset:
    xalign 0.5 yanchor 0.5 ypos 0.6 alpha 1.0
    easein 0.5 ypos 0.5
with charaenter

"Чайний сервіз на столі виглядає мило і водночас практично; пофарбований у червоний колір із квітковим мотивом."

"Він виглядає дивно на фоні простих, але загалом вишуканих меблів Ліллі, що наводить мене на думку, що це Ханако його обрала."

"Лунає легкий «дзень», коли Ханако випадково зачіпає чайником чашку, поки наливає чай."

show hanagown worry
show lilly basic_displeased_paj
with None

show teaset:
    easeout 0.5 alpha 0.0 ypos 0.6
with Pause(0.5)

hide teaset
with None

"Вона різко вдихає; мабуть, вона дуже нервує, бо це не те, через що хтось інший переймався б."

show hanagown worry_blush
with charachange

"Ханако здригається від своєї помилки."

show lilly basic_weaksmile_paj
with charachange

li "Все добре, Ханако. Немає потреби нервувати."

show hanagown normal
with charachange

"Ханако, здається, знаходить трохи впевненості в заспокійливих, м'яких словах Ліллі і вправно наливає наступні дві чашки."

show hanagown normal_blush
with charachange

ha "Ось, Хісао… Ліллі."

"Ханако обережно ставить чашку з блюдцем переді мною та Ліллі. Я міг би звикнути до такого обслуговування."

show lilly basic_smile_paj
with charachange

li "Дякую, Ханако."

hi "Так, дякую."

show hanagown smile
with charachange

ha "Н-нема за що."

show lilly basic_smileclosed_paj
with charachange

"Ліллі шукає свою чашку і, знайшовши її, делікатно сьорбає."

"Я роблю те саме. Цей чай смакує трохи краще, ніж той, що ми зазвичай п'ємо в школі."

hi "Це смачно, зовсім не схоже на той чай, що я пив раніше…"

show lilly basic_ara_paj
show hanagown normal_blush
with charachange

li "Схоже, ти обрала правильний, Ханако."

show lilly basic_smileclosed_paj
with charachange

li "Ти добре впоралася, навіть якщо це був сміливий крок."

show hanagown smile
with charachange

"Посмішка Ханако повертається, стаючи ще ширшою."

"Навіть з її понівеченим обличчям, її сором'язливу посмішку не можна назвати інакше, як «милою»."

show hanagown distant_blush
with charachange

ha "Я рада, що тобі подобається…"

"Ханако, нарешті починаючи розслаблятися, сьорбає зі своєї чашки."

return
label uk_H7a:

$ renpy.music.set_volume(0.5, 1.0, channel="music")
window hide
nvl clear
nvl show dissolve

n "Я згадую свою розмову з Мішею іншого дня."

n "Чи варто хвилюватися через поведінку Ханако, чи вона просто сором'язлива?"

n "А ще була Ліллі сьогодні вранці."

n "Занепокоєння обох здавалося щирим, і вони знають ситуацію краще за мене."

n "Але, справді, як я можу допомогти?"

n "Я не пластичний хірург, тому не можу допомогти з її зовнішністю. І я не психолог, який може зробити її більш товариською."

n "То чого, чорт забирай, хочуть від мене Ліллі та Міша?"

n "Це дратує. Ми з Ханако швидко стаємо друзями за власним бажанням, і через це здається, що всі хочуть, аби я вирішив усі її проблеми."

n "А я гадки не маю, як це зробити."

n "Ніхто не може вилікувати моє серце, ні очі Ліллі, ні будь-кого іншого, хто тут, у цій школі."

n "Проте я не бачу нічого поганого в тому, щоб стати ближчими друзями з Ханако. Тепер, коли вона звикає до мене, мені навіть подобається проводити з нею час."

$ renpy.music.set_volume(1.0, 1.0, channel="music")
nvl clear
nvl hide dissolve
window show


return
label uk_H7b:


$ renpy.music.set_volume(0.5, 1.0, channel="music")
window hide
nvl clear
nvl show dissolve

n "\n\n\n\nЩось у цьому змушує мене задуматися про запитання Ліллі за сніданком."

n "Чому я дружу з Ханако?"

n "Ліллі здається щиро стурбованою добробутом Ханако, але я не можу нічим їй допомогти."

n "Наскільки я можу судити, її шрами не обмежують її фізично, і кожен, кого я зустрів, здається, певною мірою подолав свої вади."

n "У мене немає ніяких прихованих мотивів спілкуватися з Ханако, у нас просто спільні інтереси."

n "\nХіба цього недостатньо?"

$ renpy.music.set_volume(1.0, 1.0, channel="music")
nvl clear
nvl hide dissolve
window show



return
label uk_H7c:

show lilly basic_smile_paj
with charachange

li "Отже, Хісао, тобі подобається?"

"Слова Ліллі виривають мене з роздумів, і я витрачаю секунду, щоб усвідомити, де я знаходжуся."

"Я в кімнаті з двома дівчатами в нічному вбранні. Це те, чим варто насолодитися."

hi "Так, це розслабляє. Майже як ніби я вже не в школі. Ти часто так робиш?"

show lilly basic_weaksmile_paj
with charachange

li "Досить часто, але не так часто, як ми п'ємо чай у шкільній будівлі."

"Враховуючи, що вони роблять це майже щодня, це не великий сюрприз."

"Коли я роблю ще один ковток зі своєї чашки, я з сумом помічаю, що вона порожня."

hi "Це було смачно. Дякую, Ханако, Ліллі."

show hanagown smile
with charachange

ha "Будь ласка."

show lilly basic_smile_paj
with charachange

li "Так, завжди будь ласка, Хісао. Приємно, що тут є третя людина."

hi "Що ж, щоразу, коли вам знадобиться хтось, щоб зайняти це місце, я завжди готовий. Завжди."

"Треба бути впевненим, що доніс свою думку в таких обставинах."

stop music fadeout 8.0
show lilly basic_sleepy_paj
with charachange

"Ліллі позіхає, безуспішно прикриваючи рот рукою."

show lilly basic_weaksmile_paj
with charachange

li "Вибачте, здається, я трохи втомилася."

show hanagown distant
with charachange

ha "Думаю, ми всі трохи втомилися…"

show lilly basic_ara_paj
with charachange

li "Ой-ой, які ми проникливі сьогодні ввечері, Ханако."

show lilly basic_weaksmile_paj
with charachange

li "Нам справді варто лягати спати; завтра у всіх нас заняття."

hi "Так… мені варто йти."

show lilly basic_smile_paj
with charachange

li "Дякую за твою присутність, Хісао."

show hanagown normal
with charachange

ha "Д-дякую. Ти прийдеш ще?"

hi "Навіть ціла армія не змогла б мене зупинити."

show lilly basic_cheerful_paj
with charachange

li "Я вражена твоєю рішучістю, Хісао."

hi "У будь-якому разі, ти маєш рацію. Нам краще йти."

"Я встаю і прямую до дверей."

show hanagown normal at tworight
with dissolvecharamove

"Ханако обережно встає позаду мене."

"Я зупиняюся і повертаюся до неї."

hi "Ти йдеш зі мною?"

play music music_comedy fadein 0.5

show hanagown normal_blush
with charachange

"Ханако миттєво червоніє."

show hanagown distant_blush
with charachange

ha "Ні… я… не… ця кімната… не…"

hi "Усе гаразд, я просто жартував."

show hanagown smile
with charachange

ha "О… добре… на добраніч…"

show lilly basic_smileclosed_paj
with charachange

li "На добраніч, Ханако. На добраніч, Хісао."

hi "На добраніч усім."

"І на цьому наше чаювання закінчується."

scene bg school_girlsdormhall
with locationchange

"Я досі не впевнений, що саме Ліллі хоче, щоб я зробив для Ханако, але я не хочу її підвести."

"Я чекаю, поки двері зачиняться за нами, перш ніж повернутися до Ханако."

show hanagown distant_blush
with charaenter

hi "Гей, Ханако, знаєш, тобі не обов'язково нервувати поруч зі мною чи щось таке."

hi "Я маю на увазі, ми ж друзі, так?"

show hanagown normal_blush
with charachange

ha "Т-так. Ми… друзі."

hi "Якщо захочеш десь зависнути чи ще щось, просто дай знати. Нам ще треба провести той матч-реванш із шахів, пам'ятаєш?"

show hanagown distant
with charachange

ha "З-звісно…"

show hanagown normal
with charaenter

ha "А-але я не думаю, що ти виграєш…"

hi "Було б нецікаво, якби це було легко."

show hanagown smile
with charachange

"Ханако, здається, тихо засміялася, але це з таким же успіхом міг бути просто видих."

ha "Н-на добраніч, Хісао…"

show hanagown invis at tworight
with Dissolvemove(0.5, time_warp=_ease_out_time_warp)

hide hanako
with None

stop music fadeout 5.0

"Після цього Ханако швидко відступає у свою кімнату, розташовану поруч із кімнатою Ліллі."

"Я починаю йти назад до свого гуртожитку, але сама ходьба, здається, висмоктує з мене енергію."

scene bg school_dormhisao
with locationskip

"Я ледве добираюся до своєї кімнати, як мене накриває хвиля виснаження."

play sound sfx_switch

scene bg school_dormhisao_ni
with Dissolve(0.2)

"Я скидаю взуття, падаю на ліжко і засинаю, щойно голова торкається подушки."

scene black
with dissolve

return
label uk_H8:

scene bg school_dormhallway
with locationchange

"Я зачиняю за собою двері, готовий до чергового дня занять."

show kenji invis at twoleft
with None

show kenji neutral_close at center
with Dissolvemove(0.5, time_warp=_ease_in_time_warp)

ke "Добре спалося?"

play music music_kenji fadein 0.5

"Раптова поява Кенджі змушує мене підскочити, і я ледь не стикаюся з ним лобами."

"Я знаю, що в нього поганий зір, але тепер він знає, хто я. Йому обов'язково стояти так близько?"

show kenji neutral
with charadistant

hi "О. Так. Як немовля."

show kenji tsun
with charachange

ke "Чорт, чому люди так кажуть? Ти коли-небудь чув, як спить немовля?"

ke "Вони кричать. Усю ніч. Щоночі. Немовлята ніколи не сплять добре."

"Ну ось, мій спокійний стан зник. Треба запам'ятати, що ніколи не варто використовувати метафори з Кенджі."

hi "Гаразд, я зрозумів твою думку. Це була метафора."

show kenji neutral
with charachange

ke "Так, звісно, що завгодно. Де ти був минулої ночі? Я хотів попросити про послугу, але тебе не було поруч."

"На частку секунди я роздумую, чи не сказати Кенджі правду: що я проводив час із Ханако та Ліллі."

"На щастя, ця частка секунди минає так само швидко, як і з'явилася."

hi "Я просто гуляв. Перевіряв місцевість і все таке. Знаєш, розвідка."

show kenji happy
with charachange

ke "Молодець, добре. Я знав, що ти з тих, хто планує наперед…"

hi "У будь-якому разі, що це за послуга, про яку ти хотів попросити?"

show kenji neutral
with charachange

ke "Я збирався взяти їжу на винос, але мені потрібна була решта."

hi "Чекай, що? Я дав тобі гроші минулого тижня, а ти досі не повернув мені борг!"

show kenji tsun
with charachange

ke "Тц, а я вже почав думати, що ти крутий."

"Кенджі порпається в кишені й дістає гаманець."

"Поки він відраховує 400 єн, які винен мені, я чітко бачу принаймні дві купюри по 10 000 єн."

hi "Гей, що за чортівня? Чому ти позичаєш гроші в мене, коли в тебе стільки готівки?"

"Кенджі трохи шипить, розуміючи, що його викрили."

ke "Відчепися від мене, чувак. Це погана прикмета — розмінювати велику купюру на щось, що коштує менше ніж половина її вартості. Це правило магната."

ke "Вчорашня вечеря коштуватиме мені семи років невдач. Семи років!"

show kenji happy
with charachange

ke "Хіба ти не думаєш, що це достатня причина, щоб допомогти комусь? Я б отримав менший термін, якби просто вкрав ці речі."

"Мій здоровий глузд кричить мені сказати йому щось, але, на щастя, я стримуюся."

"Сперечатися про таке з Кенджі призведе лише до подальших і складніших дискусій."

hi "Так, мабуть, ти маєш рацію. Може, тобі варто краще планувати такі речі?"

show kenji neutral
with charachange

ke "Так, чувак, я знаю. Але в мене стільки справ, це важко. А тебе ніколи немає поруч, тож я сам по собі."

ke "Ми ж ніби брати по братерству, пам'ятаєш?"

hi "Так-так, я розумію. Глобальна змова і все таке. Буду тримати вухо гостро."

show kenji neutral_close
with charachange

"Кенджі підходить достатньо близько, щоб я відчув запах часнику з його рота."

show kenji tsun_close
with charachange

ke "Краще тримай, чувак. Ти вже проводиш тут менше часу. Це перше, що вони роблять."

ke "Вони спробують нас розділити. Розділяй і володарюй. Сунь-дзи так казав."

hi "Зрозумів. А тепер мені треба йти. У мене заняття. Ти йдеш?"

show kenji neutral_close
with charachange

ke "Ні, я втомився. Я не спав усю ніч, щоб переконатися, що нічого не станеться після того, як я розміняв ту купюру."

hi "Як завжди раціональний, бачу."

show kenji tsun_close
with charachange

ke "Та байдуже. На добраніч."

stop music fadeout 3.0

show kenji invis at twoleft
with Dissolvemove(0.5, time_warp=_ease_out_time_warp)

"Кенджі поспіхом повертається до своєї кімнати, і я чую, як він замикає двері, поки йду коридором."


return
label uk_H9:

scene bg school_dormhallway
with None

scene bg school_scienceroom
show muto smile at center
with shorttimeskip

play music music_daily fadein 4.0

mu "…ось чому деякі люди не можуть згорнути язик у трубочку, або чому їхній другий палець на нозі довший за великий."

"Муто сяє напівмісячною посмішкою, дивлячись на нас, явно пишаючись своїм поясненням про рецесивні гени."

"Однак, незалежно від того, наскільки він вражений наукою, що визначає, ким ми є, клас, здається, впав у заціпеніння."

"Чому це так, що погане пояснення може зробити навіть найцікавішу річ нікчемною?"

show muto irritated
with charachange

"Я бачу, як Муто знічується, усвідомлюючи, що нічого з того, що він говорив останні пів години, не було засвоєно."

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 4.0

"Шепіт починає порушувати тишу, і, наче лавина, рівень шуму в класі починає зростати."

show muto normal
with charachange

"Переможений, Муто знаходить кілька запитань у підручнику і береться витирати дошку."

hide muto
with charaexit

"Майже як і очікувалося, Ханако збирає свої речі й іде, щойно люди починають розмовляти та сміятися між собою."

"Початковий шок від того, що хтось так відверто прогулює, почав зникати, але це не зупиняє мене від роздумів."

"Чи йде вона тому, що не хоче, щоб з нею розмовляли? А чи це просто думка про людей навколо неї руйнує її спокій?"

play sound sfx_normalbell
$ renpy.music.set_volume(1.0, 4.0, channel="ambient")

"Перш ніж я встигаю обдумати цю тему далі, дзвонить дзвінок на обід. Цікаво, чи вона просто скористалася нагодою піти раніше."

"Звичний гамір учнів, що міняють підручники на обід, лунає по всьому класу, і поки Міша відволіклася, я хапаю свій обід і прямую до дверей."

stop ambient fadeout 1.0

scene bg school_miyagi
show lilly basic_smileclosed:
    center
    ypos 1.2
with locationskip

"Ліллі вже сидить у чаювальні, накриваючи на стіл для свого обіду наодинці."

hi "Отже, Ханако тут немає?"

show lilly basic_smile
with charachange

li "О, Хісао, як ти? Боюся, я не бачила Ханако з самого ранку."

"Точно, Ханако і Ліллі живуть поруч."

"Чомусь мені здається, що їхні ранкові розмови трохи більш приземлені, ніж марення Кенджі."

hi "Це дивно. Вона пішла з уроку раніше, тож я подумав, що вона прийде сюди."

show lilly basic_displeased
with charachange

li "Отже, вона все ще йде з уроку раніше…"

hi "Га? Так, я бачив, як вона робила це кілька разів."

show lilly basic_sad
with charachange

stop music fadeout 7.0

"Ліллі трохи опускає голову, і її тон голосу помітно пригнічений. Це дуже нагадує когось, хто звик чути погані новини."

li "Я була впевнена, що вона перестане це робити, як тільки ви двоє станете друзями."

show lilly basic_weaksmile
with charachange

li "У кожного свій темп, я гадаю."

hi "Ну, я якраз сьогодні про це думав. Чому саме вона йде?"

show lilly basic_reminisce
with charachange

li "Я сама не зовсім впевнена. Особисто я думаю, що це тому, що вона не хоче опинитися в ситуації, де їй доведеться комусь відповідати."

"У мене виникає спогад про нашу першу зустріч, коли мені здалося, що вона виглядає як загнаний звір. Можливо, я був недалеко від істини."

hi "Але вона, здається, нормально розмовляє з тобою, і зі мною… трохи…"

show lilly basic_displeased
with charachange

li "Це трохи складніше. Уявляю, що перше, про що її запитують більшість людей — це її шрами та те, що сталося."

li "Вона рідко говорить про це зі мною, але я бачу, що вона не любить згадувати те, що сталося тоді."

show lilly basic_reminisce
with charachange

li "Йти з уроку і тікати від обговорень — це її превентивний удар, якщо хочеш."

hi "Га… то як це пояснює те, що вона розмовляє зі мною?"

show lilly basic_weaksmile
with charachange

li "Ти сам сказав це вчора за сніданком; ти намагався ігнорувати її шрами. Як тільки вона побачила, що ти не збираєшся запитувати її про це, вона відкрилася тобі."

hi "Гм, мабуть, ти маєш рацію. Можливо. Не знаю. Ти знаєш її краще за мене, тому я повірю тобі на слово."

play music music_normal fadein 3.0

show lilly basic_giggle
with charachange

li "Я б не переймалася цим. Впевнена, ти скоро дізнаєшся її так само добре, як і я."

show lilly basic_smileclosed
with charachange

li "Я вітаю перспективу того, що у неї з'явиться новий друг, і у вас обох такі схожі інтереси…"

hi "Ну, я навряд чи назву читання командним видом спорту. Хоча приємно мати компанію."

show lilly basic_smile
with charachange

li "Ось саме про це я й кажу. Ханако в душі все ще звичайна людина. Вона теж хоче компанії в такі моменти."

hi "Га, розумію. Здається. Чесно кажучи, ви обидві все ще трохи збиваєте мене з пантелику."

show lilly basic_smileclosed
with charachange

li "Це цілком природно, Хісао. Ми знаємо одне одного лише короткий час; нерозумно очікувати, що ти зрозумієш нас, так само як ми не можемо зрозуміти тебе."

show lilly basic_weaksmile
with charachange

li "Але це половина задоволення від того, щоб стати друзями, чи не так?"

hi "Так, так і є."

show lilly basic_giggle
with charachange

li "Хоча… я припускаю, є ще питання того, що ми протилежної статі. Чоловіки та жінки, здається, досить часто збивають одне одного з пантелику."

"Вона каже це з легким смішком, знаходячи розвагу в дивних дрібницях життя."

show lilly basic_cheerful
with charachange

li "Сподіваюся, ти не проти, але я почну їсти."

hi "Ні, звісно, я думаю, теж щось з'їм. У мене є кілька книг, які я хочу повернути до бібліотеки перед початком занять, тож мені краще поспішити."

show lilly basic_smileclosed
with charachange

li "Ти, мабуть, знайдеш Ханако там. Якщо побачиш її, чи не міг би ти сказати їй зайти до моєї кімнати пізніше ввечері? Я хотіла б поговорити з нею."

hi "Ти не прийдеш?"

show lilly basic_weaksmile
with charachange

li "На жаль, у мене пізніше збори представників класу, тож я піду, як тільки закінчу свій обід."

hi "Добре тоді, якщо я не побачу її в бібліотеці, то скажу їй на уроці. Впевнений, вона повернеться після обіду."

"Ми замовкаємо, починаючи їсти, і я знаходжу хвилинку, щоб обміркувати нашу розмову."

"Я завжди думав, що сором'язливість Ханако була просто через те, що вона соромиться своїх шрамів."

"Але це досить поверхневий погляд на неї."

"Якраз тоді, коли я подумав, що зміг розгледіти крізь туман Ліллі та Ханако, я усвідомлюю, що я ще більш розгублений, ніж на початку."

"Ліллі швидко закінчує свій обід, гостро усвідомлюючи свої збори. Я її не звинувачую."

"Шідзуне, швидше за все, буде там, і я сумніваюся, що вона хоче дати їй привід для чергової суперечки."

show lilly basic_smile
with charachange

li "Мені час іти. Завтра в той самий час?"

hi "У той самий час, на тому самому місці. Мені теж краще йти; не хочу ризикувати запізнитися."

show lilly cane_smileclosed
with charachange

show lilly cane_smileclosed at center
with charamove

stop music fadeout 4.0

"Ліллі лагідно посміхається, бере свою тростину і виходить у коридор."


return
label uk_H10:

scene bg school_hallway2
with locationchange

"Я повертаюся спиною до Ліллі, коли ми прямуємо в протилежних напрямках. З якоїсь причини я сподіваюся, що вона не вплутається в чергову сварку з Шідзуне."

"Як би мені не подобалася Ліллі, Шідзуне та Міша зіграли неабияку роль у тому, щоб допомогти мені адаптуватися, навіть якщо половина наших розмов — це ледь приховані спроби вербування."

"З іншого боку, я ледь знаю кожну з них. Можливо, вони раніше були лідерами якогось таємного товариства, але їхня любов одне до одного розлучила їх…"

"Боже, мені треба перестати читати дешеву літературу. Вона роз'їдає мій мозок. Або це, або мені треба з'їхати від Кенджі та його поганого впливу."

"Сумно, що я вже не можу відрізнити одне від іншого."

scene bg school_library at right
with locationskip

play music music_happiness fadein 2.0

"Я опускаю свої книги в отвір для повернення, і вони з приємним стукотом падають у візок."

play sound sfx_impact2

show yuuko panic_up
with vpunch

"Юко, однак, не здається такою враженою, як я."

yu "Х-Хісао! Ти мене налякав!"

hi "Вибач, я думав, ти вже мала звикнути до цього. Чи рівень грамотності тут настільки низький, що ніхто не бере книг?"

show yuuko worried_up
with charachange

yu "Га? Ні, я думаю, всі тут вміють читати…"

hi "Так… забудь."

"Є битви, які ніколи не виграти. Спроби пояснити жарти — одна з них. Мій тато навчив мене цього на гіркому досвіді."

hi "Скажи, Юко, ти не бачила Ханако? Вона пішла з уроку раніше, але її не було в її звичному місці для схованок."

show yuuko closedhappy_down
with charachange

yu "Мені здається, я бачила, як вона прослизнула сюди перед обідом…"

show yuuko panic_up
with charachange

yu "О! Але мені не можна нікому про це казати!"

hi "Я щойно сказав тобі, що бачив, як вона пішла, не треба хвилюватися…"

show yuuko smile_down
with charachange

yu "О… звісно. Вона, мабуть, десь у глибині."

hi "Дякую. Отримували якісь нові книги останнім часом?"

show yuuko worried_up
with charachange

yu "Ні, вибач. Але я дам тобі знати, коли ми це зробимо."

hi "Добре."

"Якщо я щось і знаю про бібліотекарів, незалежно від того, працюють вони повний чи неповний день, так це те, що вони цінують людей, які щиро цікавляться їхньою роботою."

hide yuuko
with charaexit

show bg school_library at Fullpan(10.0, dir="left")
with None

"Я йду вже знайомим шляхом до куточка для читання Ханако, дорогою вибираючи кілька книг."

"Іноді мені важко знайти серед полиць книгу, яка б мене зацікавила. Ім'я автора та назва з двох слів мало що означають у морі схожих слів."

"З цієї причини я іноді перечитую книги, які вже читав у минулому. Краще зробити ставку на улюблене, ніж на «темну конячку»."

"Незнайома назва від знайомого автора визирає серед корінців сусідніх книг, тож я знімаю її з полиці."

"Принаймні я не перечитую старий матеріал."

scene ev hana_library_read_std
with locationskip

"Як і очікувалося, Ханако сидить на своєму кріслі-мішку, заглибившись у примірник «Танцюй, танцюй, танцюй»."

hi "Привіт, Ханако. Як справи?"

"Я борюся з бажанням запитати, чому вона пішла з уроку раніше. Якщо підозри Ліллі були правильними, то запитання про це могло б дати протилежний ефект."

"Краще поки що залишити це. Іноді найкращий спосіб отримати відповідь від когось — це ніколи не ставити запитання."

show ev hana_library_smile_std
with charachange

ha "Привіт, Х-Хісао. У мене все добре."

"Щось не так, і через кілька секунд я розумію, що саме. Ханако посміхається."

"Вона виглядає так, ніби рада мене бачити. Це приємна зміна після звичайної, інстинктивно переляканої реакції, і я сподіваюся, що бачитиму це частіше, коли ми краще пізнаємо одне одного."

hi "Радий це чути. Як книга? Кажуть, вона вражає."

ha "В-вона хороша… здається."

ha "Я т-тільки почала, тому ще не з-знаю."

hi "Зрозуміло. Дай знати, як вона тобі; можливо, я позичу її, коли ти закінчиш."

ha "З-звісно."

"До кінця обідньої перерви залишилося хвилин п'ятнадцять. Недостатньо, щоб по-справжньому зануритися в книгу, але забагато, щоб просто стояти без діла."

show ev hana_library_read_std
with charachange

"А Ханако вже повернулася до читання, тож сумніваюся, що зможу з нею поговорити."

"Ну що ж, краще влаштуюся зручніше."

play sound sfx_pillow

"Я вмощуюсь у кріслі-мішку і розгортаю свою книгу."

"Знайомий стиль автора впадає в очі з першого ж рядка. Коли речення перетворюються на абзаци, я починаю трохи розслаблятися."

stop music fadeout 8.0

"Але як би я не намагався, я ніяк не можу налаштуватися на атмосферу книги."

"Частково це через брак часу, але більш відволікаючим фактором є Ханако."

show ev hana_library_std
with charachange

show ev hana_library_read_std
with charachange

"Кожні десять секунд вона визирає з-за своєї книги, але коли наші погляди зустрічаються, вона швидко ховається за обкладинкою."

"Мабуть, вона все ж таки хотіла про щось поговорити."

scene bg school_library
with locationskip

hi "Що таке? Ти виглядаєш як лугова собачка на варті."

show hanako emb_blushing:
    center
    ypos 1.17
with charaenter

ha "Н-… нічого."

hi "Я вже казав тобі, «нічого» означає «щось», коли ти кажеш це таким тоном."

show hanako cover_worry
with charachange

"Ханако трохи совається у своєму кріслі-мішку, сподіваючись, що змінивши позу, вона знайде потрібні слова."

show hanako emb_downsad
with charachange

ha "Я… я потрапила в аварію."

hi "Аварію? Щойно? Ти в порядку?"

show hanako emb_sad
with charachange

"Ханако хитає головою, її волосся розсипається по плечах пасмами аметисту на фоні блідої та темної шкіри."

show hanako emb_downsad
with charachange

ha "Н-ні. Коли я була м-молодшою."

play music music_hanako

"Усвідомлення врізається в мене, наче вантажівка."

ha "Коли я… коли я була…"

hi "Все добре, Ханако, ти не мусиш нічого мені розповідати, якщо не хочеш…"

"Вона знову хитає головою."

show hanako emb_sad
with charachange

ha "Н-ні. Я хочу… я маю тобі розповісти."

scene ev hanako_crayon1:
    zoom 1.0 subpixel True truecenter
    linear 20.0 zoom 1.05
with locationskip

ha "Коли я була маленькою… я потрапила в пожежу."

ha "М-мій будинок з-згорів, і я ледь… я ледь не загинула."

show ev hanako_crayon2:
    linear 8.0 zoom 1.05
with charachange

ha "П-після того… я була одна…"

scene bg school_library
show hanako emb_downsad_close:
    center
    ypos 1.1
with locationskip

"Очі Ханако виблискують у тьмяному світлі бібліотеки, і я простягаю руку, щоб взяти її за руку."

hi "Все добре, Ханако. Ти не мусиш продовжувати."

show hanako emb_sad_close
with charachange

ha "А-але… я маю…"

hi "Чому? Що змусило тебе про це заговорити?"

show hanako cover_distant_close
with charachange

ha "М-минулої ночі Ліллі р-розповіла мені про твоє серце…"

show hanako cover_worry_close
with charachange

ha "І я… я подумала, що це н-нечесно."

hi "Нечесно?"

show hanako emb_blushing_close
with charachange

ha "Т-те, що я знала про тебе, б-але ти не знав про мене…"

"Я трохи стискаю руку Ханако."

hi "Не дурій. Але так, у мене вада серця."

"Я трохи нахиляюся до Ханако."

hi "Чого я не сказав Ліллі, так це того, що мій перший напад стався, коли дівчина зізналася мені в коханні."

"Я трохи посміхаюся, щоб розрядити обстановку."

show hanako cover_worry_close
with charachange

ha "П-правда?"

hi "Правда. Хоча я давно про неї нічого не чув, тож, мабуть, усе закінчено."

"Я знаю, що все закінчено. Немає іншого способу витлумачити те, що сталося під час нашої останньої зустрічі. Певною мірою те, що я більше нічого про неї не чув, допомогло мені рухатися далі після того періоду мого життя."

hi "Отже, тепер ми обидва знаємо трохи більше одне про одного. Але ти не мусиш говорити про речі, про які не хочеш."

"Насправді, мені навіть трохи ніяково думати про той випадок. Я майже знову відчуваю запах лікарняного дезінфектора, що пече в носі."

"Уявляю, що Ханако зараз переживає те саме."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve

n "\n\nКоли я був у лікарні, я одного разу зайшов у опікове відділення, і лише одного разу. Мені було нудно, тому я пішов на прогулянку всіма відділеннями."

n "Я пройшов через онкологію і думав, що витримаю, але коли дістався до опікового відділення, я розвернувся і пішов назад до свого ліжка."

n "Подумати тільки, що Ханако провела місяці в такому місці, відчуваючи лише запах гниючої шкіри, сильного дезінфектора та стерилізованого повітря."

n "Найважчих пацієнтів тримали в ізольованих боксах, куди не могли потрапити сторонні предмети. Це означало б жодного читання."

n "\nЯ б збожеволів, якби в мене не було книг у лікарні."

n "І вона сказала, що була одна…"

n "Чи померли її батьки? Треба буде запитати про це Ліллі. Уявляю, як я можу ненароком сказати якусь дурість."

stop music fadeout 2.0

nvl clear
nvl hide dissolve

show hanako emb_timid_close
with charachange

window show

ha "Д-дякую, Хісао."

show hanako emb_downtimid_close
with charachange

ha "Я… я небагатьом людям про це розповідала."

hi "Чесно кажучи, я теж небагатьом розповідав про свої… обставини."

show hanako cover_smile_close
with charachange

ha "Т-тоді я теж нікому н-не розповім."

hi "Домовилися."

play sound sfx_warningbell

"Я змінюю хват на руці Ханако на рукостискання, коли у вікні лунають попереджувальні дзвони."

hi "Ну що ж, тоді нам краще повертатися на урок, га?"

show hanako basic_bashful_close
with charachange

ha "З-звісно."
$ renpy.music.set_volume(1.0, 0.0, channel="music")

window hide

return

# Decompiled by unrpyc {v2.0.4}: https://github.com/CensoredUsername/unrpyc master 02/23/26
# Modified by JoeLurmel with INCETON
