import gradio as gr
from transformers import AutoProcessor, AutoModelForVision2Seq
from PIL import Image
from fpdf import FPDF
import torch
import textwrap
import re
import os


DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


processor = AutoProcessor.from_pretrained("HuggingFaceTB/SmolVLM-Instruct")
model = AutoModelForVision2Seq.from_pretrained(
    "HuggingFaceTB/SmolVLM-Instruct",
    torch_dtype=torch.bfloat16 if DEVICE == "cuda" else torch.float32,
).to(DEVICE)

DEFAULT_PROMPT = "Please analyze this chart like a professional data analyst and explain the insights clearly."

def analyze_chart_and_generate_pdf(image: Image.Image):
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image"},
                {"type": "text", "text": DEFAULT_PROMPT}
            ]
        },
    ]

    chat_prompt = processor.apply_chat_template(messages, add_generation_prompt=True)
    inputs = processor(text=chat_prompt, images=[image], return_tensors="pt").to(DEVICE)

    generated_ids = model.generate(**inputs, max_new_tokens=500)
    raw_output = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

    generated_text = re.split(r"Assistant:\s*", raw_output, maxsplit=1)[-1].strip()
    cleaned_text = generated_text.encode("latin-1", errors="ignore").decode("latin-1")

    image_path = "/tmp/temp_chart_image.png"
    image.save(image_path)

    pdf_path = "/tmp/chart_analysis_result.pdf"
    pdf = FPDF()
    pdf.add_page()


    pdf.set_font("Arial", 'B', 18)
    pdf.cell(0, 15, "Chart Analysis Report", ln=True, align='C')


    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Uploaded Chart", ln=True, align='C')


    img_width = 180
    img_ratio = image.height / image.width
    img_height = img_width * img_ratio
    pdf.image(image_path, x=(210 - img_width) / 2, y=35, w=img_width, h=img_height)

    y_after_image = 35 + img_height + 10


    pdf.set_xy(10, y_after_image)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "AI-Generated Insights", ln=True)

    
    pdf.set_font("Arial", size=12)
    wrapped_lines = textwrap.wrap(cleaned_text, width=90)
    for line in wrapped_lines:
        pdf.multi_cell(0, 8, line, align='L')

    pdf.output(pdf_path)
    os.remove(image_path)

    return generated_text, pdf_path


def clear_fields():
    return None, "", None  

with gr.Blocks() as demo:
    with gr.Accordion("📘 About This Project", open=False):
        gr.Markdown("""
        This application uses the **SmolVLM** 🧠 vision-language model to analyze uploaded chart images 🖼️ and generate AI-powered explanations 💡.
        
        It also produces a downloadable **PDF report** 📄 containing:
        - 🖼️ The uploaded chart image
        - ✍️ A clearly written AI-generated analysis
        
        ---
        
        ### 🔑 Key Features
        - 📊 Support for various chart types (bar, line, pie, etc.)
        - 🗣️ Natural language insights
        - 📤 PDF export
        
        ---
        
        ### 👥 Ideal For
        - 👨‍💼 Data analysts
        - 💼 Business professionals
        - 👩‍🏫 Educators and students
        
        ---
        
        ⚙️ Built with:
        - 🤗 Hugging Face Transformers
        - 🧪 Gradio
        - 📝 FPDF
        """)


    gr.Markdown("# 📊 Chart Insight Generator with SmolVLM")
    with gr.Row():
        image_input = gr.Image(type="pil", label="Upload Chart Image")
    analyze_button = gr.Button("Analyze Chart")
    clear_button = gr.Button("Clear")  
    output_text = gr.Textbox(label="Analysis Result", lines=12, interactive=False)
    pdf_output = gr.File(label="Download PDF")

    analyze_button.click(
        fn=analyze_chart_and_generate_pdf,
        inputs=[image_input],
        outputs=[output_text, pdf_output]
    )

    
    clear_button.click(
        fn=clear_fields,
        inputs=[],
        outputs=[image_input, output_text, pdf_output]
    )

demo.launch()
