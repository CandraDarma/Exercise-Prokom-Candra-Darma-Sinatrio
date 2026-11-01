favorite_languages = {
    "jen": {"language": "python", "level": "mahir"},
    "sarah": {"language": "c", "level": "pemula"},
    "edward": {"language": "rust", "level": "menengah"},
}

for name, info in favorite_languages.items():
    print(f"{name.title()} suka {info['language'].title()} (level: {info['level']}).")
