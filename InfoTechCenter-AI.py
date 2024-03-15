import time
import sys
import os

def boot_up_sequence():
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    print("\n\nWelcome to InfoTech Center V1.0\n")
    time.sleep(3)

    print("InfoTech Center System Booting")
    # Define the number of steps in the boot-up process
    total_steps = 20

    # Use a progress bar instead of an ellipsis animation
    for step in range(1, total_steps + 1):
        # Calculate progress percentage
        progress = step / total_steps * 100

        # Update progress bar
        sys.stdout.write("\r[{:<20}] {:.0f}%".format('=' * step, progress))
        sys.stdout.flush()

        # Wait for a short duration
        time.sleep(0.5)

    # Print completion message
    print("\n\nOperating System Booted Up - Retina Scanned - Access Granted!")

if __name__ == "__main__":
    boot_up_sequence()


