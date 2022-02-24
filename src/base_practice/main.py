from collections import defaultdict
import datetime
from base_practice.entities.entities import Contributor, Skill, Proj, Role
from base_practice.io_ops import IOOps
from itertools import count


def main(filename):
    io_ops = IOOps()
    contributors = []
    projects = []
    contributor_by_skills = defaultdict(list)

    # parse the file
    (num_contr, num_proj), lines = io_ops.read_file(filename)
    index_c = 0
    for _ in range(num_contr):
        c = lines[index_c]
        con = Contributor(name=c[0])
        num_skills = int(c[1])
        for j in range(num_skills):
            line = lines[index_c + j + 1]
            skill_name = line[0]
            skill_lvl = int(line[1])
            skill = Skill(name=skill_name, level=skill_lvl)
            con.skills.append(skill)
            contributor_by_skills[skill_name].append((con, skill))
        index_c += num_skills
        contributors.append(con)
        index_c += 1

    for _ in range(num_proj):
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

    # print("parsed")

    plan = []
    end_all_ongoing_projects = -1
    for i in count(0):
        # print(f"day {i}")
        chosen = next((x for x in projects if x.hire(contributor_by_skills, i)), None)
        # print(chosen)
        if not chosen:
            if end_all_ongoing_projects < i:
                break
            continue
        projects.remove(chosen)
        assert chosen.end_day > 0
        assert len(chosen.hires) > 0
        end_all_ongoing_projects = max(chosen.end_day, end_all_ongoing_projects)
        plan.append(chosen)

    # print(plan)
    # output
    ts = datetime.datetime.now().timestamp()
    io_ops.write_objects_in_file(f"{filename}{ts}.out", plan)


if __name__ == "__main__":
    file_names = [
        # "a_an_example.in.txt",
        # "b_better_start_small.in.txt",
        # "c_collaboration.in.txt",
        # "d_dense_schedule.in.txt",
        # "e_exceptional_skills.in.txt",
        "f_find_great_mentors.in.txt",
    ]
    for f in reversed(file_names):
        main(f)
