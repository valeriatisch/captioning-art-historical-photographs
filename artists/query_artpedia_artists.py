import argparse
import json
import logging
import time

import mkwikidata


def query_painter(painting_title: str) -> list:
    """
    Load artists from wikidata database for a painting title
    (https://www.wikidata.org/wiki/Wikidata:Main_Page)
    """
    query = f"""
    SELECT ?lemma ?painting ?paintingLabel ?title ?altTitle ?artist ?artistLabel ?altName ?artLabel WHERE {{
    VALUES ?lemma {{
      "{painting_title}"@en
    }}
    ?sitelink schema:about ?painting;
      schema:isPartOf <https://en.wikipedia.org/>;
      schema:name ?lemma.
    ?painting wdt:P170 ?artist.
    OPTIONAL {{
      ?painting wdt:P1476 ?title.
    }}
    OPTIONAL {{
      ?artist skos:altLabel ?altName . FILTER (lang(?altName) = "en").
    }}
    OPTIONAL {{
      ?painting skos:altLabel ?altTitle . FILTER (lang(?altTitle) = "en").
    }}
    SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en". }}
    }}
    """

    query_result = mkwikidata.run_query(query, params={})
    # Convert response
    data = [entry["artistLabel"]["value"]
            for entry in query_result["results"]["bindings"]]

    # return distinct artists
    return list(set(data))


def map_painters(artpedia_dict: dict) -> dict:
    """
    Load for each sample artist
    Update sample with resulting sample list
    """
    artpedia_with_artists = {}
    wait_time = 5
    for key, entry in list(artpedia_dict.items()):
        artists = []
        try:
            entry['artist'] = query_painter(entry['title'])
        except Exception as exc:
            logging.error(exc)

        artpedia_with_artists[key] = entry
        # Wait a bit to not cause issues with the API rate limits
        time.sleep(wait_time)
    return artpedia_with_artists


if __name__ == "__main__":
    """
    Load artpedia annotations: 
    - each sample consists of the entries: title, year, visual and contextual sentences
    Add for each sample artists an entry for the artists
    Write resulting annotations to output file (path is passed as argument --output)
    """
    parser = argparse.ArgumentParser(description="Add artist to each image of the Artpedia dataset")
    parser.add_argument("--input", type=str, required=True,
                        help="Input file path to Artpedia annotations without artists")
    parser.add_argument("--output", type=str, required=True,
                        help="Output file path to write resulting annotations to")
    args = parser.parse_args()

    with open(args.input) as file:
        artpedia = json.load(file)

    new_artpedia = map_painters(artpedia_dict=artpedia)

    if not args.output.endswith(".json"):
        args.output += ".json"

    with open(args.output, 'w') as f:
        json.dump(new_artpedia, f, indent=4)
