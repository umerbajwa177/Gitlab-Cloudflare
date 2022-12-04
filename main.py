import gitlab
import http.client
import configargparse
import logging
import time

# Logger Requirment Setting
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
f = logging.Formatter('%(levelname)s - %(message)s')
fh = logging.FileHandler('logging.log')
fh.setFormatter(f)
logger.addHandler(fh)


# API Token GitLab
token = 'token'
gl = gitlab.Gitlab()
gl = gitlab.Gitlab('https://gitlab.com')
gl = gitlab.Gitlab(private_token=token)


#List of groups
start = time.perf_counter()
def list_groups():
    groups = gl.groups.list()
    logger.debug("Function is accurately working")
    return groups
end = time.perf_counter()
print('List_group function took:', end - start, 'seconds')



# list projects in gitlab

start = time.perf_counter()
def list_project():
    Owned_projects = gl.projects.list(owned=True)
    logger.debug("Function is accurately working")
    return Owned_projects
end = time.perf_counter()
print('list_project function took:', end - start, 'seconds')



# first check if the Subgroup already exists

start = time.perf_counter()
def sub_group():
    all_groups = gl.groups.list()
    print(all_groups)
    target_group = gl.groups.list(visibility='private')
    print("Groups are", target_group)
    subgroups = gl.groups.get(59510945, lazy=True)
    print("subgroup is", subgroups)

    group = gl.groups.get(59510945)
    projects = group.projects.list()
    print("Projects of a groups are", projects)
    logger.debug("Function is accurately working")
    print(projects)
    for project in projects:
        if(len(project.path) == 0):
            print("zero")
            print(project)
        else:
            print("no")
            print(project)

end = time.perf_counter()
print('sub_group function took:', end - start, 'seconds')




start = time.perf_counter()
def check_project():
    COMPANY_ID = "12345" 
    COMPANY_URL = "www.company.com"
    PROVISION_TYPE = "PROD"
    PROVISION_SUFFIX = "testdrive-company.com"
    if PROVISION_TYPE == "PROD":
       gl.groups.create({'name': 'www.company.com', 'path': COMPANY_URL, 'parent_id':59510945})
       logger.debug("Function is accurately working")
       print("TRAIL Done")
    if PROVISION_TYPE == "TRAIL":
       final_path = COMPANY_URL + PROVISION_SUFFIX
       gl.groups.create({'name': 'www.company.com','path': final_path, 'parent_id':59510945})
       logger.debug("Function is accurately working")
       print("PROD Done")
       #print("Project is", type(project.path))
    #print(target_group.web_url)


    #projects = gl.projects.list()
    #print("Projects are", projects)

    #real_group = gl.groups.get(subgroup_id, lazy=True)

    #print(real_group)
end = time.perf_counter()
print('check_project function took:', end - start, 'seconds')



# Another Code
#List of groups
# groups = gl.groups.list()
# print(groups)
# for gro in groups:
#     try:
#         print(gro)
#     except Exception as e:
#         create_subgroup = gl.groups.create({'name': 'newgroupsub', 'path': 'groupone', 'parent_id': 60313870})
#         print(create_subgroup) 




# Create a project in Gitlab

start = time.perf_counter()
# Create a project:
def create_project():
    create_proj = gl.projects.create({'name': 'projectpython'})
    logger.debug("Function is accurately working")
    return create_proj
    # print(create_project)
end = time.perf_counter()
print('create_project function took:', end - start, 'seconds')


# Fork project

start = time.perf_counter()

fromproj_id = ''
toproject_id = ''
def fork_project(fromproj_id, toproject_id):
    project = gl.projects.get(fromproj_id)
    fork = project.forks.create({'namespace_id': toproject_id})
    logger.debug("Function is accurately working")
    return fork
    # items = project.repository_tree()
    # print(items)
end = time.perf_counter()
print('fork_project function took:', end - start, 'seconds')



# Configargparser Step

start = time.perf_counter()
import configargparse
import os
from datetime import datetime
import time

CONFIG_PATH = os.path.expandvars("$HOME/.Chad/pythonapp.conf")


def buildArgParser() -> configargparse.ArgumentParser:
    ap = configargparse.ArgumentParser(
        default_config_files=[CONFIG_PATH],
        formatter_class=configargparse.ArgumentDefaultsRawHelpFormatter,
        description="Environment Variables Needed",
    )
    ap.add_argument("-v", action="count", default=0, help="Verbosity level, more -v means more information")
    ap.add_argument(
        "--company_url",
        action="store",
        env_var="COMPANY_URL",
        default="www.company.com",
        help="URL",
    )
    ap.add_argument(
        "--company_id",
        action="store",
        env_var="COMPANY_ID",
        default="12345",
        help="ID",
    )
    ap.add_argument(
        "--provision_type",
        action="store",
        env_var="PROVISION_TYPE",
        default="PROD",
        help="Type",
    )
    return ap
end = time.perf_counter()
print('buildArgParser function took:', end - start, 'seconds')

# argParser = buildArgParser()
# args = argParser.parse_args()
# print(args.company_id)




# CloudFlare Steps Code
email = "email"
key = "apikey"
conn = http.client.HTTPSConnection("api.cloudflare.com")

headers = {
     'X-Auth-Email': email,
     'X-Auth-Key': key
    }



# list projects from page

start = time.perf_counter()
def list_projects():
    conn.request("GET", "/client/v4/accounts/3d959d02071ae14768f75534adb0cf60/pages/projects", headers=headers)
    res = conn.getresponse()
    data = res.read()
    logger.debug("Function is accurately working")
    return data.decode("utf-8")
end = time.perf_counter()
print('list_projects function took:', end - start, 'seconds')


# CloudFlare Create Pages Project

start = time.perf_counter()
def create_projectt():
    payload = '{"name":"new-project","id":"7b162ea7-7367-4d67-bcde-1160995d5","created_on":"2017-01-01T00:00:00Z","subdomain":"new-project.pages.dev","domains":["customdomain.com","customdomain.org"],"source":{"type":"gitlab","config":{"owner":"saryaal.bajwa","repo_name":"new_project","production_branch":"main","pr_comments_enabled":true,"production_deployments_enabled":true,"preview_deployment_setting":"custom","preview_branch_includes":["release/*","production","main"],"preview_branch_excludes":["dependabot/*","dev","*/ignore"]}},"build_config":{"build_command":"npm run build","destination_dir":"build","root_dir":"/","web_analytics_tag":"cee1c73f6e4743d0b5e6bb1a0bcaabcc","web_analytics_token":"021e1057c18547eca7b79f2516f06o7x"},"deployment_configs":{"preview":{"env_vars":{"BUILD_VERSION":{"value":"3.3"}},"kv_namespaces":{"KV_BINDING":{"namespace_id":"5eb63bbbe01eeed093cb22bb8f5acdc3"}},"durable_object_namespaces":{"DO_BINDING":{"namespace_id":"5eb63bbbe01eeed093cb22bb8f5acdc3"}},"r2_buckets":{"R2_BINDING":{"name":"some-bucket"}},"d1_databases":{"D1_BINDING":{"id":"445e2955-951a-43f8-a35b-a4d0c8138f63"}},"compatibility_date":"2022-01-01","compatibility_flags":["url_standard"]},"production":{"env_vars":{"BUILD_VERSION":{"value":"3.3"}},"kv_namespaces":{"KV_BINDING":{"namespace_id":"5eb63bbbe01eeed093cb22bb8f5acdc3"}},"durable_object_namespaces":{"DO_BINDING":{"namespace_id":"5eb63bbbe01eeed093cb22bb8f5acdc3"}},"r2_buckets":{"R2_BINDING":{"name":"some-bucket"}},"d1_databases":{"D1_BINDING":{"id":"445e2955-951a-43f8-a35b-a4d0c8138f63"}},"compatibility_date":"2022-01-01","compatibility_flags":["url_standard"]}},"latest_deployment":{},"canonical_deployment":{},"production_branch":"main"}'
    conn.request("POST", "/client/v4/accounts/3d959d02071ae14768f75534adb0cf60/pages/projects", payload, headers)
    res = conn.getresponse()
    data = res.read()
    logger.debug("Function is accurately working")
    return data.decode("utf-8")
end = time.perf_counter()
print('create_projectt function took:', end - start, 'seconds')


# Cloudflare project_deployment

start = time.perf_counter()
def project_deployment():
    payload = ""
    conn.request("POST", "/client/v4/accounts/3d959d02071ae14768f75534adb0cf60/pages/projects/gmailapi/deployments", payload, headers)
    res = conn.getresponse()
    data = res.read()
    logger.debug("Function is accurately working")
    return data.decode("utf-8")
end = time.perf_counter()
print('project_deployment function took:', end - start, 'seconds')


# Cloudflare deployment information

start = time.perf_counter()
def deployment_info():
    conn.request("GET", "/client/v4/accounts/3d959d02071ae14768f75534adb0cf60/pages/projects/myappumer/deployments/7078f563-ae95-4ad3-9382-c5d86a518633", headers=headers)
    res = conn.getresponse()
    data = res.read()
    logger.debug("Function is accurately working")
    return data.decode("utf-8")

end = time.perf_counter()
print('deployment_info function took:', end - start, 'seconds')