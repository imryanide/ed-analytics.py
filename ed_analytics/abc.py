import datetime


class Commit:
    """
    Attributes
    ----------
    sha : str
        SHA of the commit

    timestamp : datetime.datetime
        Timestamp of the commit

    author : dict
        The author dictionary in the commit

    author_github_username : str
        GitHub username of the author

    htmlURL : str
        HTML URL of the commit
    """

    def __init__(self, kw):
        self.sha = kw["sha"]
        self.author = kw["author"]
        self.timestamp = datetime.datetime.strptime(
            kw["commit"]["author"]["date"], "%Y-%m-%dT%H:%M:%SZ")
        self.author_github_username = kw["author"]["login"]
        self.htmlURL = kw["html_url"]
        
        self.kw = kw

    def __getitem__(self, item):
        return self.kw[item]


class Submission:
    """Class to contain individual assignment submission operations"""

    def __init__(self, **kw) -> None:
        self.kw = kw
