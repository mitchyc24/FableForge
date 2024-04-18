import gradio as gr

def reverse_text(text):
    """Reverse the input text."""
    return text[::-1]

def interface_2():
    """Create the interface for text reversal."""
    description = "Reverse Text"
    with gr.Row():
        input_text = gr.Textbox(label="Enter text to reverse")
        output_text = gr.Textbox(label="Reversed text", interactive=True)
        button = gr.Button("Reverse", size="sm")
        button.click(reverse_text, inputs=input_text, outputs=output_text)
    return gr.Column(input_text, button, output_text, "Reversed text successfully!")