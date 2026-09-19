# コエキット掲載記録

2026-09-19の利用者説明と lp-mode-summary.md、lp-technology-summary.md、irodori-voice-probe-results.md に基づく。

「触れるもの」の先頭に開発中として掲載。Web Speech APIは検証のみ、公開版の認識はVosk。Web Speech API一般が常に外部送信するとは書かず、通常方式の検証と端末内日本語認識の不成立を区別。候補調整による認識完全解決は主張しない。YOLOと傾きセンサーとの組み合わせは構想として記載。

用語辞書は既存のindex.html内のTERMSを維持。Web Speech API、Vosk、WebAssembly、Web Workers、YOLO、3作品名を追加。コエキットは掲載作品から自動登録。自記事での作品名ツールチップ抑制を子作品名にも適用。

画像は添付の1・2・3枚目を既存と同じSVG表示枠に配置。元PNGは保持し、端末ステータスと下部ナビゲーションを表示範囲から除外。

用語確認先：
- https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API
- https://alphacephei.com/vosk/
- https://docs.ultralytics.com/ja/tasks/detect
- 制作経緯の補足：Voskは当初から採用方針であり、検証に失敗した場合は開発中止予定だった。言語モデルの配置階層による日本語認識の問題は試行錯誤で解決。Web Speech APIの失敗を受けてVoskへ転換したという因果関係にしない。
