If you are new to computer vision just like me and want to explore working on image frames and robotics, Follow the code as a start to computer vision.

The first step is to understand how exactly an image works and what exactly does an image hold.

One of the formats images are stored other than the majorly used format - RGB is HSV -- Hue Saturation Value

Structure followed:

- We are creating a window to display images and TRACKBAR - to set the lower and upper limit of Hue Saturation and Value; 

    We set Hue between 0 - 180 as if we use 360 of the color disk of HSV it will need 360 bits to store the image, So we half it and use it to store it in 8 bits i.e. 1 byte - Considering the storage complexities.

    We set Saturation and Value between 0 and 255

- Reading the image consistently from the camera feed of the system.

- Making sure the loop runs continuously for video feed

Executing the code gives you a window where you have lower and upper values of HSV

Change the Lower values and you can see how you can mask and select a particular shade of color in real time

(Please comment in the repository if you need more information)

In this SS - The "Value" of HSV is limited within a range
![Value=gray](https://github.com/SivarajuRanga1002/cv2_HSV-Variations-LiveFeed/assets/65248651/1b7ee099-875f-4552-9e64-844494fde9ff)

The saturation and Value are limited within a random range
![Saturation Adjusted](https://github.com/SivarajuRanga1002/cv2_HSV-Variations-LiveFeed/assets/65248651/ae3d10f0-8093-46b4-8b37-c137efe072b9)

The HSV is limited within a random range
![HSV_Trackbar](https://github.com/SivarajuRanga1002/cv2_HSV-Variations-LiveFeed/assets/65248651/a13ca576-900e-474f-93d1-df95a10ed85c)

---------------------------------- Explore and Test as much as possible --------------------------------------
