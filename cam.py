import cv2


def main():
    capture = cv2.VideoCapture(0)  # Capture video from camera

    print(capture.isOpened())
    print(capture.read())

    # width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    # height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    while capture.isOpened():
        retval, frame = capture.read()
        if not retval:
            break

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) > 0:
            break

    capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
