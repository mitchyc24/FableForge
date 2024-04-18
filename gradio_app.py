import gradio as gr
from modules.imagen.imagen_gradio_components import imagen_gradio_interface
from modules.imagen.reverse_text import interface_2


def main():
    with gr.Blocks() as app:
        with gr.Tab(label="Image Generation"):
            app.add(imagen_gradio_interface())
        
        with gr.Tab(label="Text Reversal"):
            app.add(interface_2())

    app.launch()

if __name__ == "__main__":
    main()