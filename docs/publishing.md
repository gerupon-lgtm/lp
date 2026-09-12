# GitHub Pagesの公開と最終更新日時

公開元はGitHub Actionsへ切り替える。GitHubのSettings → Pages → Build and deployment → SourceでGitHub Actionsを選ぶ。
その後mainへpushすると `.github/workflows/pages.yml` が公開する。既存の独自ドメイン設定は維持する。

最終更新日時は `scripts/build-site.py` が公開用HTMLを作成する時点の日時。日本時間（UTC+09:00）で表示する。
コミット日時や閲覧日時ではない。同じコミットを手動で再公開した場合も日時は更新される。実際の公開完了より少し前のビルド日時になる。
日時は公開用の `_site/index.html` だけへ埋め込み、ソースのindex.htmlは変更しない。訪問者からGitHub APIへの通信は不要。

ローカルのindex.htmlでは「最終更新：公開時に自動更新（日本時間）」と表示する。
公開時の表示をローカルで確認する場合は `python scripts/build-site.py` を実行して `_site/index.html` を開く。
公開対象はindex.html、img、favicon.svg、CNAMEと.nojekyllのみ。作業資料とスクリプトは公開しない。

2026-09-13に公開元をGitHub Actionsへ変更。mainへのpushで自動公開する。
