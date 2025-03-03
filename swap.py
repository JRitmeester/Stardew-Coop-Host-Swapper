import xml.etree.ElementTree as ET 
from xml.dom import minidom
from pathlib import Path
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <save_file_path> <current_host_name> <new_host_name>")
        sys.exit(1)
    
    path = Path(sys.argv[1])
    from_ = sys.argv[2]
    to_ = sys.argv[3]
    
    tree = ET.parse(path.as_posix())
    root = tree.getroot()
    
    player = root.find('player')
    if player.find('name').text.lower() != from_.lower():
        raise ValueError("The supposed host's name is not the host of this save file.")
    
    farmhands = root.find('farmhands')
    
    new_host = None
    for farmer in farmhands.findall('Farmer'):
        if farmer.find('name').text.lower() == to_.lower():
            new_host = farmer
            break
    else:
        raise ValueError("The new host is not a farmhand in this save file.")
    
    # Swap contents of player and new host while keeping tag names intact
    player_content = list(player)
    new_host_content = list(new_host)
    
    player.clear()
    new_host.clear()
    
    for elem in new_host_content:
        player.append(elem)
    
    for elem in player_content:
        new_host.append(elem)
    
    # Save modified XML file with proper formatting without extra newlines
    output_path = path.with_name(f"{path.stem}_modified.xml")
    rough_string = ET.tostring(root, encoding="utf-8")
    reparsed = minidom.parseString(rough_string)
    with open(output_path.as_posix(), "w", encoding="utf-8") as f:
        f.write("\n".join([line for line in reparsed.toprettyxml(indent="  ").splitlines() if line.strip()]))
    
    print(f"Successfully swapped {from_} and {to_}. Saved as {output_path.name}.")
