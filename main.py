import webview

def main():
    # iPad側で生成された VDO.Ninja の視聴用URLをここに指定
    view_url = 'https://vdo.ninja/?view=YOUR_STREAM_ID'

    window = webview.create_window(
        title='Transparent Camera',
        url=view_url,
        width=500,
        height=500,
        frameless=True,       # 枠なし
        easy_drag=True,       # ドラッグ移動
        on_top=True,          # 常に最前面
        transparent=True,     # 背景透明
        resizable=True
    )

    webview.start(gui='edgechromium', debug=False)

if __name__ == '__main__':
    main()
