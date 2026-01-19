"""
Adatbázis inicializálás mintaadatokkal
Futtatás: python -m app.init_db
"""
from app.database import engine, SessionLocal, Base
from app.models.lesson import Lesson
from app.models.word import Word
from app.models.user import User


def init_db():
    # Táblák létrehozása
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        # Ellenőrizzük, van-e már adat
        if db.query(Lesson).count() > 0:
            print("Az adatbázis már tartalmaz adatokat.")
            return

        # === INGYENES LECKÉK (első 3) ===

        # Lecke 1: Család (román)
        lesson1 = Lesson(
            title="Familia (Család)",
            description="Alapvető családtagok nevei románul",
            language="romanian",
            level="beginner",
            is_premium=False,
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
            is_premium=False,
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

        # Lecke 3: Színek (román) - utolsó ingyenes
        lesson3 = Lesson(
            title="Culori (Színek)",
            description="Alapvető színek románul",
            language="romanian",
            level="beginner",
            is_premium=False,
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

        # === PRÉMIUM LECKÉK ===

        # Lecke 4: Állatok (prémium)
        lesson4 = Lesson(
            title="Animale (Állatok)",
            description="Gyakori állatok nevei",
            language="romanian",
            level="beginner",
            is_premium=True,
            order=4
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
        ]
        db.add_all(words4)

        # Lecke 5: Ételek (angol - prémium)
        lesson5 = Lesson(
            title="Food (Ételek)",
            description="Alapvető ételek angolul",
            language="english",
            level="beginner",
            is_premium=True,
            order=5
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
        # === ADMIN USER ===
        admin = db.query(User).filter(User.name == "admin").first()
        if not admin:
            admin = User(name="admin", is_admin=True, is_premium=True)
            db.add(admin)
            print("✅ Admin user létrehozva: admin")

        db.commit()
        print("✅ Adatbázis sikeresen inicializálva!")
        print("📚 5 lecke létrehozva (3 ingyenes, 2 prémium)")

    except Exception as e:
        print(f"❌ Hiba: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    print("🚀 Adatbázis inicializálás...")
    init_db()