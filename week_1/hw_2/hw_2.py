import sys
import os


def formatter(text):
    removed_chars = "\n\t,.!?:()[]{}\"'"
    text = text.replace(" - ", " ")
    text = text.translate(str.maketrans({ch: " " for ch in removed_chars}))
    return text


def counter(text):
    result = {}
    for word in text:
        if word != "":
            if word in result.keys():
                result[word] += 1
            else:
                result[word] = 1
    return result


def main():
    filename = sys.argv[1]
    wrk_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    with open(f"{wrk_dir}/{filename}", "r", encoding="utf-8") as file:
        content = file.read()
        formatted_content = formatter(content)
        words = formatted_content.split(" ")
        words = [w.lower() for w in words]
        counts = counter(words)
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        top_words = "\n- ".join(
            [f"{word}: {count}" for word, count in sorted_counts[:10]]
        )
        print(f"Самые популярные слова:\n- {top_words}")
        pass


if __name__ == "__main__":
    main()
