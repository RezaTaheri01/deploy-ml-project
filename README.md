# 📧 Email Spam Detector

A simple Flask app that detects spam emails using a machine learning model. Includes a custom HTML + Tailwind CSS frontend with a dark/light mode toggle.

## 🔗 Resources

- 📘 Tutorial: [Deploying a Machine Learning Model](https://jovian.com/biraj/deploying-a-machine-learning-model)
- 🧠 ML Model Source: [Spam-Email-Detection (GitHub)](https://github.com/KalyanM45/Spam-Email-Detection)

## 🚀 Quick Start

```bash
git clone https://github.com/your-username/email-spam-detector.git
cd email-spam-detector
conda create -n spam-env python=3.10
conda activate spam-env
pip install -r requirements.txt
python app.py
```

Then open http://localhost:5000 in your browser.

## 🧪 Example Emails for Testing
### ✅ Non-Spam (Ham)
```
Hi Sarah,

Just a reminder about our meeting tomorrow at 10 AM.
Let me know if you need to reschedule.

Thanks,  
John
```

### 🚫 Spam
```
Congratulations! You’ve won a $1000 gift card.  
Click here to claim: http://scam-link.com
```


