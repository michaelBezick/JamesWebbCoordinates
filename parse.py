import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--filename", type=str)
args = parser.parse_args()
filename = args.filename

with open(filename, "r") as file:
    outfile = open("parsed_results.txt", "w")
    line = file.readline()
    while not line == "$$SOE\n":
        line = file.readline()
    time = file.readline()
    while not time == "$$EOE\n":
        xyz = file.readline()
        vxyz = file.readline()
        lt_rg_rr = file.readline()

        #remove labels
        time_code = time[0:18].replace("\n", "").replace(" ", "")
        x = xyz[4:27].replace("\n", "").replace(" ", "")
        y = xyz[31:53].replace("\n", "").replace(" ", "")
        z = xyz[56:79].replace("\n", "").replace(" ", "")

        vx = vxyz[4:27].replace("\n", "").replace(" ", "")
        vy = vxyz[31:53].replace("\n", "").replace(" ", "")
        vz = vxyz[56:79].replace("\n", "").replace(" ", "")

        lt = lt_rg_rr[4:27].replace("\n", "").replace(" ", "")
        rg = lt_rg_rr[31:53].replace("\n", "").replace(" ", "")
        rr = lt_rg_rr[56:79].replace("\n", "").replace(" ", "")

        outfile.write(f"{time_code},{x},{y},{z},{vx},{vy},{vz},{lt},{rg},{rr}\n")

        time = file.readline()

    outfile.close()
