from threading import Thread
from pathlib import Path
import flet as ft
import asyncio
import backend


def main(page: ft.Page):
    page.title = "Player"

    tracks: list[Path] = []

    playlist = ft.ListView(
        expand=True,
        spacing=0,
    )

    def refresh_playlist():
        playlist.controls.clear()

        for track in tracks:
            playlist.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.MUSIC_NOTE),
                    title=ft.Text(track.name),
                    on_click=lambda _, path=track: (backend.play(path), print(path)),
                )
            )

        page.update()

    async def add_tracks(_):
        files = await picker.pick_files(
            allow_multiple=True
        )
        if files:
            tracks.extend(Path(file.path) for file in files)
            refresh_playlist()

    picker = ft.FilePicker()

    page.services.append(picker)

    add_button = ft.IconButton(
        icon=ft.Icons.ADD,
        tooltip="Add tracks",
        on_click=add_tracks,
    )


    position_slider = ft.Slider(
        min=0,
        max=0,
        value=0,
        expand=True,
    )

    def toggle_play(e):
        backend.pause_switch()

        pause_switch_btn.icon = (
            ft.Icons.PAUSE_CIRCLE_ROUNDED
            if backend.is_playing()
            else ft.Icons.PLAY_CIRCLE_ROUNDED
        )

        pause_switch_btn.update()


    pause_switch_btn = ft.IconButton(
        icon=ft.Icons.PLAY_CIRCLE_ROUNDED,
        on_click=toggle_play,
    )
    stop_btn = ft.IconButton(
        icon=ft.Icons.STOP,
        on_click=lambda _: backend.stop(),
    )

    async def update_position():
        while True:
            position_slider.value = backend.position()
            position_slider.max = backend.duration()

            page.update()

            await asyncio.sleep(0.25)


    Thread(
        target=update_position,
        daemon=True,
    ).start()


    page.add(
        ft.Row(
            [
                ft.Text("Playlist", expand=True),
                add_button,
            ]
        ),
        playlist,
        position_slider,
        ft.Row(
            [
                pause_switch_btn,
                stop_btn
            ]
        )
    )
    page.run_task(update_position)


Thread(target= lambda : backend._player_instance(), daemon=True).start()

ft.run(main)
