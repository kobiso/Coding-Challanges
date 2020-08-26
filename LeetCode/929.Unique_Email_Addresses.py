class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            [local, domain] = email.split('@')
            pre_local = local.split('+')[0]            
            refined_local = pre_local.replace('.', '')
            unique.add(refined_local+'@'+domain)
        return len(unique)