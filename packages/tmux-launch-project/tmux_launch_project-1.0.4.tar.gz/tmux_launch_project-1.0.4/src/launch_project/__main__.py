import os
import sys


def run_command(*commands: str) -> None:
    command = " && ".join(commands)
    os.system(command)


def main() -> None:
    projects = sys.argv[1::]

    if len(projects) == 0:
        print("Please provide the projects you want to launch")
        quit()

    for project in projects:
        print(f"Launching prject {project}")
        run_command(
            f"cd {project}",
            f"tmux new-session -d -s {project}",
            f"tmux send-keys -t {project} 'vim .' C-m",
        )


if __name__ == "__main__":
    main()

