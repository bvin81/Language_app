"""
3. és 4. osztályos tartalom hozzáadása a meglévő adatbázishoz.
Futtatás: python add_grade3_4.py
"""
from app.database import engine, SessionLocal, Base
from app.models.lesson import Lesson
from app.models.word import Word
from app.models.user import User
from app.models.grammar import GrammarExercise
from app.models.listening import ListeningExercise
from app.models.reading import ReadingExercise, ReadingQuestion


def add_grade3_4():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        existing = db.query(Lesson).filter(Lesson.grade.in_([3, 4])).count()
        if existing > 0:
            print(f"Már létezik {existing} db 3-4. osztályos lecke. Kihagyás.")
            return

        # =============================================
        # === 3. OSZTÁLY - Román leckék (intermediate) ===
        # =============================================

        # --- Lecke: Vremea (Időjárás) ---
        l_ro3_1 = Lesson(
            title="Vremea (Időjárás)",
            description="Időjáráshoz kapcsolódó szavak románul",
            language="romanian",
            level="intermediate",
            grade=3,
            order=1
        )
        db.add(l_ro3_1)
        db.flush()

        db.add_all([
            Word(lesson_id=l_ro3_1.id, word="soare", translation="nap (égitest)",
                 example_sentence="Soarele strălucește azi. (Ma süt a nap.)"),
            Word(lesson_id=l_ro3_1.id, word="ploaie", translation="eső",
                 example_sentence="Afară plouă tare. (Odakint erősen esik.)"),
            Word(lesson_id=l_ro3_1.id, word="ninsoare", translation="hóesés",
                 example_sentence="Ninsoaratea aduce zăpadă albă. (A hóesés fehér havat hoz.)"),
            Word(lesson_id=l_ro3_1.id, word="vânt", translation="szél",
                 example_sentence="Vântul bate tare azi. (Ma erősen fúj a szél.)"),
            Word(lesson_id=l_ro3_1.id, word="nor", translation="felhő",
                 example_sentence="Pe cer sunt mulți nori. (Az égen sok felhő van.)"),
        ])

        db.add_all([
            GrammarExercise(
                lesson_id=l_ro3_1.id,
                exercise_type="fill_blank",
                question="Afară ___. (Esik az eső.)",
                correct_answer="plouă",
                wrong_answers="ninge,bate vântul,e soare",
                explanation="'Plouă' = esik. Ez az eső igéje románul.",
                difficulty=2
            ),
            GrammarExercise(
                lesson_id=l_ro3_1.id,
                exercise_type="multiple_choice",
                question="'Süt a nap' románul:",
                correct_answer="Soarele strălucește",
                wrong_answers="Plouă tare,Ninge afară,Bate vântul",
                explanation="'Soarele strălucește' = süt a nap.",
                difficulty=2
            ),
            GrammarExercise(
                lesson_id=l_ro3_1.id,
                exercise_type="word_order",
                question="azi,vântul,tare,bate",
                correct_answer="Vântul bate tare azi",
                wrong_answers="Azi bate vântul tare,Tare vântul bate azi",
                explanation="Szórend: Alany + ige + határozó + időhatározó",
                difficulty=3
            ),
        ])

        db.add_all([
            ListeningExercise(
                lesson_id=l_ro3_1.id,
                audio_url="/static/audio/ro_vremea_1.mp3",
                transcript="Azi este o zi însorită și caldă.",
                question="Milyen ma az idő?",
                correct_answer="Napos és meleg",
                wrong_answers="Esős és hideg,Havas,Szeles",
                difficulty=2,
                duration_seconds=3
            ),
            ListeningExercise(
                lesson_id=l_ro3_1.id,
                audio_url="/static/audio/ro_vremea_2.mp3",
                transcript="Plouă și bate vântul. Luați umbrela!",
                question="Mit javasolnak?",
                correct_answer="Vigyél esernyőt",
                wrong_answers="Maradj otthon,Öltözz melegen,Menj sétálni",
                difficulty=2,
                duration_seconds=4
            ),
        ])

        r_ro3_1 = ReadingExercise(
            lesson_id=l_ro3_1.id,
            title="Anotimpurile",
            content="""România are patru anotimpuri frumoase.

Primăvara, florile înfloresc și păsările cântă. Vremea este blândă și plăcută.

Vara este cald și însorit. Copiii se joacă afară și merg la piscină sau la mare.

Toamna, frunzele devin galbene și roșii. Plouă mai des și vremea se răcește.

Iarna ninge și e frig. Copiii fac oameni de zăpadă și se dau cu sania.

Fiecare anotimp are farmecul său!""",
            difficulty=2
        )
        db.add(r_ro3_1)
        db.flush()

        db.add_all([
            ReadingQuestion(reading_id=r_ro3_1.id,
                            question="Hány évszak van Romániában?",
                            correct_answer="Négy",
                            wrong_answers="Két,Három,Öt"),
            ReadingQuestion(reading_id=r_ro3_1.id,
                            question="Mi jellemzi a tavaszt?",
                            correct_answer="Virágok nyílnak és madarak énekelnek",
                            wrong_answers="Havazik és fagyos,Forró és napos,Levelek hullanak"),
            ReadingQuestion(reading_id=r_ro3_1.id,
                            question="Mit csinálnak a gyerekek nyáron?",
                            correct_answer="Kint játszanak és uszodába mennek",
                            wrong_answers="Szánkóznak,Iskolába járnak,Alszanak"),
            ReadingQuestion(reading_id=r_ro3_1.id,
                            question="Mit csinálnak a gyerekek télen?",
                            correct_answer="Hóembert építenek és szánkóznak",
                            wrong_answers="Úsznak,Fociznak,Virágokat szednek"),
        ])

        # --- Lecke: Corpul uman (Emberi test) ---
        l_ro3_2 = Lesson(
            title="Corpul uman (Emberi test)",
            description="Testrészek nevei románul",
            language="romanian",
            level="intermediate",
            grade=3,
            order=2
        )
        db.add(l_ro3_2)
        db.flush()

        db.add_all([
            Word(lesson_id=l_ro3_2.id, word="cap", translation="fej",
                 example_sentence="Am o pălărie pe cap. (Van egy sapkám a fejemen.)"),
            Word(lesson_id=l_ro3_2.id, word="mână", translation="kéz",
                 example_sentence="Spăl mâinile înainte de masă. (Étkezés előtt kezet mosok.)"),
            Word(lesson_id=l_ro3_2.id, word="picior", translation="láb",
                 example_sentence="Alerg cu picioarele. (Lábaimmal futok.)"),
            Word(lesson_id=l_ro3_2.id, word="ochi", translation="szem",
                 example_sentence="Am ochii albaștri. (Kék szemeim vannak.)"),
            Word(lesson_id=l_ro3_2.id, word="ureche", translation="fül",
                 example_sentence="Ascult muzică cu urechile. (Fülleimmel hallgatom a zenét.)"),
        ])

        db.add_all([
            GrammarExercise(
                lesson_id=l_ro3_2.id,
                exercise_type="fill_blank",
                question="Spăl ___ înainte de masă. (Étkezés előtt kezet mosok.)",
                correct_answer="mâinile",
                wrong_answers="picioarele,capul,ochii",
                explanation="'Mâinile' = a kezek (határozott névelővel, többes szám).",
                difficulty=2
            ),
            GrammarExercise(
                lesson_id=l_ro3_2.id,
                exercise_type="multiple_choice",
                question="'Kék szemeim vannak' románul:",
                correct_answer="Am ochii albaștri",
                wrong_answers="Am ochi albastru,Ochii mei albastru,Am albastri ochi",
                explanation="'Am ochii albaștri' = kék szemeim vannak. Többes számban 'albaștri'.",
                difficulty=2
            ),
            GrammarExercise(
                lesson_id=l_ro3_2.id,
                exercise_type="word_order",
                question="muzică,urechile,cu,ascult",
                correct_answer="Ascult muzică cu urechile",
                wrong_answers="Cu urechile ascult muzică,Muzică ascult cu urechile",
                explanation="'Ascult muzică cu urechile' = Fülleimmel hallgatom a zenét.",
                difficulty=3
            ),
        ])

        db.add_all([
            ListeningExercise(
                lesson_id=l_ro3_2.id,
                audio_url="/static/audio/ro_corp_1.mp3",
                transcript="Mă dor ochii pentru că citesc mult.",
                question="Miért fáj a szeme?",
                correct_answer="Mert sokat olvas",
                wrong_answers="Mert sírt,Mert fáradt,Mert beteg",
                difficulty=2,
                duration_seconds=4
            ),
            ListeningExercise(
                lesson_id=l_ro3_2.id,
                audio_url="/static/audio/ro_corp_2.mp3",
                transcript="Spăl mâinile cu apă și săpun.",
                question="Mivel mos kezet?",
                correct_answer="Vízzel és szappannal",
                wrong_answers="Csak vízzel,Kendővel,Alkohollal",
                difficulty=2,
                duration_seconds=3
            ),
        ])

        r_ro3_2 = ReadingExercise(
            lesson_id=l_ro3_2.id,
            title="Sănătatea corpului",
            content="""Corpul nostru are nevoie de îngrijire în fiecare zi.

Dimineața, ne spălăm pe față și pe mâini. Folosim apă și săpun. Ne periăm dinții de două ori pe zi.

Ochii noștri obosesc dacă privim prea mult la ecran. Este bine să facem pauze.

Picioarele ne duc peste tot. De aceea trebuie să purtăm pantofi buni.

Urechile noastre aud sunete. Nu trebuie să ascultăm muzică prea tare.

Un corp sănătos înseamnă o viață fericită!""",
            difficulty=2
        )
        db.add(r_ro3_2)
        db.flush()

        db.add_all([
            ReadingQuestion(reading_id=r_ro3_2.id,
                            question="Mivel mosunk kezet?",
                            correct_answer="Vízzel és szappannal",
                            wrong_answers="Csak vízzel,Kendővel,Krémmel"),
            ReadingQuestion(reading_id=r_ro3_2.id,
                            question="Naponta hányszor kell fogat mosni?",
                            correct_answer="Kétszer",
                            wrong_answers="Egyszer,Háromszor,Egyszer sem"),
            ReadingQuestion(reading_id=r_ro3_2.id,
                            question="Mikor fáradnak el a szemek?",
                            correct_answer="Ha sokat nézünk a képernyőre",
                            wrong_answers="Ha sokat alszunk,Ha sokat eszünk,Ha sokat futunk"),
            ReadingQuestion(reading_id=r_ro3_2.id,
                            question="Miért kell jó cipőt viselni?",
                            correct_answer="Mert a lábak mindenhova visznek",
                            wrong_answers="Mert szép,Mert olcsó,Mert divatos"),
        ])

        # --- Lecke: Transport (Közlekedés) ---
        l_ro3_3 = Lesson(
            title="Transport (Közlekedés)",
            description="Közlekedési eszközök románul",
            language="romanian",
            level="intermediate",
            grade=3,
            order=3
        )
        db.add(l_ro3_3)
        db.flush()

        db.add_all([
            Word(lesson_id=l_ro3_3.id, word="mașină", translation="autó",
                 example_sentence="Tatăl meu conduce o mașină roșie. (Apám egy piros autót vezet.)"),
            Word(lesson_id=l_ro3_3.id, word="autobuz", translation="busz",
                 example_sentence="Merg la școală cu autobuzul. (Busszal járok iskolába.)"),
            Word(lesson_id=l_ro3_3.id, word="tren", translation="vonat",
                 example_sentence="Trenul merge repede. (A vonat gyorsan megy.)"),
            Word(lesson_id=l_ro3_3.id, word="bicicletă", translation="kerékpár",
                 example_sentence="Pedalez cu bicicleta în parc. (Kerékpározom a parkban.)"),
            Word(lesson_id=l_ro3_3.id, word="avion", translation="repülőgép",
                 example_sentence="Avionul zboară sus pe cer. (A repülőgép magasan repül.)"),
        ])

        db.add_all([
            GrammarExercise(
                lesson_id=l_ro3_3.id,
                exercise_type="fill_blank",
                question="Merg la școală cu ___. (Busszal járok iskolába.)",
                correct_answer="autobuzul",
                wrong_answers="mașina,trenul,bicicleta",
                explanation="'Cu autobuzul' = busszal. Az eszközhatározó 'cu' elöljáróval képzett.",
                difficulty=2
            ),
            GrammarExercise(
                lesson_id=l_ro3_3.id,
                exercise_type="multiple_choice",
                question="'A repülőgép magasan repül' románul:",
                correct_answer="Avionul zboară sus",
                wrong_answers="Avionul merge jos,Avion zboară,Sus zboară avionul",
                explanation="'Avionul zboară sus' = a repülőgép magasan repül.",
                difficulty=2
            ),
            GrammarExercise(
                lesson_id=l_ro3_3.id,
                exercise_type="word_order",
                question="repede,trenul,merge,foarte",
                correct_answer="Trenul merge foarte repede",
                wrong_answers="Merge trenul repede foarte,Foarte repede trenul merge",
                explanation="'Trenul merge foarte repede' = a vonat nagyon gyorsan megy.",
                difficulty=3
            ),
        ])

        db.add_all([
            ListeningExercise(
                lesson_id=l_ro3_3.id,
                audio_url="/static/audio/ro_transport_1.mp3",
                transcript="Mergem la bunici cu trenul. Durează două ore.",
                question="Hogyan utaznak a nagyszülőkhöz?",
                correct_answer="Vonattal",
                wrong_answers="Autóval,Busszal,Repülővel",
                difficulty=2,
                duration_seconds=4
            ),
            ListeningExercise(
                lesson_id=l_ro3_3.id,
                audio_url="/static/audio/ro_transport_2.mp3",
                transcript="Îmi place să merg cu bicicleta în parc.",
                question="Hol szeret kerékpározni?",
                correct_answer="A parkban",
                wrong_answers="Az utcán,Az iskolánál,A kertben",
                difficulty=2,
                duration_seconds=4
            ),
        ])

        r_ro3_3 = ReadingExercise(
            lesson_id=l_ro3_3.id,
            title="Cum mergem la școală?",
            content="""Copiii merg la școală în diferite moduri.

Unii copii merg pe jos dacă școala este aproape de casă. Este sănătos să mergi pe jos.

Alți copii merg cu autobuzul. Autobuzul oprește la mai multe stații. Este convenabil și ieftin.

Unii părinți aduc copiii cu mașina. Este rapid, dar poate fi aglomerat în trafic.

Copiii mai mari pot merge cu bicicleta. Bicicleta este bună pentru sănătate și pentru mediu.

Cel mai modern mijloc de transport este metroul în orașele mari.

Tu cum mergi la școală?""",
            difficulty=2
        )
        db.add(r_ro3_3)
        db.flush()

        db.add_all([
            ReadingQuestion(reading_id=r_ro3_3.id,
                            question="Mikor jó gyalog menni iskolába?",
                            correct_answer="Ha az iskola közel van",
                            wrong_answers="Ha messze van,Ha esik az eső,Ha hideg van"),
            ReadingQuestion(reading_id=r_ro3_3.id,
                            question="Milyen a busz?",
                            correct_answer="Kényelmes és olcsó",
                            wrong_answers="Gyors és drága,Lassú és drága,Egészséges"),
            ReadingQuestion(reading_id=r_ro3_3.id,
                            question="Miért jó a kerékpár?",
                            correct_answer="Jó az egészségnek és a környezetnek",
                            wrong_answers="Mert gyors,Mert olcsó,Mert biztonságos"),
            ReadingQuestion(reading_id=r_ro3_3.id,
                            question="Mi a legmodernebb közlekedési eszköz a szövegben?",
                            correct_answer="A metró",
                            wrong_answers="A vonat,A repülő,A villamos"),
        ])

        # =============================================
        # === 3. OSZTÁLY - Angol leckék (intermediate) ===
        # =============================================

        # --- Lecke: Weather ---
        l_en3_1 = Lesson(
            title="Weather (Időjárás)",
            description="Weather words in English",
            language="english",
            level="intermediate",
            grade=3,
            order=4
        )
        db.add(l_en3_1)
        db.flush()

        db.add_all([
            Word(lesson_id=l_en3_1.id, word="sunny", translation="napos",
                 example_sentence="It is sunny today. (Ma napos az idő.)"),
            Word(lesson_id=l_en3_1.id, word="rainy", translation="esős",
                 example_sentence="It is rainy outside. (Kint esős az idő.)"),
            Word(lesson_id=l_en3_1.id, word="snowy", translation="havas",
                 example_sentence="It is snowy in winter. (Télen havas az idő.)"),
            Word(lesson_id=l_en3_1.id, word="windy", translation="szeles",
                 example_sentence="It is very windy today. (Ma nagyon szeles van.)"),
            Word(lesson_id=l_en3_1.id, word="cloudy", translation="felhős",
                 example_sentence="The sky is cloudy. (Az ég felhős.)"),
        ])

        db.add_all([
            GrammarExercise(
                lesson_id=l_en3_1.id,
                exercise_type="fill_blank",
                question="It is ___ today. I need my umbrella. (Esős van ma.)",
                correct_answer="rainy",
                wrong_answers="sunny,snowy,windy",
                explanation="'Rainy' = esős. Esernyő esős időben kell.",
                difficulty=2
            ),
            GrammarExercise(
                lesson_id=l_en3_1.id,
                exercise_type="multiple_choice",
                question="'Ma napos és meleg van' angolul:",
                correct_answer="It is sunny and warm today",
                wrong_answers="Today sunny warm is,It sunny today is,Is it sunny today",
                explanation="'It is + melléknév' az időjárás kifejezése angolul.",
                difficulty=2
            ),
            GrammarExercise(
                lesson_id=l_en3_1.id,
                exercise_type="word_order",
                question="windy,very,today,is,it",
                correct_answer="It is very windy today",
                wrong_answers="Very windy it is today,Today it is very windy",
                explanation="Időjárás angolul: It is + (very) + melléknév + időhatározó",
                difficulty=3
            ),
        ])

        db.add_all([
            ListeningExercise(
                lesson_id=l_en3_1.id,
                audio_url="/static/audio/en_weather_1.mp3",
                transcript="It is cloudy and cold. You should wear a coat.",
                question="Milyen az idő?",
                correct_answer="Felhős és hideg",
                wrong_answers="Napos és meleg,Havas,Esős és szeles",
                difficulty=2,
                duration_seconds=4
            ),
            ListeningExercise(
                lesson_id=l_en3_1.id,
                audio_url="/static/audio/en_weather_2.mp3",
                transcript="I love sunny days. I can play outside.",
                question="Mit csinál napos napokon?",
                correct_answer="Kint játszik",
                wrong_answers="Otthon marad,Tévét néz,Alszik",
                difficulty=2,
                duration_seconds=3
            ),
        ])

        r_en3_1 = ReadingExercise(
            lesson_id=l_en3_1.id,
            title="The Four Seasons",
            content="""There are four seasons in a year: spring, summer, autumn, and winter.

In spring, the weather is warm and flowers bloom. Birds come back and sing beautiful songs.

Summer is hot and sunny. Children swim in the pool and play outside every day.

In autumn, leaves turn yellow and red. It gets windy and rainy. We wear jackets.

Winter is cold and snowy. We build snowmen and drink hot chocolate.

Every season is special in its own way!""",
            difficulty=2
        )
        db.add(r_en3_1)
        db.flush()

        db.add_all([
            ReadingQuestion(reading_id=r_en3_1.id,
                            question="How many seasons are there?",
                            correct_answer="Four",
                            wrong_answers="Two,Three,Five"),
            ReadingQuestion(reading_id=r_en3_1.id,
                            question="What do children do in summer?",
                            correct_answer="Swim and play outside",
                            wrong_answers="Build snowmen,Wear jackets,Stay inside"),
            ReadingQuestion(reading_id=r_en3_1.id,
                            question="What happens to leaves in autumn?",
                            correct_answer="They turn yellow and red",
                            wrong_answers="They bloom,They grow,They disappear"),
            ReadingQuestion(reading_id=r_en3_1.id,
                            question="What do we drink in winter?",
                            correct_answer="Hot chocolate",
                            wrong_answers="Juice,Water,Lemonade"),
        ])

        # --- Lecke: Body Parts ---
        l_en3_2 = Lesson(
            title="Body Parts (Testrészek)",
            description="Parts of the human body in English",
            language="english",
            level="intermediate",
            grade=3,
            order=5
        )
        db.add(l_en3_2)
        db.flush()

        db.add_all([
            Word(lesson_id=l_en3_2.id, word="head", translation="fej",
                 example_sentence="I wear a hat on my head. (Sapkát hordok a fejemen.)"),
            Word(lesson_id=l_en3_2.id, word="hand", translation="kéz",
                 example_sentence="I wash my hands before eating. (Étkezés előtt kezet mosok.)"),
            Word(lesson_id=l_en3_2.id, word="leg", translation="láb",
                 example_sentence="I run with my legs. (A lábaimmal futok.)"),
            Word(lesson_id=l_en3_2.id, word="eye", translation="szem",
                 example_sentence="I see with my eyes. (A szemeimmel látok.)"),
            Word(lesson_id=l_en3_2.id, word="ear", translation="fül",
                 example_sentence="I hear music with my ears. (A füleimmel hallom a zenét.)"),
        ])

        db.add_all([
            GrammarExercise(
                lesson_id=l_en3_2.id,
                exercise_type="fill_blank",
                question="I see with my ___. (A szemeimmel látok.)",
                correct_answer="eyes",
                wrong_answers="ears,hands,legs",
                explanation="'Eyes' = szemek (többes szám). 'I see with my eyes.'",
                difficulty=2
            ),
            GrammarExercise(
                lesson_id=l_en3_2.id,
                exercise_type="multiple_choice",
                question="'Két kezem van' angolul:",
                correct_answer="I have two hands",
                wrong_answers="I has two hands,I have two hand,My two hands have",
                explanation="'I have' = nekem van. 'Hands' = kezek (többes szám).",
                difficulty=2
            ),
            GrammarExercise(
                lesson_id=l_en3_2.id,
                exercise_type="word_order",
                question="my,ears,hear,I,with",
                correct_answer="I hear with my ears",
                wrong_answers="With my ears I hear,My ears I hear with",
                explanation="Szórend: Alany + ige + with + my + testrész",
                difficulty=3
            ),
        ])

        db.add_all([
            ListeningExercise(
                lesson_id=l_en3_2.id,
                audio_url="/static/audio/en_body_1.mp3",
                transcript="My eyes hurt because I watch too much TV.",
                question="Miért fáj a szeme?",
                correct_answer="Mert sokat tévézik",
                wrong_answers="Mert sokat olvas,Mert beteg,Mert sokat sír",
                difficulty=2,
                duration_seconds=4
            ),
            ListeningExercise(
                lesson_id=l_en3_2.id,
                audio_url="/static/audio/en_body_2.mp3",
                transcript="Touch your head with your right hand.",
                question="Melyik kezét kell felvenni?",
                correct_answer="A jobb kezét",
                wrong_answers="A bal kezét,Mindkettőt,Egyiket sem",
                difficulty=2,
                duration_seconds=3
            ),
        ])

        r_en3_2 = ReadingExercise(
            lesson_id=l_en3_2.id,
            title="Taking Care of Your Body",
            content="""Our body is very important. We must take care of it every day.

We wash our hands with soap and water before meals. This keeps us healthy.

We brush our teeth twice a day. Healthy teeth help us eat and speak well.

Our eyes need rest. We should not look at screens for too long. Reading books is better.

Our ears can be hurt by loud music. We should listen at a low volume.

Exercise is great for our legs and whole body. Walking and running keep us strong.

A healthy body makes a happy life!""",
            difficulty=2
        )
        db.add(r_en3_2)
        db.flush()

        db.add_all([
            ReadingQuestion(reading_id=r_en3_2.id,
                            question="When do we wash our hands?",
                            correct_answer="Before meals",
                            wrong_answers="After meals,In the morning,Before bed"),
            ReadingQuestion(reading_id=r_en3_2.id,
                            question="How often do we brush our teeth?",
                            correct_answer="Twice a day",
                            wrong_answers="Once a day,Three times,Every hour"),
            ReadingQuestion(reading_id=r_en3_2.id,
                            question="What can hurt our ears?",
                            correct_answer="Loud music",
                            wrong_answers="Reading books,Washing,Sleeping"),
            ReadingQuestion(reading_id=r_en3_2.id,
                            question="What keeps our legs strong?",
                            correct_answer="Walking and running",
                            wrong_answers="Sleeping,Watching TV,Eating"),
        ])

        # --- Lecke: Transport (Közlekedés) angolul ---
        l_en3_3 = Lesson(
            title="Transport (Közlekedés)",
            description="Means of transport in English",
            language="english",
            level="intermediate",
            grade=3,
            order=6
        )
        db.add(l_en3_3)
        db.flush()

        db.add_all([
            Word(lesson_id=l_en3_3.id, word="car", translation="autó",
                 example_sentence="My dad drives a blue car. (Apám kék autót vezet.)"),
            Word(lesson_id=l_en3_3.id, word="bus", translation="busz",
                 example_sentence="I go to school by bus. (Busszal megyek iskolába.)"),
            Word(lesson_id=l_en3_3.id, word="train", translation="vonat",
                 example_sentence="The train is fast. (A vonat gyors.)"),
            Word(lesson_id=l_en3_3.id, word="bicycle", translation="kerékpár",
                 example_sentence="I ride my bicycle to the park. (Kerékpárral megyek a parkba.)"),
            Word(lesson_id=l_en3_3.id, word="airplane", translation="repülőgép",
                 example_sentence="The airplane flies high. (A repülőgép magasan repül.)"),
        ])

        db.add_all([
            GrammarExercise(
                lesson_id=l_en3_3.id,
                exercise_type="fill_blank",
                question="I go to school ___ bus. (Busszal megyek iskolába.)",
                correct_answer="by",
                wrong_answers="with,on,in",
                explanation="'By bus/train/car' = busszal/vonattal/autóval. 'By' az elöljáró közlekedésnél.",
                difficulty=2
            ),
            GrammarExercise(
                lesson_id=l_en3_3.id,
                exercise_type="multiple_choice",
                question="'A repülőgép magasan repül' angolul:",
                correct_answer="The airplane flies high",
                wrong_answers="The airplane is fly high,Airplane fly high,The airplane high flies",
                explanation="'Flies' = repül (egyes szám 3. személy). Ige + határozó.",
                difficulty=2
            ),
            GrammarExercise(
                lesson_id=l_en3_3.id,
                exercise_type="word_order",
                question="bicycle,ride,my,I,park,to,the",
                correct_answer="I ride my bicycle to the park",
                wrong_answers="My bicycle I ride to the park,I to the park ride my bicycle",
                explanation="Szórend: Alany + ige + tárgy + hová",
                difficulty=3
            ),
        ])

        db.add_all([
            ListeningExercise(
                lesson_id=l_en3_3.id,
                audio_url="/static/audio/en_transport_1.mp3",
                transcript="We traveled to the city by train. It took one hour.",
                question="Hogyan utaztak a városba?",
                correct_answer="Vonattal",
                wrong_answers="Autóval,Busszal,Repülővel",
                difficulty=2,
                duration_seconds=4
            ),
            ListeningExercise(
                lesson_id=l_en3_3.id,
                audio_url="/static/audio/en_transport_2.mp3",
                transcript="I love riding my bicycle. It is healthy and fun.",
                question="Miért szeret kerékpározni?",
                correct_answer="Mert egészséges és szórakoztató",
                wrong_answers="Mert gyors,Mert olcsó,Mert könnyű",
                difficulty=2,
                duration_seconds=3
            ),
        ])

        r_en3_3 = ReadingExercise(
            lesson_id=l_en3_3.id,
            title="Getting Around",
            content="""People use different types of transport every day.

Cars are the most common transport. They are fast and comfortable. But they cause pollution.

Buses are good for many people. They carry lots of passengers at once. They are cheap.

Trains are great for long distances. They are fast and safe. Many people use them to travel between cities.

Bicycles are healthy and eco-friendly. They do not pollute the air. Many cities have bicycle lanes.

Airplanes are the fastest transport. They can travel between countries in hours.

Choosing the right transport is important for our environment!""",
            difficulty=2
        )
        db.add(r_en3_3)
        db.flush()

        db.add_all([
            ReadingQuestion(reading_id=r_en3_3.id,
                            question="What is the most common transport?",
                            correct_answer="Cars",
                            wrong_answers="Buses,Trains,Bicycles"),
            ReadingQuestion(reading_id=r_en3_3.id,
                            question="What is good about buses?",
                            correct_answer="They carry many passengers and are cheap",
                            wrong_answers="They are the fastest,They are eco-friendly,They go underwater"),
            ReadingQuestion(reading_id=r_en3_3.id,
                            question="Why are bicycles eco-friendly?",
                            correct_answer="They do not pollute the air",
                            wrong_answers="They are fast,They are cheap,They carry many people"),
            ReadingQuestion(reading_id=r_en3_3.id,
                            question="What is the fastest transport?",
                            correct_answer="Airplanes",
                            wrong_answers="Trains,Cars,Buses"),
        ])

        # =============================================
        # === 4. OSZTÁLY - Román leckék (advanced) ===
        # =============================================

        # --- Lecke: Natura (Természet) ---
        l_ro4_1 = Lesson(
            title="Natura (Természet)",
            description="Természeti jelenségek és helyek románul",
            language="romanian",
            level="advanced",
            grade=4,
            order=1
        )
        db.add(l_ro4_1)
        db.flush()

        db.add_all([
            Word(lesson_id=l_ro4_1.id, word="munte", translation="hegy",
                 example_sentence="Munții Carpați sunt frumoși. (A Kárpátok szépek.)"),
            Word(lesson_id=l_ro4_1.id, word="râu", translation="folyó",
                 example_sentence="Râul Dunărea este lung. (A Duna folyó hosszú.)"),
            Word(lesson_id=l_ro4_1.id, word="pădure", translation="erdő",
                 example_sentence="Pădurea adăpostește multe animale. (Az erdő sok állatot rejt.)"),
            Word(lesson_id=l_ro4_1.id, word="mare", translation="tenger",
                 example_sentence="Marea Neagră este la est de România. (A Fekete-tenger Románia keleti részén van.)"),
            Word(lesson_id=l_ro4_1.id, word="câmp", translation="mező",
                 example_sentence="Pe câmp cresc flori sălbatice. (A mezőn vadvirágok nőnek.)"),
        ])

        db.add_all([
            GrammarExercise(
                lesson_id=l_ro4_1.id,
                exercise_type="fill_blank",
                question="Munții ___ sunt cei mai înalți din România. (A Kárpátok a legmagasabbak Romániában.)",
                correct_answer="Carpați",
                wrong_answers="Alpi,Pirinei,Tatri",
                explanation="'Munții Carpați' = a Kárpátok. Románia fő hegyrendszere.",
                difficulty=3
            ),
            GrammarExercise(
                lesson_id=l_ro4_1.id,
                exercise_type="multiple_choice",
                question="'Az erdő sok állatot rejt' románul:",
                correct_answer="Pădurea adăpostește multe animale",
                wrong_answers="Pădure adăpostesc multe animale,Pădurea adăpostești animale,Animale adăpostește pădurea",
                explanation="'Adăpostește' = rejt/befogad (egyes szám 3. személy).",
                difficulty=3
            ),
            GrammarExercise(
                lesson_id=l_ro4_1.id,
                exercise_type="word_order",
                question="sălbatice,câmp,pe,cresc,flori",
                correct_answer="Pe câmp cresc flori sălbatice",
                wrong_answers="Flori sălbatice pe câmp cresc,Cresc pe câmp sălbatice flori",
                explanation="'Pe câmp cresc flori sălbatice' = a mezőn vadvirágok nőnek.",
                difficulty=3
            ),
        ])

        db.add_all([
            ListeningExercise(
                lesson_id=l_ro4_1.id,
                audio_url="/static/audio/ro_natura_1.mp3",
                transcript="România are munți, câmpii și o ieșire la mare.",
                question="Mi mindene van Romániának?",
                correct_answer="Hegy, síkság és tengerpart",
                wrong_answers="Csak hegyek,Csak tengerpart,Csak folyók",
                difficulty=3,
                duration_seconds=5
            ),
            ListeningExercise(
                lesson_id=l_ro4_1.id,
                audio_url="/static/audio/ro_natura_2.mp3",
                transcript="Pădurea este importantă pentru oxigen și biodiversitate.",
                question="Miért fontos az erdő?",
                correct_answer="Az oxigenért és a biodiverzitásért",
                wrong_answers="Mert szép,Mert hűvös,Mert nagy",
                difficulty=3,
                duration_seconds=5
            ),
        ])

        r_ro4_1 = ReadingExercise(
            lesson_id=l_ro4_1.id,
            title="Natura României",
            content="""România este o țară cu o natură diversă și frumoasă.

La nord și în centrul țării se găsesc Carpații. Aceștia sunt cei mai importanți munți ai României. Vârful Moldoveanu este cel mai înalt, cu 2544 de metri.

România are mai multe râuri mari. Dunărea formează granița sudică a țării și se varsă în Marea Neagră prin Delta Dunării.

Delta Dunării este una dintre cele mai mari delte din lume. Acolo trăiesc mii de specii de păsări și pești.

Pădurile acoperă o treime din suprafața României. Ele adăpostesc urși, lupi și cerbi.

România are și câmpii fertile în sud și est. Acolo se cultivă grâu, porumb și floarea-soarelui.

Natura României trebuie protejată pentru generațiile viitoare!""",
            difficulty=3
        )
        db.add(r_ro4_1)
        db.flush()

        db.add_all([
            ReadingQuestion(reading_id=r_ro4_1.id,
                            question="Melyik a legmagasabb hegycsúcs Romániában?",
                            correct_answer="Moldoveanu (2544 m)",
                            wrong_answers="Negoiu,Omu,Retezat"),
            ReadingQuestion(reading_id=r_ro4_1.id,
                            question="Hova ömlik a Duna?",
                            correct_answer="A Fekete-tengerbe",
                            wrong_answers="A Dunába,Az Adriai-tengerbe,A Földközi-tengerbe"),
            ReadingQuestion(reading_id=r_ro4_1.id,
                            question="Milyen állatok élnek a romániai erdőkben?",
                            correct_answer="Medvék, farkasok és szarvasok",
                            wrong_answers="Oroszlánok és tigrisek,Elefántok,Pingvinek"),
            ReadingQuestion(reading_id=r_ro4_1.id,
                            question="Mit termesztenek a déli és keleti síkságokon?",
                            correct_answer="Búzát, kukoricát és napraforgót",
                            wrong_answers="Rizsét és gyapotot,Kávét és teát,Narancsot és citromot"),
        ])

        # --- Lecke: Timp liber (Szabadidő) ---
        l_ro4_2 = Lesson(
            title="Timp liber (Szabadidő)",
            description="Szabadidős tevékenységek románul",
            language="romanian",
            level="advanced",
            grade=4,
            order=2
        )
        db.add(l_ro4_2)
        db.flush()

        db.add_all([
            Word(lesson_id=l_ro4_2.id, word="lectură", translation="olvasás",
                 example_sentence="Îmi place lectura cărților de aventuri. (Szeretem kalandregények olvasását.)"),
            Word(lesson_id=l_ro4_2.id, word="muzică", translation="zene",
                 example_sentence="Cânt la pian în fiecare zi. (Minden nap zongorázom.)"),
            Word(lesson_id=l_ro4_2.id, word="sport", translation="sport",
                 example_sentence="Sportul este sănătos pentru toți. (A sport mindenkinek egészséges.)"),
            Word(lesson_id=l_ro4_2.id, word="desen", translation="rajzolás",
                 example_sentence="Desenez peisaje și animale. (Tájakat és állatokat rajzolok.)"),
            Word(lesson_id=l_ro4_2.id, word="fotografie", translation="fényképezés",
                 example_sentence="Fac fotografii cu aparatul foto. (Fényképezőgéppel fotózok.)"),
        ])

        db.add_all([
            GrammarExercise(
                lesson_id=l_ro4_2.id,
                exercise_type="fill_blank",
                question="În timpul liber, eu ___. (A szabadidőmben olvasok.)",
                correct_answer="citesc",
                wrong_answers="cânta,desenat,fotografiat",
                explanation="'Citesc' = olvasok (egyes szám 1. személy, jelen idő).",
                difficulty=3
            ),
            GrammarExercise(
                lesson_id=l_ro4_2.id,
                exercise_type="multiple_choice",
                question="'Minden nap zongorázom' románul:",
                correct_answer="Cânt la pian în fiecare zi",
                wrong_answers="Cântez pianul fiecare zi,Pian cânt zi fiecare,La pian cânt fiecare",
                explanation="'Cânt la pian' = zongorázom. 'În fiecare zi' = minden nap.",
                difficulty=3
            ),
            GrammarExercise(
                lesson_id=l_ro4_2.id,
                exercise_type="word_order",
                question="animale,peisaje,desenez,și",
                correct_answer="Desenez peisaje și animale",
                wrong_answers="Peisaje și animale desenez,Și animale desenez peisaje",
                explanation="'Desenez peisaje și animale' = tájakat és állatokat rajzolok.",
                difficulty=3
            ),
        ])

        db.add_all([
            ListeningExercise(
                lesson_id=l_ro4_2.id,
                audio_url="/static/audio/ro_timplibe_1.mp3",
                transcript="În weekenduri prefer să citesc și să ascult muzică.",
                question="Mit szeret csinálni hétvégén?",
                correct_answer="Olvasni és zenét hallgatni",
                wrong_answers="Sportolni,Főzni,Tévézni",
                difficulty=3,
                duration_seconds=5
            ),
            ListeningExercise(
                lesson_id=l_ro4_2.id,
                audio_url="/static/audio/ro_timplibe_2.mp3",
                transcript="Sportul mă ajută să fiu sănătos și fericit.",
                question="Miért sportol?",
                correct_answer="Hogy egészséges és boldog legyen",
                wrong_answers="Mert versenyez,Mert muszáj,Mert unalmas",
                difficulty=3,
                duration_seconds=4
            ),
        ])

        r_ro4_2 = ReadingExercise(
            lesson_id=l_ro4_2.id,
            title="Hobby-urile mele",
            content="""Bună! Mă numesc Radu și am unsprezece ani. Am mai multe hobby-uri pe care le iubesc.

Cel mai mult îmi place să citesc. Citesc cărți de aventuri, știință și istorie. Când citesc, călătoresc în lumi imaginare.

De asemenea, cânt la chitară. Am început să învăț acum doi ani. Exersez în fiecare zi câte 30 de minute.

În weekenduri, joc fotbal cu prietenii mei în parc. Sportul mă ajută să fiu activ și să am prieteni noi.

Uneori desenez și pictez. Îmi place să creez portrete și peisaje. Particip și la concursuri de desen la școală.

Vara, fac fotografie. Fotografiez flori, animale și locuri frumoase.

Hobby-urile sunt importante pentru că ne fac fericiți și ne ajută să ne exprimăm creativ!""",
            difficulty=3
        )
        db.add(r_ro4_2)
        db.flush()

        db.add_all([
            ReadingQuestion(reading_id=r_ro4_2.id,
                            question="Hány éves Radu?",
                            correct_answer="Tizenegy éves",
                            wrong_answers="Tíz éves,Tizenkét éves,Kilenc éves"),
            ReadingQuestion(reading_id=r_ro4_2.id,
                            question="Mióta tanul gitározni?",
                            correct_answer="Két éve",
                            wrong_answers="Egy éve,Három éve,Öt éve"),
            ReadingQuestion(reading_id=r_ro4_2.id,
                            question="Kivel focizik hétvégén?",
                            correct_answer="Barátaival",
                            wrong_answers="Egyedül,Testvérével,Apjával"),
            ReadingQuestion(reading_id=r_ro4_2.id,
                            question="Miben vesz részt az iskolában?",
                            correct_answer="Rajzversenyeken",
                            wrong_answers="Zenei versenyeken,Focitornákon,Fotóversenyeken"),
        ])

        # =============================================
        # === 4. OSZTÁLY - Angol leckék (advanced) ===
        # =============================================

        # --- Lecke: Nature ---
        l_en4_1 = Lesson(
            title="Nature (Természet)",
            description="Nature and geography words in English",
            language="english",
            level="advanced",
            grade=4,
            order=3
        )
        db.add(l_en4_1)
        db.flush()

        db.add_all([
            Word(lesson_id=l_en4_1.id, word="mountain", translation="hegy",
                 example_sentence="The mountain is covered with snow. (A hegy hóval borított.)"),
            Word(lesson_id=l_en4_1.id, word="river", translation="folyó",
                 example_sentence="The river flows to the sea. (A folyó a tengerbe folyik.)"),
            Word(lesson_id=l_en4_1.id, word="forest", translation="erdő",
                 example_sentence="The forest is home to many animals. (Az erdő sok állat otthona.)"),
            Word(lesson_id=l_en4_1.id, word="ocean", translation="óceán",
                 example_sentence="The ocean is very deep. (Az óceán nagyon mély.)"),
            Word(lesson_id=l_en4_1.id, word="valley", translation="völgy",
                 example_sentence="The valley is green and beautiful. (A völgy zöld és szép.)"),
        ])

        db.add_all([
            GrammarExercise(
                lesson_id=l_en4_1.id,
                exercise_type="fill_blank",
                question="The river ___ to the sea. (A folyó a tengerbe folyik.)",
                correct_answer="flows",
                wrong_answers="flow,flowing,flowed",
                explanation="'Flows' = folyik (egyes szám 3. személy, jelen idő). -s végződés.",
                difficulty=3
            ),
            GrammarExercise(
                lesson_id=l_en4_1.id,
                exercise_type="multiple_choice",
                question="'Az erdő sok állat otthona' angolul:",
                correct_answer="The forest is home to many animals",
                wrong_answers="The forest are home to many animals,Forest is home many animals,Many animals is home the forest",
                explanation="'Is home to' = otthona valaminek. Egyes számú alany után 'is'.",
                difficulty=3
            ),
            GrammarExercise(
                lesson_id=l_en4_1.id,
                exercise_type="word_order",
                question="deep,the,very,ocean,is",
                correct_answer="The ocean is very deep",
                wrong_answers="Very deep the ocean is,Is the ocean very deep",
                explanation="Szórend: The + alany + is + very + melléknév",
                difficulty=3
            ),
        ])

        db.add_all([
            ListeningExercise(
                lesson_id=l_en4_1.id,
                audio_url="/static/audio/en_nature_1.mp3",
                transcript="The Amazon is the largest rainforest in the world.",
                question="Mi az Amazonas?",
                correct_answer="A világ legnagyobb esőerdeje",
                wrong_answers="A világ legnagyobb folyója,A világ legmagasabb hegye,Egy óceán neve",
                difficulty=3,
                duration_seconds=4
            ),
            ListeningExercise(
                lesson_id=l_en4_1.id,
                audio_url="/static/audio/en_nature_2.mp3",
                transcript="Mountains are formed by movements of the Earth's crust.",
                question="Hogyan keletkeznek a hegyek?",
                correct_answer="A Föld kérgének mozgásával",
                wrong_answers="Vulkánoktól,Vízzel,Széltől",
                difficulty=3,
                duration_seconds=5
            ),
        ])

        r_en4_1 = ReadingExercise(
            lesson_id=l_en4_1.id,
            title="Our Planet Earth",
            content="""Earth is our home. It is a beautiful planet with many different landscapes.

About 71 percent of Earth's surface is covered by water. The Pacific Ocean is the largest ocean. It is bigger than all the continents put together!

The remaining 29 percent is land. There are seven continents: Europe, Asia, Africa, North America, South America, Australia, and Antarctica.

The tallest mountain in the world is Mount Everest. It is 8,849 meters high and is located in Asia.

The Amazon River in South America is one of the longest rivers in the world. The Amazon Rainforest around it is home to millions of plants and animals.

We must protect our planet. Climate change threatens forests, oceans, and wildlife.

Every small action counts – turn off lights, recycle, and plant trees!""",
            difficulty=3
        )
        db.add(r_en4_1)
        db.flush()

        db.add_all([
            ReadingQuestion(reading_id=r_en4_1.id,
                            question="What percentage of Earth is covered by water?",
                            correct_answer="71 percent",
                            wrong_answers="50 percent,29 percent,90 percent"),
            ReadingQuestion(reading_id=r_en4_1.id,
                            question="How many continents are there?",
                            correct_answer="Seven",
                            wrong_answers="Five,Six,Eight"),
            ReadingQuestion(reading_id=r_en4_1.id,
                            question="How tall is Mount Everest?",
                            correct_answer="8,849 meters",
                            wrong_answers="5,000 meters,10,000 meters,2,544 meters"),
            ReadingQuestion(reading_id=r_en4_1.id,
                            question="What threatens forests and oceans?",
                            correct_answer="Climate change",
                            wrong_answers="Too much rain,New buildings,Animals"),
        ])

        # --- Lecke: Hobbies ---
        l_en4_2 = Lesson(
            title="Hobbies (Hobbi)",
            description="Free time activities in English",
            language="english",
            level="advanced",
            grade=4,
            order=4
        )
        db.add(l_en4_2)
        db.flush()

        db.add_all([
            Word(lesson_id=l_en4_2.id, word="reading", translation="olvasás",
                 example_sentence="Reading books improves your vocabulary. (A könyvolvasás bővíti a szókincsedet.)"),
            Word(lesson_id=l_en4_2.id, word="painting", translation="festés",
                 example_sentence="I love painting landscapes. (Imádom a tájképfestést.)"),
            Word(lesson_id=l_en4_2.id, word="cooking", translation="főzés",
                 example_sentence="Cooking is a useful skill. (A főzés hasznos készség.)"),
            Word(lesson_id=l_en4_2.id, word="gardening", translation="kertészkedés",
                 example_sentence="Gardening is relaxing. (A kertészkedés megnyugtató.)"),
            Word(lesson_id=l_en4_2.id, word="photography", translation="fényképezés",
                 example_sentence="Photography captures beautiful moments. (A fényképezés megörökíti a szép pillanatokat.)"),
        ])

        db.add_all([
            GrammarExercise(
                lesson_id=l_en4_2.id,
                exercise_type="fill_blank",
                question="Reading books ___ your vocabulary. (A könyvolvasás bővíti a szókincsedet.)",
                correct_answer="improves",
                wrong_answers="improve,improving,improved",
                explanation="'Improves' = fejleszti (egyes szám 3. személy -s végződéssel). 'Reading' alanyként egyes számú.",
                difficulty=3
            ),
            GrammarExercise(
                lesson_id=l_en4_2.id,
                exercise_type="multiple_choice",
                question="'A főzés hasznos készség' angolul:",
                correct_answer="Cooking is a useful skill",
                wrong_answers="Cooking are a useful skill,Cook is useful skill,A useful skill cooking",
                explanation="'Cooking' főnévként egyes számú → 'is'. 'A useful skill' = egy hasznos készség.",
                difficulty=3
            ),
            GrammarExercise(
                lesson_id=l_en4_2.id,
                exercise_type="word_order",
                question="beautiful,captures,moments,photography",
                correct_answer="Photography captures beautiful moments",
                wrong_answers="Beautiful moments photography captures,Captures photography beautiful moments",
                explanation="Szórend: Alany + ige + melléknév + tárgy",
                difficulty=3
            ),
        ])

        db.add_all([
            ListeningExercise(
                lesson_id=l_en4_2.id,
                audio_url="/static/audio/en_hobbies_1.mp3",
                transcript="My favorite hobby is painting. I paint every weekend.",
                question="Mi a kedvenc hobbyja?",
                correct_answer="Festés",
                wrong_answers="Olvasás,Főzés,Kertészkedés",
                difficulty=3,
                duration_seconds=4
            ),
            ListeningExercise(
                lesson_id=l_en4_2.id,
                audio_url="/static/audio/en_hobbies_2.mp3",
                transcript="Gardening teaches patience and connects us with nature.",
                question="Mit tanít a kertészkedés?",
                correct_answer="Türelmet és a természettel való kapcsolatot",
                wrong_answers="Főzési technikákat,Fotózást,Zenét",
                difficulty=3,
                duration_seconds=5
            ),
        ])

        r_en4_2 = ReadingExercise(
            lesson_id=l_en4_2.id,
            title="Why Hobbies Are Important",
            content="""Hobbies are activities we do in our free time for fun. They are very important for our well-being.

Having a hobby helps reduce stress. When we do something we love, we forget our worries and relax.

Hobbies also help us learn new skills. Cooking teaches us to be creative and careful. Gardening teaches patience. Reading improves our language and imagination.

Some hobbies can even become careers. Many famous photographers, writers, and chefs started as hobbyists.

Hobbies connect us with other people. We can join clubs, take classes, or share our work online. This way, we make new friends who share our interests.

There is no wrong hobby. Whether you like drawing, playing chess, collecting stamps, or dancing, what matters is that you enjoy it.

Try new things and discover what you love!""",
            difficulty=3
        )
        db.add(r_en4_2)
        db.flush()

        db.add_all([
            ReadingQuestion(reading_id=r_en4_2.id,
                            question="What is a hobby?",
                            correct_answer="An activity we do in free time for fun",
                            wrong_answers="School work,A job,A chore"),
            ReadingQuestion(reading_id=r_en4_2.id,
                            question="How do hobbies help us?",
                            correct_answer="They reduce stress and teach new skills",
                            wrong_answers="They make us tired,They cost money,They are boring"),
            ReadingQuestion(reading_id=r_en4_2.id,
                            question="What does gardening teach?",
                            correct_answer="Patience",
                            wrong_answers="Speed,Creativity,Language"),
            ReadingQuestion(reading_id=r_en4_2.id,
                            question="How can hobbies connect us with people?",
                            correct_answer="By joining clubs, taking classes, or sharing online",
                            wrong_answers="By staying home alone,By watching TV,By sleeping"),
        ])

        db.commit()

        print("3. és 4. osztályos tartalom sikeresen hozzáadva!")
        print()
        print("3. osztály (intermediate):")
        print("  Román: Vremea, Corpul uman, Transport")
        print("  Angol: Weather, Body Parts, Transport")
        print()
        print("4. osztály (advanced):")
        print("  Román: Natura, Timp liber")
        print("  Angol: Nature, Hobbies")
        print()
        print("Összesen 10 új lecke, 50 szó, 30 nyelvtani feladat,")
        print("20 hallásértés feladat, 10 szöveg 40 kérdéssel.")

    except Exception as e:
        print(f"Hiba: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    print("3-4. osztályos tartalom hozzáadása...")
    add_grade3_4()
