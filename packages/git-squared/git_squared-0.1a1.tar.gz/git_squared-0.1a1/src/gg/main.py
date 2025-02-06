#!/usr/bin/env python3
import arguably
from .log import log, pad
from .branch import Branch
from .repo import repo
from .exception import GgException
from .ls import draw_tree_2
from .tree import traverse
from .confirm import confirm
from .restack import restack as _restack
import git
import subprocess
import questionary

@arguably.command
def ls():
    """
    List all branches and current status
    """
    with pad():
        r = repo()
        draw_tree_2(r, _print=True)
        if len(r.staged() + r.unstaged() + r.untracked()):
            log("")
            if len(r.staged()):
                for f in r.staged():
                    log(f"• {f}", _type="success")
            if len(r.unstaged()):
                for f in r.unstaged():
                    log(f"◦ {f}")
            if len(r.untracked()):
                for f in r.untracked():
                    log(f"◦ {f}", _type="dim")
    
# TEST - a
@arguably.command
def rm(name: str = None, *, y: bool = False):
    """
    Remove (delete) this branch or a named branch

    Args:
        name: the name of the branch to remove
        y: whether to skip confirmation
    """
    r = repo()
    current_branch = name if name else r.active_branch.name
    with confirm(f"Are you sure you want to delete {current_branch}?", _skip=y) as answer:
        if answer == "y":
            # cant delete the branch we are on
            if current_branch == r.active_branch.name:
                Branch.active().parent().checkout(_log=False)
            
            with pad():
                Branch(current_branch).delete()
    
    
@arguably.command
def go(name):
    """
    Go to a branch if it exists. Otherwise, create a new branch tracking the current branch.

    Args:
        name: the name of the branch to go to
    """
    with pad():
        Branch(name).checkout(_create=True, _log=True)
        r = repo()
        draw_tree_2(r, _print=True, _highlight=r.active_branch)

@arguably.command
def co(name):
    """
    Alias for `go` (`co` is short for `checkout`)

    Args:
        name: the name of the branch to go to
    """
    go(name)

@arguably.command
def restack():
    """
    Restack this branch and all children onto its tracking branch
    """
    with pad():
        traverse(Branch.from_head(repo().active_branch), _restack)

@arguably.command
def r():
    """
    Alias for `restack`
    """
    restack()

@arguably.command
def status():
    """
    Show git status (alias for `git status`)
    """
    subprocess.run(["git", "status"])

@arguably.command
def add(*opts):
    """
    Add files to the staging area (alias for `git add`)

    Args:
        opts: the options to pass to `git add`
    """
    subprocess.run(["git", "add", *opts])

@arguably.command()
def commit():
    """
    Commit the staged changes (using amend, ie one commit per branch)
    """
    with pad():
        Branch.active().commit()

    restack()

@arguably.command()
def c():
    """
    Alias for `commit`
    """
    commit()

@arguably.command()
def down():
    """
    Move down the tree from the current branch; ie, move to the parent branch
    """
    go(Branch.active().parent().name)

@arguably.command()
def up():
    """
    Move up the tree from the current branch; ie, move to the child branch
    """
    children = Branch.active().children()
    if len(children) == 0:
        log("Cannot go up! No child branches found")
        return
    elif len(children) == 1:
        go(children[0].name)
    else:
        choice = questionary.select(
            "Select a branch:",
            choices=[x.name for x in children]
        ).ask()
        go(choice)

@arguably.command()
def s():
    """
    Submit this branch to the remote (`s` stands for `submit`)
    """
    with pad():
        subprocess.run(["git", "push", "-f", "origin", "HEAD"])

@arguably.command()
def ss():
    """
    Submit this branch and its children to the remote (`ss`stands for `submit stack`)
    """
    with pad():
        traverse(Branch.from_head(repo().active_branch), lambda a: s())

@arguably.command()
def reset():
    """
    Reset working tree to the state of the last commit
    """
    with pad():
        subprocess.run(["git", "reset", "--hard", "HEAD"])

@arguably.command()
def cs():
    """
    Commit all changes and submit
    """
    add("--all")
    commit()
    ss()

def main():
    try:
        arguably.run()
    except GgException as e:
        log(str(e), _type="error")
    except git.exc.GitCommandError as e:
        log(str(e), _type="error")

if __name__ == "__main__":
    main()
