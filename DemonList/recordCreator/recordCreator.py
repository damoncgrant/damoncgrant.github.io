"""
- This takes in level statistics and outputs as a JSON to be added to the list.
- Can either manually enter level details or input as a spreadsheet. 
- Also will download the thumbnails from the youtube video to be used (disabled with the --noThumbnail)
- The spreadsheet must follow the format of the example one

Run to run this program use:
python3 recordCreator.py "whatever you called your spreadsheet"
"""
import argparse
import json
from pythumb import Thumbnail

parser = argparse.ArgumentParser(description="Processes CSV file and outputs as JSON")
parser.add_argument("input", nargs="?", default=None, help="Path to input file")
parser.add_argument("--noThumbnail", action="store_true", help="If this flag is set will not download thumbnails.")

args = parser.parse_args()

if args.input:      # Working with a CSV
    with open(args.input, "r") as file:
        records = file.readlines()[1:]
    
    totalOutput = {
        "levels": []
    }

    for record in records:
        output = {}
        recordSplit = record.split(",")
        output["name"] = recordSplit[0]
        output["creator"] = recordSplit[1]
        output["completionDate"] = recordSplit[2]
        output["attempts"] = recordSplit[3]
        output["enjoyment"] = recordSplit[4]
        output["worstFail"] = recordSplit[5]
        output["videoLink"] = recordSplit[6].strip()

        totalOutput["levels"].append(output)

        if not args.noThumbnail:
            print(f'Generating: "{output["name"]}" thumbnail')
            t = Thumbnail(output["videoLink"])
            t.fetch()
            t.save(dir='../images/thumbnails/', filename=output["name"], overwrite=True)
    
    with open("recordSubmitOut.json", "w") as file:
        json.dump(totalOutput, file, indent=4)
        print("\nOutputting JSON, paste this into \"levels.json\"")

else:               # Manual inputs
    output = {}
    # Gathering details
    output["name"] = input("Enter the level name:\n")
    output["creator"] = input("Enter the level creator/publisher:\n")
    output["completionDate"] = input("Enter the date of completion (DD-MM-YYYY):\n")
    output["attempts"] = input("Enter the attempt count:\n")
    output["enjoyment"] = input("Enter enjoyment:\n")
    output["worstFail"] = input("Enter the worst fail (do not put a %):\n")
    output["videoLink"] = input("Enter a link to the completion:\n")

    with open("recordSubmitOut.json", "w") as file:
        json.dump(output, file, indent=4)
        print("\nOutputting JSON, add this to the desired placement in \"levels.json\"")


