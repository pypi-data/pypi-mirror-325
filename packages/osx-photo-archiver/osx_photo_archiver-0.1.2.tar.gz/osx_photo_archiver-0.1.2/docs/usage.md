# 使用方法ガイド

## 基本的な使い方

`osx-photo-archiver`は、macOSのPhotosアプリから写真・動画を年/月ディレクトリ構造で整理してエクスポートするツールです。

### 基本コマンド

```bash
osx-photo-archiver [オプション] 出力先ディレクトリ
```

例:
```bash
# 基本的な使用方法(全ての写真を出力)
osx-photo-archiver ~/Pictures/Sorted

# 特定期間の写真のみを出力
osx-photo-archiver --from-date 2024-01-01 --to-date 2024-12-31 ~/Pictures/Sorted
```

## コマンドラインオプション

| オプション | 説明 | 必須/任意 | 例 |
|:-----------|:-----|:----------|:---|
| `出力先ディレクトリ` | 写真・動画を出力するディレクトリ | 必須 | `~/Pictures/Sorted` |
| `--from-date` | エクスポート開始日 (YYYY-MM-DD形式) | 任意 | `--from-date 2024-01-01` |
| `--to-date` | エクスポート終了日 (YYYY-MM-DD形式) | 任意 | `--to-date 2024-12-31` |
| `--skip-duplicates/--no-skip-duplicates` | 重複ファイルのスキップ設定 | 任意 | `--skip-duplicates` |
| `--help` | ヘルプメッセージの表示 | - | `--help` |

## 出力ディレクトリ構造

写真・動画は以下のような構造で出力されます:

```
出力先ディレクトリ/
├── 2024/
│   ├── 01/
│   │   ├── IMG_0001.JPG
│   │   └── IMG_0002.MOV
│   └── 02/
│       ├── IMG_0003.JPG
│       └── IMG_0004.HEIC
└── 2023/
    └── 12/
        ├── IMG_0005.JPG
        └── IMG_0006.PNG
```

## 使用例

### 1. 全ての写真をエクスポート

```bash
osx-photo-archiver ~/Pictures/Sorted
```

### 2. 特定の期間の写真をエクスポート

```bash
# 2024年の写真のみをエクスポート
osx-photo-archiver \
  --from-date 2024-01-01 \
  --to-date 2024-12-31 \
  ~/Pictures/Sorted
```

### 3. 重複ファイルを上書きする場合

```bash
osx-photo-archiver \
  --no-skip-duplicates \
  ~/Pictures/Sorted
```

## エラーメッセージと対処方法

### よくあるエラー

1. **権限エラー**
   ```
   エラー: 必要な権限が不足しています
   ```
   - 対処: [インストールガイド](installation.md)の権限設定セクションを参照

2. **日付フォーマットエラー**
   ```
   エラー: 日付フォーマットが不正です
   ```
   - 対処: YYYY-MM-DD形式(例: 2024-01-01)で指定

3. **出力先ディレクトリエラー**
   ```
   エラー: 出力先ディレクトリへの書き込み権限がありません
   ```
   - 対処: ディレクトリの権限を確認し、必要に応じて権限を付与

## ベストプラクティス

1. **定期的なバックアップ**
   - エクスポート前に重要なデータをバックアップ
   - 出力先の空き容量を確認

2. **効率的な使用方法**
   - 大量の写真をエクスポートする場合は、期間を分けて実行
   - 重複チェックを有効にして不要なコピーを防止

3. **トラブル防止**
   - コマンド実行前に権限設定を確認
   - 出力先の空き容量を確認
   - テスト用の小さなデータセットで動作確認

## 高度な使用方法

### cronを使用した定期実行

以下は毎日深夜2時に実行する例です:

```bash
# crontabの編集
crontab -e

# 以下の行を追加
0 2 * * * /path/to/venv/bin/osx-photo-archiver --from-date $(date -v-1d +%Y-%m-%d) ~/Pictures/Sorted
```

### launchdを使用した定期実行

1. `~/Library/LaunchAgents/com.user.osxphotoarchiver.plist`を作成:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.user.osxphotoarchiver</string>
    <key>ProgramArguments</key>
    <array>
        <string>/path/to/venv/bin/osx-photo-archiver</string>
        <string>--from-date</string>
        <string>2024-01-01</string>
        <string>~/Pictures/Sorted</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>2</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
</dict>
</plist>
```

2. launchdに登録:

```bash
launchctl load ~/Library/LaunchAgents/com.user.osxphotoarchiver.plist
