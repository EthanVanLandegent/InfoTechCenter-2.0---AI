import time, sys, os

def boot_up_sequence():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\nWelcome to InfoTech Center V1.0\n")
    time.sleep(3)

    total_steps = 50

    for step in range(1, total_steps + 1):
        sys.stdout.write(f"\r{'=' * step} {step *2}%")
        sys.stdout.flush()
        time.sleep(0.1)

    print("\n\nOperating System Booted Up - Retina Scanned - Access Granted!")

if __name__ == "__main__":
    boot_up_sequence()



