🏛️ HeritageLens AI
A comprehensive Streamlit web application for detecting and analyzing heritage sites, archaeological structures, and cultural landmarks using advanced YOLOv11 deep learning technology.

🌟 Features
📸 Image Detection
Upload single or multiple images
Real-time object detection with bounding boxes
Confidence scores for each detection
Cropped detection thumbnails
Interactive results display
🎥 Video Analysis
Local video file upload support
YouTube video link analysis
Real-time frame-by-frame detection
Start/stop detection controls
Comprehensive video summaries
📊 Interactive Dashboard
Detailed detection statistics
Interactive charts and visualizations
Class-wise analysis
Confidence score distributions
Combined image and video insights
📚 Educational Content
Comprehensive information about heritage classes
Cultural significance explanations
Preservation guidelines
Best practices for heritage documentation
📄 PDF Reports
Automated report generation
Detailed statistics and summaries
Professional formatting
Downloadable analysis reports
🏺 Heritage Classes Detected
Stones / Stone Pillars / Stone Structures 🗿

Ancient stone constructions and architectural elements
Megaliths, temple pillars, stone walls
Crops / Farmland 🌾

Agricultural landscapes and farming areas
Traditional farming methods and irrigation systems
Non-archaeological 🏔️

Natural landscapes (deserts, water, mountains)
Geographical features and natural formations
Heritage Sites 🏛️

Temples, palaces, forts, museums
Major cultural and historical monuments
🚀 Installation
Prerequisites
Python 3.8 or higher
CUDA-compatible GPU (recommended for better performance)
Setup Instructions
Clone or navigate to the project directory:

cd /home/surendra208/Documents/jaya/aimoodmate/ai_app
Install dependencies:

pip install -r requirements.txt
Verify model file: Ensure the YOLOv11 model weights are present at:

/home/surendra208/Documents/jaya/aimoodmate/ai_app/best.pt
🎯 Usage
Starting the Application
Run the Streamlit app:

streamlit run app.py
Open your browser: Navigate to http://localhost:8501

Using the Application
📸 Image Detection
Navigate to "Image Detection" page
Upload one or more image files
Click "Analyze Images"
View results with bounding boxes and statistics
Download PDF report if needed
🎥 Video Detection
Go to "Video Detection" page
Choose "Upload Local Video" or "YouTube Link"
Provide video file or YouTube URL
Click "Start Detection" to begin analysis
Click "Stop Detection" to view results
Generate comprehensive video analysis report
📊 Summary Dashboard
Visit "Summary Dashboard" after running detections
View combined statistics from images and videos
Explore interactive charts and visualizations
Download comprehensive analysis reports
📚 Learn About Heritage
Access "Learn About Heritage" page
Explore detailed information about each class
Understand cultural significance and preservation tips
Learn about AI in heritage preservation
🔧 Technical Details
Architecture
Frontend: Streamlit with custom CSS styling
AI Model: YOLOv11 (You Only Look Once version 11)
Framework: PyTorch with Ultralytics
Image Processing: OpenCV and PIL
Visualization: Plotly and Matplotlib
PDF Generation: ReportLab
Model Information
Model Type: YOLOv11 Object Detection
Classes: 4 heritage categories
Input: Images and video frames
Output: Bounding boxes, class labels, confidence scores
Performance
Real-time Processing: Optimized for live video analysis
Batch Processing: Efficient handling of multiple images
Memory Management: Optimized for large video files
GPU Acceleration: CUDA support for faster processing
🎨 Design Features
UI/UX
Modern Design: Clean, professional interface
Warm Color Palette: Earthy tones (sandstone, bronze, olive green)
Responsive Layout: Works on different screen sizes
Intuitive Navigation: Easy-to-use sidebar menu
Interactive Elements: Hover effects and smooth transitions
Accessibility
Clear Typography: Readable fonts and appropriate sizing
Color Contrast: High contrast for better visibility
Keyboard Navigation: Full keyboard accessibility
Screen Reader Support: Semantic HTML structure
📋 Requirements
System Requirements
RAM: 8GB minimum, 16GB recommended
Storage: 2GB free space
GPU: NVIDIA GPU with CUDA support (optional but recommended)
Internet: Required for YouTube video processing
Python Dependencies
streamlit==1.28.1
ultralytics==8.0.196
opencv-python==4.8.1.78
pillow==10.0.1
numpy==1.24.3
pandas==2.0.3
plotly==5.17.0
pytube==15.0.0
reportlab==4.0.4
matplotlib==3.7.2
seaborn==0.12.2
altair==5.1.2
streamlit-option-menu==0.3.6
streamlit-extras==0.3.5
🛠️ Troubleshooting
Common Issues
Model Loading Error:

Ensure best.pt file exists in the project root
Check file permissions
Verify model file integrity
CUDA/GPU Issues:

Install CUDA toolkit if using GPU
Check GPU compatibility
Fall back to CPU processing if needed
Memory Issues:

Reduce video resolution for large files
Process images in smaller batches
Close other applications to free memory
YouTube Download Issues:

Check internet connection
Verify YouTube URL format
Some videos may have download restrictions
Performance Optimization
For Better Speed:

Use GPU acceleration
Reduce image/video resolution
Process fewer frames per second in videos
For Better Accuracy:

Use high-quality images
Ensure good lighting conditions
Avoid heavily compressed videos
🤝 Contributing
Development Setup
Fork the repository
Create a feature branch
Make your changes
Test thoroughly
Submit a pull request
Code Style
Follow PEP 8 guidelines
Use meaningful variable names
Add comments for complex logic
Maintain consistent formatting
📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
Ultralytics for the YOLOv11 model framework
Streamlit for the web application framework
OpenCV for computer vision capabilities
Plotly for interactive visualizations
PyTorch for deep learning infrastructure
📞 Support
For issues, questions, or contributions:

Create an issue in the repository
Check the troubleshooting section
Review the documentation
🏛️ HeritageLens AI - Preserving Heritage Through Technology

Built with ❤️ for archaeologists, historians, and heritage enthusiasts worldwide.
