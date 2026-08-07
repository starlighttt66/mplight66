tracks = []
current = None


def load(paths):
    global tracks, current
    tracks = list(paths)
    current = 0 if tracks else None


def current_track():
    if current is None:
        return None
    return tracks[current]
