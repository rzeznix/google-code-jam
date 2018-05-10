import subprocess
import sys, os
import fnmatch


def main(argv):
    if len(argv) > 1:
        script_name = argv[1]
        root = os.path.dirname(os.path.abspath(__file__))
        matches = []
        for path, dirs, files in os.walk(os.path.abspath(root)):
            for filename in fnmatch.filter(files, script_name + ".py"):
                matches.append(os.path.join(path, filename))

        if len(matches) == 1:
            script_to_run = matches[0]
            in_file_path = script_to_run.replace(".py", ".in")

            if os.path.exists(in_file_path):
                with open(in_file_path, 'r') as in_file:
                    p = subprocess.Popen("python " + script_to_run, stdin=in_file, stdout=sys.stdout)
                p.wait()

            else:
                print("No input file found - provide input from console")
                p = subprocess.Popen("python " + script_to_run, stdin=sys.stdin, stdout=sys.stdout)
                p.wait()

        elif len(matches) == 0:
            print("No script found with name:", script_name)

        else:
            print("More than one script found with name:", script_name)
            for script_file_path in matches:
                print(script_file_path)
    else:
        print("Provide name of script to run")

if __name__ == "__main__":
    main(sys.argv)
