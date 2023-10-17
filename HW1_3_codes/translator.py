class CustomTranslator:
    def __init__(self):
        self.translations = {
            "en": {
                "online": "online",
                "just now": "just now",
                "less than a minute ago": "less than a minute ago",
                "a couple of minutes ago": "a couple of minutes ago",
                "an hour ago": "an hour ago",
                "today": "today",
                "yesterday": "yesterday",
                "this week": "this week",
                "a long time ago": "a long time ago"
            },
            "uk": {
                "online": "в мережі",
                "just now": "в мережі щойно",
                "less than a minute ago": "в мережі менше хвилини тому",
                "a couple of minutes ago": "в мережі кілька хвилин тому",
                "an hour ago": "в мережі годину тому",
                "today": "в мережі сьогодні",
                "yesterday": "в мережі вчора",
                "this week": "в мережі цього тижня",
                "a long time ago": "в мережі давно"
            },
            "ja": {
                "online": "オンライン",
                "just now": "たった今",
                "less than a minute ago": "1分未満前",
                "a couple of minutes ago": "数分前",
                "an hour ago": "1時間前",
                "today": "今日",
                "yesterday": "昨日",
                "this week": "今週",
                "a long time ago": "以前"
            },
            "fi": {
                "online": "verkossa",
                "just now": "juuri nyt",
                "less than a minute ago": "alle minuutti sitten",
                "a couple of minutes ago": "muutama minuutti sitten",
                "an hour ago": "tunti sitten",
                "today": "tänään",
                "yesterday": "eilen",
                "this week": "tällä viikolla",
                "a long time ago": "kauan sitten"
            }
        }

    def translate(self, text, language):
        if language in self.translations:
            return self.translations[language].get(text, text)
        else:
            print("This language is not available yet")
            return text
