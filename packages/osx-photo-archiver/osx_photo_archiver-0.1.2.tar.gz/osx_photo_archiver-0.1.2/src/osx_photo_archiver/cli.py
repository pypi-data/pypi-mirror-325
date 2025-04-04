"""
OSX Photo Archiver CLI Module
コマンドラインインターフェースを提供
"""
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

import click
from dateutil import parser as date_parser

from .core import ExportConfig, PhotoArchiver

def validate_date(ctx: click.Context, param: click.Parameter, value: Optional[str]) -> Optional[datetime]:
    """日付文字列をバリデーションし、datetime objectに変換"""
    if not value:
        return None
    try:
        return date_parser.parse(value).replace(hour=0, minute=0, second=0, microsecond=0)
    except ValueError:
        raise click.BadParameter('日付フォーマットが不正です。YYYY-MM-DD形式で指定してください。')

@click.command()
@click.argument('output_dir', type=click.Path())
@click.option(
    '--from-date',
    type=str,
    callback=validate_date,
    help='エクスポート開始日 (YYYY-MM-DD形式)'
)
@click.option(
    '--to-date',
    type=str,
    callback=validate_date,
    help='エクスポート終了日 (YYYY-MM-DD形式)'
)
@click.option(
    '--skip-duplicates/--no-skip-duplicates',
    default=True,
    help='重複ファイルをスキップするかどうか'
)
def main(
    output_dir: str,
    from_date: Optional[datetime],
    to_date: Optional[datetime],
    skip_duplicates: bool
) -> None:
    """
    macOSのPhotosアプリから写真・動画を年/月ディレクトリ構造でエクスポート

    OUTPUT_DIR: エクスポート先のディレクトリパス
    """
    try:
        config = ExportConfig(
            output_dir=Path(output_dir).resolve(),
            from_date=from_date,
            to_date=to_date,
            skip_duplicates=skip_duplicates
        )

        archiver = PhotoArchiver(config)

        # 権限チェック
        if not archiver.verify_permissions():
            click.echo('エラー: 必要な権限が不足しています。', err=True)
            click.echo('Photosライブラリへのアクセス権限とディスク全体へのアクセス権限を確認してください。', err=True)
            sys.exit(1)

        # エクスポート実行
        click.echo('写真・動画のエクスポートを開始します...')
        archiver.export()
        click.echo('エクスポートが完了しました!')

    except ValueError as e:
        click.echo(f'エラー: {str(e)}', err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f'エラー: {str(e)}', err=True)
        sys.exit(1)

if __name__ == '__main__':
    main()
