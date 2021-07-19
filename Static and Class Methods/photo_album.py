from math import ceil


class PhotoAlbum:
    MAX_PHOTOS = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / PhotoAlbum.MAX_PHOTOS)
        return cls(pages)

    def add_photo(self, label: str):
        for page in range(len(self.photos)):
            if len(self.photos[page]) < PhotoAlbum.MAX_PHOTOS:
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page+1} slot {self.photos[page].index(label)+1}"
        return "No more free slots"

    def display(self):
        result = "-----------\n"
        for page in self.photos:
            if page:
                result += " ".join(['[]' for _ in page])
            result += "\n-----------\n"
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

