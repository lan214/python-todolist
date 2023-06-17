import webbrowser

search_term = input("What to search: ").replace(" ", "+")

webbrowser.open("https://www.google.com/search?q=" + search_term)
