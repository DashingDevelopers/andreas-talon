search for <user.text>$:
    user.browser_search(text)

search for (this | dis | is):
    user.browser_search_selected()

define word <user.word>$:
    user.browser_search("https://www.merriam-webster.com/dictionary/{word}")
