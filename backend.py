from pathlib import Path

from typing import Optional
import mpv

_player = None

def _player_instance():
    global _player
    if _player is None:
        _player = mpv.MPV(
            video=False,
            audio_display="no",
            ytdl=False,
        )
    return _player


def prefetch(path: Optional[str | Path]):
    if path is None:
        return
    player = _player_instance()
    player.play(str(Path(path).resolve()))
    player.wait_until_playing(timeout=5)
    player.pause = True

def play(path: str | Path):
    _player_instance().play(str(Path(path).resolve()))

def pause_switch():
    _player_instance().pause = not _player_instance().pause

def pause():
    _player_instance().pause = True

def resume():
    _player_instance().pause = False

def stop():
    _player_instance().stop()

def seek(seconds: float):
    _player_instance().seek(seconds, reference="absolute")

def position() -> float:
    return _player_instance().time_pos or 0.0

def duration() -> float:
    return _player_instance().duration or 0.0

def get_volume() -> int:
    return int(_player_instance().volume)

def set_volume(value: int):
    _player_instance().volume = max(0, min(value, 100))

def is_playing() -> bool:
    return not _player_instance().pause

def shutdown():
    _player_instance().terminate()
