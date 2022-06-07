from ed_analytics.github import Repository
import sqlite3 as sq


rep = Repository("revacprogramming","python101-imryanide")
coms = rep.get_commits()
for commit in coms:
    print("{} \n{} \n{}".format(
        commit[0].author_github_username,
        commit[0].sha,
        commit[0].timestamp
        ))


conn = sq.connect("test.db")
cursor = conn.cursor()

cursor.execute(
        "create table test if not exists")



