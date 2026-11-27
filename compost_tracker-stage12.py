# === Stage 12: Поиск по нескольким словам ===
# Project: CompostTracker
def parse_search_terms(query):
    """Разбор поискового запроса на обязательные ключевые слова и исключения.

    Исключения задаются через префикс «-» и не входят в обязательные условия.
    Возвращает кортеж (required_terms, exclude_terms), где оба элемента — списки строк.
    """
    required_terms = []
    exclude_terms = []
    query = query.strip()
    if not query:
        return required_terms, exclude_terms
    for token in query.split():
        if token.startswith('-'):
            exclude_terms.append(token[1:].strip())
        else:
            required_terms.append(token)
    return required_terms, exclude_terms


def search_piles(piles, query):
    """Поиск куч компоста по запросу с поддержкой исключений.

    Куча считается подходящей, если она содержит все обязательные слова
    и не содержит ни одного из слов-исключений. Поиск по словам — без учёта регистра.
    """
    required_terms, exclude_terms = parse_search_terms(query)
    results = []
    for pile in piles:
        pile_terms = pile.get_terms().lower().split()
        if all(term in pile_terms for term in required_terms):
            if not any(term in pile_terms for term in exclude_terms):
                results.append(pile)
    return results


class Pile:
    """Куча компоста."""

    def __init__(self, name, volume, moisture, created_date):
        self.name = name
        self.volume = volume
        self.moisture = moisture
        self.created_date = created_date

    def get_terms(self):
        """Сбор всех слов из названия и даты закладки кучи."""
        terms = [self.name.lower()]
        if self.created_date:
            terms.extend(self.created_date.split())
        return terms
