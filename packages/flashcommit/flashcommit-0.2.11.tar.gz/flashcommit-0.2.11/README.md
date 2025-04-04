# Flash Commit

Make it great.
Test the demand with this before making the plugin.

This has changed the way I am developing software.
At least for me this tool is revolutionary.

## How to build

Build a python package
```poetry build```

## Problems

## TODO

- ensure backup is working
- add .flashcommit.rc with linter, additional coding rules
- add shell_command callback support

make full flash mode:

1. apply diff
2. ask 'is it good'
3. if yes commit while let user edit the commit message.
4. if no cancel or try again

## Feature Ideas

- internal loop to break down the problem into 'shallow problems'
- builtin api key management like --generate-key or better spin up dialog if starting without a key
- get rid of the prompting. Who is the prompter? Better not me -> pull the jira issue and iterate until its clear
- make it review an github PR and push selected comments to gh
- save all answers like ignore perm
- make the user control the config via remote settings (which config?)

## Developer Documentation

- install git hooks

## Enduser Documentation

- use `git rebase --onto HEAD~1 HEAD` if in full flash mode to drop the latest change
