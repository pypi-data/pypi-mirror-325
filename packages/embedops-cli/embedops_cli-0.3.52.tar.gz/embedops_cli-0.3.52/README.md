# EmbedOps Tools

CLI tool for enabling easier and smoother local development for embedded systems via the command line. Promotes usage of Docker and best practices for modern embedded development.

## Current Features

Parse CI YAML files to allow for jobs to be run in the same containers and the same way locally as they do on CI.

## Python Packages needed

defined in requirements.txt and setup.cfg

### YAML finding and parsing

Functionality:

- Show names of all jobs
- Show detailed job context

Limitations:

- No guarantee of YAML written by anyone other than Dojo Five employees will be able to run as expected
- Can only be run from the current working directory your pipeline scripts expect to be in as there is no way to set cwd explicitly
- Only works with BitBucket and GitLab YAML files, and GitHub Actions with only one workflow file
- Will not use, search for, nor help set environment variables defined outside of YAML
- no way to mark that a job shouldn't be run locally or hide non-runnable jobs
- Will show "hidden" GitLab jobs and allow them to be run
- Does not handle `extends:` keyword in GitLab CI/CD
- Only handles multi-line script with a **complete command** in each line.
  - This is applied to both `|` (literal) and `>` (folded) YAML multiline block scalar indicator
  - For example, it doesn't work if the `if-else` statement is called in multiple lines. \
    Working example:

    ```bash
    script: |
      FILE=.clang-format
      if [ -f "$FILE" ]; then echo "$FILE exists. Use repository $FILE."; else echo "$FILE does not exist. Use container $FILE."; cp /tools/.clang-format .clang-format; fi
    ```

    Failing example:

    ```bash
    script: |
      FILE=.clang-format
      if [ -f "$FILE" ]; then
          echo "$FILE exists. Use repository $FILE."
      else
          echo "$FILE does not exist. Use container $FILE."
          cp /tools/.clang-format .clang-format
      fi
    ```

- GitHub

  Auto-detection of the GitHub CI configuration file works only if there is one file in the .github/workflows directory. When there are more than one files in that directory, use the --filename flag to specify a GitHub CI configuration.

  Syntax:

  ```bash
  embedops-cli jobs --filename <PATH_TO_CI_CONFIG_FILE> run <JOB_NAME>
  ```

Not Implemented:

- Info to pull from YAML:
  - after/before scripts?
- `include:`, `extends:` on GitLab, `uses:` on GitHub, `pipe:` on BitBucket not supported

### Docker container launching / checking /running

Functionality:

- use parsed YAML information
- map cwd to Docker container and launch (sets mounted directory as container's cwd)
- Run script in docker container found above
- Output any artifacts in the mounted directory
- Login to the EmbedOps registry for paying clients

Limitations:

- Assume all jobs have an explicit image tag or a default image tag in yaml
- Assume all jobs have a script (not handling entrypoints)
- Must be launched from the top level working directory of the project (where YAML is stored)
- doesn't clean up after itself - all artifacts are left behind, not just desired ones.
- no way to specify clean and build vs rebuild unless explicitly defined in YAML
- Env variables used but not defined in YAML must be set by user in .env file manually, no error checking
- look for .wslconfig on Windows and suggest edits or add if not found
- Attempt to start docker if it's not running?
- Execution of the docker image is not identical to CI pipeline execution leading to potential suttle differences in output behavior
- The CLI does not:
  - utilize a bootstrap image so startup behavior compared to the CI pipeline is slightly different
  - Pass script commands to the docker image via STDIN, instead a single command is executed in full with a single `docker run`. This leads to some differences in how STDIN/STDOUT behave compared to the pipeline. A TTY is not created, an interactive session is not created (ie no `-it` passed to `docker run`), and the docker session acts as if being run in a pipe.

### Reoccurring SSL Validation Issues

Some users have experienced SSL verification issues when attempting to connect to the web domains required for CLI functionaliy (Auth0 and EmbedOps Platform). This is caused by the user's host machine not having a valid Root certificate file or that file not containing the correct certificate for validating the domains. To avoid this issue, this project forces the use of the `certifi` package's Root certificate file for validating the domains previously mentioned and nothing else.

Not Implemented:

- Run before or after script
- run entire pipeline or workflow at once
- shell and any other non-Docker based runners are not supported on any system at this time

## Endpoints

Functionality:

- Log in to EmbedOps via CLI
- Auth0 connection from embedops.io to registry

Not Implemented:

- Jobs run from CLI do not talk to API

## Installation

Funtionality:

- Available on embedops.com in PyPi package registry

Limitations:

- Little to no documentation

Not Implemented:

- New version check and message

## License

Copyright 2023 Dojo Five, LLC
