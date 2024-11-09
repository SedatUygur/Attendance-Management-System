<!-- Improved compatibility of back to top link: See: https://github.com/SedatUygur/Attendance-Management-System/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Attendance Management System</h3>

  <p align="center">
    Attendance Management System using Face Recognition!
    <br />
    <a href="https://github.com/SedatUygur/Attendance-Management-System"><strong>Explore the docs</strong></a>
    <br />
    <br />
    <a href="https://github.com/SedatUygur/Attendance-Management-System/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/SedatUygur/Attendance-Management-System/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Attendance Management System][product-screenshot]](https://example.com)

This project involves developing an attendance system which uses facial recognition to mark the attendance. It covers areas such as facial detection, alignment and recognition, along with the development of a desktop application to various use cases of the system such as registration of new attendees, taking photos and adding them to the training dataset, viewing attendance reports. This project can be used everywhere where security is essential.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][python-logo]][Python]
* [![NumPy][numpy]][numpy-url]
* [![Pandas][pandas]][pandas-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Install Python
* [Python]

### Installation

1. Download or clone my repository
   ```sh
   git clone https://github.com/SedatUygur/Attendance-Management-System.git
   ```
2. Install dlib
   ```sh
   pip install dlib
   ```
3. Install face recognition
   ```sh
   pip install face recognition
   ```
4. If you encounter problems while installing face recognition on Windows, you can follow this issue [face-recognition issue] and my comment [face-recognition issue comment] on Github.
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Find the face location and draw bounding boxes
- [x] Train images for face recognition
- [x] Preprocess and organize data for training the face recognition model
- [x] Build the face recognition model using face recognition libraries
- [x] Read webcam for real time recognition
- [x] Integrate the face recognition model with an attendance management system
- [ ] Aging - With advancing age, human face also changes.
- [ ] Illumination - Little changes in lighting conditions cause a significant impact on its recognition results
- [ ] Low Resolution - Our system must be trained on good resolution images. Nevertheless, the model will fail
- [ ] Pose - It may result in faulty or no recognition if our system is only trained on frontal faces

See the [open issues](https://github.com/SedatUygur/Attendance-Management-System/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Top contributors:

<a href="https://github.com/SedatUygur/Attendance-Management-System/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=SedatUygur/Attendance-Management-System" alt="contrib.rocks image" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Sedat Uygur - [@sedat-can-uygur](https://www.linkedin.com/in/sedat-can-uygur) - sedat.uygur@outlook.com

Project Link: [https://github.com/SedatUygur/Attendance-Management-System](https://github.com/SedatUygur/Attendance-Management-System)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
* [dlib][dlib-url]
* [opencv-python][opencv-python-url]
* [face-recognition][face-recognition-url]
* [face-recognition docs][face-recognition-docs-url]
* [face-recognition issue][face-recognition-issue-url]
* [numpy][numpy-url]
* [pandas][pandas-url]
* [tkinter][tkinter-url]
* [tkinter tutorial][tkinter-tutorial-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/SedatUygur/Attendance-Management-System.svg?style=for-the-badge
[contributors-url]: https://github.com/SedatUygur/Attendance-Management-System/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/SedatUygur/Attendance-Management-System.svg?style=for-the-badge
[forks-url]: https://github.com/SedatUygur/Attendance-Management-System/network/members
[stars-shield]: https://img.shields.io/github/stars/SedatUygur/Attendance-Management-System.svg?style=for-the-badge
[stars-url]: https://github.com/SedatUygur/Attendance-Management-System/stargazers
[issues-shield]: https://img.shields.io/github/issues/SedatUygur/Attendance-Management-System.svg?style=for-the-badge
[issues-url]: https://github.com/SedatUygur/Attendance-Management-System/issues
[license-shield]: https://img.shields.io/github/license/SedatUygur/Attendance-Management-System.svg?style=for-the-badge
[license-url]: https://github.com/SedatUygur/Attendance-Management-System/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/sedat-can-uygur
[product-screenshot]: images/screenshot.png
[dlib]: http://dlib.net/dlib-logo-small.png
[dlib-url]: https://github.com/davisking/dlib
[python-logo]: https://www.python.org/static/opengraph-icon-200x200.png
[Python]: https://www.python.org/
[opencv-python-url]: https://pypi.org/project/opencv-python/
[face-recognition]: https://pypi.org/static/images/logo-small.8998e9d1.svg
[face-recognition-url]: https://pypi.org/project/face-recognition/
[face-recognition-docs-url]: https://face-recognition.readthedocs.io/en/latest/face_recognition.html
[face-recognition issue]: https://github.com/ageitgey/face_recognition/issues/175
[face-recognition issue comment]: https://github.com/ageitgey/face_recognition/issues/175#issuecomment-2335190442
[numpy]: https://numpy.org/images/favicon.ico
[numpy-url]: https://numpy.org/
[pandas]: https://pandas.pydata.org/static/img/pandas.svg
[pandas-url]: https://pandas.pydata.org/
[tkinter]: https://docs.python.org/3/_static/py.svg
[tkinter-url]: https://docs.python.org/3/library/tkinter.html
[tkinter-tutorial-url]: https://tkdocs.com/tutorial/index.html