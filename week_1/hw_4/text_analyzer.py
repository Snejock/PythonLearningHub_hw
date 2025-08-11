import sys
import os


def formatter(text):
    removed_chars = "\n\t,.!?:()[]{}\"'"
    text = text.replace(" - ", " ")
    text = text.translate(str.maketrans({ch: " " for ch in removed_chars}))
    return text


def analyze(text):
    lines_cnt = len(text.splitlines())
    formatted_txt = formatter(text)

    # находит самое длинное и короткое слово, количество слов
    max_word, min_word = "", ""
    words_cnt = 0
    for word in formatted_txt.split(" "):
        if max_word == "" or len(word) > len(max_word):
            max_word = word
        if min_word == "" or len(word) < len(min_word):
            min_word = word
        words_cnt += 1

    # подсчитывает частоту встречаемости каждой буквы (игнорируя регистр), число символов
    chars_dct = {}
    chars_cnt = 0
    for char in formatted_txt.lower().replace(" ", ""):
        if char in chars_dct.keys():
            chars_dct[char] += 1
        else:
            chars_dct[char] = 1
        chars_cnt += 1
    sorted_chars_cnt = sorted(chars_dct.items(), key=lambda x: x[0])

    return lines_cnt, words_cnt, max_word, min_word, chars_cnt, sorted_chars_cnt


def main():
    filename = sys.argv[1]
    wrk_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    with open(f"{wrk_dir}/{filename}", "r", encoding="utf-8") as file:
        content = file.read()
        lines_cnt, words_cnt, max_word, min_word, chars_cnt, sorted_chars_cnt = analyze(content)
        print(f"Статистика файла sample.txt: {filename}")
        print(f"Строк: {lines_cnt}")
        print(f"Слов: {words_cnt}")
        print(f"Символов: {chars_cnt}")
        print(f"Самое длинное слово: {max_word}")
        print(f"Самое короткое слово: {min_word}")
        print("Частота букв: " + ", ".join([f"{char}={count}" for char, count in sorted_chars_cnt]))
    with open(f"{wrk_dir}/analysis_results.txt", "w", encoding="utf-8") as file:
        file.write(f"Статистика файла sample.txt: {filename}\n")
        file.write(f"Строк: {lines_cnt}\n")
        file.write(f"Слов: {words_cnt}\n")
        file.write(f"Символов: {chars_cnt}\n")
        file.write(f"Самое длинное слово: {max_word}\n")
        file.write(f"Самое короткое слово: {min_word}\n")
        file.write("Частота букв: " + ", ".join([f"{char}={count}" for char, count in sorted_chars_cnt]) + "\n")


if __name__ == "__main__":
    main()
