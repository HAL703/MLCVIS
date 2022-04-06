# Requirements
~~1. Shall develop a machine learning model~~ developed a machine learning model containing 3 different algorithms (technically 4)
~~2. Shall be able to implement effective image segmentation~~ effective is subjective, all 3 algorithms have their purposes
~~3. Shall be able to distinguish a single or multiple objects in given images~~ this is true now
~~4. Assuming the ML model produces new images, shall upload images to database~~ uploads images to imagekit either via a plugin or by a button
~~5. Shall discriminate pixel by pixel or by superpixels~~ MLM discriminates by pixel
~~6. Shall be able to strip non-essential objects (i.e. background)~~ this is true for some of the algorithms
7. Assuming there is time to create it, there shall be relatively simple interactibility/UI for website
~~8. Shall be usable on Windows~~ true, just need python currently
~~9. Shall have PNG/JPG conversion to SVG when ML model produces images~~ This could be produced very easily with one command or even maybe via imagekit but there is no point for this requirement for this project
~~10. Shall be synced with Git, commits often~~ have been doing, not as much as I'd like to have done but I'm getting used to it
~~11. Shall/Will be accessible on Android~~ Not easy to test since I don't have an actual server/browser to test, but image uploads can be seen on imagekit from an Android device
~~12. Will have an algorithm running at less than O(n^2)~~ Decided to try this for this project, but it wouldn't have worked as K-means is far more than n^2 (from research), and the other two are too difficult to tell
~~13. Will have image blurring~~ Can specify image blurring with imagekit
~~14. Will be able to watermark images optionally (potentially custom watermarks)~~Can watermark images optionally with imagekit
~~15. Will have website integration with image database~~ true, imagekit
~~16. Will have before/after image comparison~~ can do this manually, otherwise there is no point
~~17. Will be able to divide objects based on color or other properties~~ there is a color detection algorithm
~~18. Will have more than one algorithm for image segmentation~~ 3 main algorithms with 1 extra necessary for bit masking
~~19. Will be usable on IOS, Linux, OSX~~ pointless requirement, but can most likely access imagekit on all of these to see the file uploads
