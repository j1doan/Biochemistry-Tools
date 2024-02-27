"""
This antibody dilution calculator is to be used for [Western Blots](https://en.wikipedia.org/wiki/Western_blot).
You can calculate any dilution from any stock concentration of antibodies.
Please buy good antibodies; the experiments beg of you.

To use this calculator:
1. Install the latest version of Python3.
2. Navigate to this file's location.
2. Launch Python3's interactive mode in a shell with the command `python -i antibodies.py`.
4. You will now see >>> which means you are in interactive more. Type `import antibodies` (.py extension not needed)
5. Type antibodies.calculate_primaries() or antibodies.calculate_secondaries() depending on your needs.
"""

def calculate_primaries():
    # Preparing the standardized 1 µg/mL working stock
    print("Preparing the standardized 1 µg/mL working stock")
    Cs = float(input("Enter the starting antibody stock concentration (µg/µL): "))
    Vf = float(input("Select desired final volume for antibody incubation (mL): "))
    Vs = (1 * Vf) / Cs
    print(f"You need {Vs} mL of the starting antibody stock to prepare {Vf} mL of a 1 µg/mL working stock solution.\n")

    # Preparing the final antibody dilution
    print("Preparing the final antibody dilution")
    dilution_factor = int(input("Select desired final antibody dilution (e.g., for 1:250, enter 250): "))
    final_volume = float(input("Select desired final volume for antibody incubation (mL): "))
    volume_antibody_needed = final_volume / dilution_factor * 1000
    volume_buffer_needed = final_volume * 1000 - volume_antibody_needed
    final_concentration = 1 / dilution_factor
    print(f"You need {volume_antibody_needed} µL of the 1 µg/mL working stock solution and {volume_buffer_needed} µL of buffer to make {final_volume} mL of the final antibody incubation solution.")
    print(f"The final concentration is {final_concentration} µg/mL or {final_concentration * 1000} ng/mL.")

def calculate_secondaries():
    # Step 1: Preparing 1 µg/mL antibody working stock solution
    print("Step 1: Preparing 1 µg/mL antibody working stock solution")
    antibody_starting_concentration = float(input("Enter the antibody starting stock concentration (µg/µL): "))
    volume_needed = 1 / antibody_starting_concentration * 1000
    print(f"You need {volume_needed} µL of the antibody and {1000 - volume_needed} µL of buffer to make 1 mL of a 1 µg/mL working stock solution.\n")

    # Step 2: Preparing the final antibody dilution
    print("Step 2: Preparing the final antibody dilution")
    final_volume = float(input("Enter the desired final volume for antibody incubation (mL): "))
    dilution_factor = int(input("Enter the final antibody dilution factor (e.g., for 1:1000, enter 1000): "))
    volume_antibody_needed = final_volume / dilution_factor * 1000000
    volume_buffer_needed = final_volume * 1000 - volume_antibody_needed
    final_concentration = 1 / dilution_factor * 1000
    print(f"You need {volume_antibody_needed} µL of the 1 µg/mL working stock solution and {volume_buffer_needed} µL of buffer to make {final_volume} mL of the final antibody incubation solution.")
    print(f"The final concentration is {final_concentration} µg/mL or {final_concentration * 1000} ng/mL.")