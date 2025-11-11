thonimport json

def export_data(data, settings):
    with open(settings["output_file"], "w") as outfile:
        json.dump(data, outfile, indent=4)