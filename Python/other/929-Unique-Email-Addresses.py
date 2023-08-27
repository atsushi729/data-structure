class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        ans = set()
        for email in emails:
            local, domain = map(str, email.split("@"))

            fixed_local = self.getFixedLocalName(local)
            fixed_email = fixed_local + "@" + domain
            ans.add(fixed_email)
        return len(ans)

    def getFixedLocalName(self, local_name: str) -> str:

        local_name = local_name.replace(".", "")

        if '+' in local_name:
            index = local_name.index('+')
            local_name = local_name[:index]
        return local_name


if __name__ == "__main__":
    s = Solution()
    emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
    print(s.numUniqueEmails(emails))
