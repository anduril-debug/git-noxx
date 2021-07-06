from github import Github
import os
import github
from functions import get_repo_name,get_sort_by,get_order,get_ignore_word,get_repos,list_repos
from dotenv import load_dotenv
import sys


load_dotenv()
token = os.environ.get("GIT_TOKEN")
g = Github(token)

def do_again(cont):
    if cont == "yes":
        main()
    elif cont == "no":
        pass
    else:
        cont = input("Please write correctly! Continue? (yes or no): ")
        do_again(cont)


def main():
    repo_name = get_repo_name()
    sort = get_sort_by()
    order = get_order()
    ignore_word = get_ignore_word()

    repos = get_repos(g,repo_name,sort,order,ignore_word)

    list_repos(repos)

    cont = input("Continue? (yes or no): ")
    do_again(cont)







main()
