class Solution:
    def numUniqueEmails(self, emails):
        emails_uniq = []
        for email in emails:
            print(email)
            local, domain = email.split("@")
            if "." in local:
                local = "".join(local.split("."))
            if "+" in local:
                local = local.split("+")[0]
            new_email = local + domain
            if new_email not in  emails_uniq:
                emails_uniq.append(new_email)
            print(emails_uniq)
        return len(emails_uniq)

if __name__ == "__main__":
    emails=["a@neetcode.com","b@neetcode.com","c@neetcode.com"]
    sol = Solution()
    k = sol.numUniqueEmails(emails)
    print(k)
