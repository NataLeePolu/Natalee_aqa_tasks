adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3

# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("...."," ")
print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer_row = adwentures_of_tom_sawer.split( )
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer_row)
print(adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_h = adwentures_of_tom_sawer.lower().count("h")
print(f"Літера \"h\" зустрічається в тексті {count_h} разів")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
words_row = adwentures_of_tom_sawer.split()
count = 0
for every_word in words_row:
    words_upper = every_word.strip(".,;\"'()?!")
    if words_upper and words_upper[0].isupper():
        count += 1
print(f"В тексті {count} слів починається з великої літери")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_index = adwentures_of_tom_sawer.find('Tom')
if first_index != -1:
    second_index = adwentures_of_tom_sawer.find('Tom', first_index + 1)
    if second_index != -1:
        print(f"Слово 'Tom' вдруге зустрічається на позиції {second_index}")
    else:
        print("Слово 'Tom' вдруге не знайдено в тексті.")
else:
    print("Слово 'Tom' не знайдено в тексті.")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(". ")
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

lower_sentance = adwentures_of_tom_sawer_sentences[3].lower()
print(lower_sentance)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for sentance in adwentures_of_tom_sawer_sentences:
    if sentance.startswith("By the time"):
        print("True. Рядок починається  з 'By the time'")
    else:
        print("False. Рядок не починається  з 'By the time'")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

last_sentance = adwentures_of_tom_sawer_sentences[-1]
word_count = len(last_sentance.split())
print(f"Кількість слів в останньому реченні: {word_count}")
