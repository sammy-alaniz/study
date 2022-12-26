'''
Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.

Example 1

Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.

Example 2

Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
Output: 3

Constraints:

1 <= emails.length <= 100
1 <= emails[i].length <= 100
emails[i] consist of lowercase English letters, '+', '.' and '@'.
Each emails[i] contains exactly one '@' character.
All local and domain names are non-empty.
Local names do not start with a '+' character.
Domain names end with the ".com" suffix.

'''

# have an array that stores the received addresses
# add only if the array does not already contain the address
# after iterating through the email list, return the length of email array

class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails = []
        
        for email in emails:
            split_email = email.split('@')
            local_name = split_email[0]
            domain_name = split_email[1]
            
            # remove '.'s from local_name
            local_name = local_name.replace('.','')
                
            # plus sign rule
            plus_sign_index = local_name.find('+')
            if plus_sign_index != -1:
                split_plus_local_name = local_name.split('+')
                local_name = split_plus_local_name[0]
                
            full_name = local_name + '@' + domain_name
                
            if full_name not in unique_emails:
                unique_emails.append(full_name)
                
        return len(unique_emails)
                
              

if __name__ == "__main__":
    print('i got this right!')

    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

    sol = Solution()
    num = sol.numUniqueEmails(emails)
    print(num)