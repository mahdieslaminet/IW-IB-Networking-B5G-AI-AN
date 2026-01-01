import gradio as gr
import pandas as pd

df = pd.read_csv("iwib5gnet_v0.csv")

def search_rows(context, tech, packet):
    results = df[
        (df["ContextSwitchesPerSecond"] == context) &
        (df["programmableTechnology"] == tech) &
        (df["packetSize"] == packet)
    ]
    
    similar = df.head(5)

    return results if not results.empty else similar

with gr.Blocks(theme="soft") as demo:

    gr.HTML("""
    <div style='padding:18px;background:#0f172a;color:white;
        border-radius:18px;margin-bottom:10px'>
        <h1 style='margin:0;font-size:26px'>🔎 IBN Traffic Lookup</h1>
        <p style='opacity:.8'>جستجوی رکوردهای مشابه بر اساس پارامترهای شبکه</p>
    </div>
    """)

    with gr.Row():
        with gr.Column():
            context = gr.Number(label="ContextSwitchesPerSecond")
            tech = gr.Textbox(label="Programmable Technology")
            packet = gr.Number(label="Packet Size")

            btn = gr.Button("🔍 جستجو", variant="primary")

        with gr.Column():
            output = gr.DataFrame(
                headers=list(df.columns),
                label="نتیجه جستجو / نمونه‌های مشابه"
            )

    btn.click(search_rows, [context, tech, packet], output)

demo.launch()
