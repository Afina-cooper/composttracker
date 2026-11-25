# === Stage 11: Текстовый поиск ===
# Project: CompostTracker
import re


def highlight(text, needles):
    """Подсветить совпадения по списку игнорируя регистр."""
    if not needles:
        return text, []
    text = str(text)
    needles = [n for n in needles if n]
    if not needles:
        return text, []
    pattern = re.compile(
        "|".join(re.escape(n) for n in needles), re.IGNORECASE
    )

    def repl(match):
        return "\033[7m" + match.group(0) + "\033[0m"

    return pattern.sub(repl, text), list(pattern.finditer(text))


def search_piles(piles, query):
    """Найти кучи по текстовым полям без учёта регистра."""
    query = query.strip()
    if not query:
        return []
    pattern = re.compile(re.escape(query), re.IGNORECASE)

    results = []
    for pile in piles:
        haystack = (
            str(pile.get("название", ""))
            + " "
            + str(pile.get("влажность", ""))
            + " "
            + str(pile.get("дата закладки", ""))
        )
        if pattern.search(haystack):
            text, matches = highlight(haystack, [query])
            results.append({"pile": pile, "text": text, "matches": matches})
    return results


def format_search_results(results):
    """Собрать строку вывода с подсвеченными совпадениями."""
    lines = []
    for item in results:
        text = item["text"]
        lines.append(text)
        if item["matches"]:
            lines.append("  совпадений: " + str(len(item["matches"])))
    return "\n".join(lines)


if __name__ == "__main__":
    sample = [
        {"название": "Весенняя куча", "объём": 20, "влажность": 55, "дата закладки": "2024-03-05"},
        {"название": "Зимняя куча", "объём": 15, "влажность": 60, "дата закладки": "2023-12-20"},
        {"название": "Осеньяя куча", "объём": 30, "влажность": 50, "дата закладки": "2023-10-10"},
    ]
    query = "куча"
    results = search_piles(sample, query)
    print(format_search_results(results))
