import os
import cv2

DATA_PATH = "Data"
DATASET_PATH = DATA_PATH + "/SelectedData/"
TESTDATA_PATH = DATA_PATH + "/Altered/SelectedData/"


def matchfingerprint(inputfilename):
    sample = cv2.imread(TESTDATA_PATH + inputfilename)
    best_score = counter = 0
    filename = image = kp1 = kp2 = mp = None
    print("Starting...")
    # print(DATASET_PATH)
    for file in os.listdir(DATASET_PATH):
        counter += 1

        fingerprint_img = cv2.imread(DATASET_PATH + file)
        sift = cv2.SIFT_create()
        keypoints_1, des1 = sift.detectAndCompute(sample, None)
        keypoints_2, des2 = sift.detectAndCompute(fingerprint_img, None)
        # fast library for approx best match KNN
        matches = cv2.FlannBasedMatcher({"algorithm": 1, "trees": 10}, {}).knnMatch(des1, des2, k=2)

        match_points = []
        for p, q in matches:
            if p.distance < 0.1 * q.distance:
                match_points.append(p)

        keypoints = 0
        if len(keypoints_1) <= len(keypoints_2):
            keypoints = len(keypoints_1)
        else:
            keypoints = len(keypoints_2)
        if len(match_points) / keypoints * 100 > best_score:
            best_score = len(match_points) / keypoints * 100
            filename = file
            image = fingerprint_img
            kp1, kp2, mp = keypoints_1, keypoints_2, match_points

    print("Best match:  " + filename)
    print("Best score:  " + str(best_score))
    result = cv2.drawMatches(sample, kp1, image, kp2, mp, None)
    result = cv2.resize(result, None, fx=2.5, fy=2.5)

    # Save the result image
    cv2.imwrite("result.jpg", result)

    # Show the result on screen with Naming 2 images
    cv2.imshow("Fingerprint Matching", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


matchfingerprint("2__F_Right_index_finger_CR.BMP")
