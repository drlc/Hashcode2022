from base_practice.entities.entities import Contributor, Skill, Proj, Role
from base_practice.io_ops import IOOps

file_names = [
    "a_an_example.in.txt",
    "b_better_start_small.in.txt",
    "c_collaboration.in.txt",
    "d_dense_schedule.in.txt",
    "e_exceptional_skills.in.txt",
    "f_find_great_mentors.in.txt"
]


def main():
    io_ops = IOOps()
    contributors = []
    projects = []
    file_name = "a_an_example.in.txt"

    # parse the file
    (num_contr, num_proj), lines = io_ops.read_file(file_name)
    index_c = 0
    for i in range(num_contr):
        c = lines[index_c]
        con = Contributor(name=c[0])
        num_skills = int(c[1])
        for j in range(num_skills):
            line = lines[index_c + j + 1]
            con.skills.append(Skill(name=line[0], level=int(line[1])))
        index_c += num_skills
        contributors.append(con)
        index_c += 1

    for i in range(num_proj):
        p = lines[index_c]
        proj = Proj(name=p[0], days=int(p[1]), score=int(p[2]), best_before=int(p[3]))
        num_roles = int(p[4])
        for j in range(num_roles):
            line = lines[index_c + j + 1]
            ls = line
            proj.roles.append(Role(name=ls[0], level=int(ls[1])))
        index_c += num_roles
        projects.append(proj)
        index_c += 1

    print("parsed")
