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


def test_browser_history():
    # Test case 1: Basic navigation
    print("Test case 1: Basic navigation")
    history = BrowserHistory("homepage.com")
    history.visit("page1.com")
    history.visit("page2.com")
    assert history.back(1) == "page1.com"  # Go back to page1.com
    assert history.back(1) == "homepage.com"  # Go back to homepage.com
    assert history.forward(1) == "page1.com"  # Forward to page1.com
    assert history.forward(1) == "page2.com"  # Forward to page2.com
    print("Passed")

    # Test case 2: Back more than history
    print("Test case 2: Back more than history")
    history = BrowserHistory("homepage.com")
    history.visit("page1.com")
    assert (
        history.back(2) == "homepage.com"
    )  # Try to go back more than available history
    print("Passed")

    # Test case 3: Forward more than history
    print("Test case 3: Forward more than history")
    history = BrowserHistory("homepage.com")
    history.visit("page1.com")
    history.visit("page2.com")
    history.back(2)
    assert (
        history.forward(3) == "page2.com"
    )  # Try to go forward more than available history
    print("Passed")

    # Test case 4: Visit after going back
    print("Test case 4: Visit after going back")
    history = BrowserHistory("homepage.com")
    history.visit("page1.com")
    history.visit("page2.com")
    history.back(1)
    history.visit("page3.com")  # Visit after going back, should clear forward history
    assert (
        history.forward(1) == "page3.com"
    )  # No forward history, should stay on page3.com
    assert history.back(2) == "homepage.com"  # Go back to homepage.com
    print("Passed")

    # Test case 5: Multiple visits and navigations
    print("Test case 5: Multiple visits and navigations")
    history = BrowserHistory("homepage.com")
    history.visit("page1.com")
    history.visit("page2.com")
    history.visit("page3.com")
    assert history.back(2) == "page1.com"  # Go back to page1.com
    assert history.forward(1) == "page2.com"  # Forward to page2.com
    history.visit("page4.com")  # Visit after going back, should clear forward history
    assert (
        history.forward(1) == "page4.com"
    )  # No forward history, should stay on page4.com
    assert history.back(3) == "homepage.com"  # Go back to homepage.com
    print("Passed")


if __name__ == "__main__":
    test_browser_history()
