from threading import Thread
import flet as ft

import backend


def main(page: ft.Page):
    page.title = "Player"

    play_btn = ft.IconButton(
        icon=ft.Icons.PLAY_ARROW,
        on_click=lambda _: backend.pause(),
    )

    stop_btn = ft.IconButton(
        icon=ft.Icons.STOP,
        on_click=lambda _: backend.stop(),
    )

    page.add(
        ft.Row([play_btn, stop_btn])
    )

Thread(target= lambda : ( backend._player_instance(), backend.prefetch("assets/test.mp3")), daemon=True).start()

ft.run(main)
