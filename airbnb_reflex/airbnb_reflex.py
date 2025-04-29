import reflex as rx

from rxconfig import config

from .pages.listings import listings
from .pages.search import search_page


class State(rx.State):
    """The app state."""
    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
app.add_page(listings, route="/listings", title="Listings")
app.add_page(search_page, route="/search", title="Search")

# 🔥 STOP HERE — **NO `app.compile()`**, NO `if __name__ == "__main__"`!
