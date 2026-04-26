"""
Adatbázis inicializálás mintaadatokkal
Futtatás: python -m app.init_db
"""
from app.database import engine, SessionLocal, Base
from app.models.lesson import Lesson
from app.models.word import Word
from app.models.user import User
from app.models.grammar import GrammarExercise
from app.models.listening import ListeningExercise
from app.models.reading import ReadingExercise, ReadingQuestion


def init_db():
    # Táblák létrehozása
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        # Ellenőrizzük, van-e már adat
        if db.query(Lesson).count() > 0:
            print("Az adatbázis már tartalmaz adatokat.")
            return

        # === 1. OSZTÁLY - Román leckék ===

        # Lecke 1: Család (román)
        lesson1 = Lesson(
            title="Familia (Család)",
            description="Alapvető családtagok nevei románul",
            language="romanian",
            level="beginner",
            grade=1,
            order=1
        )
        db.add(lesson1)
        db.flush()

        words1 = [
            Word(lesson_id=lesson1.id, word="mamă", translation="anya",
                 example_sentence="Mama mea este profesoară. (Az anyám tanár.)"),
            Word(lesson_id=lesson1.id, word="tată", translation="apa",
                 example_sentence="Tatăl meu lucrează la spital. (Az apám kórházban dolgozik.)"),
            Word(lesson_id=lesson1.id, word="frate", translation="testvér (fiú)",
                 example_sentence="Am un frate mai mare. (Van egy bátyám.)"),
            Word(lesson_id=lesson1.id, word="soră", translation="testvér (lány)",
                 example_sentence="Sora mea merge la școală. (A nővérem iskolába jár.)"),
            Word(lesson_id=lesson1.id, word="bunic", translation="nagyapa",
                 example_sentence="Bunicul meu are 70 de ani. (A nagyapám 70 éves.)"),
        ]
        db.add_all(words1)

        # Lecke 2: Számok (román)
        lesson2 = Lesson(
            title="Numere (Számok)",
            description="Számok 1-től 10-ig románul",
            language="romanian",
            level="beginner",
            grade=1,
            order=2
        )
        db.add(lesson2)
        db.flush()

        words2 = [
            Word(lesson_id=lesson2.id, word="unu", translation="egy",
                 example_sentence="Am un câine. (Van egy kutyám.)"),
            Word(lesson_id=lesson2.id, word="doi", translation="kettő",
                 example_sentence="Am doi frați. (Két testvérem van.)"),
            Word(lesson_id=lesson2.id, word="trei", translation="három",
                 example_sentence="Sunt trei copii. (Három gyerek van.)"),
            Word(lesson_id=lesson2.id, word="patru", translation="négy",
                 example_sentence="Casa are patru camere. (A háznak négy szobája van.)"),
            Word(lesson_id=lesson2.id, word="cinci", translation="öt",
                 example_sentence="Sunt cinci zile în săptămână de școală. (Öt iskolai nap van egy héten.)"),
        ]
        db.add_all(words2)

        # Lecke 3: Színek (román)
        lesson3 = Lesson(
            title="Culori (Színek)",
            description="Alapvető színek románul",
            language="romanian",
            level="beginner",
            grade=1,
            order=3
        )
        db.add(lesson3)
        db.flush()

        words3 = [
            Word(lesson_id=lesson3.id, word="roșu", translation="piros",
                 example_sentence="Mărul este roșu. (Az alma piros.)"),
            Word(lesson_id=lesson3.id, word="albastru", translation="kék",
                 example_sentence="Cerul este albastru. (Az ég kék.)"),
            Word(lesson_id=lesson3.id, word="verde", translation="zöld",
                 example_sentence="Iarba este verde. (A fű zöld.)"),
            Word(lesson_id=lesson3.id, word="galben", translation="sárga",
                 example_sentence="Soarele este galben. (A nap sárga.)"),
            Word(lesson_id=lesson3.id, word="negru", translation="fekete",
                 example_sentence="Noaptea este neagră. (Az éjszaka fekete.)"),
        ]
        db.add_all(words3)

        # Lecke 4: Casa (Otthon) - 1. osztály
        lesson6 = Lesson(
            title="Casa (Otthon)",
            description="A ház és szobák nevei románul",
            language="romanian",
            level="beginner",
            grade=1,
            order=4
        )
        db.add(lesson6)
        db.flush()

        words6 = [
            Word(lesson_id=lesson6.id, word="casă", translation="ház",
                 example_sentence="Casa mea este mare. (A házam nagy.)"),
            Word(lesson_id=lesson6.id, word="cameră", translation="szoba",
                 example_sentence="Camera mea este curată. (A szobám tiszta.)"),
            Word(lesson_id=lesson6.id, word="bucătărie", translation="konyha",
                 example_sentence="Mama gătește în bucătărie. (Anya a konyhában főz.)"),
            Word(lesson_id=lesson6.id, word="baie", translation="fürdőszoba",
                 example_sentence="Baia are un duș mare. (A fürdőszobában nagy zuhany van.)"),
            Word(lesson_id=lesson6.id, word="grădină", translation="kert",
                 example_sentence="Grădina noastră are multe flori. (A kertünkben sok virág van.)"),
        ]
        db.add_all(words6)

        # === 2. OSZTÁLY - Román leckék ===

        # Lecke 5: Állatok (2. osztály)
        lesson4 = Lesson(
            title="Animale (Állatok)",
            description="Gyakori állatok nevei",
            language="romanian",
            level="beginner",
            grade=2,
            order=1
        )
        db.add(lesson4)
        db.flush()

        words4 = [
            Word(lesson_id=lesson4.id, word="câine", translation="kutya",
                 example_sentence="Câinele meu se numește Max. (A kutyám neve Max.)"),
            Word(lesson_id=lesson4.id, word="pisică", translation="macska",
                 example_sentence="Pisica doarme pe canapea. (A macska az ágyban alszik.)"),
            Word(lesson_id=lesson4.id, word="cal", translation="ló",
                 example_sentence="Calul aleargă repede. (A ló gyorsan fut.)"),
            Word(lesson_id=lesson4.id, word="pasăre", translation="madár",
                 example_sentence="Pasărea zboară în cer. (A madár az égen repül.)"),
            Word(lesson_id=lesson4.id, word="pește", translation="hal",
                 example_sentence="Peștele înoată în apă. (A hal a vízben úszik.)"),
        ]
        db.add_all(words4)

        # Lecke 6: Școala (Iskola) - 2. osztály
        lesson7 = Lesson(
            title="Școala (Iskola)",
            description="Iskolai szavak románul",
            language="romanian",
            level="beginner",
            grade=2,
            order=2
        )
        db.add(lesson7)
        db.flush()

        words7 = [
            Word(lesson_id=lesson7.id, word="școală", translation="iskola",
                 example_sentence="Școala mea este aproape. (Az iskolám közel van.)"),
            Word(lesson_id=lesson7.id, word="profesor", translation="tanár",
                 example_sentence="Profesorul nostru este bun. (A tanárunk jó.)"),
            Word(lesson_id=lesson7.id, word="elev", translation="diák",
                 example_sentence="Sunt un elev harnic. (Szorgalmas diák vagyok.)"),
            Word(lesson_id=lesson7.id, word="carte", translation="könyv",
                 example_sentence="Citesc o carte interesantă. (Egy érdekes könyvet olvasok.)"),
            Word(lesson_id=lesson7.id, word="creion", translation="ceruza",
                 example_sentence="Am un creion roșu. (Van egy piros ceruzám.)"),
        ]
        db.add_all(words7)

        # Lecke 7: Mâncarea (Ételek) - 2. osztály
        lesson8 = Lesson(
            title="Mâncarea (Ételek)",
            description="Alapvető ételek románul",
            language="romanian",
            level="beginner",
            grade=2,
            order=3
        )
        db.add(lesson8)
        db.flush()

        words8 = [
            Word(lesson_id=lesson8.id, word="pâine", translation="kenyér",
                 example_sentence="Pâinea este proaspătă. (A kenyér friss.)"),
            Word(lesson_id=lesson8.id, word="lapte", translation="tej",
                 example_sentence="Beau lapte în fiecare zi. (Minden nap tejet iszom.)"),
            Word(lesson_id=lesson8.id, word="brânză", translation="sajt",
                 example_sentence="Îmi place brânza. (Szeretem a sajtot.)"),
            Word(lesson_id=lesson8.id, word="carne", translation="hús",
                 example_sentence="Carnea este delicioasă. (A hús finom.)"),
            Word(lesson_id=lesson8.id, word="fruct", translation="gyümölcs",
                 example_sentence="Fructele sunt sănătoase. (A gyümölcsök egészségesek.)"),
        ]
        db.add_all(words8)

        # === 2. OSZTÁLY - Angol leckék ===

        # Lecke 8: Food (Ételek) - angol, 2. osztály
        lesson5 = Lesson(
            title="Food (Ételek)",
            description="Alapvető ételek angolul",
            language="english",
            level="beginner",
            grade=2,
            order=4
        )
        db.add(lesson5)
        db.flush()

        words5 = [
            Word(lesson_id=lesson5.id, word="apple", translation="alma",
                 example_sentence="I eat an apple every day. (Minden nap eszem egy almát.)"),
            Word(lesson_id=lesson5.id, word="bread", translation="kenyér",
                 example_sentence="I like bread with butter. (Szeretem a kenyeret vajjal.)"),
            Word(lesson_id=lesson5.id, word="water", translation="víz",
                 example_sentence="I drink water. (Vizet iszom.)"),
            Word(lesson_id=lesson5.id, word="milk", translation="tej",
                 example_sentence="Children need milk. (A gyerekeknek tejre van szükségük.)"),
        ]
        db.add_all(words5)

        # Lecke 9: Family (Család) - angol, 2. osztály
        lesson9 = Lesson(
            title="Family (Család)",
            description="Családtagok nevei angolul",
            language="english",
            level="beginner",
            grade=2,
            order=5
        )
        db.add(lesson9)
        db.flush()

        words9 = [
            Word(lesson_id=lesson9.id, word="mother", translation="anya",
                 example_sentence="My mother is kind. (Az anyám kedves.)"),
            Word(lesson_id=lesson9.id, word="father", translation="apa",
                 example_sentence="My father works hard. (Az apám keményen dolgozik.)"),
            Word(lesson_id=lesson9.id, word="brother", translation="testvér (fiú)",
                 example_sentence="I have a brother. (Van egy testvérem.)"),
            Word(lesson_id=lesson9.id, word="sister", translation="testvér (lány)",
                 example_sentence="My sister is tall. (A nővérem magas.)"),
            Word(lesson_id=lesson9.id, word="grandpa", translation="nagyapa",
                 example_sentence="Grandpa tells stories. (Nagyapa meséket mesél.)"),
        ]
        db.add_all(words9)

        # Lecke 10: Colors (Színek) - angol, 2. osztály
        lesson10 = Lesson(
            title="Colors (Színek)",
            description="Alapvető színek angolul",
            language="english",
            level="beginner",
            grade=2,
            order=6
        )
        db.add(lesson10)
        db.flush()

        words10 = [
            Word(lesson_id=lesson10.id, word="red", translation="piros",
                 example_sentence="The apple is red. (Az alma piros.)"),
            Word(lesson_id=lesson10.id, word="blue", translation="kék",
                 example_sentence="The sky is blue. (Az ég kék.)"),
            Word(lesson_id=lesson10.id, word="green", translation="zöld",
                 example_sentence="The grass is green. (A fű zöld.)"),
            Word(lesson_id=lesson10.id, word="yellow", translation="sárga",
                 example_sentence="The sun is yellow. (A nap sárga.)"),
            Word(lesson_id=lesson10.id, word="black", translation="fekete",
                 example_sentence="The cat is black. (A macska fekete.)"),
        ]
        db.add_all(words10)

        # Lecke 11: Animals (Állatok) - angol, 2. osztály
        lesson11 = Lesson(
            title="Animals (Állatok)",
            description="Gyakori állatok nevei angolul",
            language="english",
            level="beginner",
            grade=2,
            order=7
        )
        db.add(lesson11)
        db.flush()

        words11 = [
            Word(lesson_id=lesson11.id, word="dog", translation="kutya",
                 example_sentence="The dog is friendly. (A kutya barátságos.)"),
            Word(lesson_id=lesson11.id, word="cat", translation="macska",
                 example_sentence="The cat sleeps. (A macska alszik.)"),
            Word(lesson_id=lesson11.id, word="bird", translation="madár",
                 example_sentence="The bird sings. (A madár énekel.)"),
            Word(lesson_id=lesson11.id, word="fish", translation="hal",
                 example_sentence="The fish swims. (A hal úszik.)"),
            Word(lesson_id=lesson11.id, word="horse", translation="ló",
                 example_sentence="The horse runs fast. (A ló gyorsan fut.)"),
        ]
        db.add_all(words11)

        # Lecke 12: School (Iskola) - angol, 2. osztály
        lesson12 = Lesson(
            title="School (Iskola)",
            description="Iskolai szavak angolul",
            language="english",
            level="beginner",
            grade=2,
            order=8
        )
        db.add(lesson12)
        db.flush()

        words12 = [
            Word(lesson_id=lesson12.id, word="teacher", translation="tanár",
                 example_sentence="The teacher is nice. (A tanár kedves.)"),
            Word(lesson_id=lesson12.id, word="student", translation="diák",
                 example_sentence="I am a student. (Diák vagyok.)"),
            Word(lesson_id=lesson12.id, word="book", translation="könyv",
                 example_sentence="I read a book. (Könyvet olvasok.)"),
            Word(lesson_id=lesson12.id, word="pencil", translation="ceruza",
                 example_sentence="I have a pencil. (Van egy ceruzám.)"),
            Word(lesson_id=lesson12.id, word="classroom", translation="osztályterem",
                 example_sentence="The classroom is big. (Az osztályterem nagy.)"),
        ]
        db.add_all(words12)

        # === NYELVTANI GYAKORLATOK ===

        # Román nyelvtan - Család lecke (lesson1)
        grammar1 = [
            GrammarExercise(
                lesson_id=lesson1.id,
                exercise_type="fill_blank",
                question="Mama ___ este profesoară. (anya/az)",
                correct_answer="mea",
                wrong_answers="meu,ta,lui",
                explanation="'Mea' = enyém (nőnem). A 'mama mea' = az anyám.",
                difficulty=1
            ),
            GrammarExercise(
                lesson_id=lesson1.id,
                exercise_type="multiple_choice",
                question="Melyik a helyes? 'Az apám' románul:",
                correct_answer="Tatăl meu",
                wrong_answers="Tată mea,Tatăl ta,Tată lui",
                explanation="'Tatăl meu' = az apám. 'Meu' hímnemű birtokos névmás.",
                difficulty=1
            ),
            GrammarExercise(
                lesson_id=lesson1.id,
                exercise_type="word_order",
                question="meu,frate,mare,este",
                correct_answer="Frate meu este mare",
                wrong_answers="Meu frate mare este,Este mare meu frate",
                explanation="Helyes szórend: Alany + birtokos + állítmány + melléknév",
                difficulty=2
            ),
        ]
        db.add_all(grammar1)

        # Román nyelvtan - Számok lecke (lesson2)
        grammar2 = [
            GrammarExercise(
                lesson_id=lesson2.id,
                exercise_type="fill_blank",
                question="Am ___ câini. (két kutyám van)",
                correct_answer="doi",
                wrong_answers="două,unu,trei",
                explanation="'Doi' = kettő (hímnem). Kutyákra 'doi'-t használunk.",
                difficulty=1
            ),
            GrammarExercise(
                lesson_id=lesson2.id,
                exercise_type="multiple_choice",
                question="'Három alma' románul:",
                correct_answer="trei mere",
                wrong_answers="trei mere,patru mere,doi mere",
                explanation="'Trei' = három, 'mere' = almák (többes szám).",
                difficulty=1
            ),
            GrammarExercise(
                lesson_id=lesson2.id,
                exercise_type="fill_blank",
                question="Casa are ___ camere. (A háznak négy szobája van)",
                correct_answer="patru",
                wrong_answers="cinci,trei,șase",
                explanation="'Patru' = négy.",
                difficulty=1
            ),
        ]
        db.add_all(grammar2)

        # Román nyelvtan - Színek lecke (lesson3)
        grammar3 = [
            GrammarExercise(
                lesson_id=lesson3.id,
                exercise_type="multiple_choice",
                question="'A piros alma' románul:",
                correct_answer="mărul roșu",
                wrong_answers="mărul roșie,mere roșu,alma roșu",
                explanation="'Mărul' = az alma (határozott névelővel), 'roșu' = piros (hímnem).",
                difficulty=1
            ),
            GrammarExercise(
                lesson_id=lesson3.id,
                exercise_type="fill_blank",
                question="Cerul este ___. (Az ég kék)",
                correct_answer="albastru",
                wrong_answers="albastră,verde,roșu",
                explanation="'Albastru' = kék (hímnem). Az ég (cerul) hímnemű.",
                difficulty=1
            ),
            GrammarExercise(
                lesson_id=lesson3.id,
                exercise_type="word_order",
                question="verde,iarba,este",
                correct_answer="Iarba este verde",
                wrong_answers="Verde este iarba,Este iarba verde",
                explanation="Alany + ige + melléknév a helyes szórend.",
                difficulty=2
            ),
        ]
        db.add_all(grammar3)

        # Angol nyelvtan - Food lecke (lesson5)
        grammar5 = [
            GrammarExercise(
                lesson_id=lesson5.id,
                exercise_type="fill_blank",
                question="I eat ___ apple every day. (egy almát)",
                correct_answer="an",
                wrong_answers="a,the,some",
                explanation="'An' névelőt használunk magánhangzóval kezdődő szavak előtt.",
                difficulty=1
            ),
            GrammarExercise(
                lesson_id=lesson5.id,
                exercise_type="multiple_choice",
                question="Melyik a helyes? 'Vizet iszom':",
                correct_answer="I drink water",
                wrong_answers="I drinks water,I drinking water,Me drink water",
                explanation="Egyes szám első személyben: I + ige alapalak.",
                difficulty=1
            ),
            GrammarExercise(
                lesson_id=lesson5.id,
                exercise_type="word_order",
                question="milk,children,need",
                correct_answer="Children need milk",
                wrong_answers="Milk children need,Need children milk",
                explanation="Angol szórend: Alany + Ige + Tárgy",
                difficulty=2
            ),
        ]
        db.add_all(grammar5)

        # Román nyelvtan - Állatok lecke (lesson4)
        grammar4 = [
            GrammarExercise(
                lesson_id=lesson4.id,
                exercise_type="fill_blank",
                question="Câinele ___ aleargă în parc. (A kutya a parkban fut)",
                correct_answer="meu",
                wrong_answers="mea,ta,noastră",
                explanation="'Meu' = enyém (hímnem). 'Câinele meu' = a kutyám.",
                difficulty=1
            ),
            GrammarExercise(
                lesson_id=lesson4.id,
                exercise_type="multiple_choice",
                question="'A macska alszik' románul:",
                correct_answer="Pisica doarme",
                wrong_answers="Pisică doarme,Pisica dorm,Pisici doarme",
                explanation="'Pisica' = a macska (határozott névelővel), 'doarme' = alszik.",
                difficulty=1
            ),
            GrammarExercise(
                lesson_id=lesson4.id,
                exercise_type="word_order",
                question="zboară,pasărea,cer,în",
                correct_answer="Pasărea zboară în cer",
                wrong_answers="În cer pasărea zboară,Zboară pasărea cer în",
                explanation="Helyes szórend: Alany + Ige + Helyhatározó",
                difficulty=2
            ),
        ]
        db.add_all(grammar4)

        # Román nyelvtan - Casa lecke (lesson6)
        grammar6 = [
            GrammarExercise(
                lesson_id=lesson6.id,
                exercise_type="fill_blank",
                question="Casa ___ este mare. (A házam nagy)",
                correct_answer="mea",
                wrong_answers="meu,ta,noastră",
                explanation="'Mea' = enyém (nőnem). 'Casa' nőnemű, ezért 'mea'.",
                difficulty=1
            ),
            GrammarExercise(
                lesson_id=lesson6.id,
                exercise_type="multiple_choice",
                question="'A konyhában vagyok' románul:",
                correct_answer="Sunt în bucătărie",
                wrong_answers="Sunt bucătărie,În bucătărie sunt,Bucătărie sunt în",
                explanation="'Sunt în' = vagyok valamiben. 'Bucătărie' = konyha.",
                difficulty=1
            ),
            GrammarExercise(
                lesson_id=lesson6.id,
                exercise_type="word_order",
                question="grădină,flori,în,sunt",
                correct_answer="În grădină sunt flori",
                wrong_answers="Flori în grădină sunt,Sunt grădină în flori",
                explanation="'În grădină sunt flori' = A kertben virágok vannak.",
                difficulty=2
            ),
        ]
        db.add_all(grammar6)

        # Román nyelvtan - Școala lecke (lesson7)
        grammar7 = [
            GrammarExercise(
                lesson_id=lesson7.id,
                exercise_type="fill_blank",
                question="Profesorul ___ este bun. (A tanárunk jó)",
                correct_answer="nostru",
                wrong_answers="meu,ta,lor",
                explanation="'Nostru' = miénk. 'Profesorul nostru' = a tanárunk.",
                difficulty=1
            ),
            GrammarExercise(
                lesson_id=lesson7.id,
                exercise_type="multiple_choice",
                question="'Könyvet olvasok' románul:",
                correct_answer="Citesc o carte",
                wrong_answers="Citesc carte,O carte citesc,Carte citesc o",
                explanation="'Citesc' = olvasok, 'o carte' = egy könyvet.",
                difficulty=1
            ),
            GrammarExercise(
                lesson_id=lesson7.id,
                exercise_type="word_order",
                question="elev,un,sunt,bun",
                correct_answer="Sunt un elev bun",
                wrong_answers="Un elev bun sunt,Elev bun un sunt",
                explanation="'Sunt un elev bun' = Jó diák vagyok.",
                difficulty=2
            ),
        ]
        db.add_all(grammar7)

        # Román nyelvtan - Mâncarea lecke (lesson8)
        grammar8 = [
            GrammarExercise(
                lesson_id=lesson8.id,
                exercise_type="fill_blank",
                question="Pâinea este ___. (A kenyér friss)",
                correct_answer="proaspătă",
                wrong_answers="proaspăt,friss,bun",
                explanation="'Proaspătă' = friss (nőnem). 'Pâinea' nőnemű.",
                difficulty=1
            ),
            GrammarExercise(
                lesson_id=lesson8.id,
                exercise_type="multiple_choice",
                question="'Tejet iszom' románul:",
                correct_answer="Beau lapte",
                wrong_answers="Lapte beau,Beau un lapte,Iszom lapte",
                explanation="'Beau' = iszom, 'lapte' = tej.",
                difficulty=1
            ),
            GrammarExercise(
                lesson_id=lesson8.id,
                exercise_type="word_order",
                question="sănătoase,fructele,sunt",
                correct_answer="Fructele sunt sănătoase",
                wrong_answers="Sunt fructele sănătoase,Sănătoase sunt fructele",
                explanation="'Fructele sunt sănătoase' = A gyümölcsök egészségesek.",
                difficulty=2
            ),
        ]
        db.add_all(grammar8)

        # Angol nyelvtan - Family lecke (lesson9)
        grammar9 = [
            GrammarExercise(
                lesson_id=lesson9.id,
                exercise_type="fill_blank",
                question="My ___ is kind. (Az anyám kedves)",
                correct_answer="mother",
                wrong_answers="father,brother,sister",
                explanation="'Mother' = anya. 'My mother' = az anyám.",
                difficulty=1
            ),
            GrammarExercise(
                lesson_id=lesson9.id,
                exercise_type="multiple_choice",
                question="'Van egy testvérem' angolul:",
                correct_answer="I have a brother",
                wrong_answers="I has a brother,I am a brother,I have brother",
                explanation="'I have' = nekem van. 'A brother' = egy testvér.",
                difficulty=1
            ),
            GrammarExercise(
                lesson_id=lesson9.id,
                exercise_type="word_order",
                question="father,my,hard,works",
                correct_answer="My father works hard",
                wrong_answers="Father my works hard,Works hard my father",
                explanation="Angol szórend: Birtokos + Alany + Ige + Határozó",
                difficulty=2
            ),
        ]
        db.add_all(grammar9)

        # Angol nyelvtan - Colors lecke (lesson10)
        grammar10 = [
            GrammarExercise(
                lesson_id=lesson10.id,
                exercise_type="fill_blank",
                question="The sky is ___. (Az ég kék)",
                correct_answer="blue",
                wrong_answers="red,green,yellow",
                explanation="'Blue' = kék. 'The sky is blue' = Az ég kék.",
                difficulty=1
            ),
            GrammarExercise(
                lesson_id=lesson10.id,
                exercise_type="multiple_choice",
                question="'A fű zöld' angolul:",
                correct_answer="The grass is green",
                wrong_answers="The grass are green,Grass is green,The green is grass",
                explanation="'The grass' = a fű, 'is green' = zöld.",
                difficulty=1
            ),
            GrammarExercise(
                lesson_id=lesson10.id,
                exercise_type="word_order",
                question="black,cat,the,is",
                correct_answer="The cat is black",
                wrong_answers="Cat the is black,Is the cat black",
                explanation="Állító mondat: The + Alany + is + Melléknév",
                difficulty=2
            ),
        ]
        db.add_all(grammar10)

        # Angol nyelvtan - Animals lecke (lesson11)
        grammar11 = [
            GrammarExercise(
                lesson_id=lesson11.id,
                exercise_type="fill_blank",
                question="The dog ___. (A kutya ugat)",
                correct_answer="barks",
                wrong_answers="bark,barking,to bark",
                explanation="Egyes szám harmadik személyben '-s' végződés: 'barks'.",
                difficulty=1
            ),
            GrammarExercise(
                lesson_id=lesson11.id,
                exercise_type="multiple_choice",
                question="'A madár énekel' angolul:",
                correct_answer="The bird sings",
                wrong_answers="The bird sing,Bird sings,The birds sing",
                explanation="Egyes számú alany után 'sings' (harmadik személy).",
                difficulty=1
            ),
            GrammarExercise(
                lesson_id=lesson11.id,
                exercise_type="word_order",
                question="fast,horse,runs,the",
                correct_answer="The horse runs fast",
                wrong_answers="Horse the runs fast,Runs the horse fast",
                explanation="Szórend: The + Alany + Ige + Határozó",
                difficulty=2
            ),
        ]
        db.add_all(grammar11)

        # Angol nyelvtan - School lecke (lesson12)
        grammar12 = [
            GrammarExercise(
                lesson_id=lesson12.id,
                exercise_type="fill_blank",
                question="I ___ a student. (Diák vagyok)",
                correct_answer="am",
                wrong_answers="is,are,be",
                explanation="'I am' = én vagyok. Első személyben 'am' a létige.",
                difficulty=1
            ),
            GrammarExercise(
                lesson_id=lesson12.id,
                exercise_type="multiple_choice",
                question="'A tanár kedves' angolul:",
                correct_answer="The teacher is nice",
                wrong_answers="The teacher are nice,Teacher is nice,The nice is teacher",
                explanation="'The teacher' = a tanár, 'is nice' = kedves.",
                difficulty=1
            ),
            GrammarExercise(
                lesson_id=lesson12.id,
                exercise_type="word_order",
                question="big,classroom,the,is",
                correct_answer="The classroom is big",
                wrong_answers="Classroom the is big,Is the classroom big",
                explanation="Állító mondat: The + Alany + is + Melléknév",
                difficulty=2
            ),
        ]
        db.add_all(grammar12)

        # === HALLÁSÉRTÉS GYAKORLATOK ===
        # Megjegyzés: Az audio URL-ek placeholder-ek, valódi fájlokra cserélendők

        # Román hallásértés - Család lecke
        listening1 = [
            ListeningExercise(
                lesson_id=lesson1.id,
                audio_url="/static/audio/ro_familia_1.mp3",
                transcript="Mama mea este profesoară.",
                question="Mit csinál az anyja?",
                correct_answer="Tanár",
                wrong_answers="Orvos,Mérnök,Szakács",
                difficulty=1,
                duration_seconds=3
            ),
            ListeningExercise(
                lesson_id=lesson1.id,
                audio_url="/static/audio/ro_familia_2.mp3",
                transcript="Am un frate și o soră.",
                question="Hány testvére van?",
                correct_answer="Kettő",
                wrong_answers="Egy,Három,Nincs",
                difficulty=1,
                duration_seconds=3
            ),
        ]
        db.add_all(listening1)

        # Román hallásértés - Számok lecke
        listening2 = [
            ListeningExercise(
                lesson_id=lesson2.id,
                audio_url="/static/audio/ro_numere_1.mp3",
                transcript="Am cinci mere.",
                question="Hány almája van?",
                correct_answer="Öt",
                wrong_answers="Három,Négy,Hat",
                difficulty=1,
                duration_seconds=2
            ),
            ListeningExercise(
                lesson_id=lesson2.id,
                audio_url="/static/audio/ro_numere_2.mp3",
                transcript="Sunt trei copii în clasă.",
                question="Hány gyerek van az osztályban?",
                correct_answer="Három",
                wrong_answers="Kettő,Négy,Öt",
                difficulty=1,
                duration_seconds=3
            ),
        ]
        db.add_all(listening2)

        # Angol hallásértés - Food lecke
        listening5 = [
            ListeningExercise(
                lesson_id=lesson5.id,
                audio_url="/static/audio/en_food_1.mp3",
                transcript="I eat an apple every morning.",
                question="Mit eszik minden reggel?",
                correct_answer="Almát",
                wrong_answers="Kenyeret,Tejet,Banánt",
                difficulty=1,
                duration_seconds=3
            ),
            ListeningExercise(
                lesson_id=lesson5.id,
                audio_url="/static/audio/en_food_2.mp3",
                transcript="Children need milk to grow strong.",
                question="Mire van szükségük a gyerekeknek?",
                correct_answer="Tejre",
                wrong_answers="Vízre,Kenyérre,Almára",
                difficulty=1,
                duration_seconds=4
            ),
        ]
        db.add_all(listening5)

        # Román hallásértés - Színek lecke (lesson3)
        listening3 = [
            ListeningExercise(
                lesson_id=lesson3.id,
                audio_url="/static/audio/ro_culori_1.mp3",
                transcript="Cerul este albastru și iarba este verde.",
                question="Milyen színű az ég?",
                correct_answer="Kék",
                wrong_answers="Zöld,Piros,Sárga",
                difficulty=1,
                duration_seconds=4
            ),
            ListeningExercise(
                lesson_id=lesson3.id,
                audio_url="/static/audio/ro_culori_2.mp3",
                transcript="Mărul roșu este pe masă.",
                question="Milyen színű az alma?",
                correct_answer="Piros",
                wrong_answers="Zöld,Sárga,Fekete",
                difficulty=1,
                duration_seconds=3
            ),
        ]
        db.add_all(listening3)

        # Román hallásértés - Állatok lecke (lesson4)
        listening4 = [
            ListeningExercise(
                lesson_id=lesson4.id,
                audio_url="/static/audio/ro_animale_1.mp3",
                transcript="Câinele aleargă în parc.",
                question="Hol fut a kutya?",
                correct_answer="A parkban",
                wrong_answers="A kertben,Az utcán,A házban",
                difficulty=1,
                duration_seconds=3
            ),
            ListeningExercise(
                lesson_id=lesson4.id,
                audio_url="/static/audio/ro_animale_2.mp3",
                transcript="Pisica mea este neagră.",
                question="Milyen színű a macska?",
                correct_answer="Fekete",
                wrong_answers="Fehér,Szürke,Barna",
                difficulty=1,
                duration_seconds=3
            ),
        ]
        db.add_all(listening4)

        # Román hallásértés - Casa lecke (lesson6)
        listening6 = [
            ListeningExercise(
                lesson_id=lesson6.id,
                audio_url="/static/audio/ro_casa_1.mp3",
                transcript="Casa noastră are trei camere.",
                question="Hány szobája van a háznak?",
                correct_answer="Három",
                wrong_answers="Kettő,Négy,Öt",
                difficulty=1,
                duration_seconds=3
            ),
            ListeningExercise(
                lesson_id=lesson6.id,
                audio_url="/static/audio/ro_casa_2.mp3",
                transcript="Mama gătește în bucătărie.",
                question="Hol főz az anya?",
                correct_answer="A konyhában",
                wrong_answers="A szobában,A kertben,A fürdőszobában",
                difficulty=1,
                duration_seconds=3
            ),
        ]
        db.add_all(listening6)

        # Román hallásértés - Școala lecke (lesson7)
        listening7 = [
            ListeningExercise(
                lesson_id=lesson7.id,
                audio_url="/static/audio/ro_scoala_1.mp3",
                transcript="Profesorul nostru predă matematică.",
                question="Mit tanít a tanár?",
                correct_answer="Matematikát",
                wrong_answers="Románt,Angolt,Történelmet",
                difficulty=1,
                duration_seconds=3
            ),
            ListeningExercise(
                lesson_id=lesson7.id,
                audio_url="/static/audio/ro_scoala_2.mp3",
                transcript="Am cinci cărți în geantă.",
                question="Hány könyv van a táskában?",
                correct_answer="Öt",
                wrong_answers="Három,Négy,Hat",
                difficulty=1,
                duration_seconds=3
            ),
        ]
        db.add_all(listening7)

        # Román hallásértés - Mâncarea lecke (lesson8)
        listening8 = [
            ListeningExercise(
                lesson_id=lesson8.id,
                audio_url="/static/audio/ro_mancare_1.mp3",
                transcript="Mănânc pâine cu brânză.",
                question="Mit eszik?",
                correct_answer="Kenyeret sajttal",
                wrong_answers="Húst,Gyümölcsöt,Tejet",
                difficulty=1,
                duration_seconds=3
            ),
            ListeningExercise(
                lesson_id=lesson8.id,
                audio_url="/static/audio/ro_mancare_2.mp3",
                transcript="Laptele este în frigider.",
                question="Hol van a tej?",
                correct_answer="A hűtőben",
                wrong_answers="Az asztalon,A konyhában,A táskában",
                difficulty=1,
                duration_seconds=3
            ),
        ]
        db.add_all(listening8)

        # Angol hallásértés - Family lecke (lesson9)
        listening9 = [
            ListeningExercise(
                lesson_id=lesson9.id,
                audio_url="/static/audio/en_family_1.mp3",
                transcript="My mother works at a hospital.",
                question="Hol dolgozik az anya?",
                correct_answer="Kórházban",
                wrong_answers="Iskolában,Irodában,Boltban",
                difficulty=1,
                duration_seconds=3
            ),
            ListeningExercise(
                lesson_id=lesson9.id,
                audio_url="/static/audio/en_family_2.mp3",
                transcript="I have two sisters and one brother.",
                question="Hány nővére van?",
                correct_answer="Kettő",
                wrong_answers="Egy,Három,Nincs",
                difficulty=1,
                duration_seconds=3
            ),
        ]
        db.add_all(listening9)

        # Angol hallásértés - Colors lecke (lesson10)
        listening10 = [
            ListeningExercise(
                lesson_id=lesson10.id,
                audio_url="/static/audio/en_colors_1.mp3",
                transcript="My favorite color is blue.",
                question="Mi a kedvenc színe?",
                correct_answer="Kék",
                wrong_answers="Piros,Zöld,Sárga",
                difficulty=1,
                duration_seconds=3
            ),
            ListeningExercise(
                lesson_id=lesson10.id,
                audio_url="/static/audio/en_colors_2.mp3",
                transcript="The flowers are red and yellow.",
                question="Milyen színűek a virágok?",
                correct_answer="Piros és sárga",
                wrong_answers="Kék és zöld,Fehér és rózsaszín,Lila és narancssárga",
                difficulty=1,
                duration_seconds=3
            ),
        ]
        db.add_all(listening10)

        # Angol hallásértés - Animals lecke (lesson11)
        listening11 = [
            ListeningExercise(
                lesson_id=lesson11.id,
                audio_url="/static/audio/en_animals_1.mp3",
                transcript="The dog is playing in the garden.",
                question="Hol játszik a kutya?",
                correct_answer="A kertben",
                wrong_answers="A parkban,A házban,Az utcán",
                difficulty=1,
                duration_seconds=3
            ),
            ListeningExercise(
                lesson_id=lesson11.id,
                audio_url="/static/audio/en_animals_2.mp3",
                transcript="I have a cat and a fish.",
                question="Milyen állatai vannak?",
                correct_answer="Macska és hal",
                wrong_answers="Kutya és madár,Ló és hal,Macska és kutya",
                difficulty=1,
                duration_seconds=3
            ),
        ]
        db.add_all(listening11)

        # Angol hallásértés - School lecke (lesson12)
        listening12 = [
            ListeningExercise(
                lesson_id=lesson12.id,
                audio_url="/static/audio/en_school_1.mp3",
                transcript="The teacher is reading a book.",
                question="Mit csinál a tanár?",
                correct_answer="Könyvet olvas",
                wrong_answers="Ír,Beszél,Alszik",
                difficulty=1,
                duration_seconds=3
            ),
            ListeningExercise(
                lesson_id=lesson12.id,
                audio_url="/static/audio/en_school_2.mp3",
                transcript="There are twenty students in my classroom.",
                question="Hány diák van az osztályban?",
                correct_answer="Húsz",
                wrong_answers="Tíz,Tizenöt,Harminc",
                difficulty=1,
                duration_seconds=3
            ),
        ]
        db.add_all(listening12)

        # === SZÖVEGÉRTÉS GYAKORLATOK ===

        # Román szövegértés - Család lecke
        reading1 = ReadingExercise(
            lesson_id=lesson1.id,
            title="Familia mea",
            content="""Bună ziua! Mă numesc Ana. Am o familie mare.

Mama mea se numește Maria. Ea este profesoară. Tatăl meu se numește Ion. El lucrează la spital.

Am un frate și o soră. Fratele meu are 10 ani. Sora mea are 7 ani. Noi ne jucăm împreună în fiecare zi.

Bunicii mei locuiesc în sat. Îi vizităm în fiecare weekend.""",
            difficulty=1
        )
        db.add(reading1)
        db.flush()

        reading1_questions = [
            ReadingQuestion(
                reading_id=reading1.id,
                question="Hogy hívják az édesanyát?",
                correct_answer="Maria",
                wrong_answers="Ana,Ion,Ioana"
            ),
            ReadingQuestion(
                reading_id=reading1.id,
                question="Hol dolgozik az édesapa?",
                correct_answer="Kórházban",
                wrong_answers="Iskolában,Gyárban,Irodában"
            ),
            ReadingQuestion(
                reading_id=reading1.id,
                question="Hány éves a testvér (fiú)?",
                correct_answer="10 éves",
                wrong_answers="7 éves,8 éves,12 éves"
            ),
            ReadingQuestion(
                reading_id=reading1.id,
                question="Hol laknak a nagyszülők?",
                correct_answer="Faluban",
                wrong_answers="Városban,Külföldön,Hegyekben"
            ),
        ]
        db.add_all(reading1_questions)

        # Angol szövegértés - Food lecke
        reading5 = ReadingExercise(
            lesson_id=lesson5.id,
            title="My Breakfast",
            content="""Hello! My name is Tom. I want to tell you about my breakfast.

Every morning, I wake up at 7 o'clock. First, I drink a glass of water.

Then, I eat breakfast. I love apples and bread with butter. I also drink milk every day. My mother says milk makes me strong.

After breakfast, I brush my teeth and go to school.""",
            difficulty=1
        )
        db.add(reading5)
        db.flush()

        reading5_questions = [
            ReadingQuestion(
                reading_id=reading5.id,
                question="Mikor kel fel Tom?",
                correct_answer="7 órakor",
                wrong_answers="6 órakor,8 órakor,9 órakor"
            ),
            ReadingQuestion(
                reading_id=reading5.id,
                question="Mit iszik először reggel?",
                correct_answer="Vizet",
                wrong_answers="Tejet,Teát,Narancslét"
            ),
            ReadingQuestion(
                reading_id=reading5.id,
                question="Mit szeret enni reggelire?",
                correct_answer="Almát és kenyeret vajjal",
                wrong_answers="Tojást,Müzlit,Szendvicset"
            ),
            ReadingQuestion(
                reading_id=reading5.id,
                question="Mit csinál reggeli után?",
                correct_answer="Fogat mos és iskolába megy",
                wrong_answers="Tévét néz,Játszik,Alszik"
            ),
        ]
        db.add_all(reading5_questions)

        # Román szövegértés - Számok lecke (lesson2)
        reading2 = ReadingExercise(
            lesson_id=lesson2.id,
            title="Câți ani ai?",
            content="""Bună! Mă numesc Mihai. Am zece ani.

În familia mea suntem patru persoane. Tatăl meu are patruzeci de ani. Mama mea are treizeci și opt de ani.

Sora mea se numește Elena. Ea are șapte ani. Este mai mică decât mine cu trei ani.

La școală, în clasa mea sunt douăzeci și cinci de elevi. Avem cinci profesori.

Cel mai bun prieten al meu are nouă ani. Ne jucăm împreună în fiecare zi.""",
            difficulty=1
        )
        db.add(reading2)
        db.flush()

        reading2_questions = [
            ReadingQuestion(
                reading_id=reading2.id,
                question="Hány éves Mihai?",
                correct_answer="Tíz éves",
                wrong_answers="Hét éves,Kilenc éves,Nyolc éves"
            ),
            ReadingQuestion(
                reading_id=reading2.id,
                question="Hányan vannak a családban?",
                correct_answer="Négyen",
                wrong_answers="Hárman,Öten,Hatan"
            ),
            ReadingQuestion(
                reading_id=reading2.id,
                question="Hány éves a húga?",
                correct_answer="Hét éves",
                wrong_answers="Öt éves,Nyolc éves,Tíz éves"
            ),
            ReadingQuestion(
                reading_id=reading2.id,
                question="Hány diák van az osztályban?",
                correct_answer="Huszonöt",
                wrong_answers="Húsz,Harminc,Tizenöt"
            ),
        ]
        db.add_all(reading2_questions)

        # Román szövegértés - Színek lecke (lesson3)
        reading3 = ReadingExercise(
            lesson_id=lesson3.id,
            title="Culorile curcubeului",
            content="""După ploaie, apare curcubeul pe cer. Curcubeul are șapte culori frumoase.

Prima culoare este roșu. Este ca mărul și căpșuna. A doua culoare este portocaliu. Este ca portocala.

Apoi vine galben. Soarele este galben. Verde este culoarea ierbii și a frunzelor.

Albastru este culoarea cerului și a mării. Indigo este un albastru închis.

Ultima culoare este violet. Florile de lavandă sunt violet.

Îmi place cel mai mult culoarea verde pentru că îmi place natura.""",
            difficulty=1
        )
        db.add(reading3)
        db.flush()

        reading3_questions = [
            ReadingQuestion(
                reading_id=reading3.id,
                question="Hány színe van a szivárványnak?",
                correct_answer="Hét",
                wrong_answers="Öt,Hat,Nyolc"
            ),
            ReadingQuestion(
                reading_id=reading3.id,
                question="Mi az első színe a szivárványnak?",
                correct_answer="Piros",
                wrong_answers="Sárga,Narancssárga,Kék"
            ),
            ReadingQuestion(
                reading_id=reading3.id,
                question="Milyen színű a nap?",
                correct_answer="Sárga",
                wrong_answers="Narancssárga,Fehér,Piros"
            ),
            ReadingQuestion(
                reading_id=reading3.id,
                question="Mi a szerző kedvenc színe?",
                correct_answer="Zöld",
                wrong_answers="Kék,Piros,Lila"
            ),
        ]
        db.add_all(reading3_questions)

        # Román szövegértés - Állatok lecke (lesson4)
        reading4 = ReadingExercise(
            lesson_id=lesson4.id,
            title="La grădina zoologică",
            content="""Astăzi am fost la grădina zoologică cu familia mea. Am văzut multe animale interesante.

Prima dată am văzut leii. Leul este mare și are o coamă frumoasă. Leii dormeau la soare.

Apoi am mers să vedem elefanții. Elefantul are o trompă lungă. Elefanții mâncau fructe.

La final am vizitat maimuțele. Maimuțele se jucau în copaci. Erau foarte amuzante.

Cel mai mult mi-au plăcut girafele. Girafa are un gât foarte lung. Mâncau frunze din copaci.

A fost o zi minunată la grădina zoologică!""",
            difficulty=1
        )
        db.add(reading4)
        db.flush()

        reading4_questions = [
            ReadingQuestion(
                reading_id=reading4.id,
                question="Hova ment a család?",
                correct_answer="Állatkertbe",
                wrong_answers="Parkba,Strandra,Erdőbe"
            ),
            ReadingQuestion(
                reading_id=reading4.id,
                question="Mit csináltak az oroszlánok?",
                correct_answer="Aludtak a napon",
                wrong_answers="Futottak,Ettek,Játszottak"
            ),
            ReadingQuestion(
                reading_id=reading4.id,
                question="Mit ettek az elefántok?",
                correct_answer="Gyümölcsöt",
                wrong_answers="Húst,Füvet,Kenyeret"
            ),
            ReadingQuestion(
                reading_id=reading4.id,
                question="Melyik állat tetszett a legjobban a szerzőnek?",
                correct_answer="A zsiráf",
                wrong_answers="Az oroszlán,Az elefánt,A majom"
            ),
        ]
        db.add_all(reading4_questions)

        # Román szövegértés - Casa lecke (lesson6)
        reading6 = ReadingExercise(
            lesson_id=lesson6.id,
            title="Casa noastră",
            content="""Locuiesc într-o casă mare cu familia mea. Casa noastră are două etaje.

La parter avem bucătăria și livingul. Bucătăria este galbenă. Mama gătește acolo în fiecare zi.

Livingul este mare și confortabil. Avem o canapea albastră și un televizor mare.

La etaj sunt trei dormitoare și o baie. Camera mea este verde. Am un pat, un birou și un dulap.

În spatele casei avem o grădină frumoasă. Tata plantează legume și flori acolo.

Îmi place foarte mult casa noastră!""",
            difficulty=1
        )
        db.add(reading6)
        db.flush()

        reading6_questions = [
            ReadingQuestion(
                reading_id=reading6.id,
                question="Hány emeletes a ház?",
                correct_answer="Két emeletes",
                wrong_answers="Egy emeletes,Három emeletes,Földszintes"
            ),
            ReadingQuestion(
                reading_id=reading6.id,
                question="Milyen színű a konyha?",
                correct_answer="Sárga",
                wrong_answers="Kék,Zöld,Fehér"
            ),
            ReadingQuestion(
                reading_id=reading6.id,
                question="Hány hálószoba van az emeleten?",
                correct_answer="Három",
                wrong_answers="Kettő,Négy,Egy"
            ),
            ReadingQuestion(
                reading_id=reading6.id,
                question="Mit csinál az apa a kertben?",
                correct_answer="Zöldségeket és virágokat ültet",
                wrong_answers="Játszik,Pihen,Olvas"
            ),
        ]
        db.add_all(reading6_questions)

        # Román szövegértés - Școala lecke (lesson7)
        reading7 = ReadingExercise(
            lesson_id=lesson7.id,
            title="Prima zi de școală",
            content="""Astăzi este prima zi de școală. Mă trezesc devreme și îmi pregătesc ghiozdanul.

În ghiozdan am cinci caiete, trei cărți, creioane colorate și un penar. Penar ul meu este albastru.

La școală, profesoara noastră se numește doamna Maria. Este foarte drăguță.

În clasa mea sunt douăzeci de elevi. Stăm în bănci câte doi. Prietenul meu Andrei stă lângă mine.

La prima oră avem matematică. Învățăm numerele de la unu la zece.

Îmi place școala pentru că învăț lucruri noi în fiecare zi.""",
            difficulty=1
        )
        db.add(reading7)
        db.flush()

        reading7_questions = [
            ReadingQuestion(
                reading_id=reading7.id,
                question="Hány füzet van a táskában?",
                correct_answer="Öt",
                wrong_answers="Három,Négy,Hat"
            ),
            ReadingQuestion(
                reading_id=reading7.id,
                question="Milyen színű a tolltartó?",
                correct_answer="Kék",
                wrong_answers="Piros,Zöld,Sárga"
            ),
            ReadingQuestion(
                reading_id=reading7.id,
                question="Hány diák van az osztályban?",
                correct_answer="Húsz",
                wrong_answers="Tizenöt,Huszonöt,Harminc"
            ),
            ReadingQuestion(
                reading_id=reading7.id,
                question="Mi az első óra?",
                correct_answer="Matematika",
                wrong_answers="Román,Angol,Rajz"
            ),
        ]
        db.add_all(reading7_questions)

        # Román szövegértés - Mâncarea lecke (lesson8)
        reading8 = ReadingExercise(
            lesson_id=lesson8.id,
            title="La piață",
            content="""În fiecare sâmbătă merg la piață cu mama. Piața este plină de fructe și legume proaspete.

Mai întâi cumpărăm fructe. Luăm mere roșii, banane galbene și portocale. Fructele sunt foarte dulci.

Apoi mergem la legume. Mama cumpără roșii, castraveți și morcovi. Legumele sunt pentru salată.

La final mergem la măcelărie. Tatăl meu vrea carne de pui pentru cină.

După piață, ne oprim la brutărie. Cumpărăm pâine proaspătă. Miroase foarte bine!

Acasă, mama pregătește o masă delicioasă din toate ingredientele cumpărate.""",
            difficulty=1
        )
        db.add(reading8)
        db.flush()

        reading8_questions = [
            ReadingQuestion(
                reading_id=reading8.id,
                question="Mikor mennek a piacra?",
                correct_answer="Szombaton",
                wrong_answers="Vasárnap,Hétfőn,Pénteken"
            ),
            ReadingQuestion(
                reading_id=reading8.id,
                question="Milyen színűek az almák?",
                correct_answer="Pirosak",
                wrong_answers="Zöldek,Sárgák,Narancssárgák"
            ),
            ReadingQuestion(
                reading_id=reading8.id,
                question="Mire kellenek a zöldségek?",
                correct_answer="Salátára",
                wrong_answers="Levesre,Süteményre,Szendvicsre"
            ),
            ReadingQuestion(
                reading_id=reading8.id,
                question="Milyen húst vesznek vacsorára?",
                correct_answer="Csirkehúst",
                wrong_answers="Marhahúst,Sertéshúst,Halat"
            ),
        ]
        db.add_all(reading8_questions)

        # Angol szövegértés - Family lecke (lesson9)
        reading9 = ReadingExercise(
            lesson_id=lesson9.id,
            title="My Family",
            content="""Hello! My name is Emma. I am ten years old. I want to tell you about my family.

My family has five people. My father's name is John. He is a doctor. He works at a hospital.

My mother's name is Sarah. She is a teacher. She teaches English at a school.

I have a brother and a sister. My brother Tom is twelve years old. My sister Lily is seven years old.

We also have a dog named Max. Max is brown and very friendly. We love playing with him.

On Sundays, we have lunch together. It is my favorite day of the week!""",
            difficulty=1
        )
        db.add(reading9)
        db.flush()

        reading9_questions = [
            ReadingQuestion(
                reading_id=reading9.id,
                question="Hány éves Emma?",
                correct_answer="Tíz éves",
                wrong_answers="Hét éves,Tizenkét éves,Nyolc éves"
            ),
            ReadingQuestion(
                reading_id=reading9.id,
                question="Mi az apa foglalkozása?",
                correct_answer="Orvos",
                wrong_answers="Tanár,Mérnök,Sofőr"
            ),
            ReadingQuestion(
                reading_id=reading9.id,
                question="Mit tanít az anya?",
                correct_answer="Angolt",
                wrong_answers="Matematikát,Zenét,Történelmet"
            ),
            ReadingQuestion(
                reading_id=reading9.id,
                question="Milyen színű a kutya?",
                correct_answer="Barna",
                wrong_answers="Fekete,Fehér,Szürke"
            ),
        ]
        db.add_all(reading9_questions)

        # Angol szövegértés - Colors lecke (lesson10)
        reading10 = ReadingExercise(
            lesson_id=lesson10.id,
            title="Colors Around Me",
            content="""I see many colors every day. Colors are everywhere!

In the morning, I see the yellow sun in the blue sky. The grass in my garden is green.

My room has many colors. My bed is blue. My desk is brown. My chair is red.

I have a box of crayons. There are twelve colors: red, blue, green, yellow, orange, purple, pink, brown, black, white, gray, and gold.

My favorite color is green because I love nature. Trees and grass are green.

What is your favorite color?""",
            difficulty=1
        )
        db.add(reading10)
        db.flush()

        reading10_questions = [
            ReadingQuestion(
                reading_id=reading10.id,
                question="Milyen színű a nap?",
                correct_answer="Sárga",
                wrong_answers="Narancssárga,Piros,Fehér"
            ),
            ReadingQuestion(
                reading_id=reading10.id,
                question="Milyen színű az ágy?",
                correct_answer="Kék",
                wrong_answers="Piros,Zöld,Barna"
            ),
            ReadingQuestion(
                reading_id=reading10.id,
                question="Hány szín van a zsírkréta dobozban?",
                correct_answer="Tizenkettő",
                wrong_answers="Tíz,Nyolc,Tizenöt"
            ),
            ReadingQuestion(
                reading_id=reading10.id,
                question="Mi a szerző kedvenc színe?",
                correct_answer="Zöld",
                wrong_answers="Kék,Piros,Sárga"
            ),
        ]
        db.add_all(reading10_questions)

        # Angol szövegértés - Animals lecke (lesson11)
        reading11 = ReadingExercise(
            lesson_id=lesson11.id,
            title="My Pets",
            content="""I love animals! I have three pets at home.

My first pet is a dog. His name is Buddy. Buddy is big and brown. He likes to run in the park. He is very friendly.

My second pet is a cat. Her name is Luna. Luna is small and black. She likes to sleep on my bed. She is very soft.

My third pet is a fish. His name is Nemo. Nemo is orange and white. He swims in his tank all day.

I take care of my pets every day. I give them food and water. I love playing with Buddy and Luna.

Animals are wonderful friends!""",
            difficulty=1
        )
        db.add(reading11)
        db.flush()

        reading11_questions = [
            ReadingQuestion(
                reading_id=reading11.id,
                question="Hány háziállata van a szerzőnek?",
                correct_answer="Három",
                wrong_answers="Kettő,Négy,Egy"
            ),
            ReadingQuestion(
                reading_id=reading11.id,
                question="Milyen színű a kutya?",
                correct_answer="Barna",
                wrong_answers="Fekete,Fehér,Szürke"
            ),
            ReadingQuestion(
                reading_id=reading11.id,
                question="Hol szeret aludni a macska?",
                correct_answer="Az ágyon",
                wrong_answers="A kanapén,A széken,A padlón"
            ),
            ReadingQuestion(
                reading_id=reading11.id,
                question="Milyen színű a hal?",
                correct_answer="Narancssárga és fehér",
                wrong_answers="Kék,Piros,Sárga"
            ),
        ]
        db.add_all(reading11_questions)

        # Angol szövegértés - School lecke (lesson12)
        reading12 = ReadingExercise(
            lesson_id=lesson12.id,
            title="A Day at School",
            content="""My name is Jack. I am a student. I go to school every day from Monday to Friday.

I wake up at seven o'clock. I eat breakfast and put on my uniform. My uniform is blue and white.

At school, I have many subjects. In the morning, we have Math and English. I like English because we read stories.

At noon, we have lunch in the cafeteria. I eat a sandwich and drink juice.

In the afternoon, we have Science and Art. Art is my favorite subject. I love to draw and paint.

School finishes at three o'clock. I go home and do my homework. Then I play with my friends.""",
            difficulty=1
        )
        db.add(reading12)
        db.flush()

        reading12_questions = [
            ReadingQuestion(
                reading_id=reading12.id,
                question="Hány órakor kel fel Jack?",
                correct_answer="Hét órakor",
                wrong_answers="Hat órakor,Nyolc órakor,Kilenc órakor"
            ),
            ReadingQuestion(
                reading_id=reading12.id,
                question="Milyen színű az egyenruha?",
                correct_answer="Kék és fehér",
                wrong_answers="Fekete és fehér,Piros és kék,Zöld és sárga"
            ),
            ReadingQuestion(
                reading_id=reading12.id,
                question="Mi Jack kedvenc tantárgya?",
                correct_answer="Rajz",
                wrong_answers="Matek,Angol,Természetismeret"
            ),
            ReadingQuestion(
                reading_id=reading12.id,
                question="Hány órakor végződik az iskola?",
                correct_answer="Három órakor",
                wrong_answers="Kettő órakor,Négy órakor,Öt órakor"
            ),
        ]
        db.add_all(reading12_questions)

        # === ADMIN USER ===
        admin = db.query(User).filter(User.name == "admin").first()
        if not admin:
            admin = User(name="admin", is_admin=True)
            db.add(admin)
            print("Admin user létrehozva: admin")

        db.commit()
        print("Adatbázis sikeresen inicializálva!")
        print("12 lecke létrehozva")
        print("  1. osztály: 4 román lecke (Familia, Numere, Culori, Casa)")
        print("  2. osztály: 3 román + 5 angol lecke (Animale, Scoala, Mancarea + Food, Family, Colors, Animals, School)")
        print("  3-4. osztály: Üres (később bővíthető)")
        print("Szavak: 57 db")
        print("Nyelvtani gyakorlatok: 36 db")
        print("Hallásértés gyakorlatok: 24 db")
        print("Szövegértés gyakorlatok: 12 db (48 kérdéssel)")

    except Exception as e:
        print(f"Hiba: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    print("Adatbázis inicializálás...")
    init_db()
