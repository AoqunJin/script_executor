import argparse
from .executor import ScriptExecutor

def main():
    parser = argparse.ArgumentParser(description="Script Execution Manager")
    parser.add_argument('--mode', choices=['sequential', 'immediate'], default='sequential', help="Execution mode")
    parser.add_argument('--on_fail', choices=['continue', 'stop'], default='continue', help="Behavior on failure")
    parser.add_argument('command', nargs=argparse.REMAINDER, help="Command to execute with optional arguments")
    args = parser.parse_args()

    if not args.command:
        print("Error: No command provided.")
        return

    command_str = ' '.join(args.command)
    executor = ScriptExecutor()
    executor.submit_command(command_str, mode=args.mode, on_fail=args.on_fail)

if __name__ == '__main__':
    main()
