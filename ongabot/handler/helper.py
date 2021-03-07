def assembleEventHeader(selected):
    titleText = "ON/GA time, 21/11 kl 17.30"
    infoText = "Insert priority here"
    selectionText = "Selected: {}".format(selected)
    message = "{}\n{}\n{}".format(titleText, infoText, selectionText)
    return message


def assembleEventButtons():
    options = [
        "17.30",
        "18.30",
        "19.30",
        "20.30",
        "noop",
        "maybe baby",
    ]

    return options


def helpText():
    """Print the help text for a /start or /help command"""
    helpText = (
        "Welcome traveler, my name is ONGAbot.\n"
        "I'm the one and only, the truth speaker.\n"
        "\n"
        "My duties are:\n"
        " - Uphold the law, obviously, with weekly ON/GA polls\n"
        " - Give praise to the faithful\n"
        " - Aid the needing\n"
        " - Condemn the wicked\n"
        "\n"
        "Commandments:\n"
        "/help - To show this very helpful text\n"
        "/onga - Print the image of the one\n"
        "/newevent - Create a new event, args=TBD\n"
    )

    return helpText

