import os


def get_province_city_pairs(root_dir):
    pairs = []

    # Loop through all items in the root directory
    for province in os.listdir(root_dir):
        province_path = os.path.join(root_dir, province)
        if os.path.isdir(province_path):
            # Loop through all subfolders (cities) inside the province
            for city in os.listdir(province_path):
                city_path = os.path.join(province_path, city)
                if os.path.isdir(city_path):
                    pairs.append((province, city))

    return pairs
