from typing import List
from re import findall

# https://leetcode.com/problems/unique-email-addresses/
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniques = set()
        for email in emails:
            name, domain = findall(r'([^+]+)(?:\+[^@]+)?@([^@]+)', email)[0]
            uniques.add((name.replace('.', ''), domain))
        return len(uniques)
