''' Resizing '''
import cv2
import os

class DataPreprocessing:
    def __int__(self, data_dir):
        self.data_dir = data_dir
    def image_resize(self, ):
        for file in os.listdir(self.data_dir):
            image_path = cv2.imread(os.path.join(self.data_dir,file))
            resize_image = cv2.resize(image_path, (640, 480))
            cv2.imshow('resize_image', resize_image)
            cv2.imrite(os.path.join(self.data_dir + ".jpeg"), resize_image)
            cv2.waitKey(0)

    def image_crop(self):
        for file in os.listdir(self.data_dir):
            image_path = cv2.imread(os.path.join(self.data_dir,file))
            resize_image = cv2.resize(image_path, (640, 480))
            cropped_image = image[320:640, 420:840]
            cv2.imshow('image', cropped_image)
            cv2.imrite(os.path.join(self.data_dir + ".jpeg"), resize_image)
            cv2.waitKey(0)


    def video_crop(self,video_read_path, video_write_path, start_time, end_time):
        # video file path
        video_path = video_read_path

        # ffprobe command
        command = f'ffprobe -i {video_path} -show_entries format=duration -v quiet -of csv="p=0"'

        # run command
        output = subprocess.check_output(command, shell=True).decode('utf-8').strip()

        # float video duration
        duration = float(output)

        # input video file path
        input_file = video_read_path

        # ffmpeg command
        command = f'ffmpeg -i {input_file} -ss {start_time} -to {end_time} -c:v copy -c:a copy {video_write_path}'

        # call command using subprocess module
        subprocess.call(command, shell=True)
    def image_blurring(self, k_size):
        # k_size = 7
        for file in os.listdir(self.data_dir):
            image_path = cv2.imread(os.path.join(self.data_dir, file))
            resize_image = cv2.resize(image_path, (640, 480))

            blurr_image = cv.blur(resize_image, (k_size, k_size))
            gaussian_blurr_image = cv.GaussianBlur(resize_image, (k_size, k_size), 10)
            median_blurr_image = cv.blur(resize_image, k_size)

            cv.imshow('image', gaussian_blurr_image)
            cv2.imrite(os.path.join(self.data_dir + ".jpeg"), blurr_image)
            cv2.waitKey(0)
    def image_color_spaces(self):
        for file in os.listdir(self.data_dir):
            image_path = cv2.imread(os.path.join(self.data_dir, file))
            resize_image = cv2.resize(image_path, (640, 480))

            # bgr -> rgb
            rgb_image = cv.cvtColor(resize_image, cv.COLOR_BGR2RGB)
            gray_image = cv.cvtColor(resize_image, cv.COLOR_BGR2GRAY)
            hsv_image = cv.cvtColor(resize_image, cv.COLOR_BGR2HSV)

            cv.imshow('image', hsv_image)
            cv2.imrite(os.path.join(self.data_dir + ".jpeg"), hsv_image)
            cv2.waitKey(0)
