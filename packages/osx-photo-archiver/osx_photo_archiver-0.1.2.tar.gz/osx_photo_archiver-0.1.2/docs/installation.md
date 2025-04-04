# インストールガイド

## 前提条件

- macOS 10.15以降
- Python 3.8以降
- pip (Pythonパッケージマネージャー)
- Photos.app に写真・動画が取り込まれていること

## インストール手順

1. **Python環境の確認**

```bash
# Pythonバージョンの確認
python3 --version  # 3.8以上であることを確認

# pipの確認
pip3 --version
```

2. **仮想環境の作成(推奨)**

```bash
# 仮想環境の作成
python3 -m venv venv

# 仮想環境の有効化
source venv/bin/activate
```

3. **パッケージのインストール**

```bash
# 必要なパッケージのインストール
pip install -e .  # 開発モードでインストール
```

## 権限設定

1. **フルディスクアクセス権限の設定**

macOSのPhotosライブラリにアクセスするために、以下の手順でフルディスクアクセス権限を設定する必要があります:

1. Appleメニュー > システム環境設定 > プライバシーとセキュリティ を開く
2. 左側のメニューから「フルディスクアクセス」を選択
3. 右下の鍵アイコンをクリックしてロックを解除
4. 「+」ボタンをクリックし、以下のアプリケーションを追加:
   - ターミナル.app(コマンドラインから実行する場合)
   - Visual Studio Code.app(VSCodeから実行する場合)
5. 追加したアプリケーションのチェックボックスを有効化

## インストールの確認

1. **コマンドの確認**

```bash
# ヘルプの表示
osx-photo-archiver --help

# バージョン確認
osxphotos --version
```

2. **Photosライブラリへのアクセス確認**

```bash
# 写真の一覧を表示してアクセスをテスト
osxphotos list
```

## トラブルシューティング

### よくある問題

1. **osxphotosコマンドが見つからない場合**
   ```bash
   pip install --upgrade osxphotos
   ```

2. **権限エラーが発生する場合**
   - フルディスクアクセス権限が正しく設定されているか確認
   - ターミナルを再起動して権限を再読み込み

3. **Pythonバージョンが古い場合**
   ```bash
   brew install python@3.8  # Homebrewを使用している場合
   ```

### 追加のヘルプ

問題が解決しない場合は、以下を確認してください:

1. システムのログ(Console.app)でエラーメッセージを確認
2. `osxphotos`の[公式ドキュメント](https://github.com/RhetTbull/osxphotos)を参照
3. GitHubのIssuesページで類似の問題を検索

## アンインストール

必要に応じて、以下の手順でアンインストールできます:

```bash
# パッケージのアンインストール
pip uninstall osx-photo-archiver

# 仮想環境を使用している場合、削除
deactivate  # 仮想環境を無効化
rm -rf venv  # 仮想環境を削除
