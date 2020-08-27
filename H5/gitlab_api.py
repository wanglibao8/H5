#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Author: Jinyu
# modify: Wang
import gitlab

gl = gitlab.Gitlab.from_config('git', 'git.conf')
print(gl.version())

class GitlabApi:
    """
    定义gitlab api接口的类
    """

    @staticmethod
    def get_group():
        group_list = []
        all_groups = gl.groups.list(all=True)
        for group in all_groups:
            group_list.append(group.name)
        for index, item in enumerate(group_list):
            group_list[index] = [item, item]
        return group_list

    @staticmethod
    def get_project_id(group_name, app_name=None):
        all_groups = gl.groups.list(all=True)
        for group in all_groups:
            if group_name == group.name:
                projects_config = group.projects.list(all=True, as_list=False)
                for project in projects_config:
                    if app_name == project.name:
                        return project.id

    @staticmethod
    def get_tags(projects):
        tag_list = []
        project = gl.projects.get(projects)
        tags_all = project.tags.list()
        for tag in tags_all:
            tag_list.append(tag.name)
        for index, item in enumerate(tag_list):
            tag_list[index] = [item, item]
        return tag_list

    @staticmethod
    def get_branches(projects):
        branch_list = []
        project = gl.projects.get(projects)
        branches_all = project.branches.list()
        for branch in branches_all:
            branch_list.append(branch.name)
        for index, item in enumerate(branch_list):
            branch_list[index] = [item, item]
        return branch_list

    @staticmethod
    def get_branch(projects):
        branch_list = []
        project = gl.projects.get(projects)
        branches_all = project.branches.list()
        for branch in branches_all:
            branch_list.append(branch.name)
        return branch_list

    def create_branch(self, branch_name, group_name, app_name):
        projects = self.get_project_id(group_name, app_name)
        project = gl.projects.get(projects)
        branch = project.branches.create({'branch': branch_name, 'ref': 'master'})
        if branch.name in self.get_branch(projects):
            repo_name = branch.name
        else:
            repo_name = "branch create fail"
        return repo_name


if __name__ == '__main__':
    aa = GitlabApi.get_group()
    print(aa)
    bb = GitlabApi.get_project_id(group_name="sa", app_name="H5")
    print(bb)
    cc = GitlabApi.get_tags(bb)
    print(cc)
    dd = GitlabApi.get_branch(bb)
    print(dd)