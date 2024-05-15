# Video Understanding Project

This project demonstrates how to use OpenAI’s GPT models alongside vision models to understand and interpret video content. The goal is to extract frames from a video, process these frames using a vision model, and generate textual insights using GPT.

## Directory Structure

video_understanding_project/
│
├── data/
│ ├── raw_videos/
│ │ └── sample_video.mp4
│ ├── frames/
│ │ └── frame_001.jpg
│ └── processed_features/
│ └── frame_001_features.pt
│
├── notebooks/
│ └── video_understanding_example.ipynb
│
├── src/
│ ├── init.py
│ ├── extract_frames.py
│ ├── process_frames.py
│ ├── gpt_integration.py
│ └── utils.py
│
├── models/
│ ├── vision_model.py
│ └── gpt_model.py
│
├── requirements.txt
├── README.md
└── .env


## Prerequisites

- Python 3.7+
- [pip](https://pip.pypa.io/en/stable/)
- OpenAI API Key

## Setup

1. **Clone the Repository:**

    ```sh
    git clone https://github.com/your_username/video_understanding_project.git
    cd video_understanding_project
    ```

2. **Create a Virtual Environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Configure Environment Variables:**

    - Create a `.env` file in the project root and add your OpenAI API key:
    
      ```env
      OPENAI_API_KEY=your_openai_api_key
      ```

## Usage

1. **Extract Frames from a Video:**

    ```sh
    python src/extract_frames.py
    ```

    - This script extracts frames from a video located in `data/raw_videos/` and saves them to `data/frames/`.

2. **Process Frames to Extract Features:**

    ```sh
    python src/process_frames.py
    ```

    - This script processes the extracted frames using a vision model and saves the features to `data/processed_features/`.

3. **Generate Descriptions Using GPT:**

    ```sh
    python src/gpt_integration.py
    ```

    - This script uses GPT to generate textual descriptions based on the processed features.

## Example Notebook

An example workflow is provided in the `notebooks/video_understanding_example.ipynb` notebook. This notebook demonstrates the entire process of loading a video, extracting frames, processing frames with a vision model, and generating descriptions with GPT.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions for improvements or find bugs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [OpenAI](https://www.openai.com/) for providing the GPT models.
- [CLIP by OpenAI](https://github.com/openai/CLIP) for the vision model.

---

By following the above instructions, you should be able to set up and run the project to understand video content using GPT and vision models. If you encounter any issues or have any questions, please feel free to ask.

MIT License

Copyright (c) 2024 [HafizalJohari]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
