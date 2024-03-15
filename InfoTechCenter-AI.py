import time
import sys
import os

def boot_up_sequence():
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Print welcome message
    print("\n\nWelcome to InfoTech Center V1.0\n")

    # Wait for a few seconds
    time.sleep(3)

    # Print booting message
    print("InfoTech Center System Booting")

    # Define the number of steps in the boot-up process
    total_steps = 50

    # Use a progress bar instead of an ellipsis animation
    for step in range(1, total_steps + 1):
        # Calculate progress percentage
        progress = step / total_steps * 100

        # Update progress bar
        sys.stdout.write("\r[{:<50}] {:.0f}%".format('=' * (step * 2), progress))
        sys.stdout.flush()

        # Wait for a short duration
        time.sleep(0.1)

    # Print completion message
    print("\n\nOperating System Booted Up - Retina Scanned - Access Granted!")

if __name__ == "__main__":
    boot_up_sequence()



