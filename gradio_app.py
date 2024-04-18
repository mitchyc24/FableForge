import gradio as gr
from modules.imagen import imagen




def gradio_interface():
    iface = gr.Interface(
        fn = imagen.generate_image,
        inputs = "text",
        outputs = "image",
        title = "Image Generator",
        description = "Generate an image from a prompt.",
    )
    return iface


if __name__ == "__main__":
    app = gradio_interface()
    app.launch()