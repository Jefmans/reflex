import reflex as rx
from airbnb_reflex.layout import layout

# Dummy listings
properties = [
    {"name": "Seaside Villa", "location": "Spain", "price": 120},
    {"name": "Mountain Cabin", "location": "Switzerland", "price": 150},
    {"name": "City Loft", "location": "New York", "price": 200},
]

def listings():
    return layout(
        rx.heading("Available Listings"),
        rx.grid(
            *[
                rx.box(
                    rx.text(prop["name"], font_weight="bold"),
                    rx.text(prop["location"]),
                    rx.text(f"${prop['price']}/night"),
                    border="1px solid #ddd",
                    padding="1em",
                    border_radius="xl",
                )
                for prop in properties
            ],
            columns="1",
            spacing="4"
        )
    )
