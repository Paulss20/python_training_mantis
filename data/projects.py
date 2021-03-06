
from model.project import Project
import random
import string


# project = [
#     Project(name="project_name_1", status="development", view_state="public", description="description_1")]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Project(name=random_string("name", 10), status=random.choice(['development', 'release', 'stable', 'obsolete']),
                    view_state="public", description=random_string("description", 10))
            for i in range(1)
]