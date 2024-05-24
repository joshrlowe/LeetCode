class Node:
    def __init__(self, value):
        self.val = value
        self.next = self.prev = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.current_page = Node(homepage)

    def visit(self, url: str) -> None:
        self.current_page.next = Node(url)
        self.current_page.next.prev = self.current_page
        self.current_page = self.current_page.next

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if not self.current_page.prev:
                break
            self.current_page = self.current_page.prev
        return self.current_page.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if not self.current_page.next:
                break
            self.current_page = self.current_page.next
        return self.current_page.val
