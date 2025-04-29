import reflex as rx

def navbar():
    return rx.hstack(
        rx.text("🏡 AirReflex", font_size="2xl", font_weight="bold"),
        rx.spacer(),
        rx.link("Home", href="/"),
        rx.link("Listings", href="/listings"),
        padding="1em",
        bg="gray.100",
        border_bottom="1px solid #ccc"
    )

def layout(*children):
    return rx.vstack(
        navbar(),
        rx.container(*children, max_width="800px", margin_y="2em"),
        rx.link("Search", href="/search"),

    )
