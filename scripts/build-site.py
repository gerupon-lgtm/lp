"""Build only public assets and stamp the Pages build time in Japan time."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import shutil

def stamp(html, now):
    jst = now.astimezone(timezone(timedelta(hours=9)))
    marker = '<p id="last-updated">最終更新：公開時に自動更新（日本時間）</p>'
    if html.count(marker) != 1:
        raise ValueError('Expected exactly one last-updated marker')
    return html.replace(marker, '<p id="last-updated">最終更新：<time datetime="' +
                        jst.isoformat(timespec='seconds') + '">' +
                        jst.strftime('%Y/%m/%d %H:%M') + '</time>（日本時間）</p>')

def build(root, destination, now):
    destination.mkdir(parents=True, exist_ok=True)
    (destination / 'index.html').write_text(stamp((root / 'index.html').read_text(encoding='utf-8'), now), encoding='utf-8')
    for name in ['favicon.svg', 'CNAME']:
        shutil.copy2(root / name, destination / name)
    shutil.copytree(root / 'img', destination / 'img', dirs_exist_ok=True)
    (destination / '.nojekyll').touch()

if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    build(root, root / '_site', datetime.now(timezone.utc))
