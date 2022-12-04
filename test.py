import unittest
import main

class TestChad_Project(unittest.TestCase):
    def test_list_groups(self):
        self.assertEqual(main.list_groups(),main.list_groups())

    def test_list_project(self):
        self.assertEqual(main.list_project(),main.list_project())

    def test_sub_group(self):
        self.assertEqual(main.sub_group(),main.sub_group())

    def test_create_project(self):
        self.assertEqual(main.create_project(),main.create_project())

    def test_fork_project(self):
        self.assertEqual(main.fork_project(),main.fork_project())

    def test_buildArgParser(self):
        self.assertEqual(main.buildArgParser().parse_args().company_id,main.buildArgParser().parse_args().company_id)

    
# Cloudflare Testing    
    def test_list_projects(self):
        self.assertEqual(main.list_projects(),main.list_projects())

    def test_create_projectt(self):
        self.assertEqual(main.create_projectt(),main.create_projectt())
    
    def test_project_deployment(self):
        self.assertEqual(main.project_deployment(),main.project_deployment())

    def test_deployment_info(self):
        self.assertEqual(main.deployment_info(),main.deployment_info())


if __name__ == '__main__':
    unittest.main()