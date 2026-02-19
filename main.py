from flask import Flask, render_template
import json
import random
import os
from location_pair_generator import get_province_city_pairs

from pathlib import Path

app = Flask(__name__)

@app.route("/")
def home():
    # Load the striking arts JSON
    with open("martial_arts/striking_arts.json", "r", encoding="utf-8") as f:
        striking_arts = json.load(f)
    # Pick a random striking art
    random_striking_art = random.choice(list(striking_arts.values()))

    # Load the grappling arts JSON
    with open("martial_arts/grappling_arts.json", "r", encoding="utf-8") as f:
        grappling_arts = json.load(f)
    # Pick a random grappling art
    random_grappling_art = random.choice(list(grappling_arts.values()))

    # Load the hybrid arts JSON
    with open("martial_arts/hybrid_arts.json", "r", encoding="utf-8") as f:
        hybrid_arts = json.load(f)
    # Pick a random hybrid art
    random_hybrid_art = random.choice(list(hybrid_arts.values()))

    # Load the weapon arts JSON
    with open("martial_arts/weapon_arts.json", "r", encoding="utf-8") as f:
        weapon_arts = json.load(f)
    # Pick a random hybrid art
    random_weapon_art = random.choice(list(weapon_arts.values()))

    return render_template('./home.html',
        random_striking=random_striking_art,
        random_grappling=random_grappling_art,
        random_hybrid=random_hybrid_art,
        random_weapon=random_weapon_art)

@app.route("/digital_marketing_services")
def digital_marketing_services():
    return render_template('./digital_marketing_services.html')

# MARTIAL ARTS EXPLORER START
@app.route("/martial_arts")
def martial_arts():
    # Prepare 4 random martial arts style images (striking, grappling, hybrid, weapons) to present to the user
    # Load the striking arts JSON
    with open("martial_arts/striking_arts.json", "r", encoding="utf-8") as f:
        striking_arts = json.load(f)
    # Pick a random striking art
    random_striking_art = random.choice(list(striking_arts.values()))

    # Load the grappling arts JSON
    with open("martial_arts/grappling_arts.json", "r", encoding="utf-8") as f:
        grappling_arts = json.load(f)
    # Pick a random grappling art
    random_grappling_art = random.choice(list(grappling_arts.values()))

    # Load the hybrid arts JSON
    with open("martial_arts/hybrid_arts.json", "r", encoding="utf-8") as f:
        hybrid_arts = json.load(f)
    # Pick a random hybrid art
    random_hybrid_art = random.choice(list(hybrid_arts.values()))

    # Load the weapon arts JSON
    with open("martial_arts/weapon_arts.json", "r", encoding="utf-8") as f:
        weapon_arts = json.load(f)
    # Pick a random hybrid art
    random_weapon_art = random.choice(list(weapon_arts.values()))

    # Pass the 4 random art images to the template
    return render_template(
        './martial_arts_explorer/martial_arts.html',
        random_striking=random_striking_art,
        random_grappling=random_grappling_art,
        random_hybrid=random_hybrid_art,
        random_weapon=random_weapon_art
    )

def get_martial_arts_data(data):
    # Prepares a list of JSON object that hold information on martial arts
    items = []

    for art_key, art_data in data.items():
        item = {
            "name": art_data.get("name"),
            "image": art_data.get("image"),
            "country_of_origin": art_data.get("country_of_origin"),
            "description": art_data.get("description"),
            "wikipedia_link": art_data.get("wikipedia_link"),
            "google_search_link": art_data.get("google_search_link"),
            "youtube_search_link": art_data.get("youtube_search_link"),
        }

        items.append(item)

    return items

@app.route("/martial_arts_striking")
def martial_arts_striking():
    # Access the "database" on striking martial arts
    with open("martial_arts/striking_arts.json", encoding="utf-8") as file:
        data = json.load(file)

    # Prepare a list of JSON objects holding info on the different striking martial arts
    items = get_martial_arts_data(data)

    # Send the info list to the template
    return render_template(
        "./martial_arts_explorer/martial_arts_striking.html",
        items=items
    )

@app.route("/martial_arts_grappling")
def martial_arts_grappling():
    # Access the "database" on grappling martial arts
    with open("martial_arts/grappling_arts.json", encoding="utf-8") as file:
        data = json.load(file)

    # Prepare a list of JSON objects holding info on the different grappling martial arts
    items = get_martial_arts_data(data)

    # Send the info list to the template
    return render_template('./martial_arts_explorer/martial_arts_grappling.html', items=items)

@app.route("/martial_arts_hybrids")
def martial_arts_hybrids():
    # Access the "database" on hybrid martial arts
    with open("martial_arts/hybrid_arts.json", encoding="utf-8") as file:
        data = json.load(file)

    # Prepare a list of JSON objects holding info on the different hybrid martial arts
    items = get_martial_arts_data(data)

    # Send the info list to the template
    return render_template('./martial_arts_explorer/martial_arts_hybrids.html', items=items)

@app.route("/martial_arts_weapons")
def martial_arts_weapons():
    # Access the "database" on weapon martial arts
    with open("martial_arts/weapon_arts.json", encoding="utf-8") as file:
        data = json.load(file)

    # Prepare a list of JSON objects holding info on the different weapon martial arts
    items = get_martial_arts_data(data)

    # Send the info list to the template
    return render_template('./martial_arts_explorer/martial_arts_weapons.html', items=items)

@app.route("/martial_arts_striking/<art_key>")
def martial_art_striking_details(art_key):
    # art_key = name of a specific martial art

    # Access the "database" of striking martial arts
    with open("martial_arts/striking_arts.json", encoding="utf-8") as file:
        data = json.load(file)

    # Find all information about the art using the art_key
    art = data.get(art_key)

    # Send that specific martial arts info to the details page
    return render_template(
        "martial_arts_explorer/martial_art_striking_details.html",
        art=art
    )

@app.route("/martial_arts_grappling/<art_key>")
def martial_art_grappling_details(art_key):
    with open("martial_arts/grappling_arts.json", encoding="utf-8") as file:
        data = json.load(file)

    art = data.get(art_key)

    return render_template(
        "martial_arts_explorer/martial_art_grappling_details.html",
        art=art
    )

@app.route("/martial_arts_hybrid/<art_key>")
def martial_art_hybrid_details(art_key):
    with open("martial_arts/hybrid_arts.json", encoding="utf-8") as file:
        data = json.load(file)

    art = data.get(art_key)

    return render_template(
        "martial_arts_explorer/martial_art_hybrids_details.html",
        art=art
    )

@app.route("/martial_arts_weapons/<art_key>")
def martial_art_weapons_details(art_key):
    with open("martial_arts/weapon_arts.json", encoding="utf-8") as file:
        data = json.load(file)

    art = data.get(art_key)

    return render_template(
        "martial_arts_explorer/martial_art_weapons_details.html",
        art=art
    )
# MARTIAL ARTS EXPLORER END

# MARTIAL ARTS MEDIA START
@app.route("/martial_arts_shows/<art_key>")
def martial_arts_shows(art_key):
    # Prepare the page's drop down menu
    # Directory containing the list of martial arts show jsons whose names will be used for the drop-down menu
    directory = "martial_arts_media/martial_arts_shows"

    martial_arts_names_dict = {}

    for filename in os.listdir(directory):
        if filename.endswith("_shows.json"):
            # Remove .json from value
            value = filename.replace(".json", "")

            # Build the key
            name = value.replace("_shows", "")
            name = name.replace("_", " ")
            name = name.title()

            martial_arts_names_dict[name] = value

    # Prepare the list of shows for the specific martial art
    shows = []

    with open(f"martial_arts_media/martial_arts_shows/{art_key}.json", newline="", encoding="utf-8") as file:
        shows = json.load(file)

    target_style_name = art_key.replace("_", " ").title()

    return render_template(
        "martial_arts_media/martial_arts_media_shows.html",
        target_style=target_style_name,
        martial_arts_names_dict=martial_arts_names_dict,
        shows=shows
    )

@app.route("/martial_arts_movies/<art_key>")
def martial_arts_movies(art_key):
    # Prepare the page's drop down menu
    # Directory containing the list of martial arts movie jsons whose names will be used for the drop-down menu
    directory = "martial_arts_media/martial_arts_movies"

    martial_arts_names_dict = {}

    for filename in os.listdir(directory):
        if filename.endswith("_movies.json"):
            # Remove .json from value
            value = filename.replace(".json", "")

            # Build the key
            name = value.replace("_movies", "")
            name = name.replace("_", " ")
            name = name.title()

            martial_arts_names_dict[name] = value

    # Prepare the list of movies for the specific martial art
    movies = []

    with open(f"martial_arts_media/martial_arts_movies/{art_key}.json", newline="", encoding="utf-8") as file:
        movies = json.load(file)

    target_style_name = art_key.replace("_", " ").title()

    return render_template(
        "martial_arts_media/martial_arts_media_movies.html",
        target_style=target_style_name,
        martial_arts_names_dict=martial_arts_names_dict,
        movies=movies
    )

@app.route("/martial_arts_games")
def martial_arts_games():
    # Prepare picture cards of the various video game franchise logos, each grouped into 4 tiers
    with open("martial_arts_media/martial_arts_games/game_tiers/tier_1.json", "r", encoding="utf-8") as f:
        games1 = json.load(f)

    with open("martial_arts_media/martial_arts_games/game_tiers/tier_2.json", "r", encoding="utf-8") as f:
        games2 = json.load(f)

    with open("martial_arts_media/martial_arts_games/game_tiers/tier_3.json", "r", encoding="utf-8") as f:
        games3 = json.load(f)

    with open("martial_arts_media/martial_arts_games/game_tiers/tier_4.json", "r", encoding="utf-8") as f:
        games4 = json.load(f)

    # Send the game card lists to the template
    return render_template(
        "martial_arts_media/martial_arts_media_games.html",
        games1=games1,
        games2=games2,
        games3=games3,
        games4=games4
    )

@app.route("/martial_arts_game_details/<link>")
def martial_arts_game_details(link):
    # link = the game franchise name
    # Get game series data from the appropriately named "database"
    with open(f"martial_arts_media/martial_arts_games/{link}.json", encoding="utf-8") as file:
        data = json.load(file)
    games_list = []  # To hold the info from the various video games

    # Take the JSON data and put it into the games_list
    for game_key, game_data in data.items():
        item = {
            "name": game_data.get("name"),
            "platforms": game_data.get("platforms"),
            "release_year": game_data.get("release_year"),
            "playable_characters": game_data.get("playable_characters"),
            "martial_arts_used": game_data.get("martial_arts_used"),
            "youtube_trailer": game_data.get("youtube_trailer"),
            "youtube_combat_search": game_data.get("youtube_combat_search"),
            "wikipedia_link": game_data.get("info_links", {}).get("wikipedia"),
            "igdb_link": game_data.get("info_links", {}).get("igdb"),
            "gamespot_link": game_data.get("info_links", {}).get("gamespot"),
            "google_search_link": game_data.get("info_links", {}).get("google"),
        }
        games_list.append(item)

    # Code to get game image data, the logo of the game franchise
    tier_dict = {
        "tier_1": [
            "tekken",
            "street_fighter",
            "mortal_kombat",
            "assassins_creed",
            "ghost_of_tsushima",
        ],
        "tier_2": [
            "virtua_fighter",
            "batman_arkham",
            "yakuza",
            "soulcalibur",
            "ninja_gaiden",
        ],
        "tier_3": [
            "king_of_fighters",
            "ea_sports_ufc",
            "dead_or_alive",
            "splinter_cell",
            "fight_night",
        ],
        "tier_4": [
            "onimusha",
            "dragon_ball",
            "naruto",
            "teenage_mutant_ninja_turtles",
            "kung_fu_panda",
        ]
    }
    target_tier = None
    for tier, games in tier_dict.items():
        if link in games:
            target_tier = tier
            break
    with open(f"martial_arts_media/martial_arts_games/game_tiers/{target_tier}.json", encoding="utf-8") as file:
        data = json.load(file)
    game_tier_data = data.get(link)

    return render_template(
        "martial_arts_media/martial_arts_game_details.html",
        game_tier_data=game_tier_data,
        games_list=games_list
    )
# MARTIAL ARTS MEDIA END

# MARTIAL ARTS REAL WORLD START
@app.route("/martial_arts_real_world_character_development/<art_key>")
def martial_arts_real_world_character_development(art_key):
    # Prepare the page's drop down menu
    # Directory containing the list of martial arts character development story jsons whose names will be used for the
    # drop-down menu
    directory = "martial_arts_real_world/character_development"

    martial_arts_names_dict = {}

    for filename in os.listdir(directory):
        if filename.endswith("_character_development.json"):
            # Remove .json from value
            value = filename.replace(".json", "")

            # Build the key
            name = value.replace("_character_development", "")
            name = name.replace("_", " ")
            name = name.title()

            martial_arts_names_dict[name] = value

    # Prepare the list of stories
    stories = []

    with open(f"martial_arts_real_world/character_development/{art_key}.json", newline="", encoding="utf-8") as file:
        stories = json.load(file)

    target_style_name = art_key.replace("_", " ").title()

    return render_template(
        "martial_arts_real_world/martial_arts_real_world_character_development.html",
        target_style=target_style_name,
        martial_arts_names_dict=martial_arts_names_dict,
        stories=stories
    )

@app.route("/martial_arts_real_world_documentaries/<art_key>")
def martial_arts_real_world_documentaries(art_key):
    # Prepare the page's drop down menu
    # Directory containing the list of martial arts character development story jsons whose names will be used for the
    # drop-down menu
    directory = "martial_arts_real_world/documentaries"

    martial_arts_names_dict = {}

    for filename in os.listdir(directory):
        if filename.endswith("_documentaries.json"):
            # Remove .json from value
            value = filename.replace(".json", "")

            # Build the key
            name = value.replace("_documentaries", "")
            name = name.replace("_", " ")
            name = name.title()

            martial_arts_names_dict[name] = value

    # Prepare the list of documentaries
    stories = []

    with open(f"martial_arts_real_world/documentaries/{art_key}.json", newline="", encoding="utf-8") as file:
        stories = json.load(file)

    target_style_name = art_key.replace("_", " ").title()

    return render_template(
        "martial_arts_real_world/martial_arts_real_world_documentaries.html",
        target_style=target_style_name,
        martial_arts_names_dict=martial_arts_names_dict,
        stories=stories
    )

@app.route("/martial_arts_real_world_self_defense/<art_key>")
def martial_arts_real_world_self_defense(art_key):
    # Prepare the page's drop down menu
    # Directory containing the list of martial arts self-defense story jsons whose names will be used for the drop-down menu
    directory = "martial_arts_real_world/self-defense"

    martial_arts_names_dict = {}

    for filename in os.listdir(directory):
        if filename.endswith("_self_defense.json"):
            # Remove .json from value
            value = filename.replace(".json", "")

            # Build the key
            name = value.replace("_self_defense", "")
            name = name.replace("_", " ")
            name = name.title()

            martial_arts_names_dict[name] = value

    # Prepare the list of stories
    stories = []

    with open(f"martial_arts_real_world/self-defense/{art_key}.json", newline="", encoding="utf-8") as file:
        stories = json.load(file)

    target_style_name = art_key.replace("_", " ").title()

    return render_template(
        "martial_arts_real_world/martial_arts_real_world_self_defense.html",
        target_style=target_style_name,
        martial_arts_names_dict=martial_arts_names_dict,
        stories=stories
    )
# MARTIAL ARTS REAL WORLD END

@app.route("/martial_arts_schools/<province>/<city>/")
def martial_arts_schools(province, city):
    # Directories
    base_path = Path("martial_arts_schools/canada") / province / city
    SCHOOLS_DIR = base_path / "schools"
    INDEXES_DIR = base_path / "indexes"

    current_location = f"{city.title()}, {province.title()}"

    style_schools = []  # Holds info about martial arts schools for various styles

    # Load all index files and sort alphabetically
    # Ensures martial arts headers appear alphabetically (Aikido → Taekwondo → etc.)
    style_files = sorted(INDEXES_DIR.glob("*.json"), key=lambda x: x.stem.lower())

    # Access the data in all the index files, the martial art and the schools tied to that martial art
    for style_file in style_files:
        with open(style_file) as f:
            index_data = json.load(f)

        # Load full school info for each ID in the index, for each art and connected schools, add more school info
        schools = []
        for school_id in index_data.get("school_ids", []):
            school_file = SCHOOLS_DIR / f"{school_id}.json"
            if school_file.exists():
                with open(school_file) as sf:
                    school_data = json.load(sf)
                    schools.append(school_data)

        # Add this style and its schools to the list
        style_schools.append({
            "style": index_data.get("style", style_file.stem),
            "schools": schools
        })

    # The province & city location list
    root_directory = "martial_arts_schools/canada"
    province_city_pairs = get_province_city_pairs(root_directory)

    # Render template with all styles and schools
    return render_template("martial_arts_schools.html", current_location=current_location, style_schools=style_schools, province_city_pairs=province_city_pairs)

if __name__ == "__main__":
    app.run(debug=True)