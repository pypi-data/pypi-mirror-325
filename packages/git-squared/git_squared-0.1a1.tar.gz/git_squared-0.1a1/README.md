# git-squared (`gg`)

A CLI for stacked git workflows

The program is called `gg` and has the following commands:

```
% gg 
usage: gg [-h] command ...

positional arguments:
  command
    ls        List all branches and current status
    rm        Remove (delete) this branch or a named branch
    go        Go to a branch if it exists. Otherwise, create a new branch tracking the current branch.
    co        Alias for `go` (`co` is short for `checkout`)
    restack   Restack this branch and all children onto its tracking branch
    r         Alias for `restack`
    status    Show git status (alias for `git status`)
    add       Add files to the staging area (alias for `git add`)
    commit    Commit the staged changes (using amend, ie one commit per branch)
    c         Alias for `commit`
    down      Move down the tree from the current branch; ie, move to the parent branch
    up        Move up the tree from the current branch; ie, move to the child branch
    s         Submit this branch to the remote (`s` stands for `submit`)
    ss        Submit this branch and its children to the remote (`ss`stands for `submit stack`!)


optional arguments:
  -h, --help  show this help message and exit
```

## commands

### `gg ls` shows the stack

```
% gg ls

◯ c
◯ b
│ ◯ d
◯─┘ a
│ ◯ aaaa
│ ◯ aaa
│ ◯ aa
│ │ ◯ t1
│ │ │ ◯ t2
│ │ │ │ ◯ t3
│ │ ◯─┴─┘ test
└─┴─┴─● main

```

### `gg go` moves around the stack (or creates new branches in the stack)

```
% gg go aa

🏁 Checked out aa
...
│ ◯ d
◯─┘ a
│ ◯ aaaa
│ ◯ aaa
│ ● aa
...
└─┴─┴─◯ main


```

### `gg up`/`gg down` move up and down the stack

```
% gg up

🏁 Checked out aaa
...
│ ◯ d
◯─┘ a
│ ◯ aaaa
│ ● aaa
│ ◯ aa
...
└─┴─┴─◯ main

```
```
% gg down

🏁 Checked out aa
...
│ ◯ d
◯─┘ a
│ ◯ aaaa
│ ◯ aaa
│ ● aa
...
└─┴─┴─◯ main

```

