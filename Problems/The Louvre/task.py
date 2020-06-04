class Painting:
    museum = "the Louvre"

    def __init__(self, title, painter, creation_year):
        self.title = title
        self.creation_year = creation_year
        self.painter = painter


entry = Painting(input(), input(), int(input()))
print(f'"{entry.title}" by {entry.painter} ({entry.creation_year}) hangs in the Louvre.')
