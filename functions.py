import github
from datetime import datetime



now = datetime.now()
current_time = now.strftime("%Y-%m-%d-%H:%M")

def get_repos(g,repo_name,sort,order,ignore_word):

    f = open(f"logs/github-api.txt","a")
    f.write("\n" + current_time + ":     " + repo_name + "     " + sort + "     " + order + "     " + ignore_word  +  "\n" )
    f.close()

    try:
        print("Loading....")
        repositories = g.search_repositories(query=repo_name, sort=sort,order=order)
    except Exception as e:
        raise e


    repos = []



    for r in repositories:
        if ignore_word == "":
            repos.append(r)
        elif ignore_word in r.name:
            continue
        else:
            repos.append(r)


    return repos




def get_repo_name():
    repo_name = str(input("Enter repo name: "))

    return repo_name





def get_sort_by():
    sort_by = input("sort by? (stars,forks or updated): ")

    while sort_by != "stars" and sort_by != "forks" and sort_by != "updated":
        sort_by = input("please enter one of the option (stars,forks or updated):")

    return sort_by




def get_order():
    order = input("enter order: (asc or desc): ")

    while order != "asc" and order != "desc":
        order = input("please enter one of the option (asc or desc):")

    return order

def get_ignore_word():
    ignore_word = str(input("enter the word that you want to be ignored in the repo name(if nothing keep blank): "))

    return ignore_word


def list_repos(repos):


    for i,r in enumerate(repos):

        f = open(f"logs/responses-github-api.txt","a")
        f.write("\n" + current_time + ":  " + r.full_name  +  "\n" )
        f.close()
        print(i+1,r.full_name)
