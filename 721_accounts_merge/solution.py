from typing import List
import collections
from unionfind import UnionFind


def accounts_merge_using_union_find(
        accounts: List[List[str]]) -> List[List[str]]:

    uf = UnionFind()
    email_to_name = dict()

    for account in accounts:
        name = account[0]
        for email in account[1:]:
            email_to_name[email] = name
            uf.union(email, account[1])

    return [[email_to_name[pmail]] + sorted(emails)
            for (pmail, emails) in uf.groups().items()]
