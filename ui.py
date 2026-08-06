import flet as ft

import backend


def main(page: ft.Page):
    page.title = "Player"

    play_btn = ft.IconButton(
        icon=ft.Icons.PLAY_ARROW,
        on_click=lambda _: backend.play("assets/test.mp3"),
    )

    stop_btn = ft.IconButton(
        icon=ft.Icons.STOP,
        on_click=lambda _: backend.stop(),
    )

    page.add(
        ft.Row([play_btn, stop_btn])
    )


backend._player_instance()
ft.run(main)