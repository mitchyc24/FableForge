import gradio as gr # type: ignore
from modules.imagen import imagen

def imagen_gradio_interface():
    with gr.Row():
        with gr.Column(scale=1):
            imagen_input = gr.Textbox(label="Image Prompt",scale=4)
            imagen_button = gr.Button(value="Generate Image", size="sm", scale=1)
        with gr.Column(scale=3):
            imagen_output = gr.Image(label="Generated Image", scale=4)
    
        imagen_button.click(imagen.generate_image, inputs=imagen_input, outputs=imagen_output)
    return gr.Column(imagen_input, imagen_button, imagen_output, "Image generated successfully!")



