class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        answer = set()

        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            answer.add((local + "@" + domain))
        return len(answer)


if __name__ == "__main__":
    s = Solution()
    emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
    print(s.numUniqueEmails(emails))
