# 📊 Chart to Report: AI-Powered Chart Analysis and PDF Report Generator

**Quickly analyze your charts, get professional insights, and generate downloadable PDF reports!**

This project uses Hugging Face’s multi-modal SmolVLM-Instruct model to interpret various types of charts (bar, pie, line, etc.) and produce clear, human-like explanations.

---

## 🌐 Live Demo

Try it instantly here:
🔗 [Chart Analysis Demo](https://huggingface.co/spaces/ctntrk/Chart-Analysis)

---

## 🚀 Features

* 📊 Upload and analyze different chart images
* 🤖 AI-generated natural language insights using SmolVLM-Instruct
* 📄 Generate polished PDF reports including the chart and AI analysis
* 🧼 Clear/reset button for quick new inputs
* 💻 Easy-to-use web interface built with Gradio

---

## 🧠 Technologies Used

* **Gradio** — interactive user interface
* **PyTorch & Hugging Face Transformers** — model loading and inference
* **SmolVLM-Instruct** — vision-language model for chart understanding
* **FPDF** — PDF report creation
* **CUDA (optional)** — GPU acceleration if available

---

## 🚀 How It Works

1. **Model Loading**
   Loads the SmolVLM-Instruct vision-language model and processor from Hugging Face.

2. **User Interface**
   Built with Gradio, allowing users to upload a chart image.

3. **Prompt Creation**
   Combines the uploaded image with a default prompt instructing the model to analyze professionally.

4. **AI Inference**
   The model generates detailed chart insights in natural language.

5. **PDF Generation**
   Saves the chart image and AI explanation into a well-formatted PDF report.

6. **Output**
   Displays the analysis text and provides a downloadable PDF.

---

## 👥 Who Can Use This?

* Data analysts seeking quick chart interpretations
* Business professionals needing fast data insights and reports
* Educators and students working with visual data
* Researchers documenting data trends
* Anyone wanting to automate chart analysis without coding

---

## 🔧 Getting Started

To run locally:

### 1. Install dependencies:

```bash
pip install -r requirements.txt
```

### 2. Run the app:

```bash
python app.py
```

> 💡 The app uses Gradio to launch a browser-based interface. It may take a few seconds to load the model—please be patient.

---

## ✅ Why Use This App?

* No coding required — get instant chart insights
* Saves time and reduces manual errors
* Generates shareable PDF reports automatically
* Simple, clean UI suitable for all skill levels

---

## 🧩 Future Improvements

* Multilingual support (e.g., Turkish, Spanish)
* Support for more chart types and formats
* Enhanced user controls (tone, length, style)
* Integration with dashboards and BI tools

---

## 📬 Feedback & Contributions

Feedback and contributions are welcome! Please open an issue or submit a pull request.

---

## 📄 License

This project is open-source under the **MIT License**.

