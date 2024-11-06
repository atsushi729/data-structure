"""
1472. Design Browser History

"""
import unittest


class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class DesignBrowserHistory:
    def __init__(self, homepage: str):
        self.current = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.current.next = ListNode(url, self.current)
        self.current = self.current.next

    def back(self, steps: int) -> str:
        while self.current.prev and steps > 0:
            self.current = self.current.prev
            steps -= 1
        return self.current.val

    def forward(self, steps: int) -> str:
        while self.current.next and steps > 0:
            self.current = self.current.next
            steps -= 1
        return self.current.val


class TestBrowserHistory(unittest.TestCase):
    def test_browser_history(self):
        browser = DesignBrowserHistory("leetcode.com")
        browser.visit("google.com")
        browser.visit("facebook.com")
        browser.visit("youtube.com")
        self.assertEqual(browser.back(1), "facebook.com")  # youtube.com -> facebook.com
