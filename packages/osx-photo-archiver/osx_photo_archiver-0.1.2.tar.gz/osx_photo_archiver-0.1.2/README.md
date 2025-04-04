# OSX Photo Archiver

macOSのPhotosアプリから写真・動画を年/月ディレクトリ構造でエクスポートするツール

## 特徴

- 写真・動画を撮影日別(年/月)に自動整理
- 重複ファイルの管理(スキップ/上書き)
- 期間指定によるエクスポート
- メタデータ(EXIF)の活用
- シンプルなコマンドラインインターフェース

## インストール

```bash
pip install osx-photo-archiver
```

## 必要条件

- macOS 10.15以降
- Python 3.8以降
- Photos.appに写真・動画が取り込まれていること
- フルディスクアクセス権限の設定(必要に応じて)

## 使い方

基本的な使用方法:

```bash
osx-photo-archiver ~/Pictures/Sorted
```

期間を指定してエクスポート:

```bash
osx-photo-archiver \
  --from-date 2024-01-01 \
  --to-date 2024-12-31 \
  ~/Pictures/Sorted
```

### オプション

- `--from-date`: エクスポート開始日(YYYY-MM-DD形式)
- `--to-date`: エクスポート終了日(YYYY-MM-DD形式)
- `--skip-duplicates/--no-skip-duplicates`: 重複ファイルのスキップ設定

## 出力ディレクトリ構造

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

## ライセンス

MIT License

## 謝辞

このツールは[osxphotos](https://github.com/RhetTbull/osxphotos)を利用しています。
