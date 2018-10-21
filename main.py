import argparse
import os
import json
from shutil import rmtree
from analyze import detect_faces, get_average_hsv
from scraper import scrape

# Only works if value is between 0-1
def normalize(cap, value):
    return value * cap

# Faces is an array of face count
def results(image_count, faces, h, s, v, username):
    overall_score = 0.0
    json_file = "temp/" + username + ".json"
    FACE_SCORES = {
        0: 5,
        1: 20,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    h /= image_count
    overall_score += normalize(10, h / 180)
    s /= image_count
    overall_score += normalize(10, 1 / (1 + s))
    v /= image_count
    overall_score += normalize(10, 1 / (1 + v))

    face_value = 0
    for face_count in faces:
        # Get key, 0 is set as default
        face_value = FACE_SCORES.get(face_count, 0)
    overall_score += face_value
    
    ratio_total = 0
    with open(json_file) as f:
        posts = json.load(f)
    for post in posts:
        ratio_total += min(post['edge_media_to_comment']['count'] / post['edge_media_preview_like']['count'], 1)
    avg_ratio = ratio_total / image_count
    overall_score += normalize(20, avg_ratio)

    overall_score = (overall_score / 7) * 10
    print("{} likelyhood of depression is {}%.".format(username, overall_score))
    return overall_score
        

def main(input_folder, args, username):
    # Append '/' to folder location if not present
    input_folder += '' if '/' in input_folder else '/'
    # Filter images for jpg files only
    images = [img for img in os.listdir(input_folder) if img.endswith('.jpg')]

    # Init variables
    total_h = total_s = total_v = 0.0
    face_array = []
    image_count = 0

    for input_image in images:
        image_count += 1
        with open(input_folder + input_image, 'rb') as image:
            faces = detect_faces(image)
            face_array.append(len(faces))

            h, s, v = get_average_hsv(input_folder + input_image)
            total_h += h
            total_s += s
            total_v += v

            if args.verbose:
                print('{}: Found {} face{}\n'.format(input_image, len(faces), '' if len(faces) == 1 else 's'))
                print("Average hue: {}\nAverage saturation: {}\nAverage value: {}".format(h, s, v))          

            # Reset the file pointer, so we can read the file again
            image.seek(0)

    results(image_count, face_array, total_h, total_s, total_v, username)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Analyses an IG feed for signs and of depression')
    parser.add_argument('-d', '--debug', help="flag to keep temp files upon completion", action="store_true", default=False)
    parser.add_argument('-v', '--verbose', help="enable verbose output", action="store_true", default=False)
    args = parser.parse_args()

    folder = 'temp/'
    username = input("Enter an Instagram username: ")
    scrape(username)
    main(folder, args, username)
    try:
        if not args.debug: rmtree(folder)
    except OSError as e:
        print ("Error: %s - %s." % (e.filename, e.strerror))
