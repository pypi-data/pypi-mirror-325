from git import Repo as GitRepo
from .exception import GgException
from .branch import Branch

# Repo.get_branches = lambda self: [Branch.from_head(self, branch) for branch in self.branches]
# Repo.branch = lambda self, name: Branch.from_head(self, self.branches[name]) if name in self.branches else None
# Repo.has_branch = lambda self, name: name in self.branches
# Repo.main = lambda self: Branch.from_head(self, self.branches["main"])

class Repo(GitRepo):
    def get_branches(self):
        return [Branch.from_head(branch) for branch in self.branches]
    
    def branch(self, name):
        try:
            b = Branch.from_head(self.branches[name])
            return b
        except KeyError:
            return None
    
    def has_branch(self, name):
        return True if self.branch(name) else False
    
    def main(self):
        # todo: prompt for main branch
        branch = self.branch("main") or self.branch("master")
        if not branch:
            raise GgException("No main branch found")
        return branch
    
    def staged(self):
        return [item.a_path for item in self.index.diff("HEAD")]
    
    def unstaged(self):
        return [item.a_path for item in self.index.diff(None)]
    
    def untracked(self):
        return [item for item in self.untracked_files]
    
def repo(): 
    return Repo('.')