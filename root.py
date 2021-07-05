from github import Github
import os
import github
from functions import get_repo_name,get_sort_by,get_order,get_ignore_word,get_repos,list_repos

import sys

load_dotenv()
token = str(sys.argv[-1])
g = Github(token)

def main():
    repo_name = get_repo_name()
    sort = get_sort_by()
    order = get_order()
    ignore_word = get_ignore_word()

    repos = get_repos(g,repo_name,sort,order,ignore_word)

    list_repos(repos)





main()
