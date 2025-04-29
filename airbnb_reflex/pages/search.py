import reflex as rx
import httpx

class SearchState(rx.State):
    # query: str = ""
    result: str = ""

    async def do_search(self):
        # if not self.query:
        #     self.result = ""
        #     return
        try:
            async with httpx.AsyncClient() as client:
                resp = await client.get(f"/api/search")
                self.result = resp.text
        except Exception as e:
            self.result = f"Error: {str(e)}"

def search_page():
    return rx.vstack(
        rx.heading("Search"),
        # rx.input(
        #     placeholder="Type your query...",
        #     on_change=SearchState.set_query,
        #     width="100%",
        # ),
        rx.button("Search", on_click=SearchState.do_search),
        rx.divider(),
        rx.text("Result:"),
        rx.text(SearchState.result, color="blue.600", font_weight="medium", white_space="pre-wrap"),
        spacing="4",
        width="100%",
        max_width="600px",
        margin="auto",
        padding_top="2em"
    )
